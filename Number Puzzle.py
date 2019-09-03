import os
import msvcrt
import time
#list1=[['-',1,2,3],[4,5,6,7],[8,9,10,11],[12,13,14,15]]
chec=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
count=0
list1= [['-',1,2],[3,4,5],[6,7,8]]
import os
def random():
    import random
    global list1
    random.shuffle(list1)
    for i in range(len(list1)):
        random.shuffle(list1[i])
    for i in range(len(list1)):
        for j in range(len(list1)):
            print(list1[i][j],"\t",end="")
        print("\n")
    return list1
li=random()
while True:
    pos1=[]
    for i in range(len(li)):
        for j in range(len(li[i])):
            if li[i][j]=="-":
                pos=[i,j]
                break
    if msvcrt.kbhit():
        count=count+1
        a=msvcrt.getch()
        if str(a)=="b'w'" and pos[0]-1>=0:
            pos1=[pos[0]-1,pos[1]]
        elif str(a)=="b's'" and pos[0]+1<=len(li)-1:
            pos1=[pos[0]+1,pos[1]]
        elif str(a)=="b'a'" and pos[1]-1>=0:
            pos1=[pos[0],pos[1]-1]
        elif str(a)=="b'd'" and pos[1]+1<=len(li)-1:
            pos1=[pos[0],pos[1]+1]
        else:
            pos1=pos
            print("invalid move")
            time.sleep(1)
            count=count-1
        os.system("cls")
        if(pos[0]+1==pos1[0]and pos[1]==pos1[1])or(pos[0]==pos1[0]and pos[1]+1==pos1[1])or(pos[0]-1==pos1[0]and pos[1]==pos1[1]) or(pos[0]==pos1[0]and pos[1]-1==pos1[1]):
            li[pos[0]][pos[1]],li[pos1[0]][pos1[1]]=li[pos1[0]][pos1[1]],li[pos[0]][pos[1]]
        for i in range(len(li)):
            for j in range(len(li)):
                print(li[i][j],"\t",end="")
            print("\n")
        print("Number of moves done",count)
        if(li[0][0]==1 and li[0][1]==2 and li[0][2]==3 and li[1][0]==4 and li[1][1]==5 and li[1][2]==6 and li[2][0]==7 and li[2][1]==8 and li[2][2]=='-'):
            print("CONGRATULATIONS!!!!! \nYOU WON THE GAME!!!!  ")
     
        
        
