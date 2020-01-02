import io
import unittest
import kdtree

from unittest import TestCase
from unittest.mock import patch, Mock
from console_program.exceptions import InvalidVector
from console_program.menus import vector_menu


class VectorMenuUnitTests(TestCase):
    def setUp(self):
        self.mock_vector_size = 4
        self.mock_vector = [1, 2, 3, 4]
        self.mock_kd_tree = kdtree.create(dimensions=self.mock_vector_size)

    def tearDown(self):
        pass

    def test_generate_vector_example(self):
        vector = vector_menu._generate_vector_example(self.mock_vector_size)
        expected_vector = "0,1,2,3"

        self.assertEqual(expected_vector, vector)

    def test_validate_and_parse_vector_valid(self):
        tests = [
            ["30", 1, [30]],
            ["5.8,20,7.9", 3, [5.8, 20, 7.9]],
            ["1,2,3,4", 4, [1, 2, 3, 4]],
         ]
        for user_input, dimensions, expected_result in tests:
            with self.subTest():
                result = vector_menu._validate_and_parse_vector(user_input, dimensions)
                self.assertEqual(expected_result, result)

    def test_validate_and_parse_vector_invalid(self):
        tests = [
            ["", 4],
            ["20", 3],
            ["20,10", 3],
            ["hi", 1],
            ["1,2b", 2],
         ]
        for user_input, dimensions in tests:
            with self.subTest():
                with self.assertRaises(InvalidVector):
                    vector_menu._validate_and_parse_vector(user_input, dimensions)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_print_menu_instructions(self, mock_stdout):
        vector_menu._print_menu_instructions(self.mock_vector_size)
        value = mock_stdout.getvalue()
        expected_value = '===============\n'\
                         'Please add numeric vectors of size 4, e.g. 0,1,2,3\n'\
                         'back - return to main menu\n'\
                         '===============\n'\
                         '\n'
        self.assertEqual(value, expected_value)

    @patch.object(vector_menu, "_print_menu_instructions")
    @patch.object(vector_menu, "_get_user_input")
    def test_open_vector_menu(self, mock_get_user_input, mock_print_menu_instructions):
        handle_vector_cb = Mock()
        mock_get_user_input.side_effect = ['1,2,3,4', 'back']
        vector_menu.open_vector_menu(self.mock_kd_tree, handle_vector_cb)

        mock_print_menu_instructions.assert_called_once_with(self.mock_vector_size)
        handle_vector_cb.assert_called_once_with(self.mock_kd_tree, [1, 2, 3, 4])
