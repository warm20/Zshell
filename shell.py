import socket as skt # 实现team功能
import os

# SHL基础变量
token = []
path = "C:/"

# 初始化
os.system("cls")

# 文档定义-1
"""
0 os error (such as file already exists)
1 exit
2 ok
3 cmdError
"""

# 函数定义
def SHL():
    global token,path
    try:
        line = input(f"{path}~ $ ")
        token = line.split(" ")
        if token[0] == "exit": return 1
        if token[0] == "mkdir":
            creat = 0
            if len(token)<2: 
                print("cmd error")
                return 3
            if os.path.exists(path+token[1]) and creat == 0:
                print("file already exists")
                return 0
            elif len(token)>=2 and not os.path.exists(path+token[1]):
                os.mkdir(path+token[1])
                creat = 0
                print("success")
                return 2
        elif token[0] == "cd":
            if len(token)<2: 
                print("cmd error")
                return 3
            if token[1] == "../":
                cdlist = path.split("/")[]

            if token[1][0] == "." and token[1][1] == "/":
                token[1] = path+token[1][2:]+"/"
            if os.path.exists(token[1]) and len(token)>=2:
                path = token[1]
                print("success")
                return 2
            if not os.path.exists(token[1]):
                print("file not creat")
                return 0
    except:
        return 1

def main():
    while True:
        if SHL() == 1:  break

if __name__ == "__main__":
    main()

os.system("cls")