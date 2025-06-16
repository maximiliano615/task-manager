import json
import os
from datetime import datetime

print('indique la tarea a realizar')
task = input('')
print('indique el estado de la tarea')
print('0 = hecho, 1 = en progreso, 2 = pendiente')
progress_task = int(input())

class Task:
    def __init__ (self,task):
        self.task = task
        self.progress_task = ['hecho', 'en progreso','pendiente']
        self.id = 0
        self.list_task = {}

    def time_task(self):
        time = str(datetime.now())
        print(time)
        return time
    
    def id_task(self):
        if os.path.exists('task.json'):
            list_task = read_task_json()
            finale_task = list_task.popitem()
            number_task = int(finale_task[0])
            self.id = number_task + 1
            return self.id
        else:
            self.id += 1
            return self.id
            
    def mark_progress(self,progress):
        if progress < len(self.progress_task):
            task_progress = self.progress_task[progress]
        else:
            print('por favor escoja una opcion valida')
              

    def to_dict(self, progress):
        id_task = self.id_task()
        time_task = self.time_task()
        print(id_task)
        self.list_task = {id_task : {'tarea' : self.task , 'progreso' : self.progress_task[progress] , 'hora' : time_task}}
        print(self.list_task)
        return self.list_task

    def __str__(self):
        return f'{self.list_task} Añadido'


class save_task:
    def __init__(self,task):
        self.task = task
        self.id = 0

    def read_task_json(self):
        with(open('task.json','r') as file):
            self.task = json.load(file)
            return task
        
    def save_task_json(self,task):
        with(open('task.json','w') as file):
            json.dump(task,file,indent=4)

    def save(self, list_task):
        if os.path.exists('task.json'):
            task = read_task_json()
            task = task | list_task
            self.save_task_json(task)
        else:
            self.save_task_json(list_task)

class eliminate_task:
    def __init__(self,task):
        self.task = task

    def eliminate(self,task):
        list_task = read_task_json()
        if task in list_task:
            del list_task[task]
            #print(list_task)
            save_task_json(list_task)
            print('tarea eliminada')
        else:
            print('no existe esa tarea')




#prueba = eliminate_task(task)
#prueba.eliminate(task)





list_task = Task(task)
list_task.mark_progress(progress_task)
print(list_task)

guardado = save_task(list_task)
guardado.save(list_task.to_dict(progress_task))