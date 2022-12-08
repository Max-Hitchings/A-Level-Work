class Person:
    def __init__(self, name, hobby, age, subject):
        self.name = name
        self.hobby = hobby
        self.age = age
        self.subject = subject

    def print(self):
        print(f"{self.name}, {self.hobby}, {self.age}, {self.subject}")

    # def create(self):
class Notepad():
    def __init__(self):
        pass

    def getPersonData(self):
        name = input("Enter name")
        hobby = input("Enter hobby")
        age = input("Enter age")
        subject = input("enter fav subject")

        return name, hobby, age, subject

    def createPerson(self, personData):

        return Person(personData[0], personData[1], personData[2], personData[3])


    def write(self):
        people = []
        with open("people.txt", "w") as f:
            nPeople = int(input("how many people to create?"))

            for i in range(nPeople):
                people.append(Person(*self.getPersonData()))
                f.write(f"{people[i].name}, {people[i].hobby}, {people[i].age}, {people[i].subject}")

    def load(self):
        self.people = []

        with open("people.txt", "r") as f:
            for line in f.read().split("\n"):
                self.people.append(self.createPerson(line.split(",")))



    def search(self):
        searchField = input("what to search by? (n/h/a/s)")

        if searchField == "n":
            name = input("what name to search for?")
            for person in self.people:
                if person.name == name:
                    person.print()
# write()
n = Notepad()

n.load()
n.search()