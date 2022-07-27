
# Implement search, short & Delete operations on array of integers

# Delete operations--->
# arr_size = int(input("Enter the size of array : "))
# arr = []
# print(f'Enter {arr_size} Elements : ')
# for i in range(arr_size):
#     arr.append(input())
# print("Enter the value you want to delete : ")

# val = input()
# if val in arr:
#     arr.remove(val)
#     print("The new array is : ")
#     for i in range(arr_size-1):
#         print(arr[i],end=" ")
# else:
#     print("Element doesn't exist in the array!")



# Short operations----->

arr = [1,33,2,60,20,50,31,11,7]
temp = 0

# Displaying elements of original array
print("Elements of original array : ")
for i in range(0,len(arr)):
    print(arr[i],end=" ")

# Short the array in ascending order
for i in range(0,len(arr)):
    for j in range(i+1, len(arr)):
        if(arr[i]> arr[j]):
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp

# Display elements of the array after sorting
print("\nElements of array sorted in ascending order : ")
for i in range(0,len(arr)):
    print(arr[i], end=" ")