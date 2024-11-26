import tkinter as tk

def soma():
    n1 =float(input1.get())
    n2 =float(input2.get())
    soma = n1 + n2
    texto2.config(text=f'resultado:{soma}')

def sub():
    n1 =float(input1.get())
    n2 =float(input2.get())
    sub = n1 - n2
    texto2.config(text=f'resultado:{sub}')

def mult():
    n1 =float(input1.get())
    n2 =float(input2.get())
    mult = n1 * n2
    texto2.config(text=f'resultado:{mult}')

def div():
    n1 =float(input1.get())
    n2 =float(input2.get())
    div = n1 / n2
    texto2.config(text=f'resultado:{div}')

root = tk.Tk()
root.title('CALCULADORA')
root.geometry('620x620')

#label

texto = tk.Label(root, text='CALCULADORA')
texto.grid(row=1, column=1, padx=30, pady=20)

#input

input1= tk.Entry(root)
input1.grid(row=2, column=2)
input2= tk.Entry(root)
input2.grid(row=4, column=2)


#label -- texto

texto2=tk.Label(root, text = '=' )
texto2.grid(row = 5, column = 2)

#botao

btn = tk.Button(root, text="SOMA", command= soma)
btn.grid(row=7, column=2, pady=20)

btn = tk.Button(root, text="SUBTRAÇÃO", command= sub)
btn.grid(row=8, column=2, pady=20)

btn = tk.Button(root, text="MULTIPLICAÇÃO", command= mult)
btn.grid(row=9, column=2, pady=20)

btn = tk.Button(root, text="DIVISÃO", command= div)
btn.grid(row=10, column=2, pady=20)
root.mainloop()