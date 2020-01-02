from unittest import TestCase
from unittest.mock import patch, ANY
from console_program import __main__


class MainUnitTests(TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    @patch.object(__main__, "open_main_menu")
    @patch.object(__main__, "kdtree")
    def test_run_program(self, mock_kdtree, mock_open_main_menu):
        mock_vector_size = 4
        __main__.run_program(mock_vector_size)

        mock_kdtree.create.assert_called_once_with(dimensions=mock_vector_size)
        mock_open_main_menu.assert_called_once_with(ANY)
