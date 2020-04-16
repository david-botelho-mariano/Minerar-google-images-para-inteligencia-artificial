import time
import random
import urllib

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


chrome_opcoes = Options()
#chrome_opcoes.add_argument("--headless")
chrome_opcoes.add_argument("--log-level=3")
chrome_opcoes.binary_location = "chrome-windows/chrome.exe"

chrome_navegador = webdriver.Chrome('chrome-windows/chrome-driver.exe', chrome_options=chrome_opcoes)
chrome_navegador.set_window_size(1920,1080)
chrome_navegador.get('https://www.google.com/search?q=cachorro&tbm=isch&ved=2ahUKEwiBjsTEs-zoAhWnBrkGHYlcAGYQ2-cCegQIABAA&oq=cachorro&gs_lcp=CgNpbWcQAzIECCMQJzIECAAQQzIECAAQQzIECAAQQzIECAAQQzIECAAQQzIECAAQQzIECAAQQzIECAAQQzIECAAQQzoCCAA6BQgAEIMBUK4uWIA-YOs_aABwAHgAgAHLAYgByAqSAQUwLjcuMZgBAKABAaoBC2d3cy13aXotaW1n&sclient=img&ei=dQaYXsH_KKeN5OUPibmBsAY&bih=435&biw=992&client=firefox-b-d')
#cachorro filetype:jpg

print('[+]esperando carregamento da pagina')
time.sleep(10)

contador_imagens = 1
body_div = chrome_navegador.find_element_by_css_selector('body')

while True:
	body_div.send_keys(Keys.SPACE)
	
	for x in range(0, 4, 1):

		if x == 3:
			print("pausa")
			time.sleep(5)


		try:
			img = chrome_navegador.find_element_by_xpath('/html/body/div[2]/c-wiz/div[3]/div[1]/div/div/div/div/div[1]/div[1]/div[' + str(contador_imagens) +']/a[1]/div[1]/img')
			src = img.get_attribute('src')
			urllib.urlretrieve(src, str(contador_imagens) + ".png")
			contador_imagens = contador_imagens + 1
			print(contador_imagens)
				
		except Exception as e:
			print(e)

			try:
				#pode ser uma botao de mostrar mais
				chrome_navegador.find_element_by_xpath("/html/body/div[2]/c-wiz/div[3]/div[1]/div/div/div/div/div[5]/input").click()
			except Exception as e:
				#pode ser uma propaganda
				contador_imagens = contador_imagens + 1
				print('[+]propaganda detectada')
			
			

print("[+]acabou-se")
