import io
import unittest
import kdtree

from unittest import TestCase
from unittest.mock import patch, Mock
from console_program.menus import main_menu


class MainMenuUnitTests(TestCase):
    def setUp(self):
        self.mock_vector_size = 4
        self.mock_vector = [1, 2, 3, 4]
        self.mock_kd_tree = kdtree.create(dimensions=self.mock_vector_size)

    def tearDown(self):
        pass

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_print_menu_instructions(self, mock_stdout):
        main_menu.print_menu_instructions()
        value = mock_stdout.getvalue()
        expected_value = '===============\n' \
                         'Please select one of the following options:\n' \
                         'add - add vectors\n' \
                         'query - query vectors\n'\
                         'quit - quit program\n' \
                         '===============\n' \
                         '\n'
        self.assertEqual(value, expected_value)

    @patch.object(main_menu, "print_menu_instructions")
    @patch.object(main_menu, "get_user_input")
    @patch.object(main_menu, "open_add_menu")
    @patch.object(main_menu, "open_query_menu")
    def test_open_main_menu(self, mock_open_query_menu, mock_open_add_menu, mock_get_user_input, mock_print_menu_instructions):
        mock_get_user_input.side_effect = ['add', 'query', 'quit']
        main_menu.open_main_menu(self.mock_kd_tree)

        mock_print_menu_instructions.assert_called_with()
        mock_open_add_menu.assert_called_once_with(self.mock_kd_tree)
        mock_open_query_menu.assert_called_once_with(self.mock_kd_tree)