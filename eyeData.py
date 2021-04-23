import numpy as np

east1 = np.array([[2,0,1,0,1,3,2,2,3,3,0,4,0,4,1,1,3,0,2,3,2,1,1,4,3,1,3,0,3,3,0,0,4,0,2,4,0,0,0], 
                  [0,3,2,0,4,1,2,2,0,0,0,1,4,2,2,2,4,2,1,2,2,2,2,0,1,1,0,0,0,3,2,0,1,3,4,1,1,1,3], 
                  [3,1,0,2,2,1,0,4,4,0,0,0,2,0,0,1,0,4,0,4,0,1,4,4,1,4,2,0,3,3,0,2,2,0,3,4,2,4,1],
                  [2,3,1,3,1,3,1,3,0,0,3,1,1,3,2,1,2,0,1,4,2,2,3,1,3,3,1,4,4,1,3,4,1,4,4,1,2,1,1],
                  [0,1,4,0,0,3,2,1,2,1,1,4,1,3,0,0,4,1,1,1,0,1,0,0,2,4,1,2,4,1,0,0,4,0,3,1,0,0,1],
                  [0,4,0,3,3,1,4,3,2,3,4,1,1,2,2,1,0,1,0,1,0,0,4,0,1,2,0,4,1,2,4,4,2,4,4,2,4,0,2],
                  [1,3,3,3,1,2,2,0,3,3,0,1,0,3,1,1,3,1,1,1,2,1,1,2,1,0,3,2,2,3,1,4],
                   [1,3,1,0,4,2,4,2,2,4,1,3,0,3,0,4,1,1,0,2,0,3,1,2,3,2,0,4,3,1,3]])
east1flip = np.flip(east1, 0);

east2 = np.array([[1,2,1,0,1,3,2,2,3,3,0,4,0,4,1,1,3,0,2,3,2,1,1,4,3,1,3,0,3,3,0,0,4,0,2,4,0,0,4], 
                  [1,3,2,0,4,1,2,2,0,0,0,1,4,2,2,2,4,2,1,2,2,2,2,0,1,1,0,0,0,3,2,0,1,3,4,1,1,3,2], 
                  [3,0,2,0,1,3,2,3,0,0,4,4,2,1,0,1,4,3,0,0,1,2,1,4,1,4,0,3,1,1,0,2,4,1,0,4,2,2,3],
                  [1,0,2,4,4,1,1,1,3,2,2,2,2,3,1,4,0,3,3,3,0,1,3,0,2,3,1,0,1,0,3,2,2,4,4,1,4,2,2],
                  [0,1,4,1,1,3,0,3,0,1,4,4,1,0,2,0,2,0,3,1,1,1,1,4,2,4,1,0,3,4,2,3,2,1,3,2,1,1,2],
                  [1,4,1,1,2,0,1,2,0,0,4,0,1,0,3,0,2,2,1,2,2,4,0,2,0,4,0,0,0,0,1,0,3,2,2,1,0,4,0],
                  [0,0,1,1,3,2,2,1,0,0,4,2,2,3,1,0,4,3,2,4,2,0,1,3,1,0,3,0,1,0,2,0,0,3,0,0,2,2,1],
                  [0,2,0,1,4,2,2,4,0,3,1,2,0,3,1,3,3,0,2,3,1,0,0,0,1,0,3,3,1,0,4,4,1,2,0,1,4,2,2],
                  [0,3,4,2,0,1,0,4,3,1,0,1,1,0,0,2,0,0,1,2,4],
                  [1,3,1,4,0,2,0,2,2,0,2,0,1,4,1,3,2,2,3,1,1]])
east2flip = np.flip(east2, 0);


