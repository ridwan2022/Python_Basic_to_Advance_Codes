"""
student={
    "name":"bari",
    "age": 20
}
print(student["age"])
student["age"]= 22

print(student["age"])

student.update({
    "cgpa": 3.92,
    "blood group": "a+"
})

print(student)
print(student.keys())
print(student.values())

for i in student:
    print(student[i])

if "sumu" in student.values() or "baroi" in student.values():
    print("name is registered")
else:
    print("name is not registered")

student2= student.copy()
print(student2)

"""
# dynamicDick = {
#     19: {"name": "bari","age":20,"cgpa":3.92},
#     24: {"name": "sumu","age":19,"cgpa":4.00},
#     39: {"name": "tanvir","age":25,"cgpa":5.00, "marks":[5,6,7]}
# }

#print(dynamicDick[39]["name"])
#print(dynamicDick[39]["marks"][1])

# for roll, info in dynamicDick.items():
#     print("id:",roll)
#     for key, value in info.items():
#         print(key,':',value)

# Problem 1
# Create a dictionary of 5 students and their marks.
# Print the student with the highest marks.

student2 = {
    "s1":{"name": "abdul" ,"marks":10},
    "s2":{"name": "rahim" ,"marks":20},
    "s3":{"name": "bulbul" ,"marks":30},
    "s4":{"name": "shakir" ,"marks":40},
    "s5":{"name": "jabbar" ,"marks":50},
}
# for value in student2.values():
#print(student2["s1"]["marks"])

# for x in student2:
#     print(student2[x]['name'])

#x can be integer also it can be character
# # printing highest marks METHOD 1

# val = []
# for x in student2:
#     val.append([student2[x]['marks']])
# highest = max(val)
# print(highest)

# # printing highest marks METHOD 2
# highest_marks = max(student2[x]["marks"] for x in student2)
# print(highest_marks)


# # printing highest marks METHOD 3
largest = 0
for x in student2:
    if largest < student2[x]["marks"]:
        largest = student2[x]["marks"]
print(largest) 