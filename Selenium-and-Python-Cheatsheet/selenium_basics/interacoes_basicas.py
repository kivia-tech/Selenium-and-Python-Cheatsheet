from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep

def clicar(driver, xpath):
    driver.find_element(By.XPATH, xpath).click()

def digitar(driver, xpath, texto, enter=False):
    campo = driver.find_element(By.XPATH, xpath)
    campo.clear()
    campo.send_keys(texto)
    if enter:
        campo.send_keys(Keys.ENTER)