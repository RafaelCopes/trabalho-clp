from random import randint

import matplotlib.pyplot as plt
from _calculations_cffi import ffi, lib
from matplotlib.pyplot import figure

# número de ponto a serem redenizados
POINTS = 50000

def main():
    x = [] 
    y = [] 
    x.append(0) 
    y.append(0) 
    
    current = 0

    # para cada ponto aplica a função de acordo com sua probabilidade
    for i in range(1, POINTS): 
        z = randint(1, 100)

        if z == 1: 
            x.append(lib.f1_x(x[current], y[current])) 
            y.append(lib.f1_y(x[current], y[current])) 
        
        if z>= 2 and z<= 86:
            x.append(lib.f2_x(x[current], y[current])) 
            y.append(lib.f2_y(x[current], y[current])) 
        
        if z>= 87 and z<= 93: 
            x.append(lib.f3_x(x[current], y[current])) 
            y.append(lib.f3_y(x[current], y[current])) 
        
        if z>= 94 and z<= 100: 
            x.append(lib.f4_x(x[current], y[current])) 
            y.append(lib.f4_y(x[current], y[current])) 
            
        current = current + 1

    # plota a interface
    with plt.style.context('dark_background'):
        figure(figsize=(8, 10), dpi=80)
        plt.scatter(x, y, s = 0.2, edgecolor ='green')
        plt.grid(False)
        plt.axis('off')
        plt.show()

if __name__ == '__main__':
    main()
