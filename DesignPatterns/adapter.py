from abc import ABC, abstractmethod
from datetime import datetime

class Clients(ABC):
    
    @abstractmethod
    def getFullName(self):
        pass

    @abstractmethod
    def getAge(self):
        pass

class Patient(Clients):
    def __init__(self, fullname, age, issue):
        super().__init__()
        self.fullName = fullname
        self.age = age
        self.issue = issue

    def getFullName(self):
        return self.fullName

    def getAge(self):
        return self.age

    def getIssue(self):
        return self.issue


class User(ABC):
    @abstractmethod
    def getFirstName(self):
        pass

    @abstractmethod
    def getLastName(self):
        pass

    @abstractmethod
    def getDOB(self):
        pass

class Doctor(User):
    def __init__(self, firstname, lastname, dob, speciality):
        super().__init__()
        self.firstName = firstname
        self.LastName = lastname
        self.dob  = dob
        self.speciality = speciality
           
    def getFirstName(self):
        return self.firstName

    def getLastName(self):
        return self.LastName

    def getDOB(self):
        return self.dob
    
    def getSpeciality(self):
        return self.speciality
    
    def __str__(self):
        return str(self.__dict__)

class UserAdapter(Clients):
    def __init__(self, user: User):
        super().__init__()
        self.user = user

    def getFullName(self):
        return self.user.getFirstName() +" "+ self.user.getLastName()
    
    def getAge(self):
        today = datetime.today()
        age = today.year - self.user.getDOB().year
        if (today.month, today.day) < (self.user.getDOB().month, self.user.getDOB().day):
            age -= 1
        return age

if __name__=="__main__":
    doctor = Doctor("abhishek", "dubey", datetime.strptime("1999-07-01", "%Y-%m-%d"), "heart")
    print(doctor)

    print()
    patient = UserAdapter(doctor)
    print("name: ",patient.getFullName())
    print("age: ",patient.getAge())