import re

def validate_birth_year(byr_data):
    return int(byr_data) >= 1920 and int(byr_data) <= 2002


def validate_issuing_year(iyr_data):
    return int(iyr_data) >= 2010 and int(iyr_data) <= 2020


def validate_expiration_year(eyr_data):
    return int(eyr_data) >= 2020 and int(eyr_data) <= 2030


def validate_hair_color(hcl_data):
    return re.search("^#[a-z0-9]{6}$", hcl_data)


def validate_eye_color(ecl_data):
    return ecl_data in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}


def validate_passport_id(pid_data):
    return re.search("^[0-9]{9}$", pid_data)


def validate_height(hgt_data):
    if re.search("^[0-9]{2}in$", hgt_data):
        height = int(hgt_data[:2])
        return height >= 59 and height <= 76
    elif re.search("^[0-9]{3}cm$", hgt_data):
        height = int(hgt_data[:3])
        return height >= 150 and height <= 193
    else:
        return False

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

        passport_dict = {}

        passport_keys = set()
        for pair in passport_pairs:
            key_value = pair.split(":")
            passport_keys.add(key_value[0])
            passport_dict.update({key_value[0]:key_value[1]})

        if passport_keys == required_keys or (passport_keys - required_keys == optional_keys and len(passport_keys) == 8):
            # analysing valid passports
            if not validate_height(passport_dict.get("hgt")):
                continue
            if not validate_passport_id(passport_dict.get("pid")):
                continue
            if not validate_eye_color(passport_dict.get("ecl")):
                continue
            if not validate_hair_color(passport_dict.get("hcl")):
                continue
            if not validate_expiration_year(passport_dict.get("eyr")):
                continue
            if not validate_issuing_year(passport_dict.get("iyr")):
                continue
            if not validate_birth_year(passport_dict.get("byr")):
                continue
            valid += 1


    print("There are " + str(valid) + " valid passports.")
