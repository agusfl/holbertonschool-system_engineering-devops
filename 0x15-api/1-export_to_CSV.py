#!/usr/bin/python3
"""
Using what you did in the task #0, extend your Python script to export data in
the CSV format.

Requirements:
- Records all tasks that are owned by this employee
- Format must be: "USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"
- File name must be: USER_ID.csv

API que usamos: https://jsonplaceholder.typicode.com/
Info CSV: https://www.pythontutorial.net/python-basics/python-write-csv-file/
Info flag para agregar comillas usando el modulo csv:
https://www.adamsmith.haus/python/examples/3278/csv-write-to-a-csv-file-and-
quote-all-fields
"""

if __name__ == "__main__":
    import csv  # import csv library
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
        file_name = ID + ".csv"

        # Se crea el archivo "file_name" y se le agrega la data
        with open(file_name, 'w', encoding='UTF8', newline='') as f:
            # Se agrega la opcion de quoting para agregar comillas en el csv
            writer = csv.writer(f, quoting=csv.QUOTE_ALL)
            for attribute in json_todos:
                # Obtenemos los datos a escribir en el archivo csv
                userId = attribute["userId"]
                # El nombre lo saco del endpoint json_user
                user_name = json_user["username"]
                task_status = attribute["completed"]
                title = attribute["title"]
                # Guardo los datos en el orden que piden para escribir el csv
                data = [userId, user_name, task_status, title]
                # Uso el metodo writerow para escribir la data en el csv
                writer.writerow(data)

    except Exception as error:
        print("Error message: {}".format(error))
