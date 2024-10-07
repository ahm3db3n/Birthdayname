def calculate_birth_year(age, had_birthday):
    from datetime import datetime
    current_year = datetime.now().year
    
    # If the user has had their birthday, the birth year is simply current year minus age
    if had_birthday.lower() == 'yes':
        birth_year = current_year - age
    else:
        # If they haven't had their birthday, subtract an extra year
        birth_year = current_year - age - 1
    
    return birth_year

def main():
    # Get user input
    name = input("What is your name? ")
    age = int(input("What is your age? "))
    had_birthday = input("Have you had your birthday this year? (yes/no) ")
    
    # Calculate birth year
    birth_year = calculate_birth_year(age, had_birthday)
    
    # Display the result
    print(f"Hello, {name}! You were born in the year {birth_year}.")

# Run the main function
if __name__ == "__main__":
    main()
