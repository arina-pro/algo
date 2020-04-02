using System;
using System.Collections.Generic;
using System.Text;

namespace AlgorithmsOnGraphs {
    public class Graph {

        public List<Int>[] AdjacencyList;

        public Graph(List<Int>[] adjacencyList) {
            AdjacencyList = adjacencyList;
        }
        public Graph Factorize(Graph graph) {
            var counterArray = new int[graph.AdjacencyList];
            var factorizedGraph = graph;
            return factorizedGraph;
        }
    }
}
