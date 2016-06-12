from icalendar import Event


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
