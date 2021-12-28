
# Ex3 OOP Ariel Univercity

![image](https://user-images.githubusercontent.com/62290677/147416924-927bcdcb-8cf6-4b95-82a0-ef475f122183.png)

the project is about implementing graphs algorithm's: 

- TSP()
- ShortestPath()
- Center()

The software also has a gui to give easier use.


## Run Locally

Clone the project

```bash
  git clone https://github.com/dolev146/Ex3.git
```

Go to the project directory

```bash
  cd Ex3
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Start the Gui

```bash
windows
    python Ex3.py ./data/A0.json

mac
    python3 Ex3.py ./data/A0.json
```

please watch the demo to know the specific input sytax.
## Gui Demo

![image](https://user-images.githubusercontent.com/62290677/147415610-540a000c-b81d-4b5d-a52a-782112ef570f.png)
![image](https://user-images.githubusercontent.com/62290677/147415622-e51f93a0-b78f-45e1-aec6-41340b55e5a2.png)
![image](https://user-images.githubusercontent.com/62290677/147415636-1a498b7e-6426-49c1-ac71-a182c3b1bd14.png)
**to use the tsp input box for example you will need to**
- insert the id numbers of the node seperated by comma (' , ')
- press the Return button on the keyboard AKA Enter button

**watch the YouTube video explaining everything**
[![IMAGE ALT TEXT HERE](https://user-images.githubusercontent.com/62290677/147417843-89756c59-f705-4bda-b28d-c2324b4f7161.png)](https://www.youtube.com/watch?v=rk7QZly6sPE)

### Test our code

![image](https://user-images.githubusercontent.com/62290677/147556840-a31223db-600a-421b-b621-d58a03e749df.png)

just follow the instructions in the Ex3.py , how to disable the gui and print the results you wish to check

## Lessons Learned

we learned to work as a team with git and github.
we learend that in order to work better we first need to to plan
before we start writing the code. 
## Unit Tests

iside the [Tests directory](https://github.com/dolev146/Ex3/tree/main/Tests) you can see all the tests

![image](https://user-images.githubusercontent.com/62290677/147417425-0c38ae67-cb5f-4efe-bcf3-974d0867d4ac.png)

![image](https://user-images.githubusercontent.com/62290677/147417448-e87d4741-0427-49af-aa41-5511010f7ad4.png)

## RunTime compare

![image](https://user-images.githubusercontent.com/62290677/147417470-b8eced3e-f98e-4c74-abb0-64e6553befa5.png)
and took the result from the terminal for example:

![image](https://user-images.githubusercontent.com/62290677/147417688-f04ecc5c-e5cc-4d6c-92ea-6fae3eed0f6e.png)

| comapre vs python     | table |
| ----------- | ----------- |
| ![image](https://user-images.githubusercontent.com/62290677/147417488-8c9dba7e-3e9e-4d24-9dde-a630725ea5fc.png)      | ![image](https://user-images.githubusercontent.com/62290677/147417549-6f459c83-7d12-40e8-b94c-4253f349d487.png) |
| ![image](https://user-images.githubusercontent.com/62290677/147417580-6a682fe1-9343-48ee-b314-77a83e10a4a0.png)   | ![image](https://user-images.githubusercontent.com/62290677/147417605-0bd88385-5e85-4a2c-94b5-0efc25c9c5e3.png)        |
| ![image](https://user-images.githubusercontent.com/62290677/147417617-f793c2b8-df47-40dd-9f35-0b2c46aaa296.png)   | ![image](https://user-images.githubusercontent.com/62290677/147417622-208cd026-4435-4e5a-975f-3190f7c43081.png)        |
| ![image](https://user-images.githubusercontent.com/62290677/147419000-45e3a2d2-55a0-4a34-b256-a53e265212e9.png) | ![image](https://user-images.githubusercontent.com/62290677/147419008-aec9558b-04d9-4922-8d00-534dd1d7376b.png) |
| ![image](https://user-images.githubusercontent.com/62290677/147419017-3bfef0e6-9b25-44c3-a380-9e19dce7bd3d.png) | ![image](https://user-images.githubusercontent.com/62290677/147419028-3d810803-a0c4-4751-b96d-322a57213b63.png) |

![image](https://user-images.githubusercontent.com/62290677/147501138-c1e7f5d3-04bf-435c-96ba-c9646dacb857.png)
windows 10 pro


### data structure 

the Graph captures the data in 4 Dictionaries . 
* dictionary for the nodes  - implementing editing nodes by their id in O(1)
* dictionary for the edges  - implementing editing edges by taking the sourse and destantion of the edge, and convert it to 1 string (```src_dest```) key that gives us the edge on O(1) and 2 other dictionaries for in and out edges.


### implemented classes 

* **CNode** - Node of graph. 
* **CEdge** - Edges of graph. 
* **DiGraph**  - implementing GraphInterface 
* **GraphAlgo** - implementing GraphAlgoInterface



### Algorithms functions 
 
* center - This functions return the Node Id that in the center of the graph (relative to the rest of the vertices) and his distance.In this function we use the dijkstra algorithm to caculte the length from node to the other nodes and this help us to find the center node(vertex).
 
* tsp - This function get list of nodes(vertex) Id's and return list of nodes Id's that present the path that pass in the nodes that we get and the overall distance,also the function return "good" path and not path that pass to mach vertex and visit vertex that not necessaries .We use shortest_path function to find the best path from node to node.

* shortestPath - This function get src and dest Id and return Node list of all the Nodes Id's that in the shortest path in the same order as they show up in the path.

* Plot graph - This function search in the init graph empty nodes  and fill them with random cordinates depending on the scale :
If the graph is made from empty nodes , the scale will be automatic else, the function will find the min and max nodes in the graph to get the scaling , and combined them .
If there is only 1 node in the graph with cordinates, the other new random nodes will be around him .



## classes functions

### CEdge class functions
* src
* dest
* w
* info

### CNode class functions
* id
* info 
* previous 
* length 
* rank 
* x
* y
* z


### DiGraph (implements Graph interface) class functions
* v_size
* e_size
* get_all_v
* all_in_edges_of_node
* all_out_edges_of_node()
* get_mc()
* add_edge(int node_id)
* add_node(int node_id)
* remove_node
* remove_edge

### GraphAlgo (implements GraphAlgoInterface) class functions 
* init
* get_graph
* shortest_path
* centerPoint
* TSP
* Plot graph
* save_to_json
* load_from_json

# UML

![new image](https://user-images.githubusercontent.com/62290677/147418549-2a09e887-b739-4b54-b736-de94b72482e8.png)


 

## Authors

- [@ Dolev Dublon](https://github.com/dolev146)
- [@ Daniel Zaken](https://github.com/daniel555666)
- [@ Yakov Khodorkovski](https://github.com/yakov103)

