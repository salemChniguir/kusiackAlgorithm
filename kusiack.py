
import numpy as np
# matrix is an example of products in columns and machines in lines
# first column contains the label of each product don't touch it
matrix=[[1,0,1,1,0,1,0,0,0],
        [2,1,0,0,0,0,1,0,0],
        [3,0,0,0,1,0,0,1,0],
        [4,0,0,0,0,0,1,0,0],
        [5,0,0,0,0,0,0,0,1],
        [6,0,0,0,1,0,0,0,0],
        [7,0,0,1,0,1,0,0,1]]

array=np.array(matrix)

def small_island(array):
    """
    determinates machines and products in the same small_island

    parameters:
    -----------
    array: array
        array of 2D products & machines
    """
    linVisited=set()
    colVisited=set()
    linNext=set()
    colNext=set()
    linNext.add(0)
    products=set()
    machines=set()
    lines=set()
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
                    lines.add(l)
        return lines,products,machines

def kusiack(array):
    """
    function to execute the kusiack algorithm to search all small_islands

    parameters
    ---------
    array: array 
        array of 2D products and machines
    """
    while(array.shape[0]>=1):
        lines,products,machines=small_island(array)
        print(array)
        print("small_island: products {} with machines {}".format(["P"+str(p) for p in products],                                                          ["M"+str(m+1) for m in machines]))
        array=np.delete(array,list(lines),axis=0)




kusiack(array)
