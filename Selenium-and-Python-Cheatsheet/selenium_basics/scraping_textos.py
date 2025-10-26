def pegar_texto(driver, xpath):
    return driver.find_element("xpath", xpath).text

def pegar_varios_textos(driver, xpath_lista):
    elementos = driver.find_elements("xpath", xpath_lista)
    return [e.text for e in elementos]