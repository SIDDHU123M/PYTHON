import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np

class GUIApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced GUI Application")

        self.label = tk.Label(self.root, text="Welcome to the Advanced GUI Application!")
        self.label.pack()

        self.file_button = tk.Button(self.root, text="Select CSV File", command=self.select_file)
        self.file_button.pack()

        self.analyze_button = tk.Button(self.root, text="Analyze Data", state=tk.DISABLED, command=self.analyze_data)
        self.analyze_button.pack()

        self.ml_button = tk.Button(self.root, text="Run Machine Learning", state=tk.DISABLED, command=self.run_machine_learning)
        self.ml_button.pack()

        self.file_path = None

    def select_file(self):
        self.file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
        if self.file_path:
            self.analyze_button.config(state=tk.NORMAL)
            self.ml_button.config(state=tk.NORMAL)

    def analyze_data(self):
        if self.file_path:
            try:
                data = pd.read_csv(self.file_path)
                messagebox.showinfo("Data Analysis", f"Loaded {len(data)} rows of data.")

                # Data analysis and visualization
                plt.figure(figsize=(8, 6))
                plt.hist(data["Age"], bins=10, edgecolor="black")
                plt.xlabel("Age")
                plt.ylabel("Frequency")
                plt.title("Age Distribution")
                plt.show()
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred: {e}")

    def run_machine_learning(self):
        if self.file_path:
            try:
                data = pd.read_csv(self.file_path)

                # Generate synthetic data
                np.random.seed(0)
                X = np.random.rand(100, 1) * 10
                y = 2 * X + 3 + np.random.randn(100, 1)

                # Create and train the model
                model = LinearRegression()
                model.fit(X, y)

                # Make predictions for new data
                new_X = np.array([[5], [7]])
                predicted_y = model.predict(new_X)

                messagebox.showinfo("Machine Learning Results", f"Predicted values: {predicted_y}")
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred: {e}")

root = tk.Tk()
app = GUIApp(root)
root.mainloop()
