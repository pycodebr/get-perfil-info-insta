from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Manter o chromedriver.exe atualizado conforme a versão do seu Google chrome #
# https://chromedriver.chromium.org/downloads #
browser = webdriver.Chrome(r'.\chromedriver.exe')

browser.get('https://www.instagram.com/')

# Digita o user para fazer Login #
browser.find_element_by_name("username").send_keys('***SEU USUÁRIO***')

# Digita a senha para fazer Login #
browser.find_element_by_name("password").send_keys('***SUA SENHA***')

# Aperta Enter para Logar #
browser.find_element_by_name("password").send_keys(Keys.RETURN)

# Abre o perfil que deseja 'stalkear' #
browser.find_element_by_class_name("cq2ai").click()
browser.get('https://www.instagram.com/pycodebr/')

# Salva imagem do perfil 'stalkeado' #
browser.get_screenshot_as_file(r'.\perfil.png')