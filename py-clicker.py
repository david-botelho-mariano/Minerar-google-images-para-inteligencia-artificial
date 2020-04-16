import time
import random

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

def apagar_texto_com_delay(nome_elemento, palavra):
	print("APAGANDO...")
	elemento_alvo = chrome_navegador.find_element_by_name(nome_elemento)
	elemento_alvo.click()
	for letra in palavra:
		delay = random.uniform(0.5,1.0)
		print(delay)
		time.sleep(delay)
		elemento_alvo.send_keys(Keys.BACKSPACE)

def escrever_com_delay(nome_elemento, palavra):
	print("ESCREVENDO...")
	for letra in palavra:
		delay = random.uniform(0.1,3.0)
		print(delay)
		time.sleep(delay)
		chrome_navegador.find_element_by_name(nome_elemento).send_keys(letra)	

def realizar_login(usuario, senha):
	titulo_form = chrome_navegador.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/div/div[1]/div[2]/h2")
	action_chains = ActionChains(chrome_navegador)
	action_chains.move_to_element(titulo_form).perform()

	chrome_navegador.find_element_by_name("login").click()
	escrever_com_delay("login", usuario)

	chrome_navegador.find_element_by_name("password").click()
	escrever_com_delay("password", senha)

	chrome_navegador.find_element_by_xpath('//*[@id="botao-entrar"]').click()

	chrome_navegador.find_element_by_name("login").click()
	apagar_texto_com_delay('login' , usuario)


chrome_opcoes = Options()
#chrome_opcoes.add_argument("--headless")
chrome_opcoes.add_argument("--log-level=3")
chrome_opcoes.binary_location = "chrome-windows/chrome.exe"

chrome_navegador = webdriver.Chrome('chrome-windows/chrome-driver.exe', chrome_options=chrome_opcoes)
chrome_navegador.set_window_size(1920,1080)
chrome_navegador.get('https://www.unitins.br/PortalAluno/Account/Login')


ativo = True

while (ativo == True):
	realizar_login("abc", "1234")
