from bottle import *

@route('/static/<filename:path>')
def server_static(filename):
    return static_file(filename, root='./resources')
