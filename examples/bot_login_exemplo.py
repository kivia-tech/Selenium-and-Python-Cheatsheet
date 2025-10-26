from selenium_basics.setup_driver import iniciar_driver
from selenium_basics.navegar_e_localizar import abrir_pagina
from selenium_basics.interacoes_basicas import digitar, clicar
from selenium_basics.esperas import esperar_elemento

URL = "https://exemplo.com/login"
driver = iniciar_driver()
abrir_pagina(driver, URL)

esperar_elemento(driver, '//*[@id="username"]')
digitar(driver, '//*[@id="username"]', "usuario")

esperar_elemento(driver, '//*[@id="password"]')
digitar(driver, '//*[@id="password"]', "senha")

clicar(driver, '//*[@id="login-btn"]')

driver.quit()