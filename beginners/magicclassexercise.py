class Person:
    def __init__(self,name):
        self.name=name
    def talk(self):
        print(f'Hi there {self.name}')
        

p=Person('Nikesh')

p.talk()