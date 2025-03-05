import tkinter as tk
from tkinter import ttk
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Load the Iris dataset from an online source
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
df = pd.read_csv(url)

# Create the main application window
root = tk.Tk()
root.title("Iris Data Analysis Dashboard")

# ----- Control Frame -----
control_frame = tk.Frame(root)
control_frame.pack(side=tk.TOP, fill=tk.X, padx=10, pady=10)

# Dropdown for X-Axis selection
tk.Label(control_frame, text="X-Axis:").grid(row=0, column=0, padx=5, pady=5)
x_axis_var = tk.StringVar()
x_axis_options = list(df.columns)
x_axis_var.set(x_axis_options[0])
x_menu = tk.OptionMenu(control_frame, x_axis_var, *x_axis_options)
x_menu.grid(row=0, column=1, padx=5, pady=5)

# Dropdown for Y-Axis selection
tk.Label(control_frame, text="Y-Axis:").grid(row=0, column=2, padx=5, pady=5)
y_axis_var = tk.StringVar()
y_axis_options = list(df.columns)
# Set a default different from x-axis if possible
default_y = y_axis_options[1] if len(y_axis_options) > 1 else y_axis_options[0]
y_axis_var.set(default_y)
y_menu = tk.OptionMenu(control_frame, y_axis_var, *y_axis_options)
y_menu.grid(row=0, column=3, padx=5, pady=5)

# Radio buttons for Plot Type selection
plot_type_var = tk.StringVar(value="Scatter")
tk.Label(control_frame, text="Plot Type:").grid(row=0, column=4, padx=5, pady=5)
tk.Radiobutton(control_frame, text="Scatter", variable=plot_type_var, value="Scatter").grid(row=0, column=5, padx=5, pady=5)
tk.Radiobutton(control_frame, text="Line", variable=plot_type_var, value="Line").grid(row=0, column=6, padx=5, pady=5)

# Button to update the plot
def update_plot():
    x_col = x_axis_var.get()
    y_col = y_axis_var.get()
    plot_type = plot_type_var.get()

    # Clear the previous figure content
    fig.clf()
    ax = fig.add_subplot(111)
    if plot_type == "Scatter":
        ax.scatter(df[x_col], df[y_col])
        ax.set_title(f"Scatter Plot of {y_col} vs {x_col}")
    elif plot_type == "Line":
        ax.plot(df[x_col], df[y_col])
        ax.set_title(f"Line Plot of {y_col} vs {x_col}")
    ax.set_xlabel(x_col)
    ax.set_ylabel(y_col)
    canvas.draw()

plot_button = tk.Button(control_frame, text="Plot", command=update_plot)
plot_button.grid(row=0, column=7, padx=5, pady=5)

# ----- Plot Frame -----
plot_frame = tk.Frame(root)
plot_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

# Create an initial matplotlib figure
fig = plt.Figure(figsize=(6, 4))
ax = fig.add_subplot(111)
ax.scatter(df[x_axis_var.get()], df[y_axis_var.get()])
ax.set_title(f"Scatter Plot of {y_axis_var.get()} vs {x_axis_var.get()}")
ax.set_xlabel(x_axis_var.get())
ax.set_ylabel(y_axis_var.get())

canvas = FigureCanvasTkAgg(fig, master=plot_frame)
canvas.draw()
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

# ----- Data Preview Frame -----
data_frame = tk.Frame(root)
data_frame.pack(side=tk.BOTTOM, fill=tk.X, padx=10, pady=10)
tk.Label(data_frame, text="Dataset Preview (First 5 Rows):").pack(anchor="w")
data_preview = tk.Text(data_frame, height=7, width=100)
data_preview.pack(side=tk.LEFT, fill=tk.X, expand=True)
data_preview.insert(tk.END, df.head().to_string())
data_preview.config(state=tk.DISABLED)

root.mainloop()
