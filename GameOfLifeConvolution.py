import numpy as np
import matplotlib.pyplot as plt
import imageio
import os
from scipy import signal

# Matrix size (N x N)
N = 25;

#present = np.random.randint(0, 2, [N, N]); # random N x N matrix with 0 or 1
present = np.zeros(N*N).reshape(N, N) # N x N matrix with all elements = 0

def block(matrix, x, y):
    matrix[x: x+2, y: y+2] = np.array([[1, 1], [1, 1]]);

def glider(matrix, x, y):
    matrix[x: x+3, y: y+3] = np.array([[0, 1, 0], [0, 0, 1], [1, 1, 1]]);

def spaceship(matrix, x, y):
    matrix[x: x+4, y: y+6] = np.array([[0,0,0,1,1,0], [1,1,1,0,1,1], [1,1,1,1,1,0], [0,1,1,1,0,0]])

def toad(matrix, x, y):
    matrix[x: x+2, y: y+4] = np.array([[0,1,1,1], [1,1,1,0]]);

def dieHard(matrix, x, y):
    matrix[x: x+3, y: y+8] = np.array([[0,0,0,0,0,0,1,0], [1,1,0,0,0,0,0,0], [0,1,0,0,0,1,1,1]]);

def dora_cell(matrix, x, y):
    matrix[x: x+2, y: y+5] = np.array([[0, 0, 1, 1, 1], [1, 1, 1, 0, 0]])

kernel = np.array([[1, 1, 1], [1, 0, 1], [1, 1, 1]]);
dieHard(present, 10, 8)

files = [];

plt.imshow(present, cmap="binary");
plt.title(f"Game of Life - Generation 0");
filename1 = f"{0}.png";
files.append(filename1);
plt.savefig(filename1);

for n in range(1, 131):

    convol_world = signal.convolve2d(present, kernel, mode="same", boundary="wrap" );
    present = (((present == 1) & (convol_world > 1) & (convol_world < 4)) | ((present == 0) & (convol_world == 3)));
    
    plt.imshow(present, cmap="binary");
    plt.title(f"Game of Life - Generation {n}");
    filename = f"{n}.png";
    files.append(filename);
    plt.savefig(filename);


with imageio.get_writer('dieHard.gif', mode='I') as writer:
    for filename in files:
        image = imageio.imread(filename);
        writer.append_data(image);

for filename in set(files):
   os.remove(filename);
