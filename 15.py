import tkinter as tk
from tkinter import messagebox

def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())

        if weight <= 0 or height <= 0:
            messagebox.showerror("Input Error", "Weight and height must be positive numbers.")
            return
        
        bmi = round(weight / (height ** 2), 2)
        
        # Determine BMI category
        if bmi < 18.5:
            category = "Underweight"
        elif 18.5 <= bmi < 24.9:
            category = "Normal weight"
        elif 25 <= bmi < 29.9:
            category = "Overweight"
        else:
            category = "Obese"
        
        bmi_label.config(text=f"BMI: {bmi} ({category})")

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numerical values for weight and height.")

# Initialize GUI
root = tk.Tk()
root.title("BMI Calculator")
root.geometry("300x200")
root.resizable(False, False)

# UI Elements
tk.Label(root, text="Weight (kg):").grid(row=0, column=0, padx=10, pady=5)
weight_entry = tk.Entry(root)
weight_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Height (m):").grid(row=1, column=0, padx=10, pady=5)
height_entry = tk.Entry(root)
height_entry.grid(row=1, column=1, padx=10, pady=5)

calculate_button = tk.Button(root, text="Calculate BMI", command=calculate_bmi)
calculate_button.grid(row=2, column=0, columnspan=2, pady=10)

bmi_label = tk.Label(root, text="BMI: ")
bmi_label.grid(row=3, column=0, columnspan=2, pady=5)

# Run GUI
root.mainloop()
