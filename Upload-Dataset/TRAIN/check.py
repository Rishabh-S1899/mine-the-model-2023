import pandas as pd
import matplotlib.pyplot as plt

# Sample DataFrame
data = {
    'x_column': [1, 2, 3, 4, 5],
    'y1': [10, 20, 30, 40, 50],
    'y2': [5, 10, 15, 20, 25],
    'y3': [8, 12, 16, 20, 24]
}

df = pd.DataFrame(data)

# Extract the x-axis column and y-axis columns
x_column = 'x_column'  # Change this to the column you want as the x-axis
y_columns = [col for col in df.columns if col != x_column]

# Create a single Matplotlib window and plot all y-columns against x_column
plt.figure(figsize=(10, 6))

for column in y_columns:
    plt.plot(df[x_column], df[column], label=column)

plt.xlabel(x_column)
plt.ylabel("Values")
plt.legend()
plt.title("Dataframe Columns vs. " + x_column)
plt.grid(True)

# Show the plot
plt.show()
