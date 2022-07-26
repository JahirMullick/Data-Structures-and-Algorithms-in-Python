from multiprocessing.sharedctypes import Value


employee = {
    1: "Rohan", 2: "Ayan", 3: "Mijanur", 4: "Meraj", 5:"Taslim", 6: "Hamid"
}

# print(employee)

# if employee.
for key, value in employee.items():
    # print(employee.get(key))
    print(key," ",value)
    if (key == 3):
        employee.pop(3)
    
print(employee)