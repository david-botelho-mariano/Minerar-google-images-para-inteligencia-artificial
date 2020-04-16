import time
import urllib

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


chrome_opcoes = Options()
chrome_opcoes.add_argument("--log-level=3")
chrome_opcoes.binary_location = "chrome-windows/chrome.exe"

chrome_navegador = webdriver.Chrome('chrome-windows/chrome-driver.exe', chrome_options=chrome_opcoes)
chrome_navegador.set_window_size(1920,1080)
chrome_navegador.get('https://www.google.com/search?q=iphone&client=firefox-b-d&sxsrf=ALeKk03BuTfeo8NcyPB3UnFgfW18GDi6rA:1587065328788&source=lnms&tbm=isch&sa=X&ved=2ahUKEwiYiqGJ1-3oAhUUA9QKHZiVCaYQ_AUoA3oECA8QBQ&biw=992&bih=435')

def scrolToMaxBottom():
	for x in range(0, qtd_imagens_desejadas/4, 1):
		time.sleep(5)
		body_div.send_keys(Keys.SPACE)
		print("esperando quatro imagens da linha: " + str(x) + " serem carregadas")

		try:
			chrome_navegador.find_element_by_xpath("/html/body/div[2]/c-wiz/div[3]/div[1]/div/div/div/div/div[5]/input").click()
			print("sucesso ao pressionar o botao 'mostrar mais'")
		except Exception as e:
			pass
	
def minerarImagens():
	for id_imagem in range(0, qtd_imagens_desejadas, 1):
		try:
			img = chrome_navegador.find_element_by_xpath('/html/body/div[2]/c-wiz/div[3]/div[1]/div/div/div/div/div[1]/div[1]/div[' + str(id_imagem) +']/a[1]/div[1]/img')
			src = img.get_attribute('src')
			urllib.urlretrieve(src, "imgs-mineradas/" + str(id_imagem) + ".png")
			print("id da imagem da imagem minerada: " + str(id_imagem))
				
		except Exception as e:
			pass

if __name__ == '__main__':
	qtd_imagens_desejadas = 1000
	body_div = chrome_navegador.find_element_by_css_selector('body')
	scrolToMaxBottom()
	minerarImagens()
