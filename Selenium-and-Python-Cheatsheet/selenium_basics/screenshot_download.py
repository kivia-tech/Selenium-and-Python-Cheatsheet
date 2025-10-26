import os
from time import strftime

def tirar_print(driver, pasta="prints"):
    os.makedirs(pasta, exist_ok=True)
    nome = f"print_{strftime('%Y%m%d_%H%M%S')}.png"
    caminho = os.path.join(pasta, nome)
    driver.save_screenshot(caminho)
    print("Print salvo em:", caminho)