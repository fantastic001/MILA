
from mila.config import * 
from example import MyBaseClass, MyObject
from mila.config import get_config, get_config_str, get_config_bool, get_config_list, get_config_dict, get_config_int, get_config_float

print(get_classes_inheriting(MyBaseClass))


my_object = MyObject()

print(get_config_str("my_str", "", "This is my string", obj=my_object))
print(get_config_bool("my_bool", False, "This is a boolean", obj=my_object))
print(get_config_list("my_list", [], "This is a list", obj=my_object))
print(get_config_dict("my_dict", {}, "This is a dictionary", obj=my_object))
print(get_config("my_int", 0, "This is an integer", expected_type=int, obj=my_object))
print(get_config("my_float", 0.0, "This is a float", expected_type=float, obj=my_object))

print(get_config_int("my_int", 0, "This is an integer", obj=my_object))
print(get_config_float("my_float", 0.0, "This is a float", obj=my_object))

print(get_config_str("other_string", "default", "This is another string", obj=my_object))

