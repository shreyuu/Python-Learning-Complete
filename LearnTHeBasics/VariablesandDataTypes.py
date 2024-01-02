a=10; b=20 #variable declaration 
print(a,b)


'''<---Data Types--->
Numeric data types: int, float, complex
String data types: str
Sequence types: list, tuple, range
Binary types: bytes, bytearray, memoryview
Mapping data type: dict
Boolean type: bool
Set data types: set, frozenset'''

# Numeric datatypes
a=int(10)
b=float(10)
c=complex(3+a)
print(type(a),type(b),type(c))

# String Datatypes
a=str("helloWorld!")
b="HelloWorld"
print(type(a),type(b))

# Sequence types
a=[10,20,30]
b=(10,20,30)
c=range(1,5)
print(type(a),type(b),type(c))

# Binary types [Bytes and bytearray objects contain single bytes – the former is immutable while the latter is a mutable sequence. ]
a=b"hello"
b=bytearray(5)
c=memoryview(bytes(5))
print(type(a),type(b),type(c))

# Mapping datatype
a={1:"red",2:"green",3:"green"}
print(type(a))

# Boolean type
a=True
b=False
print(type(a),type(b))

# Set datatypes
a={"red","green","green"}
print(type(a))
b=frozenset(a) #immutable set