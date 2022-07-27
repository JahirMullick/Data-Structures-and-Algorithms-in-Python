row_num = int(input("Input number of rows :"))
column_num = int(input("Input number of columns :"))

# Assign values that is given by the user
twod_arr = [[0 for col in range(column_num)] for row in range(row_num)]

for row in range(row_num):
    for col in range(column_num):
        twod_arr[row][col] = row * col
print(twod_arr)