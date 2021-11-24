if __name__ == "__main__":
    passport_data = None
    required_keys = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
    optional_keys = {"cid"}

    with open("entry.txt", "r") as entry_file:
        raw_data = entry_file.read()
        passport_data = raw_data.split("\n\n")

    valid = 0

    for passport_entry in passport_data:
        passport_entry = passport_entry.replace("\n", " ")
        passport_pairs = passport_entry.split(" ")

        passport_keys = set()
        for pair in passport_pairs:
            key_value = pair.split(":")
            passport_keys.add(key_value[0])

        if passport_keys == required_keys or (passport_keys - required_keys == optional_keys and len(passport_keys) == 8):
            valid += 1

    print("There are " + str(valid) + " valid passports.")
