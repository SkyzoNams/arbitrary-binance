#from sources.engine import Engine
#from sources.config import Config_Loader

def handler():
    class Developer(object):
        def __init__(self, skills):
            self.skills = skills

        def __add__(self, other):
            skills = self.skills + other.skills
            return "Skills"

    A = Developer("NodeJS")
    B = Developer("Python")
    print(A + B)

    # engine_motor = Engine(Config_Loader())
    #engine_motor.run()
    

handler()