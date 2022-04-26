import os

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)
us='X'
enemy='O'
matrix=[[' ',' ',' '],
        [' ',' ',' '],
        [' ',' ',' ']]
Result=0
br=1
def Board():
    print("%c | %c | %c" % (matrix[0][0],matrix[0][1],matrix[0][2]))
    print("---------")
    print("%c | %c | %c" % (matrix[1][0],matrix[1][1],matrix[1][2]))
    print("---------")
    print("%c | %c | %c" %(matrix[2][0],matrix[2][1],matrix[2][2]))
def Taken(matrix,position,us,enemy):
    column=position//3
    row=position%3
    if(matrix[column][row]==' '):
        if(br%2==0):
            matrix[column][row]=us
            return 1
        else:
            matrix[column][row]=enemy
            return 1
    else:
        return 0   
def Condition(position):
    i=position//3
    j=position%3
    Result=1
    for n in range(3):
            for k in range(3):
                if matrix[n][k]==' ':
                    Result=0
    if(matrix[0][0]==matrix[1][1]==matrix[2][2]!=' '):
        return 1
    elif(matrix[0][2]==matrix[1][1]==matrix[2][0]!=' '):
        return 1
    elif(matrix[i][0]==matrix[i][1]==matrix[i][2]!=' '):
        return 1
    elif(matrix[0][j]==matrix[1][j]==matrix[2][j]!=' '):
        return 1
    
    if Result==1:
        return 2
    return 0
def ConditionAI(position,matrix,side):
    i=position//3
    j=position%3
    if((side==matrix[0][0]==matrix[1][1]!=' ' or side==matrix[0][0]==matrix[2][2]!=' ' or side==matrix[1][1]==matrix[2][2]!=' ') and i==j):
        if matrix[0][0]==matrix[1][1]:
            position=8
            return position
        if matrix[0][0]==matrix[2][2]:
            position=4
            return position
        if matrix[2][2]==matrix[1][1]:
            position=0
            return position
    if((side==matrix[0][2]==matrix[1][1]!=' ' and j==i-2) or (side==matrix[2][0]==matrix[0][2]!=' ' and i==j==1)  or (side==matrix[1][1]==matrix[2][0]!=' ' and i==j-2)):
        if matrix[0][2]==matrix[1][1]:
            position=6
            return position
        if matrix[2][0]==matrix[0][2]:
            position=4
            return position
        if matrix[2][0]==matrix[1][1]:
            position=2
            return position
    if((side==matrix[i][0]==matrix[i][1]!=' ' or side==matrix[i][1]==matrix[i][2]!=' ' or side==matrix[i][0]==matrix[i][2]!=' ')):
        position=i*3+j
        return position
    if((side==matrix[0][j]==matrix[1][j]!=' ' or side==matrix[1][j]==matrix[2][j]!=' ' or side==matrix[0][j]==matrix[2][j]!=' ')):
        position=i*3+j
        return position
    Result=1
    for n in range(3):
            for k in range(3):
                if matrix[n][k]==' ':
                    Result=0
    if Result==1:
        return side
    return side
