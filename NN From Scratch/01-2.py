# input neurons
input = float(input("Type your input: "))
weight1 = [1.1, 1.3]
bias1 = [0.2, 0.3]
output1_1 = input*weight1[0] + bias1[0]
output1_2 = input*weight1[1] + bias1[1]

# hidden neurons
# # 1st
weight2_1 = [2.1, 2.4]
bias2_1 = 2
output2_1 = output1_1*weight2_1[0] + output1_2*weight2_1[1] + bias2_1

# # 2nd
weight2_2 = [3.1, 4.3]
bias2_2 = 1.5
output2_2 = output1_1*weight2_2[0] + output1_2*weight2_2[1] + bias2_2

# output neuron
weight_out = [1.56, 1.32]
bias_out = 0.43
result = output2_1*weight2_2[0] + output2_2*weight2_2[1] + bias_out

print(result)
