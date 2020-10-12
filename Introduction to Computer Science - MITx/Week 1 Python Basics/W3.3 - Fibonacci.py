goal = int(input("Enter the endpoint number for Fibonacci sequence"))

result = 1
numOfIter = 0

def fib(goal):
    if numOfIter < goal:
        numOfIter += 1
        result = result + result - 1
        print(result)
        fib(goal)
    else:
        return result
    
    



fib(goal)