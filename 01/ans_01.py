FIRST_ANSWER = 0
SECOND_ANSWER = 1


def get_calibration_value(messed_calibration_line: str):
    calibration_length = len(messed_calibration_line)

    if calibration_length < 2:
        return 0

    i, j = 0, calibration_length-1

    for pos in range(0, calibration_length):
        if messed_calibration_line[pos].isnumeric():
            i = pos
            break

    for pos in range(calibration_length-1, i-1, -1):
        if messed_calibration_line[pos].isnumeric():
            j = pos
            break
    try:
        left_number = int(messed_calibration_line[i])
        rigth_number = int(messed_calibration_line[j])
        return int(str(left_number)+str(rigth_number))
    except ValueError as e:
        print(e)
        return 0


def get_calibration_value_valid_string_as_number(messed_calibration_line: str):
    calibration_length = len(messed_calibration_line)

    if calibration_length < 2:
        return 0

    i: int
    j: int

    current_number_string: str = ""

    for pos in range(0, calibration_length):
        current_number_string += messed_calibration_line[pos]
        if messed_calibration_line[pos].isnumeric():
            i = messed_calibration_line[pos]
            break

        i = next((x for x in valid_numbers_from_string
                 if x in current_number_string), None)
        if i:
            i = valid_numbers_from_string[i]
            break

    current_number_string: str = ""

    for pos in range(calibration_length-1, -1, -1):
        current_number_string = messed_calibration_line[pos] + \
            current_number_string
        if messed_calibration_line[pos].isnumeric():
            j = messed_calibration_line[pos]
            break

        j = next((x for x in valid_numbers_from_string
                 if x in current_number_string), None)
        if j:
            j = valid_numbers_from_string[j]
            break

    return int(str(i)+str(j))


get_calibration_value_of_problem: dict = {

    FIRST_ANSWER: get_calibration_value,
    SECOND_ANSWER: get_calibration_value_valid_string_as_number,
}

valid_numbers_from_string: dict = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


def sum_calibration_values(mode: int):

    sum_total_calibrations = 0

    with open('01/input_01.txt', mode='r', encoding='utf-8') as calibration_file:
    #with open('prueba.txt', mode='r', encoding='utf-8') as calibration_file:

        line: str = calibration_file.readline()

        while line:
            sum_total_calibrations += get_calibration_value_of_problem[mode](
                line.strip())

            line = calibration_file.readline()

    return sum_total_calibrations


if __name__ == "__main__":
    print(f"answer 1 = {sum_calibration_values(FIRST_ANSWER)}")
    print(f"answer 2 = {sum_calibration_values(SECOND_ANSWER)}")
