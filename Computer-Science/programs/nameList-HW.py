
class NameList():
    def __init__(self):
        self.menuOptions = [
                        [self.addName, "Add a name"],
                        [self.printItem, "Get name"],
                        [self.printSlice, "Get slice"],
                        [self.removeName, "Remove a name"],
                        [self.saveList, "Save list to file"],
                        [self.loadList, "Load list from file"],
                        [self.printList, "Print full list"]
        ]
        self.nameList = []

    def menu(self):
        usrInput = " "
        while usrInput != '':
            self.printOptions()
            usrInput = int(input())

            self.menuOptions[usrInput - 1][0]()

    def saveList(self):
        with open("nameList.txt", "w") as f:
            listStr = ""
            for name in self.nameList:
                listStr += name + ","
            f.write(listStr[:len(listStr)-1])

    def loadList(self):
        with open("nameList.txt", "r") as f:
            data = f.read()
            self.nameList = data.split(',')
    def removeName(self):
        usrPick = int(input("Enter the index to remove"))
        self.nameList.pop(usrPick)

    def printList(self):
        print(self.nameList)

    def printOptions(self):
        for i, option in enumerate(self.menuOptions):
            print(f"{i+1}. {option[1]}")

    def printItem(self):
        usrPick = input("enter the number to retrive")
        print(self.nameList[int(usrPick)-1])

    def printSlice(self):
        usrPick = input("enter the part of the list to display in the form 'start-end'")
        usrPick = usrPick.split('-')
        print(usrPick)
        print(self.nameList[int(usrPick[0])-1:int(usrPick[1])])

    def cleanList(self):
        for i in len(self.nameList):
            self.nameList[i] = self.nameList[i].lower

    def addName(self):
        self.nameList.append(input("Enter the new name: "))
        print("name added")


if __name__ == '__main__':
    nameList = NameList()
    nameList.menu()
