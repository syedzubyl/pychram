s = 5

G = [
    [0, 9, 75, 0, 0],
    [9, 0, 95, 19, 42],
    [75, 95, 0, 51, 66],
    [0, 19, 51, 0, 31],
    [0, 42, 66, 31, 0]
]

selected = [0, 0, 0, 0, 0]
no_edge = 0

selected[0] = 1

# Print for edge and weight
print("Edge :Weight\n")

while no_edge < s - 1:
    minimum = 9999
    x = 0
    y = 0

    for i in range(s):
        if selected[i]:
            for j in range(s):
                if (not selected[j]) and G[i][j]:
                    if minimum > G[i][j]:
                        minimum = G[i][j]
                        x = i
                        y = j

    print(str(x) + "-" + str(y) + ":" + str(G[x][y]))
    selected[y] = 1
    no_edge += 1
