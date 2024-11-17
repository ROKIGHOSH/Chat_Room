from main import app
from main import SocketIO
socketio = SocketIO(app)
if __name__ == "__main__":
    socketio.run(app, debug=True)