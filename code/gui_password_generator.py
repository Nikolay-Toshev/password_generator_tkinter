from tkinter import *
from password_generator import *

window = Tk()
window.title('Password Generator')
window.geometry('300x410')
window.resizable(width=False, height=False)

# Define Input Fields
num_of_symbols = Entry(window, width=5, font=('times new roman', '14'))
num_of_symbols.insert(0, '15')
num_of_passwords = Entry(window, width=5, font=('times new roman', '14'))
num_of_passwords.insert(0, '1')
num_of_numbers = Entry(window, width=5, font=('times new roman', '14'))
num_of_numbers.insert(0,0)
num_of_spec_symbols = Entry(window, width=5, font=('times new roman', '14'))
num_of_spec_symbols.insert(0, 0)


def gen():
    sc = Scrollbar(window, orient='vertical')
    sc.grid(row=5, column=1, sticky='nse',padx=15)
    t = Text(window, width=20, height=7, font=('times new roman', '16'), yscrollcommand=sc.set)
    t.tag_config('center', justify='center')
    t.insert('1.0', generate(int(num_of_symbols.get()), int(num_of_numbers.get()),
                             int(num_of_spec_symbols.get()), int(num_of_passwords.get())))
    t.tag_add('center', '1.0', 'end')
    sc.config(command=t.yview)
    t.grid(row=5, column=0, sticky='ne', pady=20)


# Locate the Input Fields
num_of_symbols.grid(row=0, column=1, pady=5)
num_of_passwords.grid(row=1, column=1, pady=5)
num_of_numbers.grid(row=2, column=1, pady=5)
num_of_spec_symbols.grid(row=3, column=1, pady=5)

# Define instructions
num_of_symbols_text = Label(window, text='Password Length ', font=('times new roman', '14'))
num_of_passwords_text = Label(window, text='Password Variations ', font=('times new roman', '14'))
num_of_numbers_text = Label(window, text='Number of Digits ', font=('times new roman', '14'))
num_of_spec_symbols_text = Label(window, text='Number of Special symbols ', font=('times new roman', '14'))

# Locate the instructions
num_of_symbols_text.grid(row=0, column=0, sticky='w', pady=5, padx=15)
num_of_passwords_text.grid(row=1, column=0, sticky='w', pady=5, padx=15)
num_of_numbers_text.grid(row=2, column=0, sticky='w', pady=5, padx=15)
num_of_spec_symbols_text.grid(row=3, column=0, sticky='w', pady=5, padx=15)

# Define a Generate Button
generate_button = Button(window, text='GENERATE', font=('times new roman', '20'), command=gen, padx=45, bg='grey')
# generate_button.grid(row=4, column=0, columnspan=2)

generate_button.grid(row=4, column=0, columnspan=2)


window.mainloop()
