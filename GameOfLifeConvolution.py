import numpy as np
import matplotlib.pyplot as plt
import imageio
import os
from scipy import signal

# Tamanho da matriz (N x N)
N = 50;

presente = np.random.randint(0, 2, [N, N]);
#presente = np.zeros(N*N).reshape(N, N)


def block(matrix, x, y):
    matrix[x: x+2, y: y+2] = np.array([[1, 1], [1, 1]]);

def glider(matrix, x, y):
    matrix[x: x+3, y: y+3] = np.array([[0, 1, 0], [0, 0, 1], [1, 1, 1]]);

def spaceship(matrix, x, y):
    matrix[x: x+4, y: y+6] = np.array([[0,0,0,1,1,0], [1,1,1,0,1,1], [1,1,1,1,1,0], [0,1,1,1,0,0]])

kernel = np.array([[1, 1, 1], [1, 0, 1], [1, 1, 1]]);

files = [];

for n in range(0, 100):

    if n == 0:
        plt.imshow(presente, cmap="binary");
        plt.title(f"Game of Life");
        #plt.show()
        filename1 = f"{n}.png";
        files.append(filename1);
        plt.savefig(filename1);

    mapa_convolucionado = signal.convolve2d(presente, kernel, mode="same", boundary="wrap" );
    presente = (((presente == 1) & (mapa_convolucionado > 1) & (mapa_convolucionado < 4)) | ((presente == 0) & (mapa_convolucionado == 3)));
    
    plt.imshow(presente, cmap="binary");
    plt.title(f"Game of Life - Geração {n}");
    #plt.show()
    filename = f"{n}.png";
    files.append(filename);
    plt.savefig(filename);


with imageio.get_writer('pretobranco3.gif', mode='I') as writer:
    for filename in files:
        image = imageio.imread(filename);
        writer.append_data(image);

for filename in set(files):
   os.remove(filename);
