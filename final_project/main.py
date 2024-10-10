from user_input import get_float

def main():
    print("(*) is required")
    get_float("Give me a number")
    get_float("Give me a number", False)
    get_float("What is your age?", True,0)
    get_float("What is your grade level?", True, 1, 12)
    
if __name__ == "__main__":
    main()