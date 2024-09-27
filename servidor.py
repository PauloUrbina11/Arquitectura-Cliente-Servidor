from flask import Flask, jsonify, request

app = Flask(__name__)

# Simulación de una base de datos de tareas en memoria
tasks = [
    {'id': 1, 'task': 'Aprender Python', 'completed': False},
    {'id': 2, 'task': 'Leer un libro de software', 'completed': False}
]

# Ruta para obtener la lista de tareas
@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)

# Ruta para agregar una nueva tarea
@app.route('/tasks', methods=['POST'])
def add_task():
    new_task = request.json
    new_task['id'] = len(tasks) + 1
    new_task['completed'] = False
    tasks.append(new_task)
    return jsonify(new_task), 201

# Ruta para actualizar el estado de una tarea (completada o no)
@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = next((t for t in tasks if t['id'] == task_id), None)
    if task is None:
        return jsonify({'error': 'Tarea no encontrada'}), 404

    task['completed'] = request.json.get('completed', task['completed'])
    return jsonify(task)

# Ruta para eliminar una tarea
@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    global tasks
    tasks = [t for t in tasks if t['id'] != task_id]
    return jsonify({'result': True})

if __name__ == '__main__':
    app.run(debug=True)
