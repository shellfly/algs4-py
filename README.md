[![PyPI version](https://badge.fury.io/py/algs4.svg)](https://badge.fury.io/py/algs4)

## Overview

This repository contains the Python source code for the algorithms in the textbook
<a href = "http://amzn.to/13VNJi7">Algorithms, 4th Edition</a> by Robert Sedgewick and Kevin Wayne.

The official Java source code is <a href="https://github.com/kevin-wayne/algs4">here</a>.

## Goals

Make a Python implementation of the library so that a Python programmer can follow this book easily or prefer to demonstrate the algorithms using Python.

Try to keep the interface and variable name consistent with the original book while writing idiomatic Python code.

## Install

```sh
pip install algs4
```

```python
from algs4.stack import Stack
```

## Index

* 1 FUNDAMENTALS

  * [Bag](algs4/bag.py)
  * [Queue](algs4/queue.py)
  * [Stack](algs4/stack.py)
  * [UnionFind](algs4/uf.py)

* 2 SORTING

  * [Selection](algs4/selection.py)
  * [Insertion](algs4/insertion.py)
  * [Shell](algs4/shell.py)
  * [Merge](algs4/merge.py)
  * [Quick](algs4/quick.py)
  * [Quick3Way](algs4/quick_3way.py)
  * [MaxPQ](algs4/max_pq.py)
  * [TopM](algs4/top_m.py)
  * [IndexMinPQ](algs4/index_min_pq.py)
  * [Multiway](algs4/multiway.py)
  * [Heap](algs4/heap.py)

* 3 SEARCHING

  * [FrequencyCounter](algs4/frequency_counter.py)
  * [SequentialSearchST](algs4/sequential_search_st.py)
  * [BinarySearchST](algs4/binary_search_st.py)
  * [BST](algs4/bst.py)
  * [RedBlackBST](algs4/red_black_bst.py)
  * [SeparateChainingHashST](algs4/separate_chaining_hash_st.py)
  * [LinearProbingHashST](algs4/linear_probing_hash_st.py)

* 4 GRAPHS
  * Graph
    * [Graph](algs4/graph.py)
    * [DepthFirstSearch](algs4/depth_first_search.py)
    * [DepthFirstPaths](algs4/depth_first_paths.py)
    * [BreadthFirstPaths](algs4/breadth_first_paths.py)
    * [CC](algs4/cc.py)
    * [Cycle](algs4/cycle.py)
    * [SymbolGraph](algs4/symbol_graph.py)
    * [DegreesOfSeparation](algs4/degrees_of_separation.py)
  * Digraph
    * [Digraph](algs4/digraph.py)
    * [DirectedDFS](algs4/directed_dfs.py)
    * [DirectedCycle](algs4/directed_cycle.py)
    * [DepthFirstOrder](algs4/depth_first_order.py)
    * [Topological](algs4/topological.py)
    * [KosarajuSCC](algs4/kosaraju_scc.py)
  * MST
    * [EdgeWeightedGraph](algs4/edge_weighted_graph.py)
    * [LazyPrimMST](algs4/lazy_prim_mst.py)
    * [PrimMST](algs4/prim_mst.py)
    * [KruskalMST](algs4/kruskal_mst.py)
  * Shortest Paths
    * [EdgeWeightedDigraph](algs4/edge_weighted_digraph.py)
    * [DijkstraSP](algs4/dijkstra_sp.py)
    * [AcyclicSP](algs4/acyclic_sp.py)
    * [BellmanFordSP](algs4/bellman_ford_sp.py)

* 5 STRING
  * [LSD](algs4/lsd.py)
  * [MSD](algs4/msd.py)
  * [Quick3string](algs4/quick3_string.py)
  * [TrieST](algs4/trie_st.py)
  * [TST](algs4/tst.py)
  * [KMP](algs4/kmp.py)
  * [NFA](algs4/nfa.py)
  * [Huffman](algs4/huffman.py)
  * [LZW](algs4/lzw.py)

## License

This code is released under MIT.

## Contribute to this repository

Issue reports and code fixes are welcome. please follow the same style as the code in the repository and add test for your
code.

[contributing guide](contributing.md)