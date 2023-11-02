def findcollinear(x1, y1, x2, y2, x3, y3):

    if (y2 - y1)*(x3-x2) == (y3 - y2)*(x2 - x1):
        print("Yes")
    else:
        print("Not")

x1, y1, x2, y2, x3, y3 = 1, 1, 1, 6, 0, 9
findcollinear(x1, y1, x2, y2, x3, y3)
