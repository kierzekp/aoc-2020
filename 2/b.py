if __name__ == "__main__":
    password_source = None

    valid_count = 0

    with open("passwords.txt", "r") as password_file:
        password_source = [x.strip("\n").split(":") for x in password_file.readlines()]

    for entry in password_source:
        requirements = entry[0].split(" ")
        required_letter = requirements[1]
        required_first_index = int(requirements[0].split("-")[0]) - 1
        required_second_index = int(requirements[0].split("-")[1]) - 1

        password = entry[1].lstrip()

        if (password[required_first_index] == required_letter and password[required_second_index] != required_letter) or (password[required_first_index] != required_letter and password[required_second_index] == required_letter):
            valid_count += 1

    print("There are " + str(valid_count) + " valid passwords.")
