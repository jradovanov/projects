# Създаване на празен списък за задачи
tasks = []


# Функция за добавяне на задача
def add_task():
    task = input("Добавете задача: ")
    tasks.append(task)
    print("Задачата е добавена успешно!")


# Функция за преглед на задачите
def view_tasks():
    print("Списък на задачите:")
    for index, task in enumerate(tasks):
        print(f"{index + 1}. {task}")


# Функция за изтриване на задача
def delete_task():
    view_tasks()
    task_index = int(input("Изберете номер на задача, която искате да изтриете: "))
    del tasks[task_index - 1]
    print("Задачата е изтрита успешно!")


# Функция за редактиране на задача
def edit_task():
    view_tasks()
    task_index = int(input("Изберете номер на задача, която искате да редактирате: "))
    new_task = input("Въведете новото съдържание на задачата: ")
    tasks[task_index - 1] = new_task
    print("Задачата е редактирана успешно!")


# Основен цикъл на програмата
while True:
    print("Моля изберете опция:")
    print("1. Добавяне на задача")
    print("2. Преглед на задачите")
    print("3. Изтриване на задача")
    print("4. Редактиране на задача")
    print("5. Изход от програмата")

    choice = int(input())

    if choice == 1:
        add_task()
    elif choice == 2:
        view_tasks()
    elif choice == 3:
        delete_task()
    elif choice == 4:
        edit_task()
    elif choice == 5:
        break
    else:
        print("Моля въведете валидна опция!")