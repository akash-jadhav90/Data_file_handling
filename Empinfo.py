


class Emp:
    def __init__(self,eid,enm,eage,esalary,eemail):
        self.empid=eid
        self.empname=enm
        self.empage=eage
        self.empsalary=esalary
        self.empemail=eemail

    def __str__(self):
        return f'{self.__dict__}'

    def __repr__(self):
        return str(self)

