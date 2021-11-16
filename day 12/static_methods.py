class Employee:
    def __init__(self, name, year_joined):
        self.name = name
        self.year_joined = year_joined
        
    #calc_year does not need an instance of a class to work
    @staticmethod
    def calc_year(year_joined, year_now):
        length = year_now - year_joined
        if length > 0:
            return f'{length} years'
        else:
            return 'less than one year'

    def seniority(self):
        n_years = self.calc_year(self.year_joined, datetime.now().year)
        print(f'{self.name} has worked in our company for {n_years}')