def Chances(br,position,us,enemy,matrix):
    chance=[[0,0],[0,0],
            [0,0],[0,0],
            [0,0],[0,0],
            [0,0],[0,0],
            [0,0]]
    points=[[3,0,3],
            [0,0,0],
            [3,0,3]]
    if matrix[1][1]=='X':
        points=[[5,0,5],
                [0,0,0],
                [5,0,5]]
    if matrix[1][1]=='X' and enemy=='X' and matrix[0][0]=='O':
        points=[[5,0,5],
                [0,0,0],
                [5,0,6]]
    elif matrix[1][1]=='X' and enemy=='X' and matrix[2][2]=='O':
        points=[[6,0,5],
                [0,0,0],
                [5,0,5]]
    elif matrix[1][1]=='X' and enemy=='X' and matrix[2][0]=='O':
        points=[[5,0,6],
                [0,0,0],
                [5,0,5]]
    elif matrix[1][1]=='X' and enemy=='X' and matrix[0][2]=='O':
        points=[[5,0,5],
                [0,0,0],
                [6,0,5]]
    if matrix[1][1]=='O' and enemy=='O':
        points=[[2,0,2],
                [0,0,0],
                [2,0,2]]
    for i in range(3):
        for j in range(3):
            if(i<2):
                if(matrix[i+1][j]==' '):
                    points[i][j]+=2
                elif(matrix[i+1][j]==enemy):
                    points[i][j]+=1
                elif(matrix[i+1][j]==us):
                    points[i][j]+=1
                if(j>0):
                    if(matrix[i+1][j-1]==' '):
                        points[i][j]+=2
                    elif(matrix[i+1][j-1]==enemy):
                        points[i][j]+=1
                    elif(matrix[i+1][j-1]==us):
                        points[i][j]+=1
                if(j<2):
                    if(matrix[i+1][j+1]==' '):
                        points[i][j]+=2
                    elif(matrix[i+1][j+1]==enemy):
                        points[i][j]+=1
                    elif(matrix[i+1][j+1]==us):
                        points[i][j]+=1
            if(j<2):
                if(matrix[i][j+1]==' '):
                    points[i][j]+=2
                elif(matrix[i][j+1]==enemy):
                    points[i][j]+=1
                elif(matrix[i][j+1]==us):
                    points[i][j]+=1
            if(i>0):
                if(matrix[i-1][j]==' '):
                    points[i][j]+=2
                elif(matrix[i-1][j]==enemy):
                    points[i][j]+=1
                elif(matrix[i-1][j]==us):
                    points[i][j]+=1
                if(j<2):
                    if(matrix[i-1][j+1]==' '):
                        points[i][j]+=2
                    elif(matrix[i-1][j+1]==enemy):
                        points[i][j]+=1
                    elif(matrix[i-1][j+1]==us):
                        points[i][j]+=1
            if(j>0):
                if(matrix[i][j-1]==' '):
                    points[i][j]+=2
                elif(matrix[i][j-1]==enemy):
                    points[i][j]+=1
                elif(matrix[i][j]==us):
                    points[i][j]+=1
                if(i>0):
                    if(matrix[i-1][j-1]==' '):
                        points[i][j]+=2
                    elif(matrix[i-1][j-1]==enemy):
                        points[i][j]+=1
                    elif(matrix[i-1][j-1]==us):
                        points[i][j]+=1
            if(matrix[i][j]!=' '):
                points[i][j]=0
    max=0
    k=0
    for i in range(3):
        for j in range(3):
            if(max<points[i][j]):
                max=points[i][j]
    for i in range(3):
        for j in range(3):
            if(max==points[i][j]):
                chance[k][0]=i
                chance[k][1]=j
                k+=1
    import random
    ch=random.randrange(0,k)
    print(ch)
    position=chance[ch][0]*3+chance[ch][1]
    return position
def Decision(br,matrix,us,enemy):

    for n in range(3):
        for k in range(3):
            position=n*3+k
            if(matrix[n][k]==' ' and ConditionAI(position,matrix,enemy)!=enemy):
                position=ConditionAI(position,matrix,enemy)
                return position
    for n in range(3):
        for k in range(3):
            position=n*3+k
            if(matrix[n][k]==' ' and ConditionAI(position,matrix,us)!=us):
                position=ConditionAI(position,matrix,us)
                return position
    for n in range(3):
        for k in range(3):
            position=Chances(br,position,us,enemy,matrix)
            return position
#Start from the user's perspective
c=int(input("Do you want to play versus human or A.I. : 1-Human 2-A.I. "))
if c==2 :
    br=int(input("Which one goes first?: 1-You 2-A.I. "))
    if(br%2==0):
        us='O'
        enemy='X'
    
    while(Result==0):
        if(br%2==0):
            position=Decision(br,matrix,us,enemy)
            br+=1
            if(Taken(matrix,position,us,enemy)==0):
                br+=1
            else:
                os.system('cls')
                clearConsole()
                Board()
            if Condition(position)==2:
                    Result=1
                    print("Le Draw! Both sides performed well")
            elif Condition(position)!=0: 
                if(br%2==0):
                    print("player 1 won! Thanks for playing-")
                else:
                    print("player 2 won! Thanks for playing-")
                Result=1
            else:
                print("The battle goes on. . .")
        else:
            position=int(input("Choose marking position[1-9]: "))
            position=position-1
            br+=1
            os.system('cls')
            clearConsole()
            if(Taken(matrix,position,us,enemy)==0):
                br+=1
                os.system('cls')
                clearConsole()
                print("This position is already taken, champ :)")
            Board()
            if Condition(position)==2:
                    Result=1
                    print("Le Draw! Both sides performed well")
            elif Condition(position)!=0:
                if(br%2==0):
                    print("player 1 won! Thanks for playing-")
                else:
                    print("player 2 won! Thanks for playing-")
                Result=1
            else:
                print("The battle goes on. . .")
#Broqch za sledene na hodovete
elif c==1:
    while(Result==0):
        position=int(input("Choose marking position[1-9]: "))
        position=position-1
        br+=1
        if(Taken(matrix,position,us,enemy)==0):
            br+=1
            os.system('cls')
            clearConsole()
            print("This position is already taken, champ :)")
        
        os.system('cls')
        clearConsole()
        Board()
        if Condition(position)==2:
                    Result=1
                    print("Le Draw! Both sides performed well")
        elif Condition(position)!=0: 
            if(br%2==0):
                print("player 1 won! Thanks for playing-")
            else:
                print("player 2 won! Thanks for playing-")
            Result=1
        else:
            print("The battle goes on. . .")
