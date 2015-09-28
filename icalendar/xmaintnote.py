import icalendar
from icalendar import Event, vText

import simplejson as _json

import re

class XMaintNoteEvent(Event):

    # XXX-kbaker 
    # controls ordering - probably not necessary
    # and can probably get rid of this class entirely 
    # besides canonical_order the library doesn't seem
    # to use any of this anyways.
    canonical_order = Event.canonical_order + ( 
        'X-MAINTNOTE-PROVIDER',
        'X-MAINTNOTE-ACCOUNT',
        'X-MAINTNOTE-MAINTENANCE-ID',
        'X-MAINTNOTE-OBJECT-ID',
        'X-MAINTNOTE-IMPACT',
    )

    # XXX-kbaker notes:
    # from what I can tell icalendar is pretty lax
    # and doesn't actually look for required or singletons
    # check out icalendar.cal,Component.add()
    # and also the commented out icalendar.cal.Component.is_compliant
    required = Event.required + (
        'X-MAINTNOTE-PROVIDER',
        'X-MAINTNOTE-ACCOUNT',
        'X-MAINTNOTE-MAINTENANCE-ID',
        'X-MAINTNOTE-OBJECT-ID',
        'X-MAINTNOTE-IMPACT',
    )
    singletons = Event.singletons + (
        'X-MAINTNOTE-PROVIDER',
        'X-MAINTNOTE-ACCOUNT',
        'X-MAINTNOTE-MAINTENANCE-ID',
        'X-MAINTNOTE-OBJECT-ID',
        'X-MAINTNOTE-IMPACT',
    )


class vXMaintNoteImpact(vText):

    """ X-MAINTNOTE-IMPACT
    """

    # list of known impact types
    impact_types = [ 
        'NO-IMPACT',
        'REDUCED-REDUNDANCY',
        'DEGRADED',
        'OUTAGE'
    ]

    # create a regex to check incoming types against
    MAINT_NOTE_IMPACT = re.compile('(?:%s)' % '|'.join(impact_types))

    def __init__(self, *args, **kwargs):
        super(vXMaintNoteImpact, self).__init__(*args, **kwargs)

        match = vXMaintNoteImpact.MAINT_NOTE_IMPACT.match(self)
        if match is None:
            raise ValueError('Expected x-maint-note-impact, got: %s' % self)


# tell the TypesFactory about vXMaintNoteImpact
icalendar.cal.types_factory['x-maintnote-impact'] = vXMaintNoteImpact
icalendar.cal.types_factory.types_map['x-maintnote-impact'] = 'x-maintnote-impact'

def encode_vDDDTypes(obj):
    if isinstance(obj, icalendar.prop.vDDDTypes):
        # convert vDDDTypes - date/time types to strings
        return unicode(obj.to_ical())
    raise TypeError(repr(o) + " is not JSON serializable")


def ical2json(cal):
    data = {}
    data[cal.name] = dict(cal.items()); 

    for component in cal.subcomponents:
        if not data[cal.name].has_key(component.name):
            data[cal.name][component.name] = []

        comp_obj = {}
        for item in component.items():
            comp_obj[item[0]] = unicode(item[1])

        data[cal.name][component.name].append(comp_obj)

    json = _json.dumps(data, default=encode_vDDDTypes, sort_keys=True, indent='    ')

    return json

def display(cal):
    return cal.to_ical().replace('\r\n', '\n').strip()
