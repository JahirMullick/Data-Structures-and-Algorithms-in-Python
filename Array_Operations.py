
# Implement search, short & Delete operations on array of integers

# Delete operations--->
arr_size = int(input("Enter the size of array : "))
arr = []
print(f'Enter {arr_size} Elements : ')
for i in range(arr_size):
    arr.append(input())
print("Enter the value you want to delete : ")

val = input()
if val in arr:
    arr.remove(val)
    print("The new array is : ")
    for i in range(arr_size-1):
        print(arr[i],end=" ")
else:
    print("Element doesn't exist in the array.")