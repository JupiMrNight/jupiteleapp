from flask import Flask, render_template, request, session, redirect, url_for
from flask_socketio import SocketIO, emit, join_room, leave_room
import secrets

app = Flask(__name__)
app.config['SECRET_KEY'] = secrets.token_hex(16)
socketio = SocketIO(app, cors_allowed_origins="*")

# Store active users and rooms
active_users = {}
chat_rooms = {'general': []}

@app.route('/')
def index():
    if 'username' not in session:
        return redirect(url_for('login'))
    return render_template('index.html', username=session['username'])

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        if username:
            session['username'] = username
            return redirect(url_for('index'))
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

@socketio.on('connect')
def handle_connect():
    if 'username' in session:
        username = session['username']
        active_users[request.sid] = username
        user_count = len(active_users)
        emit('user_connected', {'username': username, 'user_count': user_count}, broadcast=True)

@socketio.on('disconnect')
def handle_disconnect():
    if request.sid in active_users:
        username = active_users.pop(request.sid)
        user_count = len(active_users)
        emit('user_disconnected', {'username': username, 'user_count': user_count}, broadcast=True)

@socketio.on('send_message')
def handle_message(data):
    if 'username' in session:
        message_data = {
            'username': session['username'],
            'message': data.get('message', ''),
            'timestamp': data.get('timestamp', '')
        }
        emit('receive_message', message_data, broadcast=True)

@socketio.on('typing')
def handle_typing(data):
    if 'username' in session:
        emit('user_typing', {'username': session['username']}, broadcast=True, include_self=False)

if __name__ == '__main__':
    socketio.run(app, debug=True, host='0.0.0.0', port=5000)
