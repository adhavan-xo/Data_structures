r_num = int(input())
c_num = int(input())
two_d =[[[i*j for i in range(c_num)] for j in range(r_num)]]

# for i in range(r_num):
#     for j in range(c_num):
#         two_d[i][j] = i*j
print(two_d)