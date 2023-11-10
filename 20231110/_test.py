# print('Coord : {y} {y} {x}'.format(x='444', y='222'))
# # print('Coord : {} {} {x}'.format(x='444', y='222'))

print('{:*<30}'.format("hello world!"))
# print('{:*>30}'.format("hello world!"))
# print('{:30}'.format(11111111111111111111))
# # ppt '는 구분하려고 넣은 거?

# # f-string -> built in 나중에 나왔는데 왜?

# # print(f'{3.14:+o}')
# print(f'{3.14:+f}')
# print(f'{1234567890:,}')
# print(f'{1234567890:#x}')


# bug = 'ddd'
# print(f"Debugging {bug=}{bug=}{bug}")
# print(f"{'Debugging':*^30}")

# file = open('my_file.txt', 'w')
# file.write("드디어 쓸모 있어보이는 것을 배운다.\n")
# file.close()

# with open('my_file.txt', 'w') as file:
#     file.write("드디어 쓸모 있어보이는 것을 배운다.\n")
#     file.write("드디어 쓸모 있어보이는 것을 배운다.\n")


# file = open('my_file.txt', "a")
# file.write("후훗\n")

# file.close()

# write가 아니라 바로 쓰고 싶을 때 flush

with open("test.txt", 'w') as file:
    file.write("1234\n5678\n1234\n5678")

with open("test.txt", 'r') as file:
    print(file.readline())
    print(file.read())
