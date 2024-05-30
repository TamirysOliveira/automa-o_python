import pyautogui as aut
import pandas as pd
import time

# Configuração do pause entre ações do pyautogui
aut.PAUSE = 0.5

# Abrindo o navegador e acessando o formulário
aut.press('win')
aut.write('chrome')
aut.press('enter')
time.sleep(2)  # Aguardar o navegador abrir
aut.write('https://form.jotform.com/241504236417046')
aut.press('enter')
time.sleep(5)  # Aguardar a página carregar

# Lendo o arquivo CSV
tabela = pd.read_csv("bd_alunos.csv", sep=";")
time.sleep(2)

# Preenchendo o formulário
for linha in tabela.index:
    nome = tabela.loc[linha, "Nome"]
    sobrenome = tabela.loc[linha, "Sobrenome"]
    email = tabela.loc[linha, "Email"]
    telefone = tabela.loc[linha, "Telefone"]
    endereco = tabela.loc[linha, "Endereco"]
    cidade = tabela.loc[linha, "Cidade"]
    estado = tabela.loc[linha, "Estado"]

    # Clique no campo Nome
    aut.press('tab')  # Verifique estas coordenadas
    aut.write(str(nome))
    aut.press('tab')
    aut.write(str(sobrenome))
    aut.press('tab')
    aut.write(str(email))
    aut.press('tab')
    aut.write(str(telefone))
    aut.press('tab')
    aut.write('tab')
    aut.press('tab')
    aut.press('space')

    aut.press('tab')
    aut.write(str(endereco))
    aut.press('tab')
    aut.write(str(cidade))
    aut.press('tab')
    aut.write(str(estado))
    aut.press('tab')
    aut.press('tab')
    aut.press('space')
    
    time.sleep(5)  # Tempo para garantir que todas as ações sejam realizadas
    aut.click(x=2956, y=135)
    aut.write('https://form.jotform.com/241504236417046')
    aut.press('enter')
    time.sleep(5)  # Aguardar a página carregar

# Finalizando a automação
time.sleep(3)
aut.press('win')
aut.write('chrome')
aut.press('enter')
aut.write("https://www.jotform.com/tables/241504236417046")
aut.press('enter')

# Aguardar o término
time.sleep(10)
#print(aut.position())  # Use esta linha para obter a posição do mouse se necessário
