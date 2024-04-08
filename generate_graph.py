import math, random





file_adj_matrix = open("adjacency_matrix_100_first.txt", "w")


n = 100
p = 0.33
diapason = (1, 200)

adj_matrix = [[str(math.inf) for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(i + 1, n):
        if random.random() < p:
            # file_adj_matrix.write(str(random.randint(*diapason)) + " ")
            weigth = str(random.randint(*diapason))
            adj_matrix[i][j] = weigth
            adj_matrix[j][i] = weigth
        else:
            # file_adj_matrix.write("0 ")
            continue

    # file_adj_matrix.write("\n")


for i in range(n):
    file_adj_matrix.write(' '.join(adj_matrix[i]) + '\n')