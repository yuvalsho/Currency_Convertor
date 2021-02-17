from tkinter import *
from tkinter import messagebox
import requests


def exchange():
    source = var1.get()
    output = var2.get()
    amount = var3.get()
    if source.__eq__('') or output.__eq__(''):
        messagebox.showinfo('error', 'please enter two currencies to convert')
    else:
        if amount.isnumeric():
            amount = float(amount)
            if source.__eq__('USD'):
                rate = data['conversion_rates'][output]

            elif output.__eq__('USD'):
                rate = 1 / (data['conversion_rates'][source])

            else:
                rate = (data['conversion_rates'][output]) / (data['conversion_rates'][source])
            total = amount * rate
            message = f'{amount} {source}  -----> {total} {output}'
            messagebox.showinfo('conversion completed', message)
        else:
            messagebox.showinfo('error', 'amount to convert must be a number')


if __name__ == '__main__':
    top = Tk()
    top.title('currency convertor')
    top.columnconfigure(0, pad=10)
    top.columnconfigure(1, pad=10)
    top.columnconfigure(2, pad=10)
    top.rowconfigure(0, pad=10)
    top.rowconfigure(1, pad=10)
    top.rowconfigure(2, pad=10)
    url = 'https://v6.exchangerate-api.com/v6/c0382587a6dc4a003cca73d4/latest/USD'
    response = requests.get(url)
    data = response.json()
    currencies = list(data['conversion_rates'].keys())
    var1 = StringVar(top)
    var1.set('')
    var2 = StringVar(top)
    var2.set('')
    text_be = StringVar(top)
    text_be.set('please chose currency to transfer from:')
    label_before = Label(top, textvariable=text_be)
    label_before.grid(row=0, column=0)
    text_af = StringVar(top)
    text_af.set('please chose currency to transfer to:')
    label_after = Label(top, textvariable=text_af)
    label_after.grid(row=0, column=2)
    before = OptionMenu(top, var1, *currencies)
    before.grid(row=1, column=0)
    after = OptionMenu(top, var2, *currencies)
    after.grid(row=1, column=2)
    input_text = StringVar(top)
    var3 = StringVar(top)
    input_text.set('please enter amount to convert:')
    amount_label = Label(top, textvariable=input_text)
    amount_label.grid(row=1, column=1)
    input_num = Entry(top, justify=CENTER, textvariable=var3, width=20)
    input_num.grid(row=2, column=1)
    action = Button(master=top, text='convert', padx=50, command=lambda: exchange())
    action.grid(row=3, column=1)
    top.mainloop()
