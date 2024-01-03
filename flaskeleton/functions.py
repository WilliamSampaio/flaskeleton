from flask import render_template


def error_handler(e):
    data = {}
    desc = e.description
    msg = desc['message'] if 'message' in desc else desc
    data['message'] = f'Error({e.code} - {e.name}): {msg}'
    return (
        render_template('error.html', data=data),
        e.code,
    )
