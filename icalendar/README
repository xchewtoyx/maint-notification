# Fedora 22. install icalendar
sudo dnf install python-icalendar python3-icalendar -y

# run test. it just prints out an ical 

python icalendar-example.py

# TODO

* discuss a json option with the BCOP group
* find out which properties are mandatory (seems to be all) and which are optional
* find out which properties are singleton or multiple
* consider writing an icalendar.cal.Component.is_compliant routine
* research whether X-MAINTNOTE-* is a valid x-name for a content line. I'm a little rusty on reading BNF...referring to https://tools.ietf.org/html/rfc5545#section-3.1. The vendorid part is optional methinks. Which is good as it makes no sense in this case.

     x-name        = "X-" [vendorid "-"] 1*(ALPHA / DIGIT / "-")
     ; Reserved for experimental use.

     vendorid      = 3*(ALPHA / DIGIT)
     ; Vendor identification

* write an example that reads in a .ics with the X-MAINTNOTE extensions
