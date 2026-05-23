import customtkinter as ctk
from math import *
from datetime import datetime

# =========================
# APP SETTINGS
# =========================

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("520x860")
app.title("Smart Calculator")
app.resizable(False, False)

# =========================
# VARIABLES
# =========================

expression = ""

# =========================
# FUNCTIONS
# =========================

def update_display():
    display.delete(0, "end")
    display.insert(0, expression)


def press(value):
    global expression
    expression += str(value)
    update_display()


def clear():
    global expression
    expression = ""
    update_display()


def backspace():
    global expression
    expression = expression[:-1]
    update_display()


def calculate():
    global expression

    try:
        result = str(eval(expression))

        current_time = datetime.now().strftime("%H:%M:%S")

        history_box.insert(
            "0.0",
            f"[{current_time}] {expression} = {result}\n"
        )

        expression = result
        update_display()

    except:
        display.delete(0, "end")
        display.insert(0, "Error")
        expression = ""


def scientific_function(func):
    global expression

    try:
        value = float(display.get())

        operations = {
            "sqrt": sqrt(value),
            "sin": sin(radians(value)),
            "cos": cos(radians(value)),
            "tan": tan(radians(value)),
            "log": log10(value),
            "ln": log(value),
            "square": value ** 2,
            "cube": value ** 3,
            "factorial": factorial(int(value)),
            "inverse": 1 / value,
            "pi": pi
        }

        result = round(operations[func], 6)

        current_time = datetime.now().strftime("%H:%M:%S")

        history_box.insert(
            "0.0",
            f"[{current_time}] {func}({value}) = {result}\n"
        )

        expression = str(result)
        update_display()

    except:
        display.delete(0, "end")
        display.insert(0, "Error")
        expression = ""


def clear_history():
    history_box.delete("0.0", "end")


def toggle_theme():

    current_mode = ctk.get_appearance_mode()

    if current_mode == "Dark":
        ctk.set_appearance_mode("light")
    else:
        ctk.set_appearance_mode("dark")


# =========================
# TITLE
# =========================

title = ctk.CTkLabel(
    app,
    text="Smart Scientific Calculator",
    font=("Arial", 26, "bold")
)

title.pack(pady=10)

# =========================
# DISPLAY
# =========================

display = ctk.CTkEntry(
    app,
    width=420,
    height=65,
    font=("Arial", 26),
    justify="right",
    corner_radius=20
)

display.pack(pady=12)

# =========================
# MAIN BUTTON FRAME
# =========================

button_frame = ctk.CTkFrame(
    app,
    fg_color="transparent"
)

button_frame.pack(pady=5)

buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "=", "+"]
]

# =========================
# NORMAL BUTTONS
# =========================

for row_index, row in enumerate(buttons):

    for col_index, text in enumerate(row):

        if text == "=":

            button = ctk.CTkButton(
                button_frame,
                text=text,
                width=85,
                height=65,
                font=("Arial", 22, "bold"),
                fg_color="green",
                hover_color="darkgreen",
                corner_radius=18,
                command=calculate
            )

        else:

            button = ctk.CTkButton(
                button_frame,
                text=text,
                width=85,
                height=65,
                font=("Arial", 22, "bold"),
                corner_radius=18,
                hover_color="#1f6aa5",
                command=lambda value=text: press(value)
            )

        button.grid(
            row=row_index,
            column=col_index,
            padx=8,
            pady=8
        )

# =========================
# ACTION BUTTONS
# =========================

action_frame = ctk.CTkFrame(
    app,
    fg_color="transparent"
)

action_frame.pack(pady=8)

clear_button = ctk.CTkButton(
    action_frame,
    text="C",
    width=120,
    height=55,
    font=("Arial", 20, "bold"),
    fg_color="red",
    hover_color="darkred",
    corner_radius=18,
    command=clear
)

clear_button.grid(row=0, column=0, padx=8)

back_button = ctk.CTkButton(
    action_frame,
    text="⌫",
    width=120,
    height=55,
    font=("Arial", 20, "bold"),
    corner_radius=18,
    command=backspace
)

back_button.grid(row=0, column=1, padx=8)

theme_button = ctk.CTkButton(
    action_frame,
    text="Theme",
    width=120,
    height=55,
    font=("Arial", 20, "bold"),
    corner_radius=18,
    command=toggle_theme
)

theme_button.grid(row=0, column=2, padx=8)

# =========================
# SCIENTIFIC BUTTONS
# =========================

science_frame = ctk.CTkFrame(app)

science_frame.pack(pady=8)

science_buttons = [
    ("√", "sqrt"),
    ("sin", "sin"),
    ("cos", "cos"),
    ("tan", "tan"),
    ("log", "log"),
    ("ln", "ln"),
    ("x²", "square"),
    ("x³", "cube"),
    ("n!", "factorial"),
    ("1/x", "inverse"),
    ("π", "pi")
]

for index, (text, func) in enumerate(science_buttons):

    button = ctk.CTkButton(
        science_frame,
        text=text,
        width=90,
        height=50,
        font=("Arial", 16, "bold"),
        corner_radius=15,
        command=lambda f=func: scientific_function(f)
    )

    button.grid(
        row=index // 4,
        column=index % 4,
        padx=6,
        pady=6
    )

# =========================
# EXTRA BUTTONS
# =========================

extra_frame = ctk.CTkFrame(
    app,
    fg_color="transparent"
)

extra_frame.pack(pady=5)

clear_history_button = ctk.CTkButton(
    extra_frame,
    text="Clear History",
    width=180,
    height=50,
    font=("Arial", 18, "bold"),
    fg_color="red",
    hover_color="darkred",
    corner_radius=15,
    command=clear_history
)

clear_history_button.grid(row=0, column=0, padx=8)

copy_button = ctk.CTkButton(
    extra_frame,
    text="Copy Result",
    width=180,
    height=50,
    font=("Arial", 18, "bold"),
    corner_radius=15,
    command=lambda: app.clipboard_append(display.get())
)

copy_button.grid(row=0, column=1, padx=8)

# =========================
# HISTORY TITLE
# =========================

history_title = ctk.CTkLabel(
    app,
    text="Calculation History",
    font=("Arial", 20, "bold")
)

history_title.pack(pady=(8, 5))

# =========================
# HISTORY BOX
# =========================

history_box = ctk.CTkTextbox(
    app,
    width=420,
    height=80,
    font=("Consolas", 14),
    corner_radius=15
)

history_box.pack(pady=5)

# =========================
# FOOTER
# =========================

footer = ctk.CTkLabel(
    app,
    text="Developed using Python + CustomTkinter",
    font=("Arial", 12)
)

footer.pack(pady=8)

# =========================
# RUN APP
# =========================

app.mainloop()