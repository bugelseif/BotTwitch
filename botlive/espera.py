from bs4 import BeautifulSoup
import random

# HTML inicial salvo em um arquivo (por exemplo, "index.html")
html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="refresh" content="5" />
    <link rel="stylesheet" href="styles.css"/>
    <script defer="defer" src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.6.1/gsap.min.js"></script>
    <title>Sala de espera</title>
</head>
<body>
    <div>
    <h1>Sala de espera</h1>
    <div id="quadro">
        <!-- Nenhuma tarefa adicionada -->
    </div>
    </div>
</body>
<script>
    const pessoa = document.querySelectorAll('#pessoa')
    pessoa.forEach(pessoa => {
        console.log(pessoa.textContent)
    
        const posicaoAleatoriaX = Math.random() * (500);
        const posicaoAleatoriaY = Math.random() * (500);
        pessoa.style.left = `${posicaoAleatoriaX}px`;
        pessoa.style.top = `${posicaoAleatoriaY}px`;

        
        setInterval(() => {move(pessoa)}, 1000);
    });

    const move = function(item){
    let xm = Math.random() * 500
    gsap.to(item, {duration: 20, x:xm})
    let ym = Math.random() * 500
    gsap.to(item, {duration: 20, y:ym})
    }
</script>
</html>
"""

# # Salva o HTML inicial em um arquivo
# with open(r"widget\espera.html", "w", encoding="utf-8") as file:
#     file.write(html_content)

plantas = [
    "🌌", "🌠", "🌟", "⭐", "✨", "💫", "🌙", "🌑", "🌒", "🌓", 
    "🌔", "🌕", "🌖", "🌗", "🌘", "🌍", "🌎", "🌏", "🪐", "☄️", 
    "🚀", "🛰️", "🛸", "🌠"
]

# Função para adicionar tarefas ao arquivo HTML
def espera(task):
    with open(r"widget\espera.html", "r", encoding="utf-8") as file:
        soup = BeautifulSoup(file, "html.parser")
    
    task_list = soup.find("div", id="quadro")
    
    new_task = soup.new_tag("div", id="pessoa")
    astro = random.choice(plantas)
    new_task.string = task + astro
    
    task_list.append(new_task)
    
    with open(r"widget\espera.html", "w", encoding="utf-8") as file:
        file.write(str(soup))

# # Exemplo: Adicionar tarefas
# add_task_to_html("Estudar Python")
# add_task_to_html("Criar um projeto com Flask")
# add_task_to_html("Experimentar BeautifulSoup")
# add_task_to_html("Experimentar BeautifulSoup")
# add_task_to_html("Experimentar BeautifulSoup")
# add_task_to_html("Experimentar BeautifulSoup")
