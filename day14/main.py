import matplotlib.pyplot as plt

def print_map(grid, sands, sx = 500, sy = 0):

  xs = [pt[0] for pt in grid]
  ys = [-pt[1] for pt in grid]



  sand_xs = [pt[0] for pt in sands]
  sand_ys = [-pt[1] for pt in sands]

  plt.scatter(xs, ys)
  plt.scatter(sand_xs, sand_ys)
  plt.scatter(sx, -sy)
  plt.rcParams["figure.figsize"] = (15,15)
  plt.show()

def place_rocks(data):
    rocks = set()
    for line in data.split("\n"):
        points = [tuple(map(int, p.split(","))) for p in line.split(" -> ")]
        for i in range(len(points)-1):
            p1, p2 = points[i], points[i+1]
            xr = range(min(p1[0], p2[0]), max(p1[0], p2[0]) + 1)
            yr = range(min(p1[1], p2[1]), max(p1[1], p2[1]) + 1)
            rocks.update({(x, y) for x in xr for y in yr})
    return rocks

data = open("day14/input.txt").read().strip()
rocks = place_rocks(data)
sands = set()
max_y = max((y for _, y in rocks))
x, y = (500, 0)
ct = p1 = p2 = 0
while True:
    if (x, y) in rocks:  # restart sand at origin
        (x, y) = (500, 0)
    if y > max_y and p1 == 0:  # abyss part 1
        print_map(rocks, sands, x, y)
        p1 = ct
    if (x, y + 1) not in rocks and y < max_y + 1:  # drop down?
        y += 1
    elif (x - 1, y + 1) not in rocks and y < max_y + 1:  # drop left-down?
        x -= 1
        y += 1
    elif (x + 1, y + 1) not in rocks and y < max_y + 1:  # drop right-down?
        x += 1
        y += 1
    else:  # hit somoething
        ct += 1
        rocks.add((x, y))
        sands.add((x,y))
    if (x, y) == (500, 0):  # filled
        p2 = ct
        break
print(f"Part 1: {p1}")
print(f"Part 2: {p2}")