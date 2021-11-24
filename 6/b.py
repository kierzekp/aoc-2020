if __name__ == "__main__":
    group_answers = []

    with open("answers.txt", "r") as entry_file:
        raw_data = entry_file.read()
        group_answers = raw_data.split("\n\n")

    all_repeating_answers = 0
    for group in group_answers:
        person_answers = group.split("\n")
        repeating_answers = set()
        if len(person_answers) == 1:
            for answer in person_answers[0]:
                repeating_answers.add(answer)
        else:
            for answer in person_answers[0]:
                repeating_answers.add(answer)
            for person in person_answers[1:]:
                new_repeating_answers = set()
                for answer in person:
                    if answer in repeating_answers:
                        new_repeating_answers.add(answer)
                repeating_answers = new_repeating_answers
        print("Repeating snswers for group: " + str(repeating_answers))
        all_repeating_answers = all_repeating_answers + len(repeating_answers)

    print("Sum of all repeating answers: " + str(all_repeating_answers))
