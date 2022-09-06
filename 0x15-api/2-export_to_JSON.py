#!/usr/bin/python3
"""
Using what you did in the task #0, extend your Python script to export data in
the JSON format.

Requirements:

- Records all tasks that are owned by this employee
Format must be: { "USER_ID": [{"task": "TASK_TITLE", "completed": TASK_
COMPLETED_STATUS, "username": "USERNAME"}, {"task": "TASK_TITLE",
"completed": TASK_COMPLETED_STATUS, "username": "USERNAME"}, ... ]}
File name must be: USER_ID.json

API que usamos: https://jsonplaceholder.typicode.com/
Info write: https://www.w3schools.com/python/python_file_write.asp
"""

if __name__ == "__main__":
    import json  # import json library
    import requests
    from sys import argv  # for command line arguments

    # Hago un try y un except por si no se pasa una "id" cuando se corre
    try:
        ID = argv[1]  # Se guarda la ID del empleado

        # Si se le pasa la "id" en la ruta me trae solo la info de ese usuario
        # por eso es que se lo agrego a la ruta (endpoint) con el .format
        url_todos = "https://jsonplaceholder.typicode.com/todos?userId={}"\
            .format(ID)
        url_user = "https://jsonplaceholder.typicode.com/users/{}".format(ID)

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

        # Nos piden que el file name sea el numero de la id mas .csv
        file_name = ID + ".json"

        # Se crea el archivo "file_name" y se le agrega la data
        final_dic = {}
        list_data = []  # ver formato de impresion se ponen listas en el dic
        with open(file_name, 'w', encoding='UTF8', newline='') as f:
            for attribute in json_todos:
                dic_data = {}
                # Obtenemos los datos a escribir en el archivo json:
                # data es un diccionario por eso accedo de esta forma
                dic_data["task"] = attribute["title"]
                dic_data["completed"] = attribute["completed"]
                # El nombre lo saco del endpoint (ruta) json_user
                dic_data["username"] = json_user["username"]
                # Se agregan los datos a la lista de diccionarios:
                list_data.append(dic_data)

            # Guardo los datos en el orden que piden para escribir el json
            final_dic[ID] = list_data
            # Serializo el dic y lo escribo en el dic a retornar:
            f.write(json.dumps(final_dic))
            print(final_dic)

    except Exception as error:
        print("Error message: {}".format(error))
