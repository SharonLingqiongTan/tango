This is a python implementation of Tango Tree.
======== PART I FUNCTIONS ==========
1. tango.py
This file contains TangoTree class with following functions:

## access(key)
Access a node with given key.
Update preferred path during accessing.

## cut(splayTree, node)
Cut off all nodes with depth > than a given node y, simulated by cutting off all nodes with keys in [min(y), max(y)] in y's subtree.

## findMinMaxInSuc(node)
Helper function for cut, return min and max value in subtree y.

## join(S1, S2, x1, x2)
Join two preferred path, used in cut function.

2. splay.py
** Important ** 
This file refers to https://github.com/anoopj/pysplay
I added join(), split(), traversal_test() on the basis of it and made some adaption to other functions.
***************

This file contains SplayTree class with following functions:

## insert(node)
Insert a node to splay tree. Adapted from original version.

## findMin()
Find min value in splay tree.

## findMax()
Find max value in splay tree.

## find()
Find a given key in splay tree.

## splay()
Do splay for splay tree.

## join()
Join two splay tree into one. One has smaller nodes and one has larger nodes.

## split(x, inclusive)
Split the splay tree by given key. Inclusive means whether keep the root or not during split.

## traversal_test()
Use for test tree structure.

## remove() and isEmply()
Leave for future use.

3. treenode.py
Define node in this tango tree model.


4. BST.py
Use to initialize tango tree representative tree.


5. test_tango.py
Use to test tango tree. Custom test case.

======== PART II USER MANUAL ==========
1. Install python
2. Open command line, go to tango directory
3. run "python test_tango.py" in command line
4. You can change test case in test_tango.py

======== PART III FAILED SOME TEST CASES ==========

This program may fail in some test cases. Please see testcase 3 in 1000 nodes and testcase 4 in 10 nodes.


