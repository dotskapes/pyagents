from agents import GoogleFluAgent
from sys import argv

settings = {
    'host': '127.0.0.1',
    'port': 8888,
    'path': '/fudd'
}

if __name__ == '__main__':
    agent = None
    if argv[1] == 'flu':
        agent = GoogleFluAgent(settings)

    if argv[2] == 'update':
        agent.update()
