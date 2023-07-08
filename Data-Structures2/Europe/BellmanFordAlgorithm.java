import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.*;

public class BellmanFordAlgorithm {
    private static final int INF = Integer.MAX_VALUE / 2;

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

    public Map<String, Integer> bellmanFord(String source) {
        Map<String, Integer> distances = new HashMap<>();
        Map<String, String> previousNodes = new HashMap<>();

        for (String vertex : graph.keySet()) {
            distances.put(vertex, INF);
        }
        distances.put(source, 0);

        
        for (int i = 0; i < graph.size() - 1; i++) {
            for (String vertex : graph.keySet()) {
                List<Edge> neighbors = graph.get(vertex);
                if (neighbors == null) {
                    continue;
                }
                for (Edge neighbor : neighbors) {
                    String nextVertex = neighbor.destination;
                    int nextDistance = distances.get(vertex) + neighbor.weight;
                    if (nextDistance < distances.get(nextVertex) && nextDistance < INF) {
                        distances.put(nextVertex, nextDistance);
                        previousNodes.put(nextVertex, vertex);
                    }
                }
            }
        }

        for (String vertex : graph.keySet()) {
            List<Edge> neighbors = graph.get(vertex);
            if (neighbors == null) {
                continue;
            }
            for (Edge neighbor : neighbors) {
                String nextVertex = neighbor.destination;
                int nextDistance = distances.get(vertex) + neighbor.weight;
                if (nextDistance < distances.get(nextVertex) && nextDistance < INF) {
                    throw new RuntimeException("Negative cycle detected");
                }
            }
        }

        return distances;
    }

    public void printShortestPaths(String source, Map<String, Integer> distances, Map<String, String> previousNodes) {
        System.out.println("Shortest paths from " + source + ":");

        for (Map.Entry<String, Integer> entry : distances.entrySet()) {
            String destination = entry.getKey();
            int distance = entry.getValue();

            if (distance == INF) {
                System.out.println("No path to vertex " + destination);
            } else {
                List<String> path = getPath(source, destination, previousNodes);
                System.out.println(destination + ": " + " Distance: " + distance);
            }
        }
    }

    private List<String> getPath(String source, String destination, Map<String, String> previousNodes) {
        List<String> path = new ArrayList<>();
        String current = destination;
        while (current != null && !current.equals(source)) {
            path.add(0, current);
            current = previousNodes.get(current);
        }
        path.add(0, source);
        return path;
    }

    public static void main(String[] args) {
        BellmanFordAlgorithm bellmanFord = new BellmanFordAlgorithm();
        bellmanFord.readGraphFromFile("countries.txt");

        String sourceNode = "SanMarino";
        Map<String, Integer> distances = bellmanFord.bellmanFord(sourceNode);

        bellmanFord.printShortestPaths(sourceNode, distances, new HashMap<>());
    }

    public void RunBellMan(String file, String source) {
        BellmanFordAlgorithm bellmanFord = new BellmanFordAlgorithm();
        bellmanFord.readGraphFromFile(file);

        Map<String, Integer> distances = bellmanFord.bellmanFord(source);
    }

    
}
