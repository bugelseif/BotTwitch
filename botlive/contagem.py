import time
from datetime import datetime
import winsound

def tocar_alarme():
    for _ in range(4):
        winsound.Beep(1000, 300)
        time.sleep(0.3)


def contagem_regressiva(minutos):
    arquivo = "contagem.txt"
    segundos = minutos * 60
    with open(arquivo, "w") as file:
        while segundos >= 0:
            mm = segundos // 60
            ss = segundos % 60
            tempo_formatado = f"{mm:02}:{ss:02}"
            file.seek(0)
            file.truncate()
            file.write(f"{tempo_formatado}\n")
            file.flush()
            segundos -= 1
            time.sleep(1)
        
        file.seek(0)
        file.truncate()
        file.write("Pausa\n")
        file.flush()
        
        tocar_alarme()
