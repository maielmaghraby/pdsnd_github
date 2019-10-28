import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def apply_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    does not accept wrong responses.

    Returns:
        (str) city - name of the city to analyze (chicago, new york city, washington)
        (str) month - name of the month (january, february, march, april, may, june) to filter by, or "all" to apply no month filter
        (str) day - name of the day of week (saturday, sunday, monday, tuesday, wednesday, thursday, friday) to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington).

    city = input('Choose a city to analyze: ').lower()

    while city not in CITY_DATA.keys():
        city = input('Please enter another valid input: ').lower()

    # TO DO: get user input for month (all, january, february, ... , june)
    month = input('Choose all or specify a month: ').lower()
    while month not in ['january', 'february', 'march', 'april', 'may', 'june', 'all']:
        month = input('Please specify a month name or choose all: ').lower()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input('Choose all or specify a day of week: ').lower()
    while day not in ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'all']:
        day = input('Please specify a day name or choose all: ').lower()

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # TO DO: display the most common month
    df['month'] = df['Start Time'].dt.month
    popular_month = df['month'].mode()[0]
    print('Popular month is: {}'.format(popular_month))

    # TO DO: display the most common day of week
    df['day of week'] = df['Start Time'].dt.day
    popular_day = df['day of week'].mode()[0]
    print('Popular day of week is: {}'.format(popular_day))

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('Popular hour is: {}'.format(popular_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print('Common start station is: {}'.format(common_start_station))

    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print('Common end station is: {}'.format(common_end_station))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total travel time is: {}'.format(total_travel_time))

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('Mean travel time is: {}'.format(mean_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print ('Counts of user types: {}'.format(user_types))

    try:
    # TO DO: Display counts of gender
        gender_types = df['Gender'].value_counts()
        print ('Counts of gender: {}'.format(gender_types))

    # TO DO: Display earliest, most recent, and most common year of birth
        earliest_year_of_birth = df['Birth Year'].min()
        recent_year_of_birth = df['Birth Year'].max()
        common_year_of_birth = df['Birth Year'].mode()
        print('Earliest year of birth: {}'.format(earliest_year_of_birth))
        print('Most recent year of birth: {}'.format(recent_year_of_birth))
        print('Most common year of birth: {}'.format(common_year_of_birth))
    except:
        print('There are no gender or birth year columns')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = apply_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        raw_data = input('Would you like to view raw data? Enter yes or no.')
        while raw_data.lower() == 'yes':
            count = 0
            if raw_data.lower() == 'yes':
                count += 5
                print(df.iloc[: count])
                continue
            else:
                break

        # TO do: Asks the user if he/she wants to start the process again.
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
