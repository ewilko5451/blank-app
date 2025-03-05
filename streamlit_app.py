import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Title and introduction
st.title("Data Analysis Dashboard")
st.markdown("Welcome to the dashboard. Explore data interactively with visualizations and summaries.")

# Sidebar for dataset selection and visualization options
dataset_choice = st.sidebar.selectbox("Select Dataset", ["Random Data", "Iris Dataset"])

if dataset_choice == "Random Data":
    st.header("Random Data")
    # Generate a DataFrame with random data
    df = pd.DataFrame(np.random.randn(200, 3), columns=['Feature 1', 'Feature 2', 'Feature 3'])
else:
    st.header("Iris Dataset")
    # Load the Iris dataset from an online source
    df = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv")

# Display a preview of the dataset and its summary statistics
st.write("### Dataset Preview")
st.dataframe(df.head())

st.write("### Summary Statistics")
st.write(df.describe())

# Sidebar options for visualizations
st.sidebar.markdown("### Visualization Options")
x_axis = st.sidebar.selectbox("X-Axis", df.columns)
y_axis = st.sidebar.selectbox("Y-Axis", df.columns)
plot_type = st.sidebar.radio("Plot Type", ("Scatter", "Line"))

# Create and display the selected plot
st.write("### Visualization")
fig, ax = plt.subplots()
if plot_type == "Scatter":
    ax.scatter(df[x_axis], df[y_axis])
    ax.set_title(f"Scatter Plot of {y_axis} vs {x_axis}")
elif plot_type == "Line":
    ax.plot(df[x_axis], df[y_axis])
    ax.set_title(f"Line Plot of {y_axis} vs {x_axis}")
ax.set_xlabel(x_axis)
ax.set_ylabel(y_axis)
st.pyplot(fig)
