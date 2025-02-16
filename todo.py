def show_tasks(tasks):
    if not tasks:
        print("Список дел пуст!")
    else:
        print("Список дел:")
        for i, task in enumerate(tasks):
            print(f"{i + 1}. {task}")

def add_task(tasks):
    task = input("Введи задачу: ")
    tasks.append(task)
    print("Задача добавлена!")

def complete_task(tasks):
    show_tasks(tasks)
    try:
        task_number = int(input("Введи номер выполненной задачи: ")) - 1
        if 0 <= task_number < len(tasks):
            del tasks[task_number]
            print("Задача удалена из списка!")
        else:
            print("Неверный номер задачи.")
    except ValueError:
        print("Неверный ввод. Введи номер задачи.")

def main():
    tasks = []

    while True:
        print("\nВыбери действие:")
        print("1. Показать список дел")
        print("2. Добавить задачу")
        print("3. Отметить задачу как выполненную")
        print("4. Выйти")

        choice = input("Введи номер действия: ")

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            break
        else:
            print("Неверный ввод. Пожалуйста, выбери действие из списка.")

if __name__ == "__main__":
    main()