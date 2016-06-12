import logging

import icalendar
from icalendar import vText

LOGGER = logging.getLogger(__name__)


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

    def __init__(self, *args, **kwargs):
        super(vXMaintNoteImpact, self).__init__(*args, **kwargs)

        if str(self) not in self.impact_types:
            LOGGER.debug(
                'Unrecognised impact type %r should be treated as OUTAGE',
                str(self))


# tell the TypesFactory about vXMaintNoteImpact
icalendar.cal.types_factory['x-maintnote-impact'] = vXMaintNoteImpact
icalendar.cal.types_factory.types_map['x-maintnote-impact'] = 'x-maintnote-impact'

def encode_vDDDTypes(obj):
    if isinstance(obj, icalendar.prop.vDDDTypes):
        # convert vDDDTypes - date/time types to strings
        return unicode(obj.to_ical())
    raise TypeError(repr(o) + " is not JSON serializable")
