n, m = map(int, input().split())
arr = [[0]*m for i in range(n)]

x, y, dx, dy = 0, 0, 0, 1
for i in range(n*m):
    arr[x][y] = str(i + 1).ljust(3)
    if arr[(x + dx) % n][(y + dy) % m]!=0:
        dx, dy = dy, -dx
    x, y = x + dx, y + dy

for row in arr:
    print(*row)