east3 = np.array([[2,2,1,0,1,4,3,0,4,0,0,0,1,0,0,3,0,2,2,2,0,2,3,1,2,2,2,2,3,2,1,4,4,1,4,4,2,1,1],
                  [3,3,2,0,4,1,0,0,2,2,2,2,4,3,1,3,4,1,0,0,3,2,4,2,0,0,0,0,1,0,2,2,0,0,4,2,4,3,1],
                  [3,1,3,2,2,3,3,1,2,1,2,0,1,3,4,0,0,4,1,4,1,3,0,2,3,1,0,0,0,1,2,3,1,0,4,3,1,3,0],
                  [0,2,0,0,2,0,1,4,0,0,0,2,0,2,1,2,1,2,3,1,1,1,0,0,0,0,3,1,1,2,2,2,0,1,1,0,0,3,2],
                  [1,4,0,2,1,4,2,2,2,0,2,3,0,4,2,0,0,1,2,1,4,2,4,1,2,1,1,2,2,3,1,0,4,0,1,0,0,3,4],
                  [0,0,3,0,2,1,0,3,1,3,0,0,2,1,2,2,1,0,3,1,0,0,0,0,3,1,2,3,3,2,0,0,3,2,4,0,4,2,2],
                  [0,0,1,2,4,0,2,4,1,0,2,0,2,3,2,0,4,3,0,4,3,0,3,1,2,2,4,1,3,1,3,1,2,3,0,1,1,4,2],
                  [2,3,2,3,1,1,1,3,0,2,1,1,0,2,1,0,2,0,2,2,2,3,4,1,4,1,2,1,1,3,2,4,0,3,2,1,2,3,0],
                  [0,0,1,0,3,0,1,2,4,2,2,1,2,2,4,0,3,3,0,0,3,2,1,1,0,2,4,2,1,3,1,3,3,2,3,1,0,0,1],
                  [4,1,0,2,1,0,1,0,3,3,0,0,4,3,2,0,3,1,4,1,2,1,1,1,4,2,2,3,3,0,4,0,3,4,0,0,0,4,1],
                  [0,4,1,2,4,0,1,2,3,0,4],
                  [0,4,2,3,0,1,0,1,0,4]])
east3flip = np.flip(east3, 0);

east4 = np.array([[1,0,1,0,1,4,3,0,4,0,0,0,1,0,0,0,0,0,0,1,0,2,1,3,2,3,3,1,2,0,1,4,2,1,3,3,0,0,3],
                  [2,3,2,0,4,1,0,0,2,2,2,2,4,3,1,2,1,2,4,3,0,4,3,0,3,0,0,1,1,0,2,0,3,4,2,1,1,3,0],
                  [1,0,1,0,0,4,2,2,3,2,1,0,0,3,4,3,0,0,1,4,4,2,1,4,2,2,4,0,2,2,2,0,0,3,0,0,0,2,2],
                  [3,0,3,4,1,1,0,2,2,3,1,3,2,0,2,4,0,3,3,0,2,0,3,0,2,2,2,4,4,1,1,4,2,0,1,0,1,4,1],
                  [1,4,3,2,3,4,3,0,0,1,2,0,2,4,2,2,3,0,1,1,0,3,0,1,3,0,2,0,0,1,0,4,0,0,3,0,1,3,0],
                  [0,1,2,3,3,2,4,0,1,3,4,1,3,4,1,3,0,2,4,4,1,3,0,1,4,1,2,4,1,2,2,2,2,3,0,3,3,2,2],
                  [2,1,2,2,2,2,1,4,3,1,3,0,3,0,2,0,1,3,1,0,2,1,1,3,1,0,2,2,3,0,0,0,3,1,0,3,2,3,2],
                  [4,3,2,3,3,1,4,1,1,0,3,2,4,0,3,2,0,0,1,2,2,1,0,3,1,1,2,4,3,1,4,4,0,1,2,0,2,3,1],
                  [1,2,2,0,2,4,2,3,0,1,0,1,3,1,1,2,3,2,2,1,3,0,3],
                  [3,4,2,1,2,1,0,2,2,0,1,0,0,3,2,3,0,3,4,0,3,4]])
east4flip = np.flip(east4, 0);                 

