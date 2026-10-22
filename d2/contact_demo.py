contact = {}
print("欢迎使用通讯录")
while True:
    print("\n -- 菜单 --")
    print("1.添加联系人")
    print("2.查看所有联系人")
    print("3.退出")
    choice = input("请输入你的选择(1/2/3): ")
    if choice == "1":
        name= input("请输入联系人姓名: ")
        phone = input("请输入联系人电话: ")
        contact[name] = phone
        print("联系人添加成功!{name}已保存")

    elif choice == "2":
        print("\n当前通讯录：")
        if len(contact) == 0:
            print("快去添加联系人吧！")
        else:
            for name, phone in contact.items():
                print(f"姓名: {name}, 电话: {phone}")
    elif choice == "3":
        print("退出通讯录")
        break
    else:
        print("无效的选择，请重新输入")
        