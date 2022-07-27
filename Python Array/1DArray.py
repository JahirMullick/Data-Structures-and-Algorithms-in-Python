num = input("How many element to store inside the array : ")
arr = []
print("\nEnter ",num," Element : ")
num = int(num)
for i in range(num):
    element = input()
    arr.append(element)
print("\nThe array elements are :")
for i in range(num):
    print(arr[i],end=" ")