east5 = np.array([[1,1,1,0,1,4,3,0,4,0,0,0,1,0,0,0,0,0,0,1,0,2,1,3,2,3,3,1,2,0,1,4,3,0,4,4,1,3,3],
                  [3,3,2,0,4,1,0,0,2,2,2,2,4,3,1,2,1,2,4,3,0,4,3,0,3,0,0,1,1,0,2,1,1,1,1,2,4,3,0],
                  [1,0,1,2,1,4,2,2,3,3,0,2,0,2,4,0,1,4,1,4,4,2,1,2,2,2,2,2,3,0,2,1,2,2,1,3,2,3,3],
                  [3,0,3,4,1,1,0,2,2,4,0,1,2,0,2,0,4,1,3,0,2,0,0,2,2,4,2,4,2,0,2,4,0,3,4,1,2,0,2],
                  [0,1,4,1,1,0,1,1,4,1,0,3,1,1,1,0,1,0,2,4,0,1,1,0,2,0,4,0,1,0,0,1,3,1,0,0,1,3,0],
                  [2,1,1,2,1,1,1,3,0,1,1,0,4,4,1,2,1,1,1,1,2,4,0,3,4,1,0,1,2,2,0,4,0,0,4,1,2,1,3],
                  [1,0,2,0,4,1,0,4,1,2,2,1,1,3,4,1,3,0,1,3,3,0,1,3,2,4,3,0,1,1,0,4,2,0,1,0,2,2,1],
                  [0,2,0,2,0,3,0,0,2,2,4,0,0,1,0,1,2,0,4,4,2,3,1,1,0,4,2,1,1,1,1,4,2,0,3,1,1,0,2],
                  [1,3,1,2,2,4,2,2,0,2,2,2,0,4,1],
                  [2,3,2,4,4,2,1,0,1,3,3,1,4,3,1]])
east5flip = np.flip(east5, 0);



west1 = np.array([[3,1,1,0,1,3,2,2,3,3,0,4,0,4,1,1,3,0,2,3,2,1,1,4,3,1,3,0,3,3,0,0,4,0,2,4,0,0,4],
                  [0,3,2,0,4,1,2,2,0,0,0,1,4,2,2,2,4,2,1,2,2,2,2,0,1,1,0,0,0,3,2,0,1,3,4,1,1,0,1],
                  [0,2,0,2,0,1,0,4,4,0,0,0,1,0,4,0,4,4,0,4,0,1,4,4,1,4,2,0,3,3,0,2,2,0,3,4,1,3,1],
                  [1,1,1,2,1,3,1,3,0,0,0,1,1,0,2,0,2,0,1,4,2,2,3,1,3,3,1,4,4,1,3,4,1,4,4,1,4,0,1],
                  [2,1,2,2,2,3,3,0,3,2,4,4,0,0,0,2,4,3,2,3,1,1,1,0,2,2,1,2,3,1,0,3,1,0,2,2,0,4,3],
                  [4,0,3,4,3,1,4,0,1,2,2,2,1,1,1,3,4,0,2,1,0,3,0,1,4,1,3,3,4,1,2,2,1,3,3,0,1,3,2],
                  [0,2,4,1,4,2,2,1,4,2,2,2,0,3,0,2,4,2,0,0,1,2,3,2,1,2,4,0,2,3,2,3,2,0,1,4,0,3],
                  [3,1,0,1,3,2,2,1,1,2,1,3,0,2,0,3,2,2,2,2,0,0,4,2,2,3,1,0,3,1,3,2,2,4,1,1,3]])
west1flip = np.flip(west1, 0);



west2 = np.array([[3,0,1,0,1,4,3,0,4,2,3,1,1,1,1,1,3,0,1,0,3,2,0,0,1,1,4,2,1,1,1,4,2,0,4,2,1,4,4],
                  [1,3,2,0,4,1,0,0,2,4,4,1,2,0,0,2,2,2,1,4,1,0,1,3,2,4,0,0,2,2,2,2,0,1,2,0,4,0,2],
                  [1,1,0,1,2,0,2,1,0,0,4,4,0,1,2,0,2,2,0,1,4,1,0,0,2,0,2,1,3,0,0,1,3,2,4,3,3,1,2],
                  [4,0,1,1,3,0,1,1,2,0,1,0,3,2,2,3,1,3,4,3,1,4,2,2,3,1,3,2,1,3,0,3,1,1,0,0,0,0,3],
                  [1,4,3,1,1,0,2,2,3,0,2,4,2,2,4,2,0,1,0,2,1,2,2,3,1,4,2,2,0,0,1,0,3,1,1,1,2,2,3],
                  [2,0,3,4,0,1,2,3,0,0,4,1,2,2,2,2,1,3,1,3,2,2,2,0,2,3,0,2,4,2,1,4,0,2,1,1,4,4,0],
                  [1,2,2,2,0,1,0,0,0,0,1,2,1,4,3,1,0,1,2,3,3,3,1,2,0,1,0,2,2,4,2,0,3,2,2,1],
                  [0,1,1,0,1,0,1,0,1,3,2,1,2,3,1,1,0,3,0,3,2,0,3,0,2,4,1,3,2,0,3,2,2,0,3,0]])

