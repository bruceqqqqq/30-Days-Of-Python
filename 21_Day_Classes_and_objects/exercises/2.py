class PersonAccount:
    def __init__(self, name, sobrenome, income=[], expenses_properties=[]):
        self.name = name
        self.sobrenome = sobrenome
        self.income = income
        self.expenses_properties = expenses_properties

    def total_income(self):
        return sum(self.income)

    def total_expense(self):
        return sum(self.expenses_properties)

    def add_income(self, value):
        self.income.append(value)

    def add_expense(self, value):
        self.expenses_properties.append(value)

    def account_balance(self):
        return sum(self.income) - sum(self.expenses_properties)


person = PersonAccount('Diego', 'Fregolente', [1300, 420, 200, 300], [100, 90, 180, 300, 300])
print(person.name)
print(person.sobrenome)
print(person.income)
print(person.expenses_properties)
print(person.total_income())
print(person.total_expense())
person.add_expense(400)
person.add_income(400)
print(person.expenses_properties)
print(person.income)
print(person.account_balance())
