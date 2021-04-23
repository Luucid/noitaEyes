from eyeData import allTables as tbl
import matplotlib.pyplot as plt
import numpy as np



plt.axis([-31, 88,-18, 38])  #same distance between each row.
# plt.grid('k', linestyle='-', linewidth=0.3)

######################################################################################################################################################
######################################################################################################################################################
######################################################################################################################################################
    
#####to change markers, change the symbol before the letter in color, e.g for green circle, 'og'
#####view markers here https://matplotlib.org/stable/api/markers_api.html

eyeDirection = {'sc':0, 'sg':1, 'sr':2, 'sb':3, 'sk':4 }  
color = ['r', 'g', 'b', 'k', 'y']
marker = ['.', '.', '.', '.', '.']

tableList = []
dirList = []
colorList = []
alphaList = []

def changeColor(dirList):   
    available = ['r', 'g', 'b', 'c', 'y', 'm', 'k', 'w']
    clr = ['r', 'g', 'b', 'k', 'y']
    mks = np.array(['.r', '.r', '.r', '.r', '.r'])
    
    direction = {0:'center', 1:'up', 2:'right', 3:'down', 4:'left'}
    print("\n--------------------------------------")
    print("available colors: ", end='')
    for i in available: print(i, end=' ')
    print("\n--------------------------------------\n")
    
    
    for i in range(len(clr)):
        if(dirList[i]):
            clr[i] = input("choose %s eye color: " % direction[i])
            while(clr[i] not in available):
                clr[i] = input("color not available, please select available color (r, g, b, c, y, m, k, w): ") 
            color[i] = clr[i]   
            
    
    changeMarker(dirList)
    for i in range(5):
        mks[i] = marker[i]+color[i]
        
    
    return mks


    
def changeMarker(dirList):
    available = [',', '.', 'o', 'v', '^', '<', '>', '*', 
                 '1', '2', '3', '4', '8', 's', 'p', 'P', 
                 'h', 'H', '+', 'x', 'X', 'd', 'D', '|', '_']


    mark = ['.', '.', '.', '.', '.']
    direction = {0:'center', 1:'up', 2:'right', 3:'down', 4:'left'}
    
    print("\n--------------------------------------")
    print("description found at: https://matplotlib.org/stable/api/markers_api.html \n")
    for i in available: print(i, end=' ')
    print("\n--------------------------------------\n")
    
    
    for i in range(len(mark)):
        if(dirList[i]):
            mark[i] = input("choose %s eye symbol: " % direction[i])
            while(mark[i] not in available):
                mark[i] = input("symbol not available, please select available symbol: ") 
            marker[i] = mark[i]
        
    


    
    

    

def plot(xc, yc, alp, xShift, clr):
    if(yc%2 != 0):
        plt.plot((xc+xShift), yc, clr, alpha=alp)
    else:
        plt.plot(xc, yc, clr, alpha=alp)
        
        

def plotEyeTable(table, c, u, r, d, l, alp=0.3):
    xc = 0
    xShift = 0.5        #How much every second row is shifted to the right, 0.5 is how it is displayed in game.   
    
    # yc = len(table)       #to start plotting at the specified tables own height.
    yc = 12               #to start plotting all tables at y = 12.
    
    # color = {'.c':0, '^g':1, '>b':2, 'vr':3, 'sk':4 } #shapes matching eye direction   
    clr = ['.c', '^g', '>b', 'vr', 'sk'] #here you can customize the colors and markers.
    
    
    
   
        
    for i in table:
        xc = 0
        for j in i:
            # alp = alphaReset
            if (c and j == 0):       #to change alpha on only one direction, remove 'not' and set alp to something between 0-1.
                plot(xc, yc, alp, xShift, clr[j])
            elif (u and j == 1):
                plot(xc, yc, alp, xShift, clr[j])
            elif (r and j == 2):
                plot(xc, yc, alp, xShift, clr[j])
            elif (d and j == 3):
                plot(xc, yc, alp, xShift, clr[j])
            elif (l and j == 4):
                plot(xc, yc, alp, xShift, clr[j])
            xc+=1
        yc-=1
                
               
  
