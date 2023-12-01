import tkinter as tk
from tkinter import Label, Entry, Button
import math

def calculate_results():
    # Get values from the user input or use predefined values
    Pm = float(entry_Pm.get())
    Eff = float(entry_Eff.get())
    vm = float(entry_vm.get())
    powerfactor = float(entry_powerfactor.get())
    k = float(entry_k.get())
    n = float(entry_n.get())
    Nm = float(entry_Nm.get())
    number_of_poles = float(entry_number_of_poles.get())
    source_frequency = float(entry_source_frequency.get())

    # Calculate Iflc using the formula
    Iflc = Pm / (Eff * vm * powerfactor * math.sqrt(3))
    result_Iflc.config(text=f"Iflc = {Iflc:.4f}")

    # Calculate Istert using the formula
    Istert = n * Iflc
    result_Istert.config(text=f"Istert = {Istert:.4f}")

    # Calculate Tstart using the formula
    Tstart = k * (Istert ** 2)
    result_Tstart.config(text=f"Tstart = {Tstart:.4f}")

    # Calculate fs using the formula
    fs = (number_of_poles / 120) * abs((120 * source_frequency / number_of_poles) - Nm)
    result_fs.config(text=f"fs = {fs:.4f}")

    # Calculate Rr using the formula
    Rr = (3 * vm ** 2) / (2 * math.pi * fs * Tstart)
    result_Rr.config(text=f"Rr = {Rr:.4f}")

# Create the main application window
app = tk.Tk()
app.title("Motor Calculation App")
app.geometry("600x400")  # Set window size

# Customize the appearance
app.configure(bg='#3498db')  # Set background color

# Create a title label
title_label = Label(app, text="Motor Calculation", font=("Helvetica", 20, "bold"), fg='#ecf0f1', bg='#3498db')
title_label.grid(row=0, column=0, columnspan=3, pady=10)

# Create and place labels and entry widgets for user input
labels = ["Pm:", "Efficiency:", "Vm:", "Power Factor:", "k:", "n:", "Nm:", "Number of Poles:", "Source Frequency:"]
for i, label_text in enumerate(labels):
    Label(app, text=label_text).grid(row=i + 1, column=0, padx=5, pady=5)
    Entry(app).grid(row=i + 1, column=1, padx=5, pady=5)

# Button to trigger the calculation
calculate_button = Button(app, text="Calculate", command=calculate_results, bg='#2ecc71', fg='#ecf0f1', font=("Helvetica", 14, "bold"))
calculate_button.grid(row=len(labels) + 1, column=0, columnspan=3, pady=10)

# Labels to display the results
result_Iflc = Label(app, text="", font=("Helvetica", 12), fg='#ecf0f1', bg='#3498db')
result_Iflc.grid(row=len(labels) + 2, column=0, columnspan=3, pady=5)

result_Istert = Label(app, text="", font=("Helvetica", 12), fg='#ecf0f1', bg='#3498db')
result_Istert.grid(row=len(labels) + 3, column=0, columnspan=3, pady=5)

result_Tstart = Label(app, text="", font=("Helvetica", 12), fg='#ecf0f1', bg='#3498db')
result_Tstart.grid(row=len(labels) + 4, column=0, columnspan=3, pady=5)

result_fs = Label(app, text="", font=("Helvetica", 12), fg='#ecf0f1', bg='#3498db')
result_fs.grid(row=len(labels) + 5, column=0, columnspan=3, pady=5)

result_Rr = Label(app, text="", font=("Helvetica", 60), fg='#ecf0f1', bg='#3498db')
result_Rr.grid(row=len(labels) + 6, column=0, columnspan=3, pady=5)

# Run the application
app.mainloop()
