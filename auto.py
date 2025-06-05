import pyautogui
import time



# Passo 1 - abrir sistema - https://dlp.hashtagtreinamentos.com/python/intensivao/login
pyautogui.PAUSE = 0.5
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
time.sleep(1)
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(2)
# Passo 2 - fazer login
pyautogui.click(x=643, y=534)  # Ajuste as coordenadas conforme necessário
pyautogui.write("teste2025@gmail.com")
pyautogui.press("tab")
pyautogui.write("amelhorsenha123teste2025@gmail.com")
pyautogui.press("tab")
pyautogui.press("enter")


# Passo 3 - importar a base de dados
import pandas 

tabela = pandas.read_csv("produtos.csv")
for linha in tabela.index:
    pyautogui.click(x=655, y=385)
    
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(codigo)
    pyautogui.press("tab")

    marca = tabela.loc[linha, "marca"]
    pyautogui.write(marca)
    pyautogui.press("tab")

    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(tipo)
    pyautogui.press("tab")

    categoria = str(tabela.loc[linha, "categoria"])
    pyautogui.write(categoria)
    pyautogui.press("tab")

    preco_unitario = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.write(preco_unitario)
    pyautogui.press("tab")

    custo = str(tabela.loc[linha, "custo"])
    pyautogui.write(custo)
    pyautogui.press("tab")

    obs = str(tabela.loc[linha, "obs"])
    pyautogui.write("" if pandas.isna(obs) else str(obs))
    pyautogui.press("tab")
    pyautogui.press("enter")

    pyautogui.scroll(10000)

