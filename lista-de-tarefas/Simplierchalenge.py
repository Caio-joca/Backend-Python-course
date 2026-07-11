'''
Você deverá criar um programa que simule uma lista de tarefas.

1 - Adicionar tarefa
2 - Concluir tarefa
3 - Listar tarefas
0 - Sair
'''

import os
from task import Task
from tasklist import Tasklist
def add_tarefa():
    quantity= int(input('quantas tarefas voce quer adicinar'))
    for quant in range(quantity) :
        thetask= str(input('escreva a atarefa a ser adicionada'))
        entrada = int(input('diga 1 se já foi feita ou 0 se não foi feita'))
        if entrada == 1 :
            thecondition= True
        else :
            thecondition= False
        thetaskobject=Task(thetask, thecondition)
        objectlist.append(thetaskobject)

def task_viewer():
    tasklistobject =Tasklist(objectlist)
    tasklistobject.listviewer()

objectlist =[]
thetask=0
thetaskobject=0
while True :
    op=int(input('1 - Adicionar tarefa\n2 - Concluir tarefa\n3 - Listar tarefa\n0 - Sair'))
    os.system('cls')
    if op == 1 :
        add_tarefa()

    elif op == 3 :
        task_viewer()

        ''' 
    elif op == 2 :



    elif op == 4 :
    
    elif op == 0 :
        break'''