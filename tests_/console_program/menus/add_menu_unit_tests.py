import kdtree

from unittest import TestCase
from unittest.mock import patch
from console_program.menus import add_menu
from copy import deepcopy


class AddMenuUnitTests(TestCase):
    def setUp(self):
        mock_vector_size = 4
        self.mock_vector = [1, 2, 3, 4]
        self.mock_kd_tree = kdtree.create(dimensions=mock_vector_size)

    def tearDown(self):
        pass

    @patch.object(add_menu, "open_vector_menu")
    def test_open_add_menu(self, mock_open_vector_menu):
        add_menu.open_add_menu(self.mock_kd_tree)

        mock_open_vector_menu.assert_called_once_with(self.mock_kd_tree, add_menu.handle_vector)

    def test_handle_vector(self):
        test_tree = deepcopy(self.mock_kd_tree)
        test_tree.add(self.mock_vector)

        add_menu.handle_vector(self.mock_kd_tree, self.mock_vector)

        self.assertEqual(test_tree, self.mock_kd_tree)
