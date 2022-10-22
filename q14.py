print("Program to find max_element in list")
print("\n")

my_list = [1,23,45,6,7,89,98,0]

max_element = 0
for i in my_list:
    if(i >= max_element):
        max_element = i

print("Maximum element in list: ", max_element)
