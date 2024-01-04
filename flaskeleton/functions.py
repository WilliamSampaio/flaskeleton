from flask import render_template, request


def error_handler(e):
    data = {}
    desc = e.description
    msg = desc['message'] if 'message' in desc else desc
    data['message'] = f'Error({e.code} - {e.name}): {msg}'
    if request.path.startswith('/api/'):
        return {'code': e.code, 'message': e.name}, e.code
    return (
        render_template('error.html', data=data),
        e.code,
    )
