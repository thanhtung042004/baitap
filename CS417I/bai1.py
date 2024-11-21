G = []
P = []
const = 10

def CreateQ(open):
    for i in range(const):
        open.append([0, 0])  # Khởi tạo mảng con với 2 phần tử [0, 0]

def emptyQ(open):
    return len(open) - open.count(open[0]) == 0

def addQ(open, n, value, index):
    n = n + 1
    open.append([value, index])  # Thêm phần tử mới
    i = n
    while i > 1:
        j = int(i / 2)
        if open[i][0] < open[j][0]:
            open[i], open[j] = open[j], open[i]
        i = j
    return n

def removeQ(open):
    value = open[1][0]
    index = open[1][1]
    n = len(open) - 1
    open[1] = open[n]
    open.pop()  # Xóa phần tử cuối cùng
    i = 1
    while 2 * i <= n:
        j = 2 * i
        if j < n and open[j][0] > open[j + 1][0]:
            j = j + 1
        if open[i][0] <= open[j][0]:
            break
        open[i], open[j] = open[j], open[i]
        i = j
    return value, index, n

def split(string):
    parts = string.split()
    return int(parts[0]), int(parts[1]), int(parts[2])

def init(path, G):
    f = open(path)
    string = f.readline()
    n, a, z = split(string.replace('\t', ' '))

    for i in range(n + 1):
        G.append([0] * (n + 1))  # Khởi tạo ma trận G với giá trị 0

    while True:
        string = f.readline()
        if not string:
            break
        i, j, x = split(string.replace('\t', ' '))
        G[i][j] = G[j][i] = int(x)
    f.close()
    return n, a, z

def algorithm_for_tree(G, P, n, s, g):
    resul = 0
    close = [0] * (n + 1)
    o = [0] * (n + 1)
    P = [0] * (n + 1)
    open = []
    CreateQ(open)
    m = addQ(open, 0, resul, s)
    o[s] = 1
    P[s] = s
    while not emptyQ(open):
        value, u, m = removeQ(open)
        if u == g:
            resul = value
        for v in range(1, n + 1):
            if G[u][v] != 0 and o[v] == 0 and close[v] == 0:
                x = value + G[u][v]
                m = addQ(open, m, x, v)
                o[v] = 1
                P[v] = u
        close[u] = 1
        o[u] = 0
    return resul

def print_path(P, n, s, g):
    path = []
    for i in range(0, n + 1):
        path.append(0)
    print("Duong di tu %d den %d la\npath:" % (s, g), end=' ')
    path[0] = g

    i = P[g]
    k = 1
    while i != s:
        path[k] = i
        k = k + 1
        i = P[i]
    path[k] = s
    for j in range(0, k + 1):
        i = k - j
        if i > 0:
            print("%d =>" % path[i], end=' ')
        else:
            print("%d" % path[i], end=' ')

def main():
    n, s, g = init("graph6.inp", G)
    resul = algorithm_for_tree(G, P, n, s, g)
    print_path(P, n, s, g)
    print("\nresul: %d" % resul)

if __name__ == "__main__":
    main()
