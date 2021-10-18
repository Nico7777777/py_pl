import matplotlib.pyplot as plt
import numpy as np

if __name__ == "__main__":
    cardinal_of_functions_image = int(input("Cate puncte va avea graficul?"))
    xlabel = []
    ylabel = []
    for i in range(cardinal_of_functions_image):
        a = float(input("Introdu coordonata pe axa X a punctului "+str(i+1)+":"))
        xlabel.append(a)
        b = float(input("Introdu coordonata pe axa Y a punctului "+str(i+1)+":"))
        ylabel.append(b)
    plt.plot(xlabel, ylabel, 'ro')
    plt.xlabel("X")
    plt.ylabel("Y")
    #plt.plot('ro') asa nu apar puncte rosii, ci noteaza 'ro' ca valoare a axei y
    plt.show()