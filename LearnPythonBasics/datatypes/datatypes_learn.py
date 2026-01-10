a,b,c=10,20,30
# Concatenate two different datatypes
print("{} {}".format("The sum is : " , a+b+c))

# Datatypes in Python :
# Numeric
# -> int
# -> float
# -> complex
# -> list (mutable, [])
# -> tuple (immutable, ())
# -> dictionary (key : value pair, {})

# int datatype
x=10
print(x,type(x))

# float datatype
x=12.56
print(x,type(x))

# complex datatype
x=10+4j
print(x,type(x))

# list datatype
x=[1,12.5,14,"Kaushik",12+5j]
print("===================================")
for i in x:
    print(i,type(i))
print("====================================")
for i in range(len(x)):
    print(x[i],type(x[i]))

print("====================================")

# print the last value in the list directly
print(x[-1],type(x[-1]))

print("====================================")

# print the range of values (slicing operator)
print(x[1:3],type(x[1:3]))

print("====================================")

# Insert values into a list
x.insert(2,"Babbi")
print(x)

print("====================================")

# insert value at the last index of a list (using append keyword)
x.append(100+34j)
print(x)

print("====================================")

# delete values in the list
print(x)
del x[2]
print(x)

print("====================================")

# tuple datatype
val=(1,2,"Kaushik",10+34j)
print(val,type(val))
for i in val:
    print(i,type(i))

# val[2]=12+89j
# tuple is immutable, we cannot reassign the values once declared
print(val)

print("====================================")

# dictionary datatype
data={"a":2,"b":3,"c":4,"d":5}
print(data,type(data))
print(data["d"])

for key,value in data.items():
    print(key,value)

print("====================================")

# create dictionary in runtime
val={}
val["Name"]="Kaushik"
val["AGE"]=34
print(val)



