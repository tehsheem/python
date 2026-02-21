info = {
    "key" : "value",
    "name": "itachi",
    "learning" : "coding",
     "age" : 54 ,
     "subjects" : ["c", "python", "java"],
     "topics" : ("dict", "sets")
}
# print(info["name"])
# print(info["topics"])
# info["name"] = "Kakashi"
# info["salary"] = 1000
# print(info)

dict = {
    "name" : "Itachi",
    "subject" : {
        "phy" : 90,
        "chem" : 88,
        "phython" : 100
    }
}
dict.update({"specail" : "kamui"})
print(dict)
