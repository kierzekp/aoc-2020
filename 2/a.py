if __name__ == "__main__":
    password_source = None

    valid_count = 0

    with open("passwords.txt", "r") as password_file:
        password_source = [x.strip("\n").split(":") for x in password_file.readlines()]

    for entry in password_source:
        requirements = entry[0].split(" ")
        required_letter = requirements[1]
        required_lower_bound = int(requirements[0].split("-")[0])
        required_higher_bound = int(requirements[0].split("-")[1])

        password = entry[1]
        required_letter_count = 0
        for char in password:
            if (char == required_letter):
                required_letter_count += 1

        if required_letter_count >= required_lower_bound and required_letter_count <= required_higher_bound:
            valid_count += 1

    print("There are " + str(valid_count) + " valid passwords.")
