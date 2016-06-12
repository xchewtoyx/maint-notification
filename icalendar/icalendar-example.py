import logging
from icalendar import Calendar, Event
from icalendar import vCalAddress, vText

import xmaintnote # XXX kbaker's hacks for BCOP

from datetime import datetime, timedelta
#import pytz

logging.basicConfig()


def display(cal):
    return cal.to_ical().replace('\r\n', '\n').strip()

def roundTime(dt=None, roundTo=60):
   """Round a datetime object to any time laps in seconds
   dt : datetime.datetime object, default now.
   roundTo : Closest number of seconds to round to, default 1 minute.
   Author: Thierry Husson 2012 - Use it as you want but don't blame me.
   """
   if dt == None : dt = datetime.now()
   seconds = (dt - dt.min).seconds
   # // is a floor division, not a comment on following line:
   rounding = (seconds+roundTo/2) // roundTo * roundTo
   return dt + timedelta(0,rounding-seconds,-dt.microsecond)

def start_two_hours_from_now():
    """Setup two datetime dates for a meeting set two hours from now"""
    dt_now = datetime.now()
    #dt_now = datetime.utcnow()
    dt_now_rnd = roundTime(dt_now, roundTo=60*60)
    dt_mtg_start = dt_now_rnd + timedelta(0, 60*60)
    dt_mtg_end = dt_mtg_start + timedelta(0, 60*60)
    return (dt_now, dt_mtg_start, dt_mtg_end)



# cook up a datetime for our calendar entry
(dt_now, dt_mtg_start, dt_mtg_end) = start_two_hours_from_now()
dt_cal_start = dt_now - timedelta(10)

# example script to add X-MAINTNOTE to an ical

cal = Calendar()
cal.add('prodid', '-//Maint Note//https://github.com/maint-notification//')
cal.add('version', '2.0')

# either of these work fine
#event = Event()
event = xmaintnote.XMaintNoteEvent()

event.add('summary', 'Maint Note Example')
event.add('uid', '42')
event.add('sequence', 1)
#event.add('dtstart', datetime(2015, 10, 10, 8, 0, 0, tzinfo=pytz.utc))
#event.add('dtend', datetime(2015, 10, 10, 10, 0, 0, tzinfo=pytz.utc))
#event.add('dtstamp', datetime(2015, 10, 10, 0, 10, 0, tzinfo=pytz.utc))
event.add('dtstart', dt_mtg_start)
event.add('dtend', dt_mtg_end)
event.add('dtstamp', dt_now)

organizer = vCalAddress('mailto:noone@example.com')
organizer.params['cn'] = vText('Example NOC')
event['organizer'] = organizer

# maintnote stuff
event.add('x-maintnote-provider', 'example.com' )
event.add('x-maintnote-account', '137.035999173' )
event.add('x-maintnote-maintenance-id', 'WorkOrder-31415' )
event.add('x-maintnote-object-id', 'acme-widgets-as-a-service' )
event.add('x-maintnote-impact', "NO-IMPACT");
event.add('x-maintnote-status', "TENTATIVE");
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

print display(cal)
