import logging

from icalendar import vText

from xmaintnote.util import register_property

LOGGER = logging.getLogger(__name__)

@register_property
class vXMaintNoteImpact(vText):
    """ X-MAINTNOTE-IMPACT
    """
    property_name = 'x-maintnote-impact'
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
