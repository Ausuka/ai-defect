names = ["张三","李四","王五"]
for name in names:
    print("你好"+name)
print("------------------")          

count = 1
while count <= 3:
    print("这是第",count,"次循环".format(count))
    count = count + 1