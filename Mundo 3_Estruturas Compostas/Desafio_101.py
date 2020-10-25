def vote(birth_year):
    from datetime import date
    age = date.today().year - birth_year
    if age < 16:
        return f'{age} YEARS OLD: VOTE DENIED.'
    elif 16 <= age < 18 or age >= 65:
        return f'{age} YEARS OLD: VOTE OPTIONAL.'
    else:
         return f'{age} YEARS OLD: MANDATORY VOTE.'

birth_year = int(input("Type the year of birth: "))
print(vote(birth_year))
