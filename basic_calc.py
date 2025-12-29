"""
Basic Calculator using Tkinter by @jeffsih.

Created a calculator window with clickable buttons and allow simple addition and subtraction.

The current_value isnt being returned and I dont know how to do so within tkinter button commands.
    Going to use Globals instead for now. Should refactor later to use a class based approach.

Next:   - Add multiplication and division operations. (Done)
        - Allow for continuous calculations without pressing clear each time. (Done)
        - Add a clear button to reset the calculator. (Done)
        - Add a backspace button to remove the last digit entered. (Done)
            - May need further testing.
        - Handle floats. (Done)
        - Implement BIDMAS order of operations. (Done)

        TODO:   - Add keyboard support.
        TODO:   - Improve the UI layout and design.
        TODO:   - Add error handling for invalid inputs (e.g., division by zero).
        TODO:   - Add more advanced functions (e.g., square root, exponentiation).

"""

import tkinter as tk

input_values = []
operations_list = []
current_input = ""
reset_flag = False
input_on_calc = ""  # Store the full input when '=' is pressed


def on_num_click(num):
    global current_input
    # Append the number to the label text
    current = display_label["text"]
    display_label.config(text=current + str(num))
    current_input = current_input + str(num)


def on_add_click():
    global current_input
    global input_values
    global operations_list
    # Get the current value from the label
    if display_label["text"] is None or display_label["text"] == "":
        return
    # print(current_input)
    input_values.append(float(current_input))
    current_input = ""
    operations_list.append("+")
    # Append '+' to the label text
    display_label.config(text=display_label["text"] + " + ")


def on_subtract_click():
    global current_input
    global input_values
    global operations_list
    # Get the current value from the label
    if display_label["text"] is None or display_label["text"] == "":
        return

    input_values.append(float(current_input))
    current_input = ""
    operations_list.append("-")
    # Append '-' to the label text
    display_label.config(text=display_label["text"] + " - ")


def on_equal_click():
    global current_input
    global input_values
    global operations_list

    if display_label["text"] is None or display_label["text"] == "":
        return

    # Store the final input inlcuding the equal sign
    global input_on_calc
    input_on_calc = display_label["text"] + " = "

    # Append the last input value and reset current input
    print("current_input:", current_input)
    input_values.append(int(current_input))
    current_input = ""

    # Perform calculation
    result = input_values[0]
    result = calculate_bidmas(result)

    # Display result
    display_label.config(text=str(result))

    # Clear inputs for next calculation - this will be changed later
    input_values.clear()
    operations_list.clear()
    current_input = str(result)  # Allow for continuous calculations


def calculate_bidmas(result):
    global input_values
    global operations_list

    # Perform multiplication and division first
    i = 0
    while i < len(operations_list):
        if operations_list[i] == "*":
            input_values[i] = input_values[i] * input_values[i + 1]
            operations_list.pop(i)
            input_values.pop(i + 1)
        elif operations_list[i] == "/":
            input_values[i] = input_values[i] / input_values[i + 1]
            operations_list.pop(i)
            input_values.pop(i + 1)
        else:
            i += 1

    # Perform addition and subtraction
    result = input_values[0]
    for i, operation in enumerate(operations_list):
        if operation == "+":
            result += input_values[i + 1]
        elif operation == "-":
            result -= input_values[i + 1]

    return result


def on_multiply_click():
    global current_input
    global input_values
    global operations_list
    # Get the current value from the label
    if display_label["text"] is None or display_label["text"] == "":
        return

    input_values.append(float(current_input))
    current_input = ""
    operations_list.append("*")
    # Append 'x' to the label text
    display_label.config(text=display_label["text"] + " x ")


def on_divide_click():
    global current_input
    global input_values
    global operations_list
    # Get the current value from the label
    if display_label["text"] is None or display_label["text"] == "":
        return

    input_values.append(float(current_input))
    current_input = ""
    operations_list.append("/")
    # Append '÷' to the label text
    display_label.config(text=display_label["text"] + " ÷ ")


def on_clear_click():
    global current_input
    global input_values
    global operations_list
    # Clear all globals and display
    current_input = ""
    input_values.clear()
    operations_list.clear()
    display_label.config(text="")


def on_backspace_click():  # Something in here is causing an error after deleting an operator.
    global current_input
    global operations_list
    # Remove the last character from the label text
    current = display_label["text"]
    if len(current) > 0:
        if current[-1] == " ":
            # If the last character is a space, remove the last three characters (operator and spaces)
            display_label.config(text=current[:-3])
            # Also need to remove the last operation from operations_list
            if operations_list:
                operations_list.pop()

            # Set current_input to the last input value & remove it from input_values.
            current_input = input_values[-1]
            input_values.pop()

        else:
            display_label.config(text=current[:-1])
            current_input = current_input[
                :-1
            ]  # Need to investigate what this is doing exactly.


"""
Window Creation and Button Setup Followed by Main Loop.
"""


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
        btn = tk.Button(
            grid_frame,
            text=str(button_num),
            width=3,
            height=2,
            command=lambda n=button_num: on_num_click(n),
        )
        btn.grid(row=row, column=col, padx=5, pady=5)

# Add the 0 button below the grid
tk.Button(
    grid_frame, text="0", width=3, height=2, command=lambda: on_num_click(0)
).grid(row=3, column=1, padx=5, pady=5)

# Add the '+' button
tk.Button(
    grid_frame,
    text="+",
    width=3,
    height=2,
    bg="sky blue",
    command=lambda: on_add_click(),
).grid(row=0, column=3, padx=5, pady=5)

# Add the '-' button
tk.Button(
    grid_frame,
    text="-",
    width=3,
    height=2,
    bg="sky blue",
    command=lambda: on_subtract_click(),
).grid(row=1, column=3, padx=5, pady=5)

# Add the '=' button
tk.Button(
    grid_frame, text="=", width=3, height=2, bg="red4", command=lambda: on_equal_click()
).grid(row=3, column=2, padx=5, pady=5)

# Add the 'C' (clear) button
tk.Button(
    grid_frame,
    text="C",
    width=3,
    height=2,
    bg="dark green",
    command=lambda: on_clear_click(),
).grid(row=1, column=4, padx=5, pady=5)

# Add the backspace button
tk.Button(
    grid_frame,
    text="←",
    width=3,
    height=2,
    bg="orange",
    command=lambda: on_backspace_click(),
).grid(row=0, column=4, padx=5, pady=5)

# Add the 'x' (multiply) button
tk.Button(
    grid_frame,
    text="x",
    width=3,
    height=2,
    bg="sky blue",
    command=lambda: on_multiply_click(),
).grid(row=2, column=3, padx=5, pady=5)

# Add the '÷' (divide) button
tk.Button(
    grid_frame,
    text="÷",
    width=3,
    height=2,
    bg="sky blue",
    command=lambda: on_divide_click(),
).grid(row=3, column=3, padx=5, pady=5)

# Add a decimial point button
tk.Button(
    grid_frame, text=".", width=3, height=2, command=lambda: on_num_click(".")
).grid(row=3, column=0, padx=5, pady=5)

# Start the tkinter main event loop
window.mainloop()
