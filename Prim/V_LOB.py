# network - adjacency matrix (not ordered)

import math

def read_network(network, path_to_adjacency_matrix):
    network_file = open(path_to_adjacency_matrix, 'r')
    for line in network_file:
        network.append(list(map(lambda x: math.inf if math.isinf(float(x)) else int(x), line.split())))
    network_file.close()


def find_min_edge(network, used_vertex, MST):
    #  tracking matrix
    min_weight = math.inf
    temp_not_used_vertex = -1
    temp_used_vertex = -1
    for i in sorted(used_vertex):
        for j in range(V):
            if j in used_vertex:
                continue
            temp_weight = network[i][j]
            if temp_weight < min_weight:
                temp_used_vertex = i
                min_weight = temp_weight
                temp_not_used_vertex = j

    if temp_not_used_vertex == -1:
        print("CHTO ETO, MIN EDGE NOT FOUND. DOLBAN")

    used_vertex.add(temp_not_used_vertex)
    MST[(temp_used_vertex, temp_not_used_vertex)] = min_weight
    return min_weight


network = []
read_network(network, '../adjacency_matrix_100_first.txt')
V = len(network)

# print(len(network))
# for line in network:
#     print(line)

used = set()
MST = dict()
SUMM_LENGTH = 0


used.add(0)

while len(MST) != V - 1:
    SUMM_LENGTH += find_min_edge(network, used, MST)

print(MST)
print(len(MST))
print(SUMM_LENGTH)