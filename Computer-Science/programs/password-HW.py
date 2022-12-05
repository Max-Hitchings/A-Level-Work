class Password():
    def __init__(self, password):
        self.password = password
        self.valid = False
        self.errors = []

    def isValid(self):
        if self.checkCase() and self.checkLen() and self.checkPatterens():
            print("all good")
        else:
            self.printErrors()

    def checkCase(self):
        digit, lower = False, False

        for char in self.password:
            if not char.isdigit() and not char.islower():
                self.addError(f"{char} is not a valid character")
                return False
            elif char.isdigit():
                digit = True
            elif char.islower():
                lower = True

        if digit is False or lower is False:
            self.addError("Does not contain both digits and characters")
            return False
        return True

    def checkPatterens(self):
        for i in range(len(self.password)):
            for delta in range(i+1, len(self.password)+1):
                if self.password[i:delta] == self.password[delta:(delta*2)-i]:
                    self.addError(f"'{self.password[i:delta]}' is immediately followed by '{self.password[delta:(delta*2)-i]}'")
                    return False

        return True
                # print(f"{self.password[i:delta]} ± {self.password[delta:(delta*2)-i]}")
                # pass
                # delta += 1
                # if i+delta < len(self.password):
                #     if self.password[i:i+delta] == self.password[i+delta:i+(delta*2)]:
                #         print(f"{self.password[i:i+delta]} == {self.password[i+delta:i+(delta*2)]}")
                #         return False
                #     else:
                #         print(f"{self.password[i:i+delta]} != {self.password[i+delta:i+(delta*2)]}")
                # leftover = len(self.password) - i
                # for j in range(leftover):
                #     if char == self.password[i+1]:
                #         return False

    def checkLen(self):
        if len(self.password) >= 5 and len(self.password) <= 12:
            return True
        self.addError("Too short")
        return False

    def addError(self, newError):
        self.errors.append(newError)

    def printErrors(self):
        print("Rejected because: ")
        for error in self.errors:
            print("    ",error)


password = Password(input("enter a new password"))

password.isValid()