def plotTables():
    xc = 0
    xShift = 0.5        #How much every second row is shifted to the right, 0.5 is how it is displayed in game.   
    # yc = len(table)       #to start plotting at the specified tables own height.
    yc = 12               #to start plotting all tables at y = 12.    
    alpTemp = 0.5
   
    direction = [False, False, False, False, False] #c, u, r, d, l = False
    dirLib = {0:'center', 1:'up', 2:'right', 3:'down', 4:'left'}
    alp = [0, 0, 0, 0, 0]
     
    run = True
    table = ''
    
    
    
    while(run):
  
        table = input("select table to print, type 'exit' to quit: ")
        
        while(table not in tbl and table != 'exit'):
            table = input("tables does not exist, pelase select table to print, type 'exit' to quit: ")
        if(table=='exit'):
            run = False
            
        if(run):   
            tableList.append(tbl[table])     
            
            for i in range(len(direction)):
                c = input("Do you want to plot %s eyes? (y/n): " %dirLib[i])
                while(c != 'y' and c != 'n'):
                    c = input("Do you want to plot %s eyes? (y/n): " %dirLib[i])
                if(c == 'y'):
                    direction[i] = True
                else:
                    direction[i] = False
            dirList.append(direction)
 
            tmpColorList = changeColor(direction)
            colorList.append(tmpColorList)
             
            for i in range(5):
                if(direction[i] == True):
                    alpTemp = input("please select %s eye's alpha(between 0 and 1): " % dirLib[i])
                    while(alpTemp.isdigit() == False):
                        alpTemp = input("please select %s eye's alpha(between 0.0 and 1.0): " % dirLib[i])
                    alpTemp = float(alpTemp)
                    if(alpTemp <= 0):
                        alpTemp = 0.0
                    elif(alpTemp >= 1):
                        alpTemp = 1.0
                    
                    alp[i] = alpTemp
                    
            
            alphaList.append(np.array(alp.copy()))
        
     
    for n in range(len(tableList)):
        yc = 12 
        for i in tableList[n]:
            xc = 0
            for j in i:   
                if (dirList[n][j]):       
                    plot(xc, yc, alphaList[n][j], xShift, colorList[n][j])
                
                xc+=1
            yc-=1
                
        
          
###########################TRIAGRAMS###################################  
                


def genTri(msg, base='x'):
    msgLen = 0
    for row in msg:
        for i in row:
            msgLen+=1
    

    trig = np.array([[0, 0, 0]]* (msgLen//3))
    r = 0    
    c = 1
  
    
    for i in range(1, len(msg), 2):
        c = 1
        while(c < len(msg[i-1]) and c < len(msg[i])):
           
            if(r % 2 == 0): #even
                trig[r][1] = msg[i-1][c]                
                trig[r][0] = msg[i-1][c-1]
                trig[r][2] = msg[i][c-1]
       
            else: #odd             
                trig[r][1] = msg[i][c]                
                trig[r][0] = msg[i][c+1]
                trig[r][2] = msg[i-1][c+1]                 
                c += 3                
            
            r += 1         
            
    if(trig[-1][0] == 0 and trig[-1][1] == 0 and trig[-1][2] == 0):
        trig[-1][1] = msg[-2][c]               
        trig[-1][0] = msg[-2][c-1]
        trig[-1][2] = msg[-1][c-1]
    
    if(base == 'b5'):
        return base5(trig)
    elif(base == 'b10'):
        return base10(base5(trig))
    else:
        return trig
        
def base5(trigArr):
    
    bs5 = []
     
    for i in range(len(trigArr)):
        tmp = ""
        for j in range(len(trigArr[i])):
         
            tmp += str(trigArr[i][j])
        bs5.append(tmp)
    return bs5
    

def base10(trigArr):
    bs10 = []
    
    for val in trigArr:
        bs10.append((int(val[0]) * 25) + (int(val[1]) * 5) + int(val[2]))
    return bs10   



def plotAlongX(arr, color = "-r"):
    n = len(arr)
    x = np.arange(0, n)
    y = []
    for val in arr:
        y.append(int(val))
        
    plt.plot(x, y, color)




######################################################################################################################################################
######################################################################################################################################################
###############################################################################################################################################################################

#############################################################
###########(table, center, up,  right, down, left, alpha)########
#############################################################

plotTables()
# plotEyeTable(tbl['east1'], True, True, True, True,True, 0.2)
# plotEyeTable(tbl['west1'], True, True, True, True,True, 0.2)
# plotEyeTable(tbl['east2'], True, True, True, True, True, 0.2)

# plotEyeTable(tbl['west2'], True, True, True, True, True, 0.1)
# plotEyeTable(tbl['east3'], True, True, True, True, False, 0.1)
# plotEyeTable(tbl['west3'], True, True, True, True, False, 0.1)

# plotEyeTable(tbl['east4'], True, True, True, True, True, 0.1)
# plotEyeTable(tbl['west4'], True, True, True, True, False, 0.1)
# plotEyeTable(tbl['east5'], True, True, True, True, True, 0.1)


# plt.show()  ###if not using spyder, or if the plot wont show up, un-comment this line.


##################################################################
#########################TRIAGRAMS################################
##################################################################

#######################BASE 10####################################

# e1t10 = genTri(east1, 'b10')
# w1t10 = genTri(west1, 'b10')
# e2t10 = genTri(east2, 'b10')

# w2t10 = genTri(west2, 'b10')
# e3t10 = genTri(east3, 'b10')
# w3t10 = genTri(west3, 'b10')

# e4t10 = genTri(east4, 'b10')
# w4t10 = genTri(west4, 'b10')
# e5t10 = genTri(east5, 'b10')
   

#########################BASE 5###################################


# e1t5 = genTri(east1, 'b5')
# w1t5 = genTri(west1, 'b5')
# e2t5 = genTri(east2, 'b5')

# w2t5 = genTri(west2, 'b5')
# e3t5 = genTri(east3, 'b5')
# w3t5 = genTri(west3, 'b5')

# e4t5 = genTri(east4, 'b5')
# w4t5 = genTri(west4, 'b5')
# e5t5 = genTri(east5, 'b5')

##################################################################










