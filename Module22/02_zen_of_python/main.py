zen = open('zen.txt', 'r')

zen_list = [i for i in zen]
zen_list.reverse()
for i in zen_list:
    print(i)
    
zen.close()