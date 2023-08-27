import pandas as pd
import matplotlib.pyplot as plt

def analyze_data():
    # Load data from a CSV file
    data = pd.read_csv("data.csv")

    # Display basic information about the dataset
    print("Dataset Info:")
    print(data.info())

    # Display descriptive statistics
    print("\nDescriptive Statistics:")
    print(data.describe())

    # Perform data analysis
    # ...

    # Create a histogram of a numeric column
    plt.figure(figsize=(8, 6))
    plt.hist(data["Age"], bins=10, edgecolor="black")
    plt.xlabel("Age")
    plt.ylabel("Frequency")
    plt.title("Age Distribution")
    plt.show()

    # Create a scatter plot of two numeric columns
    plt.figure(figsize=(8, 6))
    plt.scatter(data["Height"], data["Weight"], alpha=0.7)
    plt.xlabel("Height")
    plt.ylabel("Weight")
    plt.title("Height vs Weight")
    plt.show()

# Call the function when running data_analysis.py directly
if __name__ == "__main__":
    analyze_data()
