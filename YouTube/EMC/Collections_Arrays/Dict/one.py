#Dict {} is a collection, which is orderde and changable no dulicate members
# Do not allow duplicate, duplicate value will overwrite existing value 
# Any type of data can be stored 
# Key:Value pair {"Name":"Vasu"} 
# get(), keys(), values(), items() 
# update({"Year":"2000"}), thisdict ["color"]="red", This dict.pop("Model"), del(), clear()

#CRUD
#Create
a={
    "Name":"Vasu",
    "Age":23,
    "Qulification":"BBA",
    "From":"Chennai",
    "Location":"Bangalore"
}
#Read
print(a)

#Update
#Modify
a["Age"]=24
a["Color"]="Blue"
a["JobRole"]="MERN Devloer"
print(a.keys())
print(a.values())
print(a.items())

#Delete
a.pop('Age')
del a["From"]
print(a)