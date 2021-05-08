nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
             [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]

new_list = [nice_list[step_1][step_2][step_3] for step_3 in range(3) for step_2 in range(3) for step_1 in range(2)]
print(new_list)
