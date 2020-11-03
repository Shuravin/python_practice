import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5, 6]
squares = [1, 4, 9, 16, 25, 36]

plt.style.use("fivethirtyeight")
fig, ax = plt.subplots()
ax.plot(input_values, squares, linewidth = 3)

#set chart title and label axes

ax.set_title("Squares", fontsize = 18)
ax.set_xlabel("Value", fontsize = 16)
ax.set_ylabel("Square of Value", fontsize = 16)

# set size of tick labels
ax.tick_params(axis = "both", labelsize = 14)

plt.show()