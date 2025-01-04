import requests

clima_emojis = {
    "Parcialmente nublado": "⛅",
    "Ensolarado": "☀️",
    "Nublado": "☁️",
    "Possibilidade de chuva irregular": "☁️",
    "Chuva": "🌧️",
    "Chuva fraca": "🌧️",
    "Aguaceiros fracos": "🌧️",
    "Tempestade": "⛈️",
    "Neve": "❄️",
    "Nevoeiro": "🌫️",
    "Chuvisco": "🌦️",
    "Céu limpo": "🌟"
}

def clima_mensagem(cidade):
    response = requests.get(f"https://wttr.in/{cidade}?lang=pt&format=%m+%t+%C")

    # Verificar se a requisição
    if response.status_code == 200:
        clima_texto = response.text.strip()
        retorno = clima_texto.split()
        lua = retorno.pop(0)
        temperatura = retorno.pop(0)
        clima = " ".join(map(str, retorno))
        
        # Buscar o emoji correspondente
        emoji = clima_emojis.get(clima, " ")
        
        return(f"Clima em {cidade}: {emoji}  {clima} | {temperatura} | {lua}")
    else:
        return("Não foi possível obter a previsão do tempo.")