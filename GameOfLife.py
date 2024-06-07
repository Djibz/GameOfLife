import tkinter as tk
import numpy as np
from PIL import Image, ImageTk
from scipy import signal

MAX_ITERATION = -1
DELAY = 1
CONVOLUTION_MATRIX = np.ones((3, 3), dtype=int)
CONVOLUTION_MATRIX[1, 1] = 0

def state_func(n, s):
    if n == 3: return 1
    if n == 2: return s
    return 0

v_state_func = np.vectorize(state_func)

class GameOfLife():
    def __init__(self, array):
        self.iteration = 0
        self.array = array
        self.root = tk.Tk()
        self.canvas = tk.Canvas(self.root,width=500,height=500)
        self.canvas.pack()
        self.img = None
        self.update_clock()
        self.root.mainloop()

    def play(self):
        count_matrix = signal.convolve2d(self.array, CONVOLUTION_MATRIX, mode='same', boundary='wrap')
        self.array = v_state_func(count_matrix, self.array)


    def update_clock(self):
        self.img =  ImageTk.PhotoImage(image=Image.fromarray((self.array-1)*(-255)).resize((500, 500), resample=0))

        self.canvas.create_image(0, 0, anchor="nw", image=self.img)
        self.iteration += 1
        self.play()
        if MAX_ITERATION == -1 or self.iteration < MAX_ITERATION:
            self.root.after(DELAY, self.update_clock)

array = np.zeros((100, 100), dtype=int)
array[1, 2] = 1
array[2, 3] = 1
array[3, 1:4] = 1

# array[10:14, 10:14] = 1
# 
# array[20:22, 20:22] = 1
# array[19, 21] = 1
# array[22, 20] = 1

app=GameOfLife(array)