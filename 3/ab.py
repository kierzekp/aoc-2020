if __name__ == "__main__":
    map_section = None

    with open("map.txt", "r") as map_file:
        map_section = [x.strip("\n") for x in map_file.readlines()]

    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

    rolling_product = 1

    for slope in slopes:
        x_position = 0
        trees_hit = 0

        for y_position, map_line in enumerate(map_section):
            if y_position % slope[1] != 0:
                continue
            if map_line[x_position] == "#":
                trees_hit += 1
            x_position += slope[0]
            if x_position >= len(map_line):
                x_position = abs(len(map_line) - x_position)

        print("Number of trees hit for slope " + str(slope) + ": " + str(trees_hit))

        rolling_product *= trees_hit

    print("Product of the number of all trees hit is " + str(rolling_product))
