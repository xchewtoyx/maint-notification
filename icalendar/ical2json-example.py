
import simplejson as _json

import icalendar
from icalendar import Calendar, Event
from icalendar import vCalAddress, vText

import xmaintnote # XXX kbaker's hacks for BCOP

from datetime import datetime
import pytz


def ical2json(cal):
    data = {}
    data[cal.name] = {}

    for item in cal.items():
        if isinstance(item[1], icalendar.prop.vDDDTypes):
            # convert vDDDTypes - date/time types to strings
            data[cal.name][item[0]] = unicode(item[1].to_ical())
        else:
            data[cal.name][item[0]] = unicode(item[1])

    for component in cal.subcomponents:
        if not data[cal.name].has_key(component.name):
            data[cal.name][component.name] = []

        comp_obj = {}
        for item in component.items():
            if isinstance(item[1], icalendar.prop.vDDDTypes):
                # convert vDDDTypes - date/time types to strings
                comp_obj[item[0]] = unicode(item[1].to_ical())
            else:
                comp_obj[item[0]] = unicode(item[1])

        data[cal.name][component.name].append(comp_obj)

    json = _json.dumps(data, sort_keys=True, indent='    ')

    return json


def display(cal):
    return cal.to_ical().replace('\r\n', '\n').strip()

# example script to add X-MAINTNOTE to an ical

cal = Calendar()
cal.add('prodid', '-//Maint Note//https://github.com/maint-notification//')
cal.add('version', '2.0')
cal.add('dtstart', datetime(2015,4,4,8,0,0))
cal['dtstart'].to_ical()
cal.add('summary', 'Maint Note Example')

# either of these work fine
#event = Event()
event = xmaintnote.XMaintNoteEvent()

event.add('uid', '42')
event.add('dtstart', datetime(2015, 10, 10, 8, 0, 0, tzinfo=pytz.utc))
event.add('dtend', datetime(2015, 10, 10, 10, 0, 0, tzinfo=pytz.utc))
event.add('dtstamp', datetime(2015, 10, 10, 0, 10, 0, tzinfo=pytz.utc))

# maintnote stuff
event.add('x-maintnote-provider', 'example.com' )
event.add('x-maintnote-account', '137.035999173' )
event.add('x-maintnote-maintenance-id', 'WorkOrder-31415' )
event.add('x-maintnote-object-id', 'acme-widgets-as-a-service' )
event.add('x-maintnote-impact', "NO-IMPACT");
# test the regex
#event.add('x-maintnote-impact', "GARBAGE");


if 0:
    organizer = vCalAddress('MAILTO:noone@example.com')
    organizer.params['cn'] = vText('Max Rasmussen')
    organizer.params['role'] = vText('CHAIR')
    event['organizer'] = organizer
    event['location'] = vText('Odense, Denmark')
    event['uid'] = '20050115T101010/27346262376@mxm.dk'
    event.add('priority', 5)
    
    attendee = vCalAddress('MAILTO:maxm@example.com')
    attendee.params['cn'] = vText('Max Rasmussen')
    attendee.params['ROLE'] = vText('REQ-PARTICIPANT')
    event.add('attendee', attendee, encode=0)
    
    attendee = vCalAddress('MAILTO:the-dude@example.com')
    attendee.params['cn'] = vText('The Dude')
    attendee.params['ROLE'] = vText('REQ-PARTICIPANT')
    event.add('attendee', attendee, encode=0)



cal.add_component(event)

print ical2json(cal)
