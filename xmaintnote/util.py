import icalendar
import simplejson as _json


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


def register_property(property_type):
    property_name = property_type.property_name
    icalendar.cal.types_factory[property_name] = property_type
    icalendar.cal.types_factory.types_map[property_name] = property_name
    return property_type
