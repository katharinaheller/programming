# Text Type
text_type = "Hello, World!"  # str

# Numeric Types
integer_type = 42  # int
float_type = 3.14  # float
complex_type = 2 + 3j  # complex

# Sequence Types
list_type = [1, 2, 3]  # list
tuple_type = (4, 5, 6)  # tuple
range_type = range(1, 5)  # range

# Mapping Type
dictionary_type = {"key": "value"}  # dict

# Set Types
set_type = {1, 2, 3}  # set
frozenset_type = frozenset({4, 5, 6})  # frozenset

# Boolean Type
boolean_type = True  # bool

# Binary Types
bytes_type = b"binary data"  # bytes
bytearray_type = bytearray([65, 66, 67])  # bytearray
memoryview_type = memoryview(b"example")  # memoryview

# None Type
none_type = None  # NoneType

# Displaying the types and their values
print("Text Type:", type(text_type))
print("Numeric Types:", type(integer_type), type(float_type), type(complex_type))
print("Sequence Types:", type(list_type), type(tuple_type), type(range_type))
print("Mapping Type:", type(dictionary_type))
print("Set Types:", type(set_type), type(frozenset_type))
print("Boolean Type:", type(boolean_type))
print("Binary Types:", type(bytes_type), type(bytearray_type), type(memoryview_type))
print("None Type:", type(none_type))
