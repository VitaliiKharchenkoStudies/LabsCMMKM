import pandas
import pandas as pd
import colorama  # Import the colorama library
from colorama import Fore  # Import the Fore module for foreground color


data = pd.read_csv('titanic.csv')


# task 1
def sex_count():
    male = (data['Sex'] == 'male').sum()
    female = (data['Sex'] == 'female').sum()
    print(f"{male},{female}")
    return male, female


# task 2
def survived_percentage():
    passengers = data["PassengerId"].count()
    survived = (data["Survived"] == 1).sum()  # Assuming '1' indicates survival
    percentage = round((survived * 100) / passengers, 2)
    print(percentage)
    return percentage


# task 3
def first_class_members_percentage():
    passengers = data["PassengerId"].count()
    survived = (data["Pclass"] == 1).sum()
    percentage = round((survived * 100) / passengers, 2)
    print(percentage)
    return percentage


# task 4
def calculate_age_statistics():
    average_age = data["Age"].mean()
    median_age = data["Age"].median()
    print(f"{round(average_age)},{round(median_age)}")
    return round(average_age), round(median_age)


# task 5
def calculate_correlation():
    correlation = data['SibSp'].corr(data['Parch'])
    print(correlation)
    return correlation


# task 6
def extract_first_name(full_name):
    # Split the full name into parts using a comma and space
    name_parts = full_name.split(', ')
    if len(name_parts) > 1:
        # The first name is the second part
        return name_parts[1]
    else:
        # If there's only one part, return it as the first name
        return name_parts[0]


def most_popular_female_name():
    # Extract the first names from the "Name" column
    data['First Name'] = data['Name'].apply(extract_first_name)

    # Filter for female passengers
    female_passengers = data[data['Sex'] == 'female']

    # Group by first name and count occurrences
    name_counts = female_passengers['First Name'].value_counts()

    # Find the most popular female name
    most_popular_name = name_counts.idxmax()
    count = name_counts.max()
    print(f"{most_popular_name}, {count}")
    return most_popular_name, count


def main_menu():
    while True:
        print("\nTitanic Data Analysis Menu:")
        print(Fore.GREEN + "1. Count of Male and Female Passengers")
        print("2. Percentage of Surviving Passengers")
        print("3. Percentage of First-Class Passengers")
        print("4. Calculate Age Statistics")
        print("5. Calculate Correlation between SibSp and Parch")
        print("6. Most Popular Female Name")
        print("7. Exit" + Fore.RESET)

        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            sex_count()
        elif choice == '2':
            survived_percentage()
        elif choice == '3':
            first_class_members_percentage()
        elif choice == '4':
            calculate_age_statistics()
        elif choice == '5':
            calculate_correlation()
        elif choice == '6':
            most_popular_female_name()
        elif choice == '7':
            print(Fore.RED + "Exiting the program. Goodbye!" + Fore.RESET)
            break
        else:
            print(Fore.YELLOW + "Invalid choice. Please enter a valid option (1-7)." + Fore.RESET)

if __name__ == "__main__":
    main_menu()