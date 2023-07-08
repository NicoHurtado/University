import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.*;

public class Dijkstra {
    private static final int INF = Integer.MAX_VALUE;

    private Map<String, List<Edge>> graph;

    private class Edge {
        String destination;
        int weight;

        Edge(String destination, int weight) {
            this.destination = destination;
            this.weight = weight;
        }
    }

    public void readGraphFromFile(String filePath) {
        graph = new HashMap<>();

        try (BufferedReader br = new BufferedReader(new FileReader(filePath))) {
            String line;
            while ((line = br.readLine()) != null) {
                String[] nodes = line.split(" ");
                String source = nodes[0];
                String destination = nodes[1];
                int weight = Integer.parseInt(nodes[2]);

                if (!graph.containsKey(source)) {
                    graph.put(source, new ArrayList<>());
                }
                graph.get(source).add(new Edge(destination, weight));
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public Map<String, Integer> dijkstra(String source) {
        Map<String, Integer> distances = new HashMap<>();
        Map<String, String> previousNodes = new HashMap<>();

        for (String vertex : graph.keySet()) {
            distances.put(vertex, INF);
        }
        distances.put(source, 0);

        PriorityQueue<Node> pq = new PriorityQueue<>();
        pq.offer(new Node(source, 0));

        while (!pq.isEmpty()) {
            Node currNode = pq.poll();
            String currVertex = currNode.vertex;
            int currDistance = currNode.distance;

            if (currDistance > distances.get(currVertex)) {
                continue;
            }

            List<Edge> neighbors = graph.get(currVertex);
            if (neighbors == null) {
                continue;
            }

            for (Edge neighbor : neighbors) {
                String nextVertex = neighbor.destination;
                int nextDistance = currDistance + neighbor.weight;

                if (nextDistance < distances.get(nextVertex)) {
                    distances.put(nextVertex, nextDistance);
                    previousNodes.put(nextVertex, currVertex);
                    pq.offer(new Node(nextVertex, nextDistance));
                }
            }
        }

        return distances;
    }

    public void printShortestPath(String source, String destination, Map<String, Integer> distances, Map<String, String> previousNodes) {
        int distance = distances.get(destination);
    
        if (distance == INF) {
            System.out.println("No path from " + source + " to " + destination);
        } else {
            System.out.print(source + " to " + destination + ": ");
            List<String> path = new ArrayList<>();
    
            String current = destination;
            while (current != null) {
                path.add(current);
                current = previousNodes.get(current);
            }
    
            Collections.reverse(path);
    
            for (int i = 0; i < path.size() - 1; i++) {
                System.out.print(path.get(i) + " -> ");
            }
    
            System.out.println(destination);
            System.out.println("Distance: " + distance);
        }
    }
    

    private class Node implements Comparable<Node> {
        String vertex;
        int distance;

        Node(String vertex, int distance) {
            this.vertex = vertex;
            this.distance = distance;
        }

        @Override
        public int compareTo(Node other) {
            return Integer.compare(this.distance, other.distance);
        }
    }

    public static void main(String[] args) {
        Dijkstra dijkstra = new Dijkstra();
        dijkstra.readGraphFromFile("countries.txt");

        String sourceNode = "Germany";
        String destinationNode = "Russia";

        Map<String, Integer> distances = dijkstra.dijkstra(sourceNode);
        Map<String, String> previousNodes = new HashMap<>();
        dijkstra.printShortestPath(sourceNode, destinationNode, distances, previousNodes);
    }
}
