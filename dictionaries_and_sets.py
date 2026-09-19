# dictionary and sets
info={
    "key":"valve",
    "name":"shazia",
    "gpa":"9.2",
}
print(info)# ham apny value ka andar  lists ko b store kar skty hai


info={
    "name":"shazia",
    "marks":["uu","try","fdfg"],
    "learning":"paython",
}
print(info)
# key hamaysha koi string honachaya ya numbr but valaue mai koi b data type  acceptable  hai mtlb key ka anadr koi immutable data type hona chaya but valave mai allmutable hona chaya types 
# nested dictionarry
name={
    "value":77,
   "marks":{
        "phy":45,
        "chmy":88,
        "maths":90,

    }
}
print(name.keys())# returns all the keys
print(list(name.values()))# returun all the  vales
print(name.items())# returns all the valuea and keys 
# sets practices questions
dictionary={
    "cat" : "a samll animal",
    "table" : ["a pice of furniture","list of facts and figures"]
}
print(dictionary)
sets={
    "python","java script","java","python","c++","c++","c",
    "python","java","java"
}
print(sets)
print(len(sets))
marks={}# empty dictionary
x=int(input("enter phy:"))
marks.update({"phy":x})
x=int(input("enter maths:"))
marks.update({"maths":x})
x=int(input("enter chemst:"))
marks.update({"chemst":x})
print(marks)