west2flip = np.flip(west2, 0);


west3 = np.array([[1,1,1,0,1,4,3,0,4,0,4,4,0,2,3,1,0,1,0,3,3,2,3,2,1,2,0,1,1,3,2,4,0,0,3,2,0,2,3],
                  [4,3,2,0,4,1,0,0,2,3,4,2,1,2,0,3,0,1,4,4,1,2,1,2,2,2,2,4,0,1,4,2,0,2,1,1,1,3,0],
                  [0,3,3,0,3,1,1,3,4,2,2,4,1,4,4,1,1,1,3,0,3,0,0,3,1,4,2,2,3,4,0,4,2,1,3,1,1,1,2],
                  [4,3,1,4,1,3,2,0,0,2,1,0,1,4,1,2,0,2,1,1,2,4,3,1,2,3,0,2,0,3,1,1,1,4,3,0,0,2,1],
                  [1,0,3,1,3,3,2,1,4,2,0,0,2,3,0,0,1,1,1,4,3,0,3,4,1,4,3,0,3,3,1,1,0,1,2,2,1,2,0],
                  [1,0,1,1,3,2,2,1,1,1,2,0,4,4,2,3,1,0,1,3,1,3,2,1,2,3,1,0,2,0,3,1,1,0,2,2,2,0,0],
                  [1,2,0,1,2,0,1,2,3,1,3,0,0,1,1,0,2,4,0,1,4,1,3,3,0,2,1,0,2,3,0,0,2,2,2,0,0,4,4],
                  [2,1,0,3,1,2,2,2,0,0,0,1,4,4,0,1,2,2,0,0,3,2,3,2,1,4,2,1,4,1,3,3,2,1,3,1,2,2,0],
                  [1,2,0,2,2,4,0,2,2,2,3,4,2,0,3,0,3,3,1,2,0,2,4,4,0,4,0,2,0,0],
                  [0,0,2,1,2,1,1,0,0,1,4,1,1,0,2,2,4,2,1,0,3,4,0,2,4,1,1,4,4,2]])
west3flip = np.flip(west3, 0);


west4 = np.array([[3,0,1,0,1,4,3,0,4,0,0,0,1,0,0,0,0,0,0,1,0,2,1,3,2,3,3,1,2,0,1,4,0,0,4,0,0,0,2],
                  [2,3,2,0,4,1,0,0,2,2,2,2,4,3,1,2,1,2,4,3,0,4,3,0,3,0,0,1,1,0,2,2,2,1,1,3,1,4,2],
                  [2,1,1,3,1,0,2,1,4,0,0,1,0,3,2,1,2,2,2,4,1,1,2,4,3,0,0,1,0,0,1,3,1,2,2,3,3,1,3],
                  [0,3,0,2,2,1,2,3,0,1,3,2,3,0,1,4,3,0,4,1,3,4,2,0,3,0,0,0,3,2,3,3,2,4,2,1,1,4,0],
                  [0,4,0,2,1,0,2,4,0,1,0,3,2,0,2,2,1,0,2,4,3,0,2,1,0,1,2,1,0,3,0,1,2,0,3,3,2,3,2],
                  [4,0,2,2,1,1,1,0,3,1,3,2,4,1,2,1,0,2,1,4,2,4,4,0,3,1,1,1,2,2,0,2,1,4,3,1,1,4,1],
                  [2,0,4,2,3,3,2,4,1,2,0,3,3,0,2,0,2,3,3,0,1,0,4,1,2,0,4,2,4,1,0,1,2,2,3,2,1,0,1],
                  [3,1,1,1,4,0,3,1,1,4,2,1,2,3,2,1,2,2,4,1,0,2,4,0,1,3,2,4,4,0,0,3,0,2,2,1,4,4,0],
                  [2,2,4,3,1,4,1,1,4,0,4,2,1,2,1,1,1,4,1,4,0,1,3,0],
                  [0,2,0,2,3,1,0,0,0,0,3,1,0,0,0,1,0,2,1,4,0,0,1,1]])
west4flip = np.flip(west4, 0);





allTables = {'east1':east1, 'west1':west1, 'east2':east2, 'west2':west2, 'east3':east3, 'west3':west3, 'east4':east4, 'west4':west4, 'east5':east5}

