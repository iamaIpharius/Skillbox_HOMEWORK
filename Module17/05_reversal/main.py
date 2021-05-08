S = input('Введите строку: ')

list_of_h_index = []


for i in range(len(S)):
    if S[i] == 'h':
        list_of_h_index.append(i)


start = S[:list_of_h_index[0] + 1]
mid = S[list_of_h_index[0] + 1:list_of_h_index[1]]
mid_rev = mid[::-1]
end = S[list_of_h_index[1]:]
print(list_of_h_index)
print(start + mid_rev + end)
