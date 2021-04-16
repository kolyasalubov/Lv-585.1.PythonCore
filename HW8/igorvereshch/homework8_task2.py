class Human:
    def __init__(self, name):
        self.name = name

    def greet(self, msg = 'Hello,'):
        print(f"{msg} {self.name}")

    @classmethod
    def info(cls):
        print("Humans are also known as 'Homo Sapiens'")

    @staticmethod
    def speak(msg = "Hi!"):
        print(f"Someone said: '{msg}'")


albert = Human("Albert")

albert.greet("Say 'Hi!' to")
albert.greet()
print('_____________________________________________________________________')
albert.info()
print('_____________________________________________________________________')
albert.speak()
albert.speak("Few people are capable of expressing with equanimity opinions\n" +\
            "               which differ from the prejudices of their social environment.\n" +\
            "               Most people are even incapable of forming such opinions.")
