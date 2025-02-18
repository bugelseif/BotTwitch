import requests


def clima_mensagem(cidade):
    response = requests.get(f"https://wttr.in/{cidade}?lang=pt&format=%l+%c+%C+%t+%f")

    # Verificar se a requisição
    if response.status_code == 200:
        clima_texto = response.text.strip()
        retorno = clima_texto.split()
        sensacao = retorno.pop(-1)
        temp = retorno.pop(-1)
        texto = " ".join(str(element) for element in retorno)

        return(f"{texto} Temperatura: {temp} Sensação: {sensacao}")
    else:
        return("Não foi possível obter a previsão do tempo.")