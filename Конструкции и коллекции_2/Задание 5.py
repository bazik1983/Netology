my_list = ['a', 'b', 'c', 'd', 'e', 'f']
vl = my_list[-1]
for i in my_list[-2::-1]:
  vl = { i: vl }
print(vl)