#Calculator just to showcase code I can write
import sys
from statistics import median
import cowsay

def main():
    introduce()
    mode()

def introduce():
    try:
        print('Welcome to my calculator! It has a simple and advanced mode. Would you like to know more?')
        a = input('y/n: ').lower().strip()
        if a == 'y':
            print('Simple mode will do basic math.')
            print('Advanced should be used for the following:')
            print('Finding out how much to tip at a restaurant', end=' | ')
            print('Finding the median of a list of numbers', end=' | ')
            print('Getting the power of a number')
            print('Bonus: there is also a hidden cow mode. type "moo" instead of s or a')
    except EOFError:
        sys.exit('Goodbye')
def tipcal():
    while True:
        try:
            x=input('How much was the bill? $')
            x=float(x)
            y=input('Percent to tip? ').replace('%', '')
            y=(float(y) / 100)
            z = (x*y)
            print('Tip amount: ', '$', z, sep='')
            break
        except ValueError:
            print('Invalid input. Please only input numbers')


def mediancal(): #Median Calcluator
    d= []
    while True:
        z = input('enter numbers, type f when done: ')
        if z == 'f':
            print('the median of your list is', median(d))
            sys.exit()
        else:
            z=float(z)
            d.append(z)

def powcal(): #Power Calculator
    x = input('Number? ')
    y = input('To the power of? ')
    x=float(x)
    y=float(y)
    z= pow(x, y)
    print(x, 'to the power of', y, 'is', z)
    sys.exit()

def advanced():
    l = input('tip, median, or power? ').lower().replace(' ', '')
    if l == 'tip':
        tipcal()
    elif l == 'median':
        mediancal()
    elif l == 'power':
        powcal()

def simple():
    try:
        prob = input('Input: ').replace(' ', '').lower()
        for char in prob:
            if char in ['+', '-', 'x', '*', '/']:
                z=char
        x, y = prob.split(z)
        x=float(x)
        y=float(y)
        if z == '+':
            ans = (x + z)
            print(x, z, y, 'is', ans)
        elif z == '-':
            ans = (x - y)
            print(x, z, y, 'is', ans)
        elif z == 'x' or z == '*':
            ans = (x * y)
            print(x, z, y, 'is', ans)
        else:
            ans = (x/y)
            print(x, z, y, 'is', ans)
    except ValueError:
        sys.exit('Invalid Input')
def cow():
    try:
        prob = input('Input: ').replace(' ', '').lower()
        for char in prob:
            if char in ['+', '-', 'x', '*', '/']:
                z=char
        x, y = prob.split(z)
        x=float(x)
        y=float(y)
        if z == '+':
            ans = (x + z)
            cowsay.cow(ans)
        elif z == '-':
            ans = (x - y)
            cowsay.cow(ans)
        elif z == 'x' or z == '*':
            ans = (x * y)
            cowsay.cow(ans)
        else:
            ans = (x/y)
            cowsay.cow(ans)
    except ValueError:
        sys.exit('Invalid Input')
def mode():
    try:
        a = input('Select Mode (a/s): ').lower().strip()
        if a == 'a':
            advanced()
        if a == 's':
            simple()
        elif a == 'moo':
            cow()
    except EOFError:
        sys.exit('Goodbye')

main()