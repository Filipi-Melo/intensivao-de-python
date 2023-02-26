import pyperclip as pyc, pyautogui as gui, pandas as pd
from pyautogui._pyautogui_win import _position
from pyautogui import click, hotkey, press
from time import sleep

gui.PAUSE=0.4
sleep(3)
print(_position())

arquivo = "./exportar/Vendas.xlsx"
tabela = pd.read_excel(arquivo)

print(tabela)
fatura = tabela["Valor Final"].sum()
print('\nFatura: ',fatura)

quantidade = tabela["Quantidade"].sum()
print('Quantidade: ',quantidade)

click(472, 735)
hotkey("ctrl","t")
pyc.copy("https://mail.google.com/mail/u/1/#inbox")
hotkey("ctrl","v")
sleep(1)
press("enter")
sleep(3)

click(x=60,y=200)
sleep(3)
pyc.copy("test@gmail.com")
hotkey("ctrl","v")
press("tab")

pyc.copy("Resultado da análise")
hotkey("ctrl","v")
press("tab")
texto = f"""Faturamento: R${fatura:,.2f} 
Quantidade: {quantidade:,} unidades

Feito com Python.
"""

pyc.copy(texto)
hotkey("ctrl","v")
click(966,694)
sleep(0.5)
click(363, 150)
sleep(0.5)
press("enter")
press("tab")
sleep(0.8)
press("enter")

sleep(3)
hotkey("ctrl","w")