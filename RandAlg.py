import itertools
import numpy as np
import random


def is_rainbow(edge, c):
    colors = set()
    for i in edge:
        if c[i] in colors:
            return False
        colors.add(c[i])
    return True



def RandLocSearch(V, E, c, F, r):
    counter = 0
    sec_counter = 0
    rainbow_edges = []
    colors = list(range(r))
    for i in range(len(V) - r):
        for edge in E:
            if F[np.in1d(F, edge)].shape[0] == r and is_rainbow(edge, c):
                return 0
            if is_rainbow(edge, c) == False:
                counter += 1
            else:
                rainbow_edges.append(edge)
            if F[np.in1d(F, edge)].shape[0] != r - 1:
                sec_counter += 1
        if counter == len(E):
            return c
        if sec_counter == len(E):
            return c
        np.random.shuffle(rainbow_edges)
        v = -1
        for edge in rainbow_edges:
            if np.array(edge)[np.in1d(edge, F)].shape[0] == r - 1:
                v = np.array(edge)[~np.in1d(edge, F)]
                break
        new_color = random.choice(colors)
        if v == -1:
            continue
        while c[v[0]] == new_color:
            new_color = random.choice(colors)
        c[v[0]] = new_color
        F = F.tolist()
        F.append(v[0])
        F = np.array(F)
    return 0


                




def RandNRC(V, E, a, r, comb):
    colors = list(range(r))
    for i in range(1, int(a * (r / 2) ** len(V))):
        for j in comb:
            helpful = list(j)
            np.random.shuffle(helpful)
            F = np.array(helpful)
            d = dict()
            for k in V:
                if k not in F:
                    d[k] = random.choice(colors)
                else:
                    d[k] = np.where(F == k)[0][0]
            if type(RandLocSearch(V, E, d, F, r)) == dict:
                return d
    return 0



#n = int(input())
#r = int(input())
#a = int(input())
#V = np.array(list(range(n)))
#counter_3_2 = 0
#good_counter_3_2 = 0
#for n in range(6, 12):
    #r = 3
    #a = 2
    #V = np.array(list(range(n)))
    #ALL_E = list(itertools.combinations(V, r))
    #E = []
    #for j in range(5):
        #print(j)
        #for i in ALL_E:
            #criterion1 = random.randint(0, 1)
            #criterion2 = random.randint(0, 1)
            #if criterion1 == 1 and criterion2 == 1:
                #E.append(i)
        #if type(RandNRC(V, E, a, r, ALL_E)) == dict:
            #good_counter_3_2 += 1
        #counter_3_2 += 1
#print(counter_3_2, good_counter_3_2)

