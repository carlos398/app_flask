from src.app import app

HOST = 'localhost'
PORT = 4000
DEBUG = True
ENVIROMENT = 'development'

if __name__ == '__main__':
    app.run(HOST, PORT, DEBUG)