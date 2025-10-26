from selenium_basics.setup_driver import iniciar_driver
from selenium_basics.navegar_e_localizar import abrir_pagina
from selenium_basics.scraping_textos import pegar_varios_textos
from time import sleep

driver = iniciar_driver()
abrir_pagina(driver, "https://books.toscrape.com/")
sleep(2)

titulos = pegar_varios_textos(driver, "//h3/a")
for t in titulos:
    print("Livro:", t)

driver.quit()