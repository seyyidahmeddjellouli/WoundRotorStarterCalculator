import tkinter as tk
from tkinter import Label, Entry, Button, Frame
import math

def calculate_results():
    # Get values from user input or use predefined values
    Pm = float(entry_Pm.get())
    Iflc = float(entry_Iflc.get())
    Nm = float(entry_Nm.get())
    Istart = float(entry_Istart.get())
    Tstart_per = float(entry_Tstart_per.get())
    motor_starting_time = float(entry_motor_starting_time.get())
    vm = float(entry_vm.get())

    # fixed values
    powerfactor = 0.85
    k = 0.01
    Nm = 1750
    number_of_poles = 4
    source_frequency = 50

    # Perform the calculation
    Iflc = Istart / motor_starting_time
    Tfullload = k * (Iflc ** 2)
    Tstart = Tfullload * Tstart_per
    fs = (number_of_poles / 120) * abs((120 * source_frequency / number_of_poles) - Nm)

    # Display the result
    Rr = (3 * vm ** 2) / (2 * math.pi * fs * Tstart)
    result_Rr.config(text=f"Rr = {Rr:.4f}")

# Create the main application window
app = tk.Tk()
app.title("Motor Calculation GUI")
app.geometry("400x400")  # Set the initial size of the window

# Custom styles
font_label = ("Helvetica", 12)
font_entry = ("Helvetica", 12)
font_button = ("Helvetica", 14, "bold")
font_result = ("Helvetica", 14, "italic")

# Create and place labels and entry widgets for user input
Label(app, text="Pm:", font=font_label).grid(row=0, column=0, padx=10, pady=10)
entry_Pm = Entry(app, font=font_entry)
entry_Pm.grid(row=0, column=1, padx=10, pady=10)

Label(app, text="Iflc:", font=font_label).grid(row=1, column=0, padx=10, pady=10)
entry_Iflc = Entry(app, font=font_entry)
entry_Iflc.grid(row=1, column=1, padx=10, pady=10)

Label(app, text="Nm:", font=font_label).grid(row=2, column=0, padx=10, pady=10)
entry_Nm = Entry(app, font=font_entry)
entry_Nm.grid(row=2, column=1, padx=10, pady=10)

Label(app, text="Istart:", font=font_label).grid(row=3, column=0, padx=10, pady=10)
entry_Istart = Entry(app, font=font_entry)
entry_Istart.grid(row=3, column=1, padx=10, pady=10)

Label(app, text="Tstart_per:", font=font_label).grid(row=4, column=0, padx=10, pady=10)
entry_Tstart_per = Entry(app, font=font_entry)
entry_Tstart_per.grid(row=4, column=1, padx=10, pady=10)

Label(app, text="Motor Starting Time:", font=font_label).grid(row=5, column=0, padx=10, pady=10)
entry_motor_starting_time = Entry(app, font=font_entry)
entry_motor_starting_time.grid(row=5, column=1, padx=10, pady=10)

Label(app, text="Vm:", font=font_label).grid(row=6, column=0, padx=10, pady=10)
entry_vm = Entry(app, font=font_entry)
entry_vm.grid(row=6, column=1, padx=10, pady=10)

# Button to trigger the calculation
calculate_button = Button(app, text="Calculate", font=font_button, command=calculate_results)
calculate_button.grid(row=7, column=0, columnspan=2, pady=20)

# Frame for the result
result_frame = Frame(app, bd=1, relief=tk.SOLID)
result_frame.grid(row=8, column=0, columnspan=2, pady=10)

# Label to display the result
result_Rr = Label(result_frame, text="", font=font_result)
result_Rr.pack(pady=5)

# Run the application
app.mainloop()
