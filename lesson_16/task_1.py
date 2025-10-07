class Employee:
    def __init__(self, name: str, salary: float):
        self.name = name
        self.salary = salary


class Manager(Employee):

    def __init__(self, name: str, salary: float, department: str, **kwargs):
        super().__init__(name, salary, **kwargs)  # без kwargs ругалось
        self.department = department


class Developer(Employee):

    def __init__(self, name: str, salary: float, programming_language: str, **kwargs):
        super().__init__(name, salary, **kwargs)
        self.programming_language = programming_language


class TeamLead(Manager, Developer):

    def __init__(self, name: str, salary: float, department: str, programming_language: str, team_size: int):
        super().__init__(
            name=name,
            salary=salary,
            department=department,
            programming_language=programming_language

        )

        self.team_size = team_size


lead = TeamLead(
    name="Peter",
    salary=5000.00,
    department="DevOps Department",
    programming_language="Python",
    team_size=8
)

required_employee_attrs = ['name', 'salary']

required_manager_attrs = ['department', 'team_size']

required_developer_attrs = ['programming_language']

all_required_attr = required_employee_attrs + required_manager_attrs + required_developer_attrs

print()
print(" Check if required attributes exist for class TeamLead")
print()

test_passed = True

for attr in all_required_attr:
    if hasattr(lead, attr):
        print(f"Attribute '{attr}' exists.")
        print("-" * 25)
    else:
        print(f"Attribute '{attr}' doesn't exist. Fail!")
        print("-" * 25)
        test_passed = False
