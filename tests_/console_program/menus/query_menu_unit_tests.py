import io
import unittest
import kdtree

from unittest import TestCase
from unittest.mock import patch
from console_program.menus import query_menu


class QueryMenuUnitTests(TestCase):
    def setUp(self):
        mock_vector_size = 4
        self.mock_vector = [4, 0, 0, 0]
        self.mock_kd_tree = kdtree.create(dimensions=mock_vector_size)

    def tearDown(self):
        pass

    @patch.object(query_menu, "open_vector_menu")
    def test_open_add_menu(self, mock_open_vector_menu):
        query_menu.open_query_menu(self.mock_kd_tree)

        mock_open_vector_menu.assert_called_once_with(self.mock_kd_tree, query_menu.handle_vector)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_handle_vector_empty_tree(self, mock_stdout):
        query_menu.handle_vector(self.mock_kd_tree, self.mock_vector)
        self.assertEqual(mock_stdout.getvalue(), "No vectors added for querying\n")

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_handle_vector_tree_with_values(self, mock_stdout):
        self.mock_kd_tree.add([1, 0, 0, 0])
        self.mock_kd_tree.add([0, 1, 0, 0])
        self.mock_kd_tree.add([0, 0, 1, 0])
        self.mock_kd_tree.add([0, 0, 0, 1])

        query_menu.handle_vector(self.mock_kd_tree, self.mock_vector)
        self.assertEqual(mock_stdout.getvalue(), "Nearest vector is: [1, 0, 0, 0]\n")
