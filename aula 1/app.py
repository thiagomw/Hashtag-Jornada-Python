import pyautogui
import time
import pandas as pd

# Passo a passo do seu aplicativo / lógica do aplicativo

# Passo 1: Entrar no sistema
# Abrir o navegador

link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
login = "teste"
senha = "teste"

pyautogui.PAUSE = 0.5

pyautogui.press("win")
pyautogui.write("Firefox")
pyautogui.press("enter")
time.sleep(1)
pyautogui.write(link)
pyautogui.press("enter")
# Fazer uma pausa maior para o site carregar, caso for preciso
time.sleep(3)

# Passo 2: Fazer login
# Cliclar no campo de e-mail

pyautogui.click(x=1720, y=401)
pyautogui.write(login)
pyautogui.press("tab")
pyautogui.write(senha)
pyautogui.press("enter")
time.sleep(3)

# Passo 3: Abrir a base de dados (importar o arquivo)

tabela = pd.read_csv("./aula 1/produtos.csv")

# Passo 4: Cadastrar 1 produto

# Passo 5: Repetir o passo 4 até acabar a lista de produtos

for linha in tabela.index:

    codigo = str(tabela.loc[linha, "codigo"])
    marca = str(tabela.loc[linha, "marca"])
    tipo = str(tabela.loc[linha, "tipo"])
    categoria = str(tabela.loc[linha, "categoria"])
    preco_unitario = str(tabela.loc[linha, "preco_unitario"])
    custo = str(tabela.loc[linha, "custo"])
    obs = str(tabela.loc[linha, "obs"])

    pyautogui.click(x=1687, y=274)
    pyautogui.write(codigo)
    pyautogui.press("tab")
    pyautogui.write(marca)
    pyautogui.press("tab")
    pyautogui.write(tipo)
    pyautogui.press("tab")
    pyautogui.write(categoria)
    pyautogui.press("tab")
    pyautogui.write(preco_unitario)
    pyautogui.press("tab")
    pyautogui.write(custo)
    pyautogui.press("tab")
    if obs != "nan":
        pyautogui.write(obs)
    pyautogui.press("tab")

    pyautogui.press("enter") # Clicou no botão enviar
    
    # Voltar para o inicio da tela
    pyautogui.scroll(3000) 
