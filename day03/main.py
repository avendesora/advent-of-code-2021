from statistics import median, mode

from helpers import read_input_as_2d_int_array, transpose_2d_array


def read_input(filename: str) -> list[list[int]]:
    return transpose_2d_array(read_input_as_2d_int_array(filename))


def get_gamma_and_epsilon_rates(input_2d_array: list[list[int]]) -> tuple[int, int]:
    gamma_rate_string: str = ""
    epsilon_rate_string: str = ""

    for bit_array in input_2d_array:
        most_common = mode(bit_array)
        gamma_rate_string += str(most_common)
        epsilon_rate_string += str(abs(most_common - 1))

    return int(gamma_rate_string, 2), int(epsilon_rate_string, 2)


def get_power_consumption(gamma: int, epsilon: int) -> int:
    return gamma * epsilon


def get_oxygen_generator_rating(input_2d_array: list[list[int]]) -> int:
    filtered_data: list[list[int]] = input_2d_array.copy()
    temp_data: list[list[int]] = []

    for counter in range(len(filtered_data)):
        bit_array = filtered_data[counter]
        most_common = 1 if median(bit_array) == 0.5 else mode(bit_array)
        row_index: int = 0

        for bit in bit_array:
            if bit == most_common:
                for column_index in range(len(filtered_data)):
                    value: int = filtered_data[column_index][row_index]

                    if len(temp_data) <= column_index:
                        temp_data.append([value])
                    else:
                        temp_data[column_index].append(value)

            row_index += 1

        filtered_data = temp_data.copy()
        temp_data = []

    return int("".join([str(column[0]) for column in filtered_data]), 2)


def get_co2_scrubber_rating(input_2d_array: list[list[int]]) -> int:
    filtered_data: list[list[int]] = input_2d_array.copy()
    temp_data: list[list[int]] = []

    for counter in range(len(filtered_data)):
        bit_array = filtered_data[counter]
        most_common = 0 if median(bit_array) == 0.5 else abs(mode(bit_array) - 1)
        row_index: int = 0

        for bit in bit_array:
            if bit == most_common:
                for column_index in range(len(filtered_data)):
                    value: int = filtered_data[column_index][row_index]

                    if len(temp_data) <= column_index:
                        temp_data.append([value])
                    else:
                        temp_data[column_index].append(value)

            row_index += 1

        filtered_data = temp_data.copy()
        temp_data = []

        if len(filtered_data[0]) == 1:
            break

    return int("".join([str(column[0]) for column in filtered_data]), 2)


def get_life_support_rating(oxygen_generator: int, co2_scrubber: int) -> int:
    return oxygen_generator * co2_scrubber


if __name__ == "__main__":
    binary_data = read_input("input.txt")

    # Part One
    gamma_rate, epsilon_rate = get_gamma_and_epsilon_rates(binary_data)
    power_consumption = get_power_consumption(gamma_rate, epsilon_rate)
    print(f"The power consumption of the submarine is {power_consumption}.")

    # Part Two
    oxygen_generator_rating = get_oxygen_generator_rating(binary_data)
    co2_scrubber_rating = get_co2_scrubber_rating(binary_data)
    life_support_rating = get_life_support_rating(
        oxygen_generator_rating, co2_scrubber_rating
    )
    print(f"The life support rating of the submarine is {life_support_rating}.")
