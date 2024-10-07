def calculate_birth_year(age, had_birthday):
    from datetime import datetime
    current_year = datetime.now().year
    
    
    if had_birthday.lower() == 'yes':
        birth_year = current_year - age
    else:

        birth_year = current_year - age - 1
    
    return birth_year

def main():
    name = input("What is your name? ")
    age = int(input("What is your age? "))
    had_birthday = input("Have you had your birthday this year? (yes/no) ")
    
    birth_year = calculate_birth_year(age, had_birthday)
    
    print(f"Hello, {name}! You were born in the year {birth_year}.")

if __name__ == "__main__":
    main()
