# Author: Viktor Kolchenko viktor.kolchenko@gmail.com
bukovel_graph = [
[0, 4, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[2, 0, 2, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 4, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,	0],
[0,	0,	0,	0,	6,	0,	4,	0,	0,	2,	0,	0,	0,	0,	0,	0,	0,	0],
[0,	0,	0,	3,	0,	0,	0,	0,	0,	4,	3,	0,	0,	0,	0,	0,	0,	0],
[0,	0,	0,	0,	0,	0,	0,	16,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0],
[0,	0,	1,	0,	0,	0,	0,	0,	1,	0,	0, 0, 0, 0, 0,	0,	0,	0],
[0,	0,	0,	0,	0,	8,	0,	0,	0,	0,	0,	0,	2,	0,	0,	0,	0,	0],
[0,	0,	0,	0,	0,	0,	1,	0,	0,	0,	0,	0,	0,	0,	8,	0,	0,	0],
[0,	0,	0,	0,	8,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0],
[0,	0,	0,	0,	0,	0,	0,	0,	0,	5,	0,	0,	0,	0,	4,	0,	0,	0],
[0,	0,	5,	0,	0,	0, 0,	0,	0,	0,	0,	0,	0,	3,	0,	0,	0,	0],
[0,	0,	0,	0,	0,	0, 0,	4,	0,	0,	0,	3,	0,	6,	0,	6,	0,	0],
[0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	6,	0,	0,	4,	0,	10,	0],
[0,	0,	0,	0,	0,	0,	0,	0,	16,	0,	2,	0,	0,	8,	0,	0,	0,	0],
[0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	3,	0,	0,	0,	3,	0],
[0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	5,	0,	0,	0,	3],
[0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	6,	0]
] 

b = bukovel_graph

# Sorry for short variables names. Code was written on Android tablet with QPython.
def route_from(start_point, to=6):
    if start_point == to:
        return {'time': 0, 'checkpoints': [to]}

    inf = 99999
    v = len(b)
    next = {}
    g = {}
    for n, line in enumerate(b):
        g[n] = {}
        next[n] = {}
        for k, weight in enumerate(line):
            next[n][k] = k
            if weight:
                g[n][k] = weight
    #print g
    
    for k in range(v):
        for i in range(v):
            for j in range(v):
                if g[i].get(k, inf) + g[k].get(j, inf) < g[i].get(j, inf):
                    g[i][j] = g[i].get(k, inf) + g[k].get(j, inf)
                    next[i][j] = next[i][k]
        
    path = [start_point]
    step = start_point
    if not next[start_point].get(to):
        path = []
    else:
        while step != to:
            step = next[step][to]
            path.append(step)

    return {'time': g[start_point][to], 'checkpoints': path}

#print route_from(7)
