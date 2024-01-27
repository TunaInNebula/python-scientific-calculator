from tkinter import Tk, Button, Label, ttk

square_islem = "**0.5"
tan_calc = ""

special_command_list = ["/", "-", "+", "*", "%", "** 0.5","(",")"]
num_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

current_text = ""


def num_button_clicked(number, command):
    global current_text
    current_text += str(number) + str(command)
    result_label.config(text=current_text)

def del_button_clicked():
    global current_text
    current_text = current_text[:-1]
    result_label.config(text=current_text)

def clear_button_clicked():
    global current_text
    current_text = ""
    result_label.config(text="Sonuç: ")
def enter_button_clicked():
    global current_text
    try:
        result = eval(current_text)
        result_label.config(text="Sonuç: " + str(result))
    except Exception as e:
        print(current_text)
        result_label.config(text="Hata: Geçersiz İfade")


win = Tk()
win.title("Hesap Makinesi")
result_label = Label(win, text="Sonuç: ")
result_label.grid(row=0, column=0, columnspan=4)

button_width = 8
padding = (5, 5)

# Number Buttons
for i in range(0, 10):
    ttk.Button(win, text=str(i), command=lambda i=i: num_button_clicked(i, ""), width=button_width, padding=padding).grid(
        row=((i + 1) - 1) // 3 + 1, column=((i + 1) - 1) % 3)

second_label = Label(win, text="FONKSİYONLAR")
second_label.config(bg="grey")
second_label.config(padx=25)
second_label.grid(row=5, column=0, columnspan=4)

# other buttons
for i, command in enumerate(special_command_list):
    ttk.Button(win, text=str(command), command=lambda command=command: num_button_clicked("", command),
               width=button_width, padding=padding).grid(row=6, column=i)


ttk.Button(win, text="DEL", command=del_button_clicked, width=button_width, padding=padding).grid(row=10, column=0)
ttk.Button(win, text="CLEAR", command=clear_button_clicked, width=button_width, padding=padding).grid(row=10, column=1)
ttk.Button(win, text="ENTER", command=enter_button_clicked, width=button_width, padding=padding).grid(row=10, column=2)

# special butons
square_islem_button = ttk.Button(win, text=" √ ", command=lambda: num_button_clicked("", square_islem), width=button_width,
                            padding=padding)
square_islem_button.grid(row=7, column=4)


win.mainloop()
