import argparse

from cached_kd_tree import CachedKdTree
from console_program.menus.main_menu import open_main_menu


def run_program(vector_size: int):
    kd_tree = CachedKdTree(dimensions=vector_size)
    open_main_menu(kd_tree)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--vector_size")

    args = parser.parse_args()
    vec_size = args.vector_size
    if not vec_size or not vec_size.isdigit():
        print("Usage: --vector_size <integer>")
    else:
        run_program(int(vec_size))

