import java.io.File;
import java.io.IOException;
import java.util.*;

public class BFS {

    public static final int WHITE = 0;
    public static final int GRAY = 1;
    public static final int BLACK = 2;

    private AdjacencyList al;
    private Queue<BFNode> queue;
    private HashMap<String, BFNode> vertices;

    public BFS(String fileName) {
        al = new AdjacencyList(fileName);
        vertices = new HashMap<>();
    }

    public String toString() {
        StringBuilder sb = new StringBuilder();
        for (BFNode node : vertices.values()) {
            sb.append(node.country).append(" distance: ").append(node.distance).append("\n");
        }
        return sb.toString();
    }

    public void computeDistances(String source) {
        for (String vertex : al.graph.keySet()) {
            vertices.put(vertex, new BFNode(vertex));
        }

        queue = new LinkedList<>();
        BFNode sourceNode = vertices.get(source);
        sourceNode.color = GRAY;
        sourceNode.distance = 0;
        queue.add(sourceNode);

        while (!queue.isEmpty()) {
            BFNode u = queue.remove();
            LinkedList<String> neighbors = al.graph.getOrDefault(u.country, new LinkedList<>());
            for (String neighbor : neighbors) {
                BFNode v = vertices.get(neighbor);
                if (v.color == WHITE) {
                    v.color = GRAY;
                    v.distance = u.distance + 1;
                    v.pi = u.country;
                    queue.add(v);
                }
            }
            u.color = BLACK;
        }
    }

    public static void main(String[] args) {
        BFS bfs = new BFS("countriesBFS.txt");
        String source = "Germany";
        bfs.computeDistances(source);
        System.out.println("\n");
        System.out.println("Minimum Distances (Minimum Jumps between countries) From: " + source + '\n');
        System.out.println(bfs);
    }
}

class BFNode {
    public String country;
    public int color;
    public int distance;
    public String pi;

    public BFNode(String country) {
        this.country = country;
    }

    public String toString() {
        return "Number: " + country + " Distance: " + distance;
    }
}

class AdjacencyList {
    HashMap<String, LinkedList<String>> graph;
    int E;

    public AdjacencyList(String filename) {
        try {
            Scanner in = new Scanner(new File(filename));
            graph = new HashMap<>();
            E = 0;

            while (in.hasNext()) {
                String u = in.next();
                String v = in.next();
                addEdge(u, v);
                E++;
            }

            in.close();
        } catch (IOException e) {
            System.out.println("No se pudo abrir el archivo " + filename);
            System.exit(1);
        }
    }

    public void addEdge(String u, String v) {
        graph.putIfAbsent(u, new LinkedList<>());
        graph.putIfAbsent(v, new LinkedList<>());
        graph.get(u).add(v);
    }

    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append("Number of vertices: ").append(graph.size()).append(" Number of edges: ").append(E).append("\n");

        for (String u : graph.keySet()) {
            sb.append(u).append(" ----> ");
            for (String v : graph.get(u)) {
                sb.append(v).append(" -> ");
            }
            sb.append("\n");
        }

        return sb.toString();
    }
}