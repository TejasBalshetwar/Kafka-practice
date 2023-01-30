from flask import Flask,render_template
from flask_socketio import SocketIO,send,emit,join_room,leave_room
from ksql_use import ksql_client
from logger import logger
import json 


app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'

socketio = SocketIO(app)
ROOMS = ['room1','room2','room3','room4']

def str_to_json(str):
    return json.loads(str)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/logs')
def logs():
    return render_template('logs.html',rooms= ROOMS)

@socketio.on('message') #predefined event
def message(data):
    print(f"\n{data}\n")
    send(data,broadcast=True)
    emit('my-event',"this is a custom event message",broadcast=True)

@socketio.on('play_log')
def live_log(msg):
    if msg == "start":
        try:
            rows = ksql_client.query("print logstash from beginning;")
            for row in rows:
                if "finalMessage" not in row and "header" not in row :
                    # print(str_to_json(row[53:row.find("}")+1]))
                    a = row[row.find("{"):row.find("}")+1]
                    if (len(a)>4):
                        data = json.loads(a)
                        socketio.emit('log',data,ignore_queue=True)
        except Exception as e:
            pass
    else:
        socketio.send("Stopped")

@socketio.on('join')
def join(data):
    join_room(data['room'])
    send("joined room")

@socketio.on('leave')
def leave(data):
    leave_room(data['room'])
    send("left room")

if __name__ == '__main__':
    socketio.run(app)