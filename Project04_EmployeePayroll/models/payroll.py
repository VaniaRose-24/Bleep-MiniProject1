from models.employee import Employee

class Payroll(Employee):

    HRA = 0.20
    DA = 0.10
    TAX = 0.05

    def calculate_salary(self):

        basic = self.get_salary()

        hra = basic * self.HRA
        da = basic * self.DA
        tax = basic * self.TAX

        return basic + hra + da - tax

    def display(self):

        print("\n----------------------------")
        print("Employee ID :", self.get_id())
        print("Name        :", self.get_name())
        print("Basic Salary:", self.get_salary())
        print("Net Salary  :", self.calculate_salary())
        print("----------------------------")