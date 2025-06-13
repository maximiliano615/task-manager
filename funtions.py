import json
import os

print('indique la tarea a realizar')
task = input('')
print('indique el estado de la tarea')
print('0 = done, 1 = in progress, 2 = todo')
progress_task = int(input())

class Task:
    def __init__ (self,task):
        self.task = task
        self.progress_task = ['done', 'in progress','todo'] 

    def mark_progress(self,progress):
        if progress < len(self.progress_task):
            task_progress = self.progress_task[progress]
        else:
            print('por favor escoja una opcion valida')
              

    def to_dict(self, progress):
        list_task = {self.task : self.progress_task[progress]}
        return list_task

    def __str__(self):
        return f'{self.list_task} Añadido'
        
def read_task_json():
    with(open('task.json','r') as file):
        task = json.load(file)
        return task
    
            
def save_task_json(task):
    with(open('task.json','w') as file):
        json.dump(task,file,indent=4)

def save(list_task):
    if os.path.exists('task.json'):
        task = read_task_json()
        print(type(task))
        task = task | list_task
        print(task)
        save_task_json(task)
    else:
        save_task_json(list_task)

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




prueba = eliminate_task(task)
prueba.eliminate(task)





#list_task = Task(task)
#list_task.mark_progress(progress_task)

#save(list_task.to_dict(progress_task))