from imageio import imread
import numpy as np
import sys
from hilbert import decode, encode

def hilbert_flatten(array):
    D = array.ndim
    S = np.arange(np.array(array.shape).prod())
    L = decode(S, D, 8).T.tolist()

    return array[tuple(L)]

np.set_printoptions(threshold=sys.maxsize)

im = imread("lolol.jpg")
gray = im[:,:,0]
hilc = hilbert_flatten(gray)
print(hilc)










