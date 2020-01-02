from console_program.exceptions import InvalidVector


BACK_OPTION = 'back'


def open_vector_menu(kd_tree, handle_vector_cb):
    dimensions = kd_tree.dimensions
    _print_menu_instructions(dimensions)

    while True:
        user_input = _get_user_input()
        if user_input == BACK_OPTION:
            break

        try:
            vector = _validate_and_parse_vector(user_input, dimensions)
            handle_vector_cb(kd_tree, vector)
        except InvalidVector as e:
            print(e)


def _get_user_input():
    return input("")


def _print_menu_instructions(dimensions):
    example_vector = _generate_vector_example(dimensions)
    print(
        '===============\n'
        f'Please add numeric vectors of size {dimensions}, e.g. {example_vector}\n'
        f'{BACK_OPTION} - return to main menu\n'
        '===============\n'
    )


def _validate_and_parse_vector(user_input, expected_dimensions):
    try:
        vector = [float(val) for val in user_input.split(',')]
        if len(vector) != expected_dimensions:
            raise InvalidVector(f"Vector is not of size {expected_dimensions}")

        return vector

    except ValueError:
        raise InvalidVector("Vector is not numeric!")


def _generate_vector_example(dimensions):
    return ','.join([str(val) for val in (range(0, dimensions))])
