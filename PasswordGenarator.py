import tkinter as tk
import random
import string

def generate_password():
    length = int(length_var.get())
    use_letters = letters_var.get()
    use_numbers = numbers_var.get()
    use_symbols = symbols_var.get()
    
    characters = ""
    if use_letters:
        characters += string.ascii_letters
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation
    
    if not characters:
        password_var.set("Selecione pelo menos um tipo de caractere")
        return
    
    password = "".join(random.choice(characters) for _ in range(length))
    password_var.set(password)

# Criando a janela principal
root = tk.Tk()
root.title("Gerador de Senhas")
root.geometry("300x300")

# Variáveis
length_var = tk.StringVar(value="12")
letters_var = tk.BooleanVar(value=True)
numbers_var = tk.BooleanVar(value=True)
symbols_var = tk.BooleanVar(value=True)
password_var = tk.StringVar()

# Layout
tk.Label(root, text="Comprimento da senha (até 12):").pack()
tk.Spinbox(root, from_=1, to=12, textvariable=length_var).pack()
tk.Checkbutton(root, text="Letras", variable=letters_var).pack()
tk.Checkbutton(root, text="Números", variable=numbers_var).pack()
tk.Checkbutton(root, text="Símbolos", variable=symbols_var).pack()
tk.Button(root, text="Gerar Senha", command=generate_password).pack()
tk.Entry(root, textvariable=password_var, state='readonly', width=30).pack()

# Rodando a interface
tk.mainloop()



