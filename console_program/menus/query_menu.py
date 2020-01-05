from console_program.menus.vector_menu import open_vector_menu


def open_query_menu(kd_tree):
    open_vector_menu(kd_tree, handle_vector)


def handle_vector(kd_tree, vector):
    if not kd_tree.data:
        print("No vectors added for querying")
        return

    nearest_vector, _ = kd_tree.search_nn(vector)
    print(f"Nearest vector is: {nearest_vector.data}")
