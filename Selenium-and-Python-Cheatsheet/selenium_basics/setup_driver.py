from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def iniciar_driver(headless=False):
    options = Options()
    if headless:
        options.add_argument("--headless=new")
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    return driver

if __name__ == "__main__":
    driver = iniciar_driver()
    driver.get("https://google.com")
    input("Pressione Enter para sair...")
    driver.quit()