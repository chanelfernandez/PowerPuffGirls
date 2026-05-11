def confirm_choice(message):
    while True:
        answer = input(f"{message} (yes/no): ").lower()

        if answer == "yes":
            return True
        elif answer == "no":
            return False
        else:
            print("Invalid input. Please type 'yes' or 'no'.")

