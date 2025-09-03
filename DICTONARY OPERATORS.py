print("\t\tDICTIONARY OPERATORS")
print("\t\t--------------------")
my_dict={"Name":"Pooja","Age":"24","City":"Paris"}
my_dict=dict(Name="Pooja",Age="24",City="Paris")
print("\ninitally,my_dict:",my_dict)
print("\nmy_dict[name]:",my_dict["Name"])
print("update age as 30 in my_dict")
my_dict["Age"]=30
print("\nNow my_dict:",my_dict)
print("delete the city in my_dict")
del my_dict["City"]
print("\nNow my_dict:",my_dict)
print("Name"in my_dict)
my_dict["Name"]
print("\nAddress in my_dict:")
print("Address" in my_dict)
print("\nKey in my_dict:")
for Key in my_dict:
    print(Key)
    print("\nValue in my_dict:")
for values in my_dict.values():
    print(values)
    print("\nKey in my value pair in my_dict:")
for key,value in my_dict.items():
    print(key,value)
    print("\nNow no of values in my_dict:")
    print(len(my_dict))
    

    
