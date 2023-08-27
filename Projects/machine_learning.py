from sklearn.linear_model import LinearRegression
import numpy as np

def run_ml():
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

    # Display model parameters and predictions
    print("Model Coefficients:", model.coef_)
    print("Model Intercept:", model.intercept_)
    print("\nPredictions for new data:")
    for i in range(len(new_X)):
        print(f"Input: {new_X[i][0]}, Predicted Output: {predicted_y[i][0]}")

# Call the function when running machine_learning.py directly
if __name__ == "__main__":
    run_ml()
