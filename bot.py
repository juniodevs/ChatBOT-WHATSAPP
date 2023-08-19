from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import os
import time
import requests

agent = {"User-Agent": 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}

usuario = 'iramarjunhorveras@gmail.com'
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
        time.sleep(2)

        #PEGAR A MENSAGEM DO CLIENTE
        todas_as_mensagens = driver.find_elements(By.CLASS_NAME,'_21Ahp')
        todas_as_msg_texto = [e.text for e in todas_as_mensagens]
        msg = todas_as_msg_texto[-1]
        print(msg)
        time.sleep(5)

        #RESPONODENDO CLIENTE
        resposta = requests.get('http://localhost/CHATBOT/index.php?', params={'msg': msg, 'telefone': telefone_final, 'usuario': usuario}, headers=agent)
        time.sleep(2)
        resposta = resposta.text
        campo_de_texto = driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p')
        campo_de_texto.click()
        time.sleep(1)
        campo_de_texto.send_keys(resposta, Keys.ENTER)


        #FECHAR CONTATO
        webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
        time.sleep(2)


    except:
        time.sleep(4)

while True:
    bot()