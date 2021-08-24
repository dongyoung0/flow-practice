#fizzbuzz

def fizzbuzz():
    n = int(input("Input number: "))
    for i in range(1,n+1):
        print(i)
        if i%15==0:
            print(f'{i} fizzbuzz')
fizzbuzz()
