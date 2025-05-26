import pyautogui as py
import time
import tkinter as tk
from tkinter import simpledialog, messagebox
import pyperclip

def acessar_simples_nacional(cnpj):
    py.sleep(1)
    py.click(x=1361, y=743)
    py.sleep(2)
    py.click(x=58, y=752)
    py.sleep(2)
    py.write('google chrome')
    py.sleep(2)
    py.press('enter')
    py.sleep(2) 
    py.write('consulta optante pelo simples nacional')
    py.sleep(2) 
    py.press('enter')
    py.sleep(2)
    py.click(x=320, y=366)
    py.sleep(2) 
    py.click(x=226, y=417)
    py.sleep(2)
    py.write(cnpj)
    py.sleep(2)
    py.press('tab')
    py.sleep(2)
    py.press('enter')
    py.sleep(2)
    py.tripleClick(x=249, y=644)
    py.sleep(2)
    py.hotkey('ctrl', 'c')
    py.sleep(2)

    # Mostrar conteúdo copiado
    resultado = pyperclip.paste()
    messagebox.showinfo("Resultado", f"RESULTADO:\n{resultado}")

# Criar janela para pegar o CNPJ e iniciar a automação
def main():
    root = tk.Tk()
    root.withdraw()  # Oculta a janela principal
    cnpj = simpledialog.askstring("CNPJ", "Digite o CNPJ (somente números):")

    if cnpj:
        acessar_simples_nacional(cnpj)
    else:
        messagebox.showwarning("Aviso", "Você não digitou o CNPJ.")

main()