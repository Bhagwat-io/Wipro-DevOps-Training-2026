# f=open("greeting.tx","w") if no file is available it wwill create automatically files 
# f.write("my name is murali and i am corporate trainer  ")
# f.close()
# f=open("greeting.tx","a") # append
# f.write("\n Dealing now python ")
# f.close()

# read() --> read all the data in single time keep in memory buffer

# f=open("greeting.tx","r")
# contenet=f.read()
# print(contenet)
# f.close()

#readline() readd line by line
# f=open("greeting.tx","r")
# print(f.readline())
# print(f.readline())
# f.close()

#readlines() --retun list 

# f=open("greeting.tx","r")
# lines=f.readlines() #it should consider each line as one single lement in the list as having indesx
# print(lines[1])
# f.close()

# with statement  context manager
    #automatically file will be closed 
    #avoids forgetting close()

# with open(r"C:\Users\babud\Downloads\questionpaper.txt","r") as file:
#     # for f in file:
#     #     print(f,end='')
#     print(file.read(1000)) # read only 100 characters 

# readd the file take only answers and save them into another file 

with open(r'..\questionpaper.txt','r') as readfile: #realative  path mention only directory parent
    for line in readfile:
        if line.startswith('Answer') is True:
            with open(r'..\answer.txt','a') as appendfile:
             appendfile.write(line)