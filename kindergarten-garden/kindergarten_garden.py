class Garden:
    def __init__(self, diagram, students = ["Alice", "Bob", "Charlie", "David", "Eve", "Fred", "Ginny", "Harriet", "Ileana", "Joseph", "Kincaid", "Larry"]):
        self.plantDict = {'R': "Radishes", 'C':"Clover", 'G':"Grass", 'V':"Violets"}
        self.students = sorted(students)

        #Generate clusters and store with each person
        #for example: ['VVCCGGVV','CVAVCCGG]
        self.clusters = diagram.split('\n')
        
        #Generate dictionary of student:XXXX for each student, where X represents flower acronym (string) and student is a string
        self.belongings = {}
        for student in self.students:
            studentPosition = self.students.index(student)*2
            self.belongings[student] = self.clusters[0][studentPosition:studentPosition+2] + self.clusters[1][studentPosition:studentPosition+2]
        
    def plants(self, student):
        #Iterate through already generated 4 alphabet bundles for called student
        return [self.plantDict[flower] for flower in self.belongings[student]]