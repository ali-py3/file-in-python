# r --> read
# w --> write
# a --> append
# x --> create
#######################################
# file = open('name of the file','mode')
# file.close()
#######################################
# file = open('test.txt','x')
# file.close()

# a = input("enter your name = ")
# file = open('test.txt','w')
# file.write(' programmer')
# file.close()

# appends = input("enter your name = ")
# file = open('test.txt','a')
# file.write('\n'+appends)
# file.close()

# file = open('test.txt','r')
# out = file.read()
# out = file.readline(3)
# out = file.readlines()
# print(out)
# print(file.mode)
# file.close()
# print(file.closed)
#######################################
# with open('name of the file','mode') as file:
#######################################
# with open('test.txt','r') as file:
#     print(file.read())
#######################################
myList = ['spydev','Pr','vala','pzk']
with open('MyList.txt','x') as file:
    with open('MyList.txt','w') as wfile:
        for item in myList:
            wfile.write(item+'\n')
    with open('MyList.txt','r') as rfile:
        print(rfile.read())
        