from flask import Flask
from flask_socketio import SocketIO, emit
from flask_cors import CORS


app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*", logger=True, engineio_logger=True)
CORS(app, resources={r"/socket.io/*": {"origins": "http://localhost:3000"}})

@app.route('/')
def home():
    return 'Hello, World!'

@socketio.on('connect')
def handle_connect():
    print('Client connected')

@socketio.on('disconnect')
def handle_disconnect():
    print('Client disconnected')

@socketio.on('message')
def handle_message(message):
    print('MESSAGE INCOMING!!!!')
    print('Received message: ' + message)

@socketio.on('my_event')
def handle_my_event(message):
    # Emitting a response back to the client
    emit('my_response', {'data': 'This is a message from the server'})

@socketio.on_error_default
def default_error_handler(e):
    print('An error occurred:', e)

@app.route('/send_message')
def send_message():
    # Emitting a message to all connected clients
    print('Sending message to all clients')
    socketio.emit('message', {'data': 'Message sent from a Flask route!'})
    return "Message sent!"

if __name__ == '__main__':
    socketio.run(app, host="0.0.0.0", port=5001, debug=True)


# Nescesito correr mi servidor en mi IP
