from question_d import create_multiplication_table, display_table


def get_user_choice(prompt: str) -> bool:
    while True:
        choice = input(prompt).lower()
        if choice in ('y', 'yes'):
            return True
        if choice in ('n', 'no'):
            return False
        print("Please enter 'y' or 'n'")


def main():
    print("Multiplication Table Generator\n" + "-" * 30)
    
    while True:
        table = create_multiplication_table()
        display_table(table)
        
        if not get_user_choice("\nGenerate another table? (y/n): "):
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()