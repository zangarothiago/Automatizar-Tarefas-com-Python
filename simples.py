import pyautogui as py
import time

cnpj = '54289996000126'

def acessar_simples_nacional():
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
    py.press
    py.press('enter')
    py.sleep(2)
    py.tripleClick(x=249, y=644)
    py.sleep(2)
    py.hotkey('ctrl', 'c')
    py.sleep(2)


acessar_simples_nacional()