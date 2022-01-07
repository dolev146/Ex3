import os
from unittest import TestCase
from Classes.GraphAlgo import GraphAlgo

gaA0 = GraphAlgo()
gaA2 = GraphAlgo()
gaA5 = GraphAlgo()


class RuntimeTest(TestCase):

    def setUp(self) -> None:
        global gaA0
        global gaA2
        global gaA5
        script_dir = os.path.dirname(__file__)
        rel_path = "../data_ex3/A0.json"
        abs_file_path = os.path.join(script_dir, rel_path)
        gaA0 = GraphAlgo()
        gaA0.load_from_json(abs_file_path)
        script_dir = os.path.dirname(__file__)
        rel_path = "../data_ex3/A2.json"
        abs_file_path = os.path.join(script_dir, rel_path)
        gaA2 = GraphAlgo()
        gaA2.load_from_json(abs_file_path)
        script_dir = os.path.dirname(__file__)
        rel_path = "../data_ex3/A5.json"
        abs_file_path = os.path.join(script_dir, rel_path)
        gaA5 = GraphAlgo()
        gaA5.load_from_json(abs_file_path)

    def test_tspA0(self):
        global gaA0
        gaA0.TSP([1, 4, 3, 9])

    def test_tspA2(self):
        global gaA2
        gaA2.TSP([1, 4, 3, 9])

    def test_tspA5(self):
        global gaA5
        gaA5.TSP([1, 4, 3, 9])

    def test_centerA0(self):
        global gaA0
        gaA0.centerPoint()
    def test_centerA2(self):
        global gaA2
        gaA2.centerPoint()

    def test_centerA5(self):
        global gaA5
        gaA5.centerPoint()

    def test_shortestpathA0(self):
        global gaA0
        gaA0.shortest_path(1,4)

    def test_shortestpathA2(self):
        global gaA2
        gaA2.shortest_path(1,4)

    def test_shortestpathA5(self):
        global gaA5
        gaA5.shortest_path(1,4)
