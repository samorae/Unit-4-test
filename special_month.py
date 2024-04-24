
'''
Name: Eli Samora
Date: 4/22/24
Assignment: Unit 3 and 4 Take Home Exam
'''
def main():
    season = ''
    user_month = input('Enter the name of the month: ')
    user_day = int(input('Enter the day (1-31): '))

    if user_month.lower() == 'march' and user_day >= 20:
        season = 'Spring'
    elif user_month.lower() == 'april':
        season = 'Spring'
    elif user_month.lower() == 'may':
        season = 'Spring'
    elif user_month.lower() == 'june' and user_day < 21:
        season = "Spring "
    elif user_month.lower() == 'june' and user_day >= 21:
        season = 'Summer'
    elif user_month.lower() == 'july':
        season = 'Summer '
    elif user_month.lower() == 'august':
        season = 'Summer'
    elif user_month.lower() == 'september' and user_day < 22:
        season = 'Summer'
    elif user_month.lower() == 'september' and user_day >= 22:
        season = 'Fall'
    elif user_month.lower() == 'october':
        season = 'Fall'
    elif user_month.lower() == 'november':
        season = 'Fall'
    elif user_month.lower() == 'december' and user_day < 21:
        season = 'Fall'
    elif user_month.lower() == 'december' and user_day >= 21:
        season = 'Winter'
    elif user_month.lower() == 'january':
        season = 'Winter'
    elif user_month.lower() == 'february':
        season = 'Winter'
    elif user_month.lower() == 'march' and user_day < 20:
        season = 'Winter'
    else:
        print("That isn't a month or day")
    user_month_final = user_month.capitalize()
    end_print = f'{user_month_final} {user_day} is in {season}'
    print(end_print)
# do not modify below this
if __name__=='__main__':
    main()
    
    