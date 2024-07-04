import pandas as pd
import csv
from datetime import datetime
from datetime import timedelta
import time                                                 
chicago = 'chicago.csv'
new_york_city = 'new_york_city.csv'
washington = 'washington.csv'
with open(chicago) as c:
    viewer = csv.DictReader(c)
    chicago_list=[row for row in viewer]

with open(new_york_city) as c:
    viewer = csv.DictReader(c)
    new_york_list=[row for row in viewer]

with open(washington) as c:
    viewer = csv.DictReader(c)
    washington_list=[row for row in viewer]

data={}
data[chicago]=chicago_list
data[new_york_city]=new_york_list
data[washington]=washington_list
def total_city():
    cities = ''
    while cities.lower() not in ['chicago', 'new york', 'washington']:
        cities = input('\nHello there! Let\'s Its time for us to explore some US bikeshare data!\n'
                     'Would you like to have a look at data for Chicago, New York, or'
                     ' Washington?\n')
        if cities.lower() == "chicago":
            return "chicago.csv"
        elif cities.lower() == "new york":
            return "new_york_city.csv"
        elif cities.lower() == "washington":
            return "washington.csv"
        else:
            print('not a valid input. Please input either '
                  'Chicago, New York, or Washington.')

def total_time():
    time_period = ''
    while time_period.lower() not in ['month', 'day', 'none']:
        time_period = input('\nWould you like to filter the data by month, day,'
                            ' or not at all? Type "none" for no time filter.\n')
        if time_period.lower() not in ['month', 'day', 'none']:
            print('Sorry, I do not understand your input.')
    return time_period

def total_month():
    month_input = ''
    number_of_months = {'january': 1, 'february': 2, 'march': 3, 'april': 4,
                   'may': 5, 'june': 6}
    while month_input.lower() not in number_of_months.keys():
        month_input = input('\nchoose a month? January, February, March, April,'
                            ' May, or June?\n')
        if month_input.lower() not in number_of_months.keys():
            print('Sorry, invalid input. Please enter a '
                  'month between January and June')
    month = number_of_months[month_input.lower()]
    return ('2017-{}'.format(month), '2017-{}'.format(month + 1))

def total_day():
    current_month = total_month()[0]
    month = int(current_month[5:])
    expire_date = False
    while expire_date == False:    
        is_int = False
        day = input('\nWhich day? your input should be an an integer.\n')
        while is_int == False:
            try:
                day = int(day)
                is_int = True
            except ValueError:
                print('Sorry, invalid input. Please type your'
                      ' response as an integer.')
                day = input('\nWhich day? your input should be an an integer.\n')
        try:
            start_date = datetime(2017, month, day)
            expire_date = True
        except ValueError as e:
            print(str(e).capitalize())
    end_date = start_date + timedelta(days=1)
    return (str(start_date), str(end_date))
def favoured_day(db):
    days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday',
                    'Saturday', 'Sunday']
    index = int(db['start_time'].dt.dayofweek.mode())
    most_fav_day = days_of_week[index]
    print('The most favoured day of week for start time is {}.'.format(most_fav_day))


def favoured_month(db):
    months = ['January', 'February', 'March', 'April', 'May', 'June']
    index = int(db['start_time'].dt.month.mode())
    most_fav_month = months[index - 1]
    print('The most favoured month is {}.'.format(most_fav_month))

def most_visited_hour(db):
    most_fav_hour = int(db['start_time'].dt.hour.mode())
    if most_fav_hour == 0:
        am_or_pm = 'am'
        pop_hour_readable = 12
    elif 1 <= most_fav_hour < 13:
        am_or_pm = 'am'
        pop_hour_readable = most_fav_hour
    elif 13 <= most_fav_hour < 24:
        am_or_pm = 'pm'
        pop_hour_readable = most_fav_hour - 12
    print('The most popular hour of day for start time is {}{}.'.format(pop_hour_readable, am_or_pm))

def trip_duration(db):
    total_duration = db['trip_duration'].sum()
    minute, second = divmod(total_duration, 60)
    hour, minute = divmod(minute, 60)
    print('The total trip duration is {} hours, {} minutes and {}'
          ' seconds.'.format(hour, minute, second))
    average_duration = round(db['trip_duration'].mean())
    minut, sec = divmod(average_duration, 60)
    if minut > 60:
        hr, minut = divmod(minut, 60)
        print('The average trip duration is {} hours, {} minutes and {}'
              ' seconds.'.format(hr, minut, sec))
    else:
        print('The average trip duration is {} minutes and {} seconds.'.format(minut, sec))

def favoured_stations(db):
    fav_start = db['start_station'].mode().to_string(index = False)
    fav_end = db['end_station'].mode().to_string(index = False)
    print('The most favoured start station is {}.'.format(fav_start))
    print('The most favoured end station is {}.'.format(fav_end))

def favoured_trip(db):
    most_pop_trip = db['journey'].mode().to_string(index = False)
    print('The most favoured trip is {}.'.format(most_pop_trip))

def users(db):
    subs = db.query('user_type == "Subscriber"').user_type.count()
    cust = db.query('user_type == "Customer"').user_type.count()
    print('Number of subscribers are {} and ustomers are {}.'.format(subs, cust))

def gender(db):
    num_of_male = db.query('gender == "Male"').gender.count()
    num_of_female = db.query('gender == "Male"').gender.count()
    print('Number of male users are {} and female users are {}.'.format(num_of_male, num_of_female))

def year_of_birth(db):
    early = int(db['birth_year'].min())
    just_arrived = int(db['birth_year'].max())
    pop_year = int(db['birth_year'].mode())
    print('The older users are born in {}.\nyoungesters are born in {}.'
          '\nThe most popular birth year is {}.'.format(early,just_arrived, pop_year))

def display_of_data(db):
    def is_valid(display):
        if display.lower() in ['yes', 'no']:
            return True
        else:
            return False
    h = 0
    t = 5
    proper_input = False
    while proper_input == False:
        display = input("\ni hope you don't mind viewing individual trip data? "
                        'Type \'yes\' or \'no\'.\n')
        proper_input = is_valid(display)
        if proper_input == True:
            break
        else:
            print("not a valid input. Please type 'yes' or"
                  " 'no'.")
    if display.lower() == 'yes':
        
        print(db[db.columns[0:-1]].iloc[h:t])
        display_more = ''
        while display_more.lower() != 'no':
            valid_input = False
            while valid_input == False:
                display_more = input('\nWould you like to view more individual'
                                     ' trip data? Type \'yes\' or \'no\'.\n')
                valid_input = is_valid(display_more)
                if valid_input == True:
                    break
                else:
                    print("Sorry, I do not understand your input. Please type "
                          "'yes' or 'no'.")
            if display_more.lower() == 'yes':
                h += 5
                t += 5
                print(db[db.columns[0:-1]].iloc[h:t])
            elif display_more.lower() == 'no':
                break


def statistical_algorithm():
    city = total_city()
    print('analysing data........')
    db = pd.read_csv(city, parse_dates = ['Start Time', 'End Time'])
    
   
    new_labels = []
    for col in db.columns:
        new_labels.append(col.replace(' ', '_').lower())
    db.columns = new_labels
    
   
    pd.set_option('max_colwidth', 100)
    
    
    db['journey'] = db['start_station'].str.cat(db['end_station'], sep=' to ')

    
    time_period = total_time()
    if time_period == 'none':
        db_filter = db
    elif time_period == 'month' or time_period == 'day':
        if time_period == 'month':
            filter_lower, filter_upper = total_month()
        elif time_period == 'day':
            filter_lower, filter_upper = total_day()
        print('Filtering data...')
        db_filter = db[(db['start_time'] >= filter_lower) & (db['start_time'] < filter_upper)]
    print('\nCalculating the first statistic...')

    if time_period == 'none':
        start_time = time.time()
        
        
        favoured_month(db_filter)
        print("It took %s seconds." % (time.time() - start_time))
        print("next statistcal data on its way sir...")
    
    if time_period == 'none' or time_period == 'month':
        start_time = time.time()
        
        
        favoured_day(db_filter)
        print("It took %s seconds." % (time.time() - start_time))
        print("\next statistcal data on its way sir...")    
        start_time = time.time()
   
        most_visited_hour(db_filter)
        print("It took %s seconds." % (time.time() - start_time))
        print("next statistcal data on its way sir...")
        start_time = time.time()
        
        trip_duration(db_filter)
        print("It took %s seconds." % (time.time() - start_time))
        print("next statistcal data on its way sir...")
        start_time = time.time()

        favoured_stations(db_filter)
        print("It took %s seconds." % (time.time() - start_time))
        print("next statistcal data on its way sir...")
        start_time = time.time()

        favoured_trip(db_filter)
        print("It took %s seconds." % (time.time() - start_time))
        print("next statistcal data on its way sir...")
        start_time = time.time()

        users(db_filter)
        print("It took %s seconds." % (time.time() - start_time))
    
    if city == 'chicago.csv' or city == 'new_york_city.csv':
        print("\next statistcal data on its way sir......")
        start_time = time.time()
        
       
        gender(db_filter)
        print("It took %s seconds." % (time.time() - start_time))
        print("\nnext statistcal data on its way sir...")
        start_time = time.time()

       
        year_of_birth(db_filter)
        print("It took %s seconds." % (time.time() - start_time))

    
    display_of_data(db_filter)

    
    restart = input('\nWould you like to restart? Type \'yes\' or \'no\'.\n')
    while restart.lower() not in ['yes', 'no']:
        print("not a valid input. Please type in 'yes' or 'no'.")
        restart = input('\nwanna restart? Type \'yes\' or \'no\'.\n')
    if restart.lower() == 'yes':
        statistical_algorithm()


if __name__ == "__main__":
	statistical_algorithm()