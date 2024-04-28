from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample todo list
todo_list = []

# Route for the home page
@app.route('/')
def index():
    return render_template('index.html', todo_list=todo_list)

# Route to add a new todo item
@app.route('/add', methods=['POST'])
def add_todo():
    todo_item = request.form.get('todo')
    if todo_item:
        todo_list.append(todo_item)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)