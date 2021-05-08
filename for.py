# for语句
# ==================================================
# c = 0
# a = "123456789"
# for i in a:
#     print(i)
#     c=c+1
# print(c)

# ==================================================

# for i in range(1,10):
#     print(i)

# ==================================================
# a = [1,2,3,4,56,7,8,9]
# for i in range(len(a)):
#     print(a[i])

# ==================================================
# 遍历字典
# account = [{"username":"zhangy","password":"123456"},{"username":"hehm","password":"123456"}]

# regusername = input("请输入username：")
# regpassword = input("请输入password：")

# time = 1
# for a in account:
#     username = a["username"]

#     if regusername == username:
#         print("用户名已存在")
#         break

#     else:
#         if time == len(account):
#             account.append({"username":regusername,"password":regpassword})
#             print("注册成功")
#             break
#         else:
#             time = time + 1
# print(account)

# ==================================================
# while语句，continue语句
# a=5
# while a>0:
#     a = a-1
#     if a==3:
#         continue
#     if a<0:
#         break
#     print("a={}".format(a))