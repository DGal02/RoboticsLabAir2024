import random
import numpy as np
import matplotlib.pyplot as plt
import os
from datetime import datetime

fileName = "random.txt"


def zad2():
    for i in range(1, 101):
        output = ''
        output += 'Fizz' * (i % 3 == 0)
        output += 'Buzz' * (i % 5 == 0)
        print(output or i)


def zad3(n):
    with open(fileName, 'w') as file:
        for _ in range(n):
            file.write(f"{random.randint(1, 100)}\n")


def loadNumbers():
    numbers = []
    with open(fileName, 'r') as file:
        for line in file:
            numbers.append(int(line.strip()))

    return numbers


def zad4():
    numbers = loadNumbers()
    print(f"średnia: {np.mean(numbers)}, odchylenie standardowe: {np.std(numbers)}")


def generateFibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


def zad5(n):
    with open(fileName, 'w') as file:
        for number in generateFibonacci(n):
            file.write(f"{number}\n")


def zad6():
    numbers = loadNumbers()
    plt.plot(numbers, marker='o', linestyle='-', color='b', label='Ciąg Fibonacciego')
    plt.title("Liczby ciągu Fibonacciego")
    plt.xlabel("Indeks")
    plt.ylabel("Wartość")
    plt.legend()
    plt.grid(True)
    plt.show()


def zad7(n, printValues=True):
    squaresDict = {x: x ** 2 for x in range(1, n + 1)}
    if printValues:
        print(squaresDict)

    return squaresDict


def zad8(n):
    print(sum(zad7(n, False).values()))


def generateRandomData():
    return os.urandom(100)


def zad9():
    for _ in range(10):
        dateFileName = datetime.now().strftime("%Y_%m_%d_%H_%M_%S_%f")
        with open(f"{dateFileName}.bin", 'wb') as file:
            file.write(generateRandomData())


zad9()
