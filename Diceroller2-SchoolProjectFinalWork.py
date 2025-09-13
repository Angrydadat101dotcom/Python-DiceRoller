import tkinter as tk
from PIL import Image, ImageTk
import random

def roll_dice():
    """Rolls the selected dice and displays the results."""
    # Get the state of each checkbox (1 if checked, 0 if unchecked)
    d4_enabled = d4_var.get()
    d6_enabled = d6_var.get()
    d8_enabled = d8_var.get()
    d10_enabled = d10_var.get()
    d12_enabled = d12_var.get()
    d20_enabled = d20_var.get()
    d100_enabled = d100_var.get()
    
    
    
    
    results = []
    
    if d4_enabled:
        results.append(f"d4: {random.randint(1, 4)}")
    if d6_enabled:
        results.append(f"d6: {random.randint(1, 6)}")
    if d8_enabled:
        results.append(f"d8: {random.randint(1, 8)}")
    if d10_enabled:
        results.append(f"d10: {random.randint(1, 10)}")
    if d12_enabled:
        results.append(f"d12: {random.randint(1, 12)}")
    if d20_enabled:
        results.append(f"d20: {random.randint(1, 20)}")
        
    if d100_enabled:
        results.append(f"d100: {random.randint(1, 100)}")
        
    if results:
        # Update the result label with the rolled values
        result_label.config(text="\n".join(results))
    else:
        result_label.config(text="Select at least one die to roll.")

# Create the main window
root = tk.Tk()
root.title("AD&D Dice Roller")
root.geometry("600x400")  # Set window size as needed


# Load the image using Pillow

image_path = "OGADND2E2.jpg"

pil_image = Image.open(image_path)


# Convert the Pillow image to a Tkinter-compatible format

tk_image = ImageTk.PhotoImage(pil_image)


# Create Label widget with image to act as background

background_label = tk.Label(root, image=tk_image)

background_label.place(x=0, y=0, relwidth=1, relheight=1)


# Keep a reference to prevent garbage collection

background_label.image = tk_image

# Create variables to hold the state of the checkboxes
d4_var = tk.IntVar()
d6_var = tk.IntVar()
d8_var = tk.IntVar()
d10_var = tk.IntVar()
d12_var = tk.IntVar()
d20_var = tk.IntVar()
d100_var = tk.IntVar()

# Create the heading label
heading_label = tk.Label(root, text="Select dice to roll:", font=("Helvetica", 14))
heading_label.pack(pady=10)

# Create the checkboxes for each die type
d4_checkbox = tk.Checkbutton(root, text="4-sided die (d4)", variable=d4_var)
d4_checkbox.pack(anchor="w", padx=20)

d6_checkbox = tk.Checkbutton(root, text="6-sided die (d6)", variable=d6_var)
d6_checkbox.pack(anchor="w", padx=20)

d8_checkbox = tk.Checkbutton(root, text="8-sided die (d8)", variable=d8_var)
d8_checkbox.pack(anchor="w", padx=20)

d10_checkbox = tk.Checkbutton(root, text="10-sided die (d10)", variable=d10_var)
d10_checkbox.pack(anchor="w", padx=20)

d12_checkbox = tk.Checkbutton(root, text="12-sided die (d12)", variable=d12_var)
d12_checkbox.pack(anchor="w", padx=20)

d20_checkbox = tk.Checkbutton(root, text="20-sided die (d20)", variable=d20_var)
d20_checkbox.pack(anchor="w", padx=20)

d100_checkbox = tk.Checkbutton(root, text="100-sided die(percentile) (d100)", variable=d100_var)
d100_checkbox.pack(anchor="w", padx=20)



# Create a button to roll the dice
roll_button = tk.Button(root, text="Roll Dice", command=roll_dice)
roll_button.pack(pady=20)

# Create a label to display the results
result_label = tk.Label(root, text="", font=("Helvetica", 12))
result_label.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()