# Impressões coloridas
class Cor:
    VERDE = "\033[92m"
    VERMELHO = "\033[91m"
    NORMAL = "\033[0m"

print(f"{Cor.VERDE}Sucesso!{Cor.NORMAL}")
print(f"{Cor.VERMELHO}Erro!{Cor.NORMAL}")