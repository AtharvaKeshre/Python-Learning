class Employee:
    company = "Apple"
    def show(tinde):
        print(f"The name is {tinde.name} and company is {tinde.company}")

    @classmethod #by default jo 1st argument hota h vo instance milta hai but @classmethod decorator lagnae se usko 1st args as a class milta h
    def changeCompany(cls, newCompany):
        cls.company = newCompany


e1 = Employee()
e1.name = "Atharva"
e1.show()
e1.changeCompany("Tesla")
e1.show()
print(Employee.company)
