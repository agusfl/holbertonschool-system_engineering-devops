#!/usr/bin/python3
"""
Using what you did in the task #0, extend your Python script to export data in
the JSON format.
Requirements:

- Records all tasks from all employees
- Format must be: { "USER_ID": [ {"username": "USERNAME", "task": "TASK_TITLE"
, "completed": TASK_COMPLETED_STATUS}, {"username": "USERNAME", "task":
"TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, ... ], "USER_ID":
[ {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_
STATUS}, {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_
COMPLETED_STATUS}, ... ]}
- File name must be: todo_all_employees.json

API que usamos: https://jsonplaceholder.typicode.com/
"""

if __name__ == "__main__":
    import json  # import json library
    import requests

    # Traigo las url con metodo GET de HTTP
    url_todos = "https://jsonplaceholder.typicode.com/todos"
    url_user = "https://jsonplaceholder.typicode.com/users"

    # Request URL for to do list:
    res_todos = requests.get(url_todos)
    # Pasar datos a JSON para obtener un diccionario de python y poder
    # trabajar con los datos en python - aca traemos los datos de todo list
    json_todos = res_todos.json()

    # Request URL for Users:
    res_user = requests.get(url_user)
    # Pasar datos a JSON para obtener un diccionario de python y poder
    # trabajar con los datos en python - aca traemos los datos de todo list
    json_user = res_user.json()

    file_name = "todo_all_employees.json"

    # Se setea un diccionario vacio que es el que se va a retornar luego
    final_dic = {}
    # Se crea el archivo "file_name" y se le agrega la data
    with open(file_name, 'w', encoding='UTF8', newline='') as f:
        for user in json_user:
            list_data = []  # ver formato de impresion,se ponen listas en dic
            for attribute in json_todos:
                # Comparamos IDs para poner todas las tareas de cada user
                if attribute["userId"] == user["id"]:
                    # Defino dic vacio para agregar los datos en cada iter
                    dic_data = {}
                    # Obtenemos los datos a escribir en el archivo json:
                    # data es un diccionario por eso accedo de esta forma
                    # El nombre lo saco del endpoint (ruta) json_user
                    dic_data["username"] = user["username"]
                    dic_data["task"] = attribute["title"]
                    dic_data["completed"] = attribute["completed"]
                    # Se agregan los datos a la lista de diccionarios:
                    list_data.append(dic_data)
            # Guardo los datos en el orden que piden para escribir el json
            final_dic[user["id"]] = list_data
        # Serializo el dic y lo escribo en el dic a retornar, se convierte
        # un objeto de python (final_dic) en un objeto JSON (tipo string)
        f.write(json.dumps(final_dic))
