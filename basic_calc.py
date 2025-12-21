"""
Next steps:

Create a calculator window with clickable buttons and allow simple addition and subtraction
"""

import tkinter as tk

def on_num_click(num):
    # Append the number to the label text
    current = display_label["text"]
    display_label.config(text=current + str(num))


# Create the main window
window = tk.Tk()
window.title("3x3 Button Grid with Display")
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
        btn = tk.Button(grid_frame, text=str(button_num), width=3, height=3,
                        command=lambda n=button_num: on_num_click(n))
        btn.grid(row=row, column=col, padx=5, pady=5)

window.mainloop()

