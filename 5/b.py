def analyse_letter(letter, lb, hb):
	midpoint = (hb - lb) // 2
	size = hb - lb + 1
	if letter == "F" or letter == "L":
		if size == 2:
			return lb, lb
		else:
			return lb, lb + midpoint
	elif letter == "B" or letter == "R":
		if size == 2:
			return hb, hb
		else:
			return lb + midpoint + 1, hb
	else:
		raise Exception("chuj!")


def calculate_seat_id(row_index, column_index):
	return row_index * 8 + column_index

if __name__ == "__main__":
	boarding_data = None

	with open("data.txt", "r") as data_file:
		boarding_data = [x.strip("\n") for x in data_file.readlines()]

	lower_bound_rows = 0
	higher_bound_rows = 127
	lower_bound_seats = 0
	higher_bound_seats = 7

	seat_ids = []

	for boarding_entry in boarding_data:
		for letter in boarding_entry:
			if letter == "F" or letter == "B":
				(lower_bound_rows, higher_bound_rows) = analyse_letter(letter, lower_bound_rows, higher_bound_rows)
			elif letter == "L" or letter == "R":
				(lower_bound_seats, higher_bound_seats) = analyse_letter(letter, lower_bound_seats, higher_bound_seats)
		seat_id = calculate_seat_id(lower_bound_rows, lower_bound_seats)
		seat_ids.append(seat_id)

		lower_bound_rows = 0
		higher_bound_rows = 127
		lower_bound_seats = 0
		higher_bound_seats = 7

	seat_ids.sort()

	for index, seat_id in enumerate(seat_ids):
		if index != 0 and index != len(seat_ids) - 1:
			if seat_ids[index - 1] != seat_id - 1 or seat_ids[index + 1] != seat_id + 1:
				print("There is not a seat preceeding or after seat id " + str(seat_id))