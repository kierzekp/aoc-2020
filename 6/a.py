if __name__ == "__main__":
    group_answers = []

    with open("answers.txt", "r") as entry_file:
        raw_data = entry_file.read()
        group_answers = raw_data.split("\n\n")

    unique_answers = set()
    all_answers = 0
    for group in group_answers:
        for answer in group:
            if answer != "\n":
                unique_answers.add(answer)
        print("Number of unique answers for group: " + str(len(unique_answers)))
        all_answers = all_answers + len(unique_answers)
        unique_answers = set()

    print("Sum of all answers: " + str(all_answers))
