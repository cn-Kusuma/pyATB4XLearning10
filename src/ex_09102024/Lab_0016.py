from unittest import case

user_type = input("Enter the user type, admin, user, guest")
user_type = user_type.lower()
match user_type:
    case "admin" | "manager":
        print("Hello sir")

    case "guest":
        print("Hello, Guest")

    case _:
        print("Hello, There")