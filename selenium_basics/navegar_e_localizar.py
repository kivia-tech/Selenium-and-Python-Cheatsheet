from selenium.webdriver.common.by import By

def abrir_pagina(driver, url):
    driver.get(url)

def encontrar_por_xpath(driver, xpath):
    return driver.find_element(By.XPATH, xpath)

def encontrar_por_css(driver, seletor):
    return driver.find_element(By.CSS_SELECTOR, seletor)