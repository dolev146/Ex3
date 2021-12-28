import sys

from Classes.GraphAlgo import GraphAlgo
from gui import constants
from gui.newcontrol import GUI

if __name__ == '__main__':
    if len(sys.argv) > 1:
        print("OK")
        json_file = sys.argv[1]
        constants.ga.load_from_json(file_name=json_file)
        GUI()
    else:
        print("no json path added ")
        print("exit program")
        sys.exit()
    # if u mant tot test outputs on terminal just comment the above lines, to stop the gui
    # and use the example bellow
    # ga = GraphAlgo()
    # ga.load_from_json("./data/A0.json")
    # print(ga.centerPoint())
    # print(ga.TSP([7, 5, 3]))
    # print(ga.shortest_path(1, 5))
