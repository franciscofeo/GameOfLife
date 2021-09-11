import numpy as np
import matplotlib.pyplot as plt
import imageio
import os
from scipy import signal
import time


# Tamanho da matriz (N x N)
N = 50;

"""
 Abaixo tenho 2 opções de matrizes iniciais, a primeira é uma matriz aleatória N x N onde cada entrada possui um valor aleatório
 de 0 ou 1. Já a segunda, é uma matriz de zeros N x N, ela eu uso para quando queremos ver apenas 1 tipo de célula, que estão definidas
 abaixo (acho bacana usar ela quando for colocar o pygame). 
 
 Uma vai estar sempre comentada pra não ter confusão e pro python não precisar compilar e usar memória atoa.
 """

presente = np.random.randint(0, 2, [N, N]);
#presente = np.zeros(N*N).reshape(N, N)

"""
Aqui eu coloquei apenas 3 tipos, mas ainda vou pôr mais algumas, tá me faltando só paciência kkkk
basicamente cada função abaixo é uma célula diferente, onde ele pega um intervalo da nossa matriz que é passada como parâmetro e insere
a célula nesse intervalo. Pra ficar mais fácil de ver, coloca o nome no google pra ver o desenho.
"""

def block(matrix, x, y):
    matrix[x: x+2, y: y+2] = np.array([[1, 1], [1, 1]]);

def glider(matrix, x, y):
    matrix[x: x+3, y: y+3] = np.array([[0, 1, 0], [0, 0, 1], [1, 1, 1]]);

def spaceship(matrix, x, y):
    matrix[x: x+4, y: y+6] = np.array([[0,0,0,1,1,0], [1,1,1,0,1,1], [1,1,1,1,1,0], [0,1,1,1,0,0]])


"""
Agora a coisa fica mais complicada, dá uma lidinha naquele link que te mandei sobre convolução e vai dar pra ter uma ideia. Abaixo eu
defino o kernel que vamos usar na convolução, ele construído nessa forma vai funcionar para contar quantos vizinhos cada célula tem.

"""

kernel = np.array([[1, 1, 1], [1, 0, 1], [1, 1, 1]]);

# Esse Files é uma lista vazia onde vamos guardar os nomes dos arquivos de imagem pra depois apagar quando estivermos criando o gif
# (faz parte do método pra criar gif, precisa preocupar muito com isso não kk)

files = [];

t1 = time.time(); # Esse bixim aqui é só pra no final a gente ver quanto tempo o código demora (frescura minha, dá pra tirar isso)


# Agora o código em si:

for n in range(0, 100):

    """
    Esse primeiro if aqui é pra aparecer na animação o nosso mundo na configuração 0, ou seja, a configuração inicial,  as linhas onde
    tem o filename, files.append faz parte daquele método de salvar e excluir as imagens    
    """
    if n == 0:
        plt.imshow(presente, cmap="binary");
        plt.title(f"Game of Life");
        #plt.show()
        filename1 = f"{n}.png";
        files.append(filename1);
        plt.savefig(filename1);

    """
    Agora sim, a matriz mapa_convolucionado como o nome diz é a convolução da nossa matriz atual (presente) com o kernel que a gente definiu 
    ali em cima, depois tenta dar um print nele e você vai ver que cada entrada é igual ao número de vizinhos das células da matriz presente.
    O boundary = wrap no método é simplesmente pra falar que as bordas são infinitas, como a gente quer mesmo.

    Aí depois, a gente reatribui a matriz presente para agora com as regras do jogo da vida, a condição antes da barra corresponde ao True,
    logo se ele validar nessa parte vai retornar um valor True, senão vai retornar um valor False. Esse jeito de escrever condicional é meio
    esquisitinho mesmo, mas ele faz essas condições para cada elemento da matriz presente e mapa_convolucionado. Por exemplo, no primeiro
    ele fala que se presente == 1 (célula viva) e mapa_convolucionado > 1 e < 4 retornar True, ou seja, a partícula vive.

    Depois disso é aquela frescura denovo pra salvar as imagens na lista pra depois apagar, o código mesmo já acabou aqui kkk
    """

    mapa_convolucionado = signal.convolve2d(presente, kernel, mode="same", boundary="wrap" );
    presente = (((presente == 1) & (mapa_convolucionado > 1) & (mapa_convolucionado < 4)) | ((presente == 0) & (mapa_convolucionado == 3)));
    
    plt.imshow(presente, cmap="binary");
    plt.title(f"Game of Life - Geração {n}");
    #plt.show()
    filename = f"{n}.png";
    files.append(filename);
    plt.savefig(filename);


"""
Daqui pra baixo é só o uso daquelas bibliotecas imageio e os pra fazer o gif, depois se quiser te explico melhor mas depois vou falar com
o gerson e ver se o jeito dele é mais rápido pq ele faz as animações em poucas linhas e dá até raiva
"""

with imageio.get_writer('pretobranco3.gif', mode='I') as writer:
    for filename in files:
        image = imageio.imread(filename);
        writer.append_data(image);

for filename in set(files):
   os.remove(filename);

Dt = time.time() - t1

print(f"Duration: {Dt} seconds");