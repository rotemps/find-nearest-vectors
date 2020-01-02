from console_program.menus.vector_menu import open_vector_menu


def open_add_menu(kd_tree):
    open_vector_menu(kd_tree, handle_vector)


def handle_vector(kd_tree, vector):
    kd_tree.add(vector)
