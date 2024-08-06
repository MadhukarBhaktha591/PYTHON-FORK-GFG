#06ListOfTupleToDictionary.py

#method1 use setdefault()

def Convert(tup, di):
    for a, b in tup:
        di.setdefault(a, []).append(b)
    return di

tups = [("akash", 10), ("gaurav", 12), ("anand", 14), 
     ("suraj", 20), ("akhil", 25), ("ashish", 30)]
dictionary = {}
print (Convert(tups, dictionary))

#example2
list_1=[("Nakul",93), ("Shivansh",45), ("Samved",65),
           ("Yash",88), ("Vidit",70), ("Pradeep",52)]
dict_1=dict()
for student,score in list_1:
    dict_1.setdefault(student,[]).append(score)
print(dict_1)

#method2: Use of dict() method

def Convert(tup,di):
    di=dict(tup)
    return di

tups = [("akash", 10), ("gaurav", 12), ("anand", 14), 
    ("suraj", 20), ("akhil", 25), ("ashish", 30)]
dictionary = {}
print (Convert(tups, dictionary))

# Python code to convert into dictionary
print (dict([('Sachin', 10), ('MSD', 7), ('Kohli', 18), ('Rohit', 45)]))