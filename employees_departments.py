class Employee:

    def __init__(self, name, job_title, start_date):
        self.name = name
        self.job_title = job_title
        self.start_date = start_date


class Company:

    def __init__(self, name, address, industry_type):
        self.name = name
        self.address = address
        self.industry_type = industry_type
        self.employees = list()

teen_titans = Company("Teen Titans", "123 San Francisco Bay", "crime fighting")
justice_league = Company("Justice League", "345 Watchtower Road", "world saving")

robin = Employee("Robin", "Leader", "1/1/2006")
cyborg = Employee("Cyborg", "Tech Genius", "5/3/2010")
beast_boy = Employee("Beast Boy", "Pet", "11/11/2011")
superman = Employee("Superman", "Leader", "8/2/1986")
batman = Employee("Batman", "Caped Crusader", "4/6/1994")

teen_titans.employees.extend([robin, cyborg, beast_boy])
justice_league.employees.extend([superman, batman])

print(f"{teen_titans.name} is in the {teen_titans.industry_type} industry and has the following employees:")
for employee in teen_titans.employees:
    print(f"* {employee.name}, {employee.job_title}")

print(f"{justice_league.name} is in the {justice_league.industry_type} industry and has the following employees:")
for employee in justice_league.employees:
    print(f"* {employee.name}, {employee.job_title}")

