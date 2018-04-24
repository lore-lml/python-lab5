from flask import Flask, render_template, redirect, url_for, request
import tasks
app = Flask(__name__)


@app.route('/')
def hello_world():
    return redirect(url_for('index'))


@app.route('/index')
def index():
    (result, ids) = tasks.get_tasks()
    return render_template('index.html', tasks = result, ids = ids)


@app.route('/new_task', methods=[ 'POST' ])
def new_task():
    task = request.form['new_task']
    if task != "":
        tasks.insert_task(task)
    return redirect(url_for('index'))


@app.route('/delete_page/<id_task>')
def remove_task(id_task):
    tasks.delete_task(id_task)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run()
