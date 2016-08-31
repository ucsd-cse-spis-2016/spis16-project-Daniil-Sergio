import matplotlib.pyplot as plt
from collections import defaultdict
import time
 

def PokemonGOimage(totals,highlight):
    labels = 'Valor', 'Mystic', 'Instinct'
    
    sizes = [totals[0],totals[1],totals[2]]
    
    colors = ['r', 'deepskyblue', 'gold']
    
    if highlight == 1:
        explode = (0.1, 0, 0)
    elif highlight == 2:
        explode = (0,0.1,0)
    elif highlight == 3:
        explode = (0, 0, 0.1)
    else:
        explode = (0, 0, 0)


    plt.pie(sizes, explode = explode, labels = labels, colors = colors, autopct='%1.1f%%', shadow = True, startangle =90)
    plt.axis('equal')
    image = plt.savefig("Pokemon_GO_distribution.png")

    return image
