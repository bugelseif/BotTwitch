import time
from datetime import datetime


def aparece_tela(nome):
    arquivo = "nome.txt"
    with open(arquivo, "w") as file:
        file.seek(0)
        file.truncate()
        file.write(f"{nome}\n")
        file.flush()
        time.sleep(30)
        
        file.seek(0)
        file.truncate()
        file.write("\n")
        file.flush()
        
