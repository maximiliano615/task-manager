import os
import json
from datetime import datetime
from funtions import Task, save_task, eliminate_task, read_json, rm_json, modify_task

print("""Este programa es un gestor de tareas

Que opcion desea realizar?

1 = crear tarea
2 = inspeccionar tareas
3 = modificar estado de la tarea
4 = eliminar tarea
5 = salir
""")


option = int(input())
while option != 5:
    lector = rm_json()
    lector.rm_task_json()
    if option == 1:
        task = input("indique la tarea a realizar => ")
        progress_task = int(input("""indique el estado de la tarea => 
            
        0 = hecho
        1 = en progreso
        2 = pendiente

        => """))
        list_task = Task(task)
        list_task.mark_progress(progress_task)
        guardado = save_task(list_task)
        guardado.save(list_task.to_dict(progress_task))
        print("tarea guardada")
        option = int(input("Que mas desea realizar? => "))

    elif option == 2:
        list_task = read_json().read_task_json()
        print(list_task)
        option = int(input("Que mas desea realizar? => "))

    elif option == 3:
        id = input("Indique el id de la tarea a modificar => ")
        list_task = modify_task(id)
        print(list_task)
        progress = int(input("a que estado desea modificar la tarea => "))
        list_task.modify(id,progress)
        option = int(input("Que mas desea realizar? => "))

    elif option == 4:
        task = input("Indique el id de la tarea a eliminar => ")
        eliminar = eliminate_task(task)
        eliminar.eliminate(task)
        option = int(input("Que mas desea realizar? => "))

    elif option == 5:
        print("Adios")
        break

    else:
        print("Opcion invalida")
        option = int(input())





