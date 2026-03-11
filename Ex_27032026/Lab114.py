class Person:
    #Attributes
    name: None
    id: None
    age: None
    phone_number: None

    #Behaviours
    def talk(self): # No Arg -> No Return
        print("I can talk")

    def speak(self, name): # Arg with No Return
        print("I cam Speak")
        print("Speak", name)

    def sleep(self, name): # Arg with Return
        print("I am Sleeping")
        return None

    def walk(self):
        print("I am walking")

    def walk_return(self): # No Arg with Return
        return "I am walking"

# Object of Person Class
# ObjectRef = Object() -> ClassName
amit = Person()
# amit.name = "Amit Kumar"
amit.talk()

lucky = Person()
lucky.name = "Lucky"
lucky.walk()


