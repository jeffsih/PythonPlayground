"""
Basic Calculator using Tkinter

Create a calculator window with clickable buttons and allow simple addition and subtraction
Implement the actual calculation logic for '=' button.
The current_value isnt being returned and I dont know how to do so within tkinter button commands.
    Going to use Globals instead for now. Should refactor later to use a class based approach.

Note: At this time BIDMAS is not implemented.
"""

import tkinter as tk

input_values = []
operations_list = []
current_input = 0

def on_num_click(num):
    global current_input
    # Append the number to the label text
    current = display_label["text"]
    display_label.config(text=current + str(num))
    current_input = current + str(num)
    

def on_add_click():
    global current_input
    # Get the current value from the label
    if display_label["text"] is None or display_label["text"] == "":
        return
    print(current_input)
    input_values.append(int(current_input)) 
    current_input = ""
    operations_list.append('+')
    # Append '+' to the label text
    display_label.config(text=display_label["text"] + " + ")


def on_subtract_click():
    global current_input
    # Get the current value from the label
    if display_label["text"] is None or display_label["text"] == "":
        return
    
    input_values.append(int(current_input)) 
    current_input = ""
    operations_list.append('-')
    # Append '-' to the label text
    display_label.config(text=display_label["text"] + " - ")


# Create the main window
window = tk.Tk()
window.title("Calculator")
window.geometry("350x350")

# Display label
display_label = tk.Label(window, text="", font=("Arial", 16))
display_label.pack(pady=10)

# Frame to hold the grid
grid_frame = tk.Frame(window)
grid_frame.pack()

# Create a 3×3 grid of buttons
for row in range(3):
    for col in range(3):
        button_num = row * 3 + col + 1
        btn = tk.Button(grid_frame, text=str(button_num), width=3, height=2,
                        command=lambda n=button_num: on_num_click(n))
        btn.grid(row=row, column=col, padx=5, pady=5)

# Add the 0 button below the grid
tk.Button(
    grid_frame,
    text="0",
    width=3,
    height=2,
    command=lambda: on_num_click(0)
).grid(row=3, column=1, padx=5, pady=5)

# Add the '+' button
tk.Button(
    grid_frame,
    text="+",
    width=3,
    height=2,
    command=lambda: on_add_click()
).grid(row=0, column=3, padx=5, pady=5)

# Add the '-' button
tk.Button(
    grid_frame,
    text="-",
    width=3,
    height=2,
    command=lambda: on_subtract_click()
).grid(row=1, column=3, padx=5, pady=5)

# Add the '=' button
tk.Button(
    grid_frame,
    text="=",
    width=3,
    height=2,
    command=lambda: None  # Placeholder for future implementation
).grid(row=3, column=2, padx=5, pady=5)

window.mainloop()

