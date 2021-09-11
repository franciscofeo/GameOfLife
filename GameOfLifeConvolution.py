import numpy as np
import matplotlib.pyplot as plt
import imageio
import os
from scipy import signal

# Matrix size (N x N)
N = 50;

present = np.random.randint(0, 2, [N, N]);
#present = np.zeros(N*N).reshape(N, N)

def block(matrix, x, y):
    matrix[x: x+2, y: y+2] = np.array([[1, 1], [1, 1]]);

def glider(matrix, x, y):
    matrix[x: x+3, y: y+3] = np.array([[0, 1, 0], [0, 0, 1], [1, 1, 1]]);

def spaceship(matrix, x, y):
    matrix[x: x+4, y: y+6] = np.array([[0,0,0,1,1,0], [1,1,1,0,1,1], [1,1,1,1,1,0], [0,1,1,1,0,0]])

kernel = np.array([[1, 1, 1], [1, 0, 1], [1, 1, 1]]);
#spaceship(present, 4, 4)

files = [];

for n in range(0, 180):

    if n == 0:
        plt.imshow(present, cmap="binary");
        plt.title(f"Game of Life");
        #plt.show()
        filename1 = f"{n}.png";
        files.append(filename1);
        plt.savefig(filename1);

    convol_world = signal.convolve2d(present, kernel, mode="same", boundary="wrap" );
    present = (((present == 1) & (convol_world > 1) & (convol_world < 4)) | ((present == 0) & (convol_world == 3)));
    
    plt.imshow(present, cmap="binary");
    plt.title(f"Game of Life - Generation {n}");
    #plt.show()
    filename = f"{n}.png";
    files.append(filename);
    plt.savefig(filename);


with imageio.get_writer('myGif.gif', mode='I') as writer:
    for filename in files:
        image = imageio.imread(filename);
        writer.append_data(image);

for filename in set(files):
   os.remove(filename);
