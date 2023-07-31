# Store all students information in dictionary format
class Student:
    def GetStudent(self):
        self.__rollno = input("Enter Roll No:")
        self.__name = input("Enter Name:")
        self.__physicsMarks = int(input("Enter Physics Marks:"))
        self.__chemistyMarks = int(input("Enter Chemistry Marks:"))
        self.__mathMarks = int(input("Enter Maths Marks:"))
        return(self.__rollno)

    def PutStudent(self):
        print(self.__rollno,self.__name,((self.__physicsMarks+self.__chemistyMarks+self.__mathMarks)/3))
    def Search(self,min,max):
        per = (self.__physicsMarks+self.__mathMarks+self.__chemistyMarks)/3
        if(per>=min and per<=max):
            return True
        else:
            return False
