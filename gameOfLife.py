import numpy as np 
import matplotlib.pyplot as plt
import matplotlib.animation as animation   

def checkRule(cel, neigbourCount):
    # Overpopulation : alive cel dies if it has 4 or more neigbours
    if cel and (neigbourCount >= 4):
        return False
    # Loneliness : alive cel dies if it has less then 2 neigbours
    if cel and (neigbourCount < 2):
        return False
    # Birth : cel gets born if it has exatly 3 neigbours
    if not cel and (neigbourCount == 3):
        return True
    else:
        return cel

def neigbouGrid(grid):
    # neigbourgrid = sum of the cells around a cell (up, down, left, right and 4 diagonals)
    NG = np.zeros(grid.shape)
          
    #up
    NG[:-1,:] += grid[1:,:] 
    #down
    NG[1:,:] += grid[:-1,:] 
    #left
    NG[:,:-1] += grid[:,1:] 
    #right
    NG[:,1:] += grid[:,:-1] 
    #up left
    NG[:-1,:-1] += grid[1:,1:] 
    #up right
    NG[:-1,1:] += grid[1:,:-1] 
    #down left
    NG[1:,:-1] += grid[:-1,1:] 
    #down right
    NG[1:,1:] += grid[:-1,:-1]     
    return NG

def iterate(grid):
    rows, columns = grid.shape
    newgrid = np.zeros((rows, columns))
    NG = neigbouGrid(grid)
    for i in range(rows):  
        for j in range(columns):
            newgrid[i,j] = checkRule(grid[i,j],NG[i,j])
    return newgrid

def createRandomGrid(N):
    return np.random.choice([1,0], N*N, p=[0.2, 0.8]).reshape(N, N)

def updateImage(frameNum, img, grid):
    newGrid = iterate(grid)
    
    # update data
    img.set_data(newGrid)
    grid[:] = newGrid[:]
    return img,

def main():
    N = 100
    grid = createRandomGrid(N)
    
    fig, ax = plt.subplots()
    img = ax.imshow(grid, interpolation='nearest')
    ani = animation.FuncAnimation(fig, updateImage, fargs=(img, grid),
                                  frames = 10,
                                  interval=500,
                                  save_count=50)
    plt.show()
    


if __name__=="__main__":
    main()