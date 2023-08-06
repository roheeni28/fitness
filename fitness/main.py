import subprocess
import tkinter as tk
from tkinter import messagebox, font
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from PIL import Image, ImageTk

def predict_fitness_points(row_data):
    # Load the dataset from CSV file
    dataset = pd.read_csv('dataset_updated.csv')

    # Clean the dataset by dropping rows with NaN or infinity values
    dataset = dataset.dropna()
    dataset = dataset[~dataset.isin([np.nan, np.inf, -np.inf]).any(1)]

    # Prepare the feature matrix and target variable
    X = dataset[['Age', 'Heart Rate (bpm)', 'Steps', 'BMI', 'Blood Glucose (mg/dL)', 'Cholesterol (mg/dL)', 'Sleep Duration (hours)', 'Caloric Expenditure (kcal)', 'Hydration (ml)', 'Resting Heart Rate (bpm)', 'Exercise Duration (minutes)']]
    y = dataset['Fitness Points']

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Create and train the multiple linear regression model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Create the feature vector for prediction
    user_input = pd.DataFrame([row_data[1:]], columns=X.columns)  # Exclude User ID from the input

    # Predict the output value based on user input
    prediction = model.predict(user_input)[0]

    return round(prediction, 2)

def predict_output():
    try:
        # Get the user input for feature values
        user_id = int(entry_user_id.get())
        age = float(entry_age.get())
        heart_rate = float(entry_heart_rate.get())
        steps = float(entry_steps.get())
        bmi = float(entry_bmi.get())
        blood_glucose = float(entry_blood_glucose.get())
        cholesterol = float(entry_cholesterol.get())
        sleep_duration = float(entry_sleep_duration.get())
        caloric_expenditure = float(entry_caloric_expenditure.get())
        hydration = float(entry_hydration.get())
        resting_heart_rate = float(entry_resting_heart_rate.get())
        exercise_duration = float(entry_exercise_duration.get())

        # Prepare the new row to be added to the dataset
        new_row = [user_id, age, heart_rate, steps, bmi, blood_glucose, cholesterol, sleep_duration, caloric_expenditure, hydration, resting_heart_rate, exercise_duration]

        # Predict the fitness points for the new data
        fitness_points = predict_fitness_points(new_row)

        # Append the fitness points to the new row
        new_row.append(fitness_points)

        # Save the new data to the "dataset_updated.csv" file
        with open('dataset_updated.csv', 'a') as f:
            f.write(','.join(map(str, new_row)) + '\n')

        # Show the predicted fitness points in a messagebox
        messagebox.showinfo("Success", f"The predicted fitness points are: {fitness_points}")

    except Exception as e:
        messagebox.showerror("Error", str(e))

# Create the main window
window = tk.Tk()
window.title("Fitness Points Prediction")
window.geometry("500x600")
window.configure(bg="#ffffff")

# Define custom fonts
title_font = font.Font(family="Helvetica", size=24, weight="bold")
label_font = font.Font(family="Helvetica", size=12)
button_font = font.Font(family="Helvetica", size=14, weight="bold")

# Create a grid layout
grid = tk.Frame(window)
grid.pack()
grid.columnconfigure(0, weight=1)
grid.columnconfigure(1, weight=1)
grid.rowconfigure(0, weight=1)

# Add the title
label_title = tk.Label(grid, text="Fitness Points Prediction", font=title_font)
label_title.grid(row=0, column=0, columnspan=2, sticky="ew")

# Add the user ID input
label_user_id = tk.Label(grid, text="Enter User ID:", font=label_font)
label_user_id.grid(row=1, column=0, sticky="e")
entry_user_id = tk.Entry(grid)
entry_user_id.grid(row=1, column=1, sticky="w")

# Add the other inputs
label_age = tk.Label(grid, text="Enter Age:", font=label_font)
label_age.grid(row=2, column=0, sticky="e")
entry_age = tk.Entry(grid)
entry_age.grid(row=2, column=1, sticky="w")

# Heart rate input
label_heart_rate = tk.Label(grid, text="Enter Heart Rate (bpm):", font=label_font)
label_heart_rate.grid(row=3, column=0, sticky="e")
entry_heart_rate = tk.Entry(grid)
entry_heart_rate.grid(row=3, column=1, sticky="w")

# Steps input
label_steps = tk.Label(grid, text="Enter Steps:", font=label_font)
label_steps.grid(row=4, column=0, sticky="e")
entry_steps = tk.Entry(grid)
entry_steps.grid(row=4, column=1, sticky="w")

# BMI input
label_bmi = tk.Label(grid, text="Enter BMI:", font=label_font)
label_bmi.grid(row=5, column=0, sticky="e")
entry_bmi = tk.Entry(grid)
entry_bmi.grid(row=5, column=1, sticky="w")

# Blood glucose input
label_blood_glucose = tk.Label(grid, text="Enter Blood Glucose (mg/dL):", font=label_font)
label_blood_glucose.grid(row=6, column=0, sticky="e")
entry_blood_glucose = tk.Entry(grid)
entry_blood_glucose.grid(row=6, column=1, sticky="w")

# Cholesterol input
label_cholesterol = tk.Label(grid, text="Enter Cholesterol (mg/dL):", font=label_font)
label_cholesterol.grid(row=7, column=0, sticky="e")
entry_cholesterol = tk.Entry(grid)
entry_cholesterol.grid(row=7, column=1, sticky="w")

# Sleep duration input
label_sleep_duration = tk.Label(grid, text="Enter Sleep Duration (hours):", font=label_font)
label_sleep_duration.grid(row=8, column=0, sticky="e")
entry_sleep_duration = tk.Entry(grid)
entry_sleep_duration.grid(row=8, column=1, sticky="w")

# Caloric expenditure input
label_caloric_expenditure = tk.Label(grid, text="Enter Caloric Expenditure (kcal):", font=label_font)
label_caloric_expenditure.grid(row=9, column=0, sticky="e")
entry_caloric_expenditure = tk.Entry(grid)
entry_caloric_expenditure.grid(row=9, column=1, sticky="w")

# Hydration input
label_hydration = tk.Label(grid, text="Enter Hydration (ml):", font=label_font)
label_hydration.grid(row=10, column=0, sticky="e")
entry_hydration = tk.Entry(grid)
entry_hydration.grid(row=10, column=1, sticky="w")

# Resting heart rate input
label_resting_heart_rate = tk.Label(grid, text="Enter Resting Heart Rate (bpm):", font=label_font)
label_resting_heart_rate.grid(row=11, column=0, sticky="e")
entry_resting_heart_rate = tk.Entry(grid)
entry_resting_heart_rate.grid(row=11, column=1, sticky="w")

# Exercise duration input
label_exercise_duration = tk.Label(grid, text="Enter Exercise Duration (minutes):", font=label_font)
label_exercise_duration.grid(row=12, column=0, sticky="e")
entry_exercise_duration = tk.Entry(grid)
entry_exercise_duration.grid(row=12, column=1, sticky="w")

# Add space after each row
for i in range(13):
    grid.rowconfigure(i, pad=10)

# Add the predict button
predict_button = tk.Button(grid, text="Predict and Save Data", command=predict_output, font=label_font)
predict_button.grid(row=13, column=0, columnspan=2, sticky="ew")

# Start the main event loop
window.mainloop()
