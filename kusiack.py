
import numpy as np
matrix=[[1,0,1,1,0,1,0,0,0],     # lignes=Products
        [2,1,0,0,0,0,1,0,0],     # columns=Machines
        [3,0,0,0,1,0,0,1,0],	 # first column contains the
        [4,0,0,0,0,0,1,0,0],	 #label of each product don't touch it
        [5,0,0,0,0,0,0,0,1],
        [6,0,0,0,1,0,0,0,0],
        [7,0,0,1,0,1,0,0,1]]
array=np.array(matrix)
def ilot(array):
    linVisited=set()
    colVisited=set()
    linNext=set()
    colNext=set()
    linNext.add(0)
    products=set()
    machines=set()
    linges=set()
    while(1):
        linVisited=linNext-linVisited
        if(len(linVisited)==0):
            break;
        colNext=set()
        linNext=set()
        for l in linVisited:
            for c in range(1,len(array[0])):
                    if array[l][c]==1:
                        colNext.add(c) #add the column c to be visited
                        machines.add(c)
        colVisited=colNext-colVisited
        if(len(colVisited)==0):
            break;
        for c in colVisited:
            for l in range(len(array[:,0])):
                if array[l][c]==1:
                    linNext.add(l) #add the line l to be visited
                    products.add(array[l][0])
                    linges.add(l)
        return linges,products,machines
def kusiack(array):
    while(array.shape[0]>=1):
        linges,products,machines=ilot(array)
        print(array)
        print("ilot: products {} with machines {}".format(["P"+str(p) for p in products],                                                          ["M"+str(m+1) for m in machines]))
        array=np.delete(array,list(linges),axis=0)




kusiack(array)
