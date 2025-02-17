

# Find if the given array is a mountain array with only 1 peak
# Mountain array is an array where the element values increases, reaches a peak, and then decreases

int_array = [1, 2, 3, 5, 4, 2, 0]
length_int_array = len(int_array)
second_array = []

for subtraction_element in range(length_int_array):
    second_array_element = int_array[subtraction_element + 1] - int_array[subtraction_element]
    second_array.append(second_array_element)

#sign_change_array = []

#for sign_change_element in range(len(second_array)):
#    if sign_change_element > 0:
#        sign_change_value = second_array[sign_change_element + 1] - second_array[sign_change_element]
#        sign_change_array.append(sign_change_value)

#int_array = [1, 2, 3, 5, 4, 2, 0]

#second_array = [1, 1, 2, -1, -2, -2]

#second-sub = [0, 1, -3, -1, 0]

