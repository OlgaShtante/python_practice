def multiplication_table_1():
    for i in range(1, 11):
        row = [i * j for j in range(1, 11)]
        print(" ".join("{:3}".format(cell) for cell in row))

multiplication_table_1()

print(" *"*20) #add delimiter between outputs

def multiplication_table_2():
    i = 1
    while i <= 10:
        row = [i * j for j in range(1, 11)]
        print(" ".join("{:3}".format(cell) for cell in row))
        i += 1
multiplication_table_2()