# f = open("demo.txt", "r")
# data = f.readline()
# print(data)
# data1 = f.readline()
# print(data1)
# f.close()

# f = open("demo.txt", "a")
# f.write("\naa")
# f.close

# f = open("demo.txt", "a+")
# f.write("ab")
# print(f.read())
# f.close()

# with open("demo.txt", "r") as f:
#     print(f.read())

import os

# os.remove("demo.txt")

# with open("demo.txt", "r") as f:
#     data = f.read()
# newdata = data.replace("java", "python")

# with open("demo.txt", "w") as f:
#     f.write(newdata)

count = 0
with open("demo.txt", "r") as f:
    data = f.read()

num = data.split(",")
for val in num:
    if(int(val)%2 == 0):
        count += 1
print(count)