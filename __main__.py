from agents import GoogleFluAgent
from sys import argv

if __name__ == '__main__':
    agent = None
    if argv[1] == 'flu':
        agent = GoogleFluAgent()

    if argv[2] == 'update':
        agent.update()
