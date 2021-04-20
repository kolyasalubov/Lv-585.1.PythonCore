class Human:
    def __init__(self, name):
        self.name = name

    def messsege (self):
        print ("Welcone on board {} !".format (self.name))
    
    @classmethod
    def info (cls):
        print ('The species that you and all other living human beings on this planet belong to is Homo sapiens.')
    
    @staticmethod
    def greet():
        print('Nice to meet you!')

roman = Human ("Roman")

roman.messsege()
roman.info()
roman.greet()
