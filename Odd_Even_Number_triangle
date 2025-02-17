start_no = 1            # Start Number for the lists
max_row_numb = 10       # Maximum Number of Rows to be printed
#no_of_items = row_numb
even_list = list()
odd_list = list()
n_odd = 0               # Place holder variable for 'Odd'
n_even = 0              # Place holder variable for 'Even'

for loop_iteratn_num in range(max_row_numb):    # Prepare lists of odd/even numbers (rows of even and odd numbers)
    odd_list.append(start_no +2*loop_iteratn_num)    #For every loop_iteratn_num add '2' to the first number (start_no) and create odd list
    even_list.append(start_no + 2*loop_iteratn_num + 1) ##For every loop_iteratn_num add '1' to the odd_list and create even list

for loop_iteratn_num in range(max_row_numb):

    if((loop_iteratn_num + 1) % 2) == 1:         # Items = Odd (For 'odd Iteration number')

        row_index_odd = (n_odd)*(n_odd) + 1     # Generate the  sequence of 'indices' of Odd_list to generate the 'list' of 'Odd numbers' for this 'loop_iteratn_num'
        print(odd_list[row_index_odd - 1: row_index_odd + loop_iteratn_num])     # OKAY!
        n_odd = n_odd + 1                       # Increment 'n_odd' for next iteration

    if((loop_iteratn_num + 1) % 2) == 0:

        row_index_even = (n_even+1)*(n_even+1)-n_even
        print(even_list[row_index_even - 1: row_index_even + loop_iteratn_num])
        n_even = n_even + 1                     # Increment 'n_even' for next iteration

