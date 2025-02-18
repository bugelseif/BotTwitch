from bs4 import BeautifulSoup

# HTML inicial salvo em um arquivo (por exemplo, "index.html")
html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="refresh" content="5" />
    <link rel="stylesheet" href="styles.css"/>
    <title>Perguntas</title>
</head>
<body>
    <div>
    <h1>Perguntas:</h1>
    <ul id="lista">

    </ul>
    </div>
</body>
</html>
"""

# # Salva o HTML inicial em um arquivo
with open(r".\perguntas\perguntas.html", "w", encoding="utf-8") as file:
    file.write(html_content)


# Função para adicionar tarefas ao arquivo HTML
def pergunta(pessoa, pergunta):
    with open(r"perguntas\perguntas.html", "r", encoding="utf-8") as file:
        soup = BeautifulSoup(file, "html.parser")
    
    pergunta_list = soup.find("ul", id="lista")
    
    nova_pergunta = soup.new_tag("li", id="pegunta")
    nova_pergunta.string =f'{pessoa}: {pergunta}'
    
    pergunta_list.append(nova_pergunta)
    
    with open(r"perguntas\perguntas.html", "w", encoding="utf-8") as file:
        file.write(str(soup))

# # Exemplo: Adicionar tarefas
# pergunta("pessoa","Como faz isso funcionar?")

