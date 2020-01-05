from functools import lru_cache

import kdtree


class CachedKdTree:
    def __init__(self, dimensions):
        self._kd_tree = kdtree.create(dimensions=dimensions)

    def add(self, vector):
        self._kd_tree.add(vector)

    def search_nn(self, vector):
        return self._cached_search_nn(tuple(vector))

    @lru_cache(maxsize=None)
    def _cached_search_nn(self, vector_tuple):
        return self._kd_tree.search_nn(vector_tuple)

    @property
    def dimensions(self):
        return self._kd_tree.dimensions

    @property
    def data(self):
        return self._kd_tree.data
