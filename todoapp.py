tasks = []
completedtasks= []

while True:
    user = int(input("1 TO MARK ONE TASK AS COMPLETED \n2 TO ADD A NEW TASK\n3 TO SEE COMPLETED TASKS\n4 TO SEE UPCOMMING TASK\n"))
    if (user == 1):
        taskToDel = int(input("type the number of the task"))
        for i, val  in enumerate(tasks):
           if val[0] == str(taskToDel):
                print(f'{val} will be completed')
                completedtasks.append(val)
                del tasks[i]
    elif (user == 2):
        taskToInsert = input("what you wanna to add?")
        print(taskToInsert)
        taskLenght = str(len(tasks))
        tasks.append(taskLenght+":"+ taskToInsert) 
        print(tasks)
    elif (user == 3):
        print(completedtasks)
    elif (user == 4):
        print(tasks)
