class PhoneNumber:
    def __init__(self, number):
        self.rawnumber = "".append([i for i in number if i.isdigit()])
        self.number = self.rawnumber[1:] if self.rawnumber[0] == '1' else self.rawnumber

        
    def clean(self):
        cleanSlate = ""
        for i in self.number:
            if i.isdigit():
                cleanSlate += str(i)
        if cleanSlate[0] == '1':
            return cleanSlate[1:]
        
        return cleanSlate
