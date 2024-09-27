import requests

# URL del servidor (por defecto Flask corre en localhost:5000)
url = 'http://127.0.0.1:5000/tasks'

# Obtener lista de tareas
def get_tasks():
    response = requests.get(url)
    if response.status_code == 200:
        tasks = response.json()
        print("\nLista de tareas:")
        for task in tasks:
            status = 'Completada' if task['completed'] else 'Pendiente'
            print(f"{task['id']}. {task['task']} - {status}")
    else:
        print("Error al obtener tareas.")

# Añadir una nueva tarea
def add_task(task_description):
    new_task = {'task': task_description}
    response = requests.post(url, json=new_task)
    if response.status_code == 201:
        print("Tarea añadida correctamente.")
    else:
        print("Error al añadir tarea.")

# Marcar tarea como completada
def complete_task(task_id):
    response = requests.put(f"{url}/{task_id}", json={'completed': True})
    if response.status_code == 200:
        print("Tarea completada.")
    else:
        print("Error al completar tarea.")

# Eliminar una tarea
def delete_task(task_id):
    response = requests.delete(f"{url}/{task_id}")
    if response.status_code == 200:
        print("Tarea eliminada.")
    else:
        print("Error al eliminar tarea.")

# Menú simple para interactuar
def main():
    while True:
        print("\nOpciones:")
        print("1. Ver tareas")
        print("2. Añadir tarea")
        print("3. Completar tarea")
        print("4. Eliminar tarea")
        print("5. Salir")
        option = input("Selecciona una opción: ")

        if option == '1':
            get_tasks()
        elif option == '2':
            task_description = input("Describe la tarea: ")
            add_task(task_description)
        elif option == '3':
            task_id = input("ID de la tarea a completar: ")
            complete_task(task_id)
        elif option == '4':
            task_id = input("ID de la tarea a eliminar: ")
            delete_task(task_id)
        elif option == '5':
            break
        else:
            print("Opción no válida, intenta de nuevo.")

if __name__ == "__main__":
    main()
