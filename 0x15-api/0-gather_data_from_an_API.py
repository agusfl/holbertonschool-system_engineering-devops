#!/usr/bin/python3
"""
Write a Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
Requirements:

- You must use urllib or requests module
- The script must accept an integer as a parameter, which is the employee ID
- The script must display on the standard output the employee TODO list
progress in this exact format:
* First line: Employee EMPLOYEE_NAME is done with tasks(NUMBER_OF_DONE_TASKS
/TOTAL_NUMBER_OF_TASKS):
* * EMPLOYEE_NAME: name of the employee
* * NUMBER_OF_DONE_TASKS: number of completed tasks
* * TOTAL_NUMBER_OF_TASKS: total number of tasks, which is the sum of completed
and non-completed tasks
* Second and N next lines display the title of completed tasks: TASK_TITLE
(with 1 tabulation and 1 space before the TASK_TITLE)

API que usamos: https://jsonplaceholder.typicode.com/
"""

if __name__ == "__main__":
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
        # Ver los datos poniendo: print(json_todos),
        # Lo que se devuelve es una lista de dics- (print(type(json_todos)))
        json_todos = res_todos.json()

        # Request URL for Users:
        res_user = requests.get(url_user)
        # Pasar datos a JSON para obtener un diccionario de python y poder
        # trabajar con los datos en python - aca traemos los datos de todo list
        # Ver los datos poniendo: print(json_user)
        json_user = res_user.json()

        # Employee name:
        EMPLOYEE_NAME = json_user["name"]
        # Hago un contador de tasks completadas, lo seteo en cero y despues le
        # sumo valores:
        NUMBER_OF_DONE_TASKS = 0
        # Contador para el total de tasks, lo seteo en cero y despues le sumo
        # valores
        TOTAL_NUMBER_OF_TASKS = 0

        # Creo una lista vacia para apendiar solo las tareas completadas
        TASK_TITLE = []
        for task in json_todos:
            # Se suman el total de tasks
            TOTAL_NUMBER_OF_TASKS += 1
            # Aca nos traemos el valor del atributo "completed" - si es "True"
            # significa que la tarea fue completada, entonces sumamos uno al
            # contador de tareas completadas y apendiamos en la lista creada
            if task["completed"] is True:
                # Se suma las tasks completas
                NUMBER_OF_DONE_TASKS += 1
                TASK_TITLE.append(task["title"])

        print("Employee {} is done with tasks({}/{}):"
              .format(EMPLOYEE_NAME, NUMBER_OF_DONE_TASKS,
                      TOTAL_NUMBER_OF_TASKS))

        # Se hace un for para imprimir las tasks completas guardadas en la
        # lista que creamos -> TASK_TITLE
        for task in TASK_TITLE:
            # Se pide que se imprima con un tabulador antes por eso el \t
            print("\t {}".format(task))

    except Exception:
        print("Usage: 0-gather_data_from_an_API.py ID_number")
