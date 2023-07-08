import java.io.BufferedReader;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.*;

public class FloydWarshallAlgorithm {
    private static final int INF = Integer.MAX_VALUE;

    private Map<String, Map<String, Integer>> graph;

    public void readGraphFromFile(String filePath) {
        graph = new HashMap<>();

        try (BufferedReader br = new BufferedReader(new FileReader(filePath))) {
            String line;
            while ((line = br.readLine()) != null) {
                String[] nodes = line.split(" ");
                String source = nodes[0];
                String destination = nodes[1];
                int weight = Integer.parseInt(nodes[2]);

                graph.putIfAbsent(source, new HashMap<>());
                graph.putIfAbsent(destination, new HashMap<>());

                graph.get(source).put(destination, weight);
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public Map<String, Map<String, Integer>> floydWarshall() {
        Map<String, Map<String, Integer>> distances = new HashMap<>(graph);

        for (String intermediate : graph.keySet()) {
            for (String source : graph.keySet()) {
                for (String destination : graph.keySet()) {
                    if (distances.get(source).get(intermediate) != null &&
                            distances.get(intermediate).get(destination) != null) {
                        int newDistance = distances.get(source).get(intermediate) + distances.get(intermediate).get(destination);

                        if (distances.get(source).get(destination) == null || newDistance < distances.get(source).get(destination)) {
                            distances.get(source).put(destination, newDistance);
                        }
                    }
                }
            }
        }

        return distances;
    }

    public void printShortestPaths(Map<String, Map<String, Integer>> distances) {
        try (FileWriter writer = new FileWriter("outputFloydW.txt")) {
            writer.write("Shortest paths between all pairs of vertices:\n\n");

            for (String source : distances.keySet()) {
                for (String destination : distances.get(source).keySet()) {
                    int distance = distances.get(source).get(destination);
                    writer.write(source + " -> " + destination + ": " + distance + "\n");
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public static void main(String[] args) {
        FloydWarshallAlgorithm floydWarshall = new FloydWarshallAlgorithm();
        floydWarshall.readGraphFromFile("countries.txt");
        Map<String, Map<String, Integer>> distances = floydWarshall.floydWarshall();
        floydWarshall.printShortestPaths(distances);
    }

    public void RunFloydWarshall(String file) {
        FloydWarshallAlgorithm floydWarshall = new FloydWarshallAlgorithm();
        floydWarshall.readGraphFromFile(file);

        Map<String, Map<String, Integer>> distances = floydWarshall.floydWarshall();
        
    }
}
