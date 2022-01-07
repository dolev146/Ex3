from unittest import TestCase
from Classes.GraphAlgo import GraphAlgo
import os
from math import inf


class TestGraphAlgo(TestCase):

    def test_load_from_json(self):
        script_dir = os.path.dirname(__file__)
        rel_path = "./data_ex3/short1.json"
        abs_file_path = os.path.join(script_dir, rel_path)
        ga = GraphAlgo()
        ga.load_from_json(abs_file_path)
        self.assertEqual(len(ga.get_graph().get_all_v()), 4)
        self.assertEqual(ga.get_graph().e_size(), 0)

    def test_save_to_json(self):
        """
        because of the problem with python that needs the absolute path if the file you
        try to open is in a directory that is not in the Which is not smaller than her in her hierarchy or neighbor
        in the location of the function activation
        we use the absolute path for the checks.
        ** update we learned to use os.path
        to fix that we will need to change the func but it will need to change the behave of te func
        but it will ruin the gui functionality
        """
        script_dir = os.path.dirname(__file__)
        rel_path = "./data_ex3/short1.json"
        abs_file_path = os.path.join(script_dir, rel_path)
        ga = GraphAlgo()
        ga.load_from_json(abs_file_path)
        ga.get_graph().remove_node(1)
        ga.save_to_json("save_to_json_func_test")
        a = 5
        # self.assertEqual(len(ga.get_graph().get_all_v()), 4)
        # self.assertEqual(ga.get_graph().e_size(), 0)

    def test_shortest_path(self):
        script_dir = os.path.dirname(__file__)
        rel_path = "./data_ex3/short1.json"
        abs_file_path = os.path.join(script_dir, rel_path)
        ga = GraphAlgo()
        ga.load_from_json(abs_file_path)
        cost, list_node = ga.shortest_path(1, 2)
        self.assertEqual(cost, inf)
        self.assertEqual(list_node, [])
        rel_path2 = "./data_ex3/short2.json"
        abs_file_path2 = os.path.join(script_dir, rel_path2)
        ga2 = GraphAlgo()
        ga2.load_from_json(abs_file_path2)
        cost2, list_node2 = ga2.shortest_path(0, 1)
        self.assertEqual(cost2, 1)
        self.assertEqual(list_node2, [0, 1])
        rel_path3 = "./data_ex3/short3.json"
        abs_file_path3 = os.path.join(script_dir, rel_path3)
        ga3 = GraphAlgo()
        ga3.load_from_json(abs_file_path3)
        cost3, list_node3 = ga3.shortest_path(0, 2)
        self.assertEqual(cost3, 2)
        self.assertEqual(list_node3, [0, 1, 2])

    def test_plot_graph(self):
        """
        because of the problem with python that needs the absolute path if the file you
        try to open is in a directory that is not in the Which is not smaller than her in her hierarchy or neighbor
        in the location of the function activation
        we use the absolute path for the checks.
        ** update we learned to use os.path to fix that
        """
        script_dir = os.path.dirname(__file__)
        rel_path = "./data_ex3/T1.json"
        abs_file_path = os.path.join(script_dir, rel_path)
        ga = GraphAlgo()
        ga.load_from_json(abs_file_path)
        ga.plot_graph()
        self.assertNotEqual(ga.get_graph().get_all_v().get(0).x, None)
        self.assertNotEqual(ga.get_graph().get_all_v().get(1).x, None)
        self.assertNotEqual(ga.get_graph().get_all_v().get(2).x, None)
        self.assertNotEqual(ga.get_graph().get_all_v().get(3).x, None)
        rel_path = "./data_ex3/T2.json"
        abs_file_path = os.path.join(script_dir, rel_path)
        ga.load_from_json(abs_file_path)
        ga.plot_graph()
        self.assertNotEqual(ga.get_graph().get_all_v().get(0).x, None)
        self.assertNotEqual(ga.get_graph().get_all_v().get(1).x, None)
        self.assertNotEqual(ga.get_graph().get_all_v().get(2).x, None)
        self.assertNotEqual(ga.get_graph().get_all_v().get(3).x, None)
        rel_path = "./data_ex3/T3.json"
        abs_file_path = os.path.join(script_dir, rel_path)
        ga.load_from_json(abs_file_path)
        ga.plot_graph()
        self.assertNotEqual(ga.get_graph().get_all_v().get(0).x, None)
        self.assertNotEqual(ga.get_graph().get_all_v().get(1).x, None)
        self.assertNotEqual(ga.get_graph().get_all_v().get(2).x, None)
        self.assertNotEqual(ga.get_graph().get_all_v().get(3).x, None)

    def test_TSP(self):
        script_dir = os.path.dirname(__file__)
        rel_path = "./data_ex3/tsp_test1.json"
        abs_file_path = os.path.join(script_dir, rel_path)
        ga = GraphAlgo()
        ga.load_from_json(abs_file_path)
        list_node ,cost  = ga.TSP([1, 2, 3])
        print(cost)
        print(list_node)
        self.assertEqual(2, 2)
        self.assertEqual(list_node, [1, 2, 3])

    def test_center(self):
        script_dir = os.path.dirname(__file__)
        rel_path = "./data_ex3/center_test1.json"
        abs_file_path = os.path.join(script_dir, rel_path)
        ga = GraphAlgo()
        ga.load_from_json(abs_file_path)
        list_node, cost = ga.centerPoint()
        print(cost)
        print(list_node)
        self.assertEqual(cost, 1)
        self.assertEqual(list_node, 0)
        rel_path2 = "./data_ex3/center_test2.json"
        abs_file_path2 = os.path.join(script_dir, rel_path2)
        ga2 = GraphAlgo()
        ga2.load_from_json(abs_file_path2)
        list_node2, cost2 = ga2.centerPoint()
        print(cost2)
        print(list_node2)
        self.assertEqual(cost2, 9223372036854775807)
        self.assertEqual(list_node2, -1)
        rel_path3 = "./data_ex3/center_test3.json"
        abs_file_path3 = os.path.join(script_dir, rel_path3)
        ga3 = GraphAlgo()
        ga3.load_from_json(abs_file_path3)
        list_node3, cost3 = ga3.centerPoint()
        print(cost3)
        print(list_node3)
        self.assertEqual(cost3, 3.0)
        self.assertEqual(list_node3, 0)
