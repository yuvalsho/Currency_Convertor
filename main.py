from tkinter import *
from tkinter import messagebox
import requests


def exchange(og, choice1, choice2):
    rate = 0
    if choice1.__eq__('USD'):
        rate = data['conversion_rates'][choice2]

    elif choice2.__eq__('USD'):
        rate = 1 / (data['conversion_rates'][choice2])

    else:
        rate = (data['conversion_rates'][choice2]) / (data['conversion_rates'][choice1])
    total = og * rate
    message = f'{og} {choice1} -> {total} {choice2}'
    messagebox.showinfo('convertion completed', message)


if __name__ == '__main__':
    top = Toplevel()
    top.columnconfigure(0, pad=5)
    top.columnconfigure(1, pad=5)
    top.rowconfigure(0, pad=5)
    top.rowconfigure(0, pad=5)
    url = 'https://v6.exchangerate-api.com/v6/c0382587a6dc4a003cca73d4/latest/USD'
    response = requests.get(url)
    data = response.json()
    currencies = list(data['conversion_rates'].keys())
    var1 = StringVar(top)
    var1.set('')
    var2 = StringVar(top)
    var2.set('')
    text_be = StringVar(top)
    text_be.set('please chose currency to transfer from')
    label_before = Label(top, textvariable=text_be)
    label_before.grid(row=0, column=1)
    text_af = StringVar(top)
    text_af.set('please chose currency to transfer to')
    label_after = Label(top, textvariable=text_af)
    label_after.grid(row=0, column=0)
    before = OptionMenu(top, var1, currencies)
    before.grid(row=1, column=1)
    after = OptionMenu(top, var2, currencies)
    after.grid(row=1, column=0)
    original = var1.get()
    target = var2.get
    amount = 0
    action = Button(top, text='convert', activebackground=True, command=exchange(amount, original, target))
    top.mainloop()
