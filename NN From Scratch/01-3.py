# random number
from random import seed
from random import random
from random import uniform

seed(1)

# Get input
input = int(input("Type your integer: "))

# Neural network
# # Input neuron
w1 = [random(), random()]
b1 = random()
n1out1 = input*w1[0] + b1
n1out2 = input*w1[1] + b1

# # Hidden Neurons
# # # 1st hidden neuron
w2 = random()
b2 = random()
n2out = n1out1*w2 + b2

# # # 2nd hidden neuron
w3 = random()
b3 = random()
n3out = n1out2*w3 + b3

# # Output neuron
w4 = [random(), random()]
b4 = random()
result = n2out*w4[0] + n3out*w4[1] + b4

print(result)


# Training function
def training():
    global w1
    global w2
    global w3
    global w4
    global result
    delta = result - input
    i = 0
    while i <= 10:
        if delta > 0:
            w1[0] = uniform(w1[0], 1)
            w1[1] = uniform(w1[1], 1)
            w2 = uniform(w2, 1)
            w3 = uniform(w3, 1)
            w4 = [uniform(w4[0], 1), uniform(w4[1], 1)]
        elif delta < 0:
            w1 = [uniform(-1, w1[0]), uniform(-1, w1[1])]
            w2 = uniform(-1, w2)
            w3 = uniform(-1, w3)
            w4 = [uniform(-1, w4[0]), uniform(-1, w4[1])]
        else:
            break
        result = n2out*w4[0] + n3out*w4[1] + b4
        delta = result - input
        print(f"Delta is {delta}")
        i += 0.5
        seed(i)


training()
