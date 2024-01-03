from datetime import datetime

from flask import Blueprint, flash, redirect, render_template, request, url_for

from flaskeleton.extensions.database import db
from flaskeleton.models import DoDoStatus, ToDoList

web = Blueprint(
    'web', __name__, template_folder='pages', static_folder='assets'
)


@web.route('/')
def index():
    data = {'status': [], 'pending': [], 'done': [], 'canceled': []}
    for status in db.session.query(DoDoStatus).all():
        status_item = status.__dict__.copy()
        del status_item['_sa_instance_state']
        data['status'].append(status_item)
    for item in db.session.query(ToDoList).all():
        list_item = item.__dict__.copy()
        if '_sa_instance_state' in list_item:
            del list_item['_sa_instance_state']
        if list_item['to_do_status_id'] == 1:
            data['pending'].append(list_item)
        elif list_item['to_do_status_id'] == 2:
            data['done'].append(list_item)
        elif list_item['to_do_status_id'] == 3:
            data['canceled'].append(list_item)
    return render_template('index.html', data=data)


@web.route('/add-item', methods=['POST'])
def add_item():
    form = request.form.copy()
    item = ToDoList()
    item.description = form['description']
    item.to_do_status_id = form['to_do_status_id']
    if form['to_do_status_id'] != '1':
        item.updated_at = datetime.now()
    db.session.add(item)
    db.session.commit()
    flash('Task created!', 'success')
    return redirect(url_for('web.index'))


@web.route('/action-item', methods=['POST'])
def action_item():
    form = request.form.copy()
    item = db.session.query(ToDoList).get(int(form['id']))
    if not item:
        flash('Task not found!', 'error')
        return redirect(url_for('web.index'))
    if form['action'] == 'done':
        item.to_do_status_id = 2
        item.updated_at = datetime.now()
    elif form['action'] == 'canceled':
        item.to_do_status_id = 3
        item.updated_at = datetime.now()
    else:
        flash('Status invalid!', 'error')
        return redirect(url_for('web.index'))
    db.session.commit()
    flash('Task updated!', 'success')
    return redirect(url_for('web.index'))


@web.route('/restore-item/<int:id>', methods=['GET'])
def restore_item(id):
    item = db.session.query(ToDoList).get(int(id))
    if not item:
        flash('Task not found!', 'error')
        return redirect(url_for('web.index'))
    item.to_do_status_id = 1
    item.updated_at = datetime.now()
    db.session.commit()
    flash('Task restored!', 'success')
    return redirect(url_for('web.index'))


def init_app(app):
    app.register_blueprint(web)
