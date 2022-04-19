# -*- coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from datetime import datetime
import time

import push

import slack_mensage
import configparser

config = configparser.ConfigParser()
config.read("config.ini");

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--disable-gpu')


browser = webdriver.Chrome(executable_path=r"chromedriver.exe",options=chrome_options)

class Consulta:

    def login(self, usuario=config['default']["usuario"],senha=config['default']["senha"]):
        try:
            erro = "Sem erros"
            browser.get("http://equiplano.toledo.pr.gov.br:7474/maestro/maestroLogin/load")
            username = browser.find_element_by_id("login")
            password = browser.find_element_by_id("senha")
            username.clear()

            username.send_keys(usuario)
            password.send_keys(senha)
            time.sleep(1)
            login_attempt = browser.find_element_by_xpath("//*[@type='submit']")
            login_attempt.submit()

            print(" ########## Acesso realizado com sucesso em: " + datetime.now().strftime(
                '%d/%m/%Y %H:%M:%S' + " ##########"))

            browser.get("http://equiplano.toledo.pr.gov.br:7474/maestro/maestroErro/list")

            time.sleep(2)
            e = browser.find_elements_by_class_name('sorting_1')
            data = (e[0].text)

            # Hora coletada nos logs do maestro
            data_maestro = data[11::]
            hora_maestro = data_maestro[:2:]
            minuto_maestro = data_maestro[3:5:]

            # Hora do servidor
            data_local = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
            data_local = data_local[11::]
            hora_local = data_local[:2:]
            minuto_local = data_local[3:5:]

            # Calulando a diferença entre os horarios coletados
            hora = int(hora_local) - int(hora_maestro)
            minuto = int(minuto_local) - int(minuto_maestro)

            if ((hora + minuto) > int(config['default']["tempo_maestro"])):
                print(True)
                push.push()
                erro = slack_mensage.mensage_slack('O maestro de Toledo pode estar parado. \núltima consulta com sucesso: ' + data)
                return erro
            else:
                return "Última consulta com sucesso: " + data
        except: return "Problema ao tentar fazer acesso em: " + datetime.now().strftime('%d/%m/%Y %H:%M'), 'Tempo para conexão excedido'