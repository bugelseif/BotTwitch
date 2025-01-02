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
    <title>To-Do List</title>
</head>
<body>
    <div>
    <h1>To-Do List</h1>
    <ul id="taskList">
        <!-- Nenhuma tarefa adicionada -->
    </ul>
    </div>
</body>
</html>
"""

# # Salva o HTML inicial em um arquivo
# with open(r"widget\widget.html", "w", encoding="utf-8") as file:
#     file.write(html_content)

# Função para adicionar tarefas ao arquivo HTML
def add_task_to_html(task):
    with open(r"widget\widget.html", "r", encoding="utf-8") as file:
        soup = BeautifulSoup(file, "html.parser")
    
    task_list = soup.find("ul", id="taskList")
    
    new_task = soup.new_tag("li")
    new_task.string = task
    
    task_list.append(new_task)
    
    with open(r"widget\widget.html", "w", encoding="utf-8") as file:
        file.write(str(soup))

# # Exemplo: Adicionar tarefas
# add_task_to_html("Estudar Python")
# add_task_to_html("Criar um projeto com Flask")
# add_task_to_html("Experimentar BeautifulSoup")
# add_task_to_html("Experimentar BeautifulSoup")
# add_task_to_html("Experimentar BeautifulSoup")
# add_task_to_html("Experimentar BeautifulSoup")
