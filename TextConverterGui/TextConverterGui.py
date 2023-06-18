import tkinter as tk
from tkinter import filedialog

def convert_file():
    try:
        zsafe_value = float(zsafe_entry.get())
        zbottom_value = float(zbottom_entry.get())
        zsurface_value = float(zsurface_entry.get())
        feedrate_slow_value = float(feedrate_slow_entry.get())
        feedrate_fast_value = float(feedrate_fast_entry.get())
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return

    source_file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if not source_file_path:
        return

    destination_file_path = source_file_path.replace(".txt", ".nc")

    with open(source_file_path, "r") as source_file:
        source_data = source_file.readlines()

    converted_data = []

    # Adding initial lines
    converted_data.append("G90\n")
    converted_data.append("M03 S1000\n")

    for line in source_data:
        line = line.strip()
        if line.startswith("X") and "Y" in line:
            x_value = float(line.split("X")[1].split("Y")[0]) * 25.4 / 10000  # Convert X coordinate from inches to mm
            y_value = float(line.split("Y")[1]) * 25.4 / 10000  # Convert Y coordinate from inches to mm

            # Adding the required lines for each X and Y line
            converted_data.append(f"G1 Z{zsafe_value} F{feedrate_fast_value}\n")
            converted_data.append(f"G0 X{x_value} Y{y_value}\n")
            converted_data.append(f"G1 Z{zsurface_value} F{feedrate_fast_value}\n")
            converted_data.append(f"G1 Z{zbottom_value} F{feedrate_slow_value}\n")
        else:
            # Ignore other lines
            pass

    # Adding final lines
    converted_data.append("M05\n")
    converted_data.append("M02\n")

    with open(destination_file_path, "w") as destination_file:
        destination_file.writelines(converted_data)

    print("Conversion successful!")

window = tk.Tk()
window.title("File Converter")

# Set window dimensions and position
window.geometry("400x300")
window.resizable(False, False)

# Create a frame for the labels and entry fieldss
frame = tk.Frame(window)
frame.pack(pady=20)

# Z Safe
zsafe_label = tk.Label(frame, text="Z Safe (mm):")
zsafe_label.grid(row=0, column=0, padx=10, pady=5)

zsafe_entry = tk.Entry(frame)
zsafe_entry.grid(row=0, column=1, padx=10, pady=5)

# Z Bottom
zbottom_label = tk.Label(frame, text="Z Bottom (mm):")
zbottom_label.grid(row=1, column=0, padx=10, pady=5)

zbottom_entry = tk.Entry(frame)
zbottom_entry.grid(row=1, column=1, padx=10, pady=5)

# Z Surface
zsurface_label = tk.Label(frame, text="Z Surface (mm):")
zsurface_label.grid(row=2, column=0, padx=10, pady=5)

zsurface_entry = tk.Entry(frame)
zsurface_entry.grid(row=2, column=1, padx=10, pady=5)

# Feedrate Slow
feedrate_slow_label = tk.Label(frame, text="Feedrate Slow (mm/s):")
feedrate_slow_label.grid(row=3, column=0, padx=10, pady=5)

feedrate_slow_entry = tk.Entry(frame)
feedrate_slow_entry.grid(row=3, column=1, padx=10, pady=5)

# Feedrate Fast
feedrate_fast_label = tk.Label(frame, text="Feedrate Fast (mm/s):")
feedrate_fast_label.grid(row=4, column=0, padx=10, pady=5)

feedrate_fast_entry = tk.Entry(frame)
feedrate_fast_entry.grid(row=4, column=1, padx=10, pady=5)

# Convert Button
convert_button = tk.Button(window, text="CONVERT", command=convert_file)
convert_button.pack(pady=10)

window.mainloop()
