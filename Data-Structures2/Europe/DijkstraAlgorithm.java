import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.*;

public class DijkstraAlgorithm {
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
        DijkstraAlgorithm dijkstra = new DijkstraAlgorithm();
        dijkstra.readGraphFromFile("countries.txt");

        String sourceNode = "Spain";
        Map<String, Integer> distances = dijkstra.dijkstra(sourceNode);

        dijkstra.printShortestPaths(sourceNode, distances, new HashMap<>());
    }

    public void RunDijkstra(String fileName, String source) {
        DijkstraAlgorithm dijkstra = new DijkstraAlgorithm();
        dijkstra.readGraphFromFile(fileName);

        Map<String, Integer> distances = dijkstra.dijkstra(source);

    }
}
