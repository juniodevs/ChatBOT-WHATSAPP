from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import os
import time
import requests

# #API 
# agent = {"User-Agent": 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}

# #CHAVE    xgLNUFtZsAbhZZaxkRh5ofM6Z0YIXwwv
# api = requests.get("https://editacodigo.com.br/index/api-whatsapp/xgLNUFtZsAbhZZaxkRh5ofM6Z0YIXwwv" ,  headers=agent)
# time.sleep(1)
# api = api.text
# api = api.split(".n.")
# bolinha_notificacao = api[3].strip()
# contato_cliente = api[4].strip()
# caixa_msg = api[5].strip()
# msg_cliente = api[6].strip()
# caixa_msg2 = api[7].strip()
# caixa_pesquisa = api[8].strip()


dir_path = os.getcwd()
chrome_options2 = Options()
chrome_options2.add_argument(r"user-data-dir=" + dir_path + "/pasta/sessao")
driver = webdriver.Chrome(options=chrome_options2)
driver.get('https://web.whatsapp.com/')
time.sleep(10)

def bot():
    try:
        #CAPTURAR NOTIFCAÇÃO
        notificacao = driver.find_element(By.CLASS_NAME,'aumms1qt')
        notificacao = driver.find_elements(By.CLASS_NAME,'aumms1qt')
        clica_notificacao = notificacao[-1]
        acao_notificacao = webdriver.ActionChains(driver)
        acao_notificacao.move_to_element_with_offset(clica_notificacao,0,-20)
        acao_notificacao.click()
        acao_notificacao.perform()
        acao_notificacao.click()
        acao_notificacao.perform()
        time.sleep(1)
        #CAPTURAR TELEFONE
        telefone_cliente = driver.find_element(By.XPATH, '//*[@id="main"]/header/div[2]/div/div/div/span')
        telefone_final = telefone_cliente.text
        print (telefone_final)

    except:
        print('Olá')
        time.sleep(4)

while True:
    bot()