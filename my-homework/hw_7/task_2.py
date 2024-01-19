
for i in range(1, 11):
    row = [i * j for j in range(1, 11)]
    print(" ".join("{:3}".format(cell) for cell in row))
