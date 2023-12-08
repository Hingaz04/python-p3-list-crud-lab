def create_an_empty_list():
    return []


def create_a_list():
    new_list = [1, 'apple', 3.14, True]
    return new_list


def add_element_to_end_of_list(input_list, element):

    input_list.append(element)
    return input_list


def add_element_to_start_of_list(input_list, element):
    input_list.insert(0, element)
    return input_list


def remove_element_from_end_of_list(input_list):
    input_list.pop()
    return input_list


def remove_element_from_start_of_list(input_list):
    del input_list[0]
    return input_list


def retrieve_first_element_from_list(input_list):
    return input_list[0]


def retrieve_element_from_index(input_list, index):
    return input_list[index]


def retrieve_last_element_from_list(input_list):
    return input_list[-1]
