def days_in_feb(user_year):
    while True:
        if user_year % 4 == 0 and user_year % 100 != 0:
            return 29
        elif user_year % 400 == 0:                     
            return 29
        else:                                           
            return 28
while True:
    if __name__ == '__main__':
        user_year = int(input())
        day = days_in_feb(int(user_year))
        print(f'{user_year} has {day} days in February.')
