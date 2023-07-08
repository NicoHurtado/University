import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;

public class Analysis {
    String File_without_weights = "countriesBFS.txt";
    String File = "countries.txt";
    String source = "Germany";
    int [] ExecutionTimes = new int[4];

    public void RunAnalysis() {
        // Sin pesos
        BFS bfs = new BFS(File_without_weights);
        long startTime = System.currentTimeMillis(); // Inicio
        bfs.computeDistances(source);
        long endTime = System.currentTimeMillis();  // Fin
        long bfsExecutionTime = endTime - startTime;
        ExecutionTimes[0] = (int) bfsExecutionTime;
        System.out.println("Tiempo de ejecución de BFS: " + bfsExecutionTime + " milisegundos");

        // Con pesos
        BellmanFordAlgorithm bellmanFord = new BellmanFordAlgorithm();
        startTime = System.currentTimeMillis(); // Inicio
        bellmanFord.RunBellMan(File, source);
        endTime = System.currentTimeMillis(); // Fin
        long bellmanFordExecutionTime = endTime - startTime;
        ExecutionTimes[1] = (int) bellmanFordExecutionTime; 
        System.out.println("Tiempo de ejecución de Bellman-Ford: " + bellmanFordExecutionTime + " milisegundos");

        DijkstraAlgorithm dijkstra = new DijkstraAlgorithm();
        startTime = System.currentTimeMillis(); // Inicio
        dijkstra.RunDijkstra(File, source);
        endTime = System.currentTimeMillis(); // Fin
        long dijkstraExecutionTime = endTime - startTime;
        ExecutionTimes[2] = (int) dijkstraExecutionTime;
        System.out.println("Tiempo de ejecución de Dijkstra: " + dijkstraExecutionTime + " milisegundos");

        FloydWarshallAlgorithm floydWarshall = new FloydWarshallAlgorithm();
        startTime = System.currentTimeMillis(); // Inicio
        floydWarshall.RunFloydWarshall(File);
        endTime = System.currentTimeMillis(); // Fin
        long floydWarshallExecutionTime = endTime - startTime;
        ExecutionTimes[3] = (int) floydWarshallExecutionTime;
        System.out.println("Tiempo de ejecución de Floyd-Warshall: " + floydWarshallExecutionTime + " milisegundos");
    }

    public static void main(String[] args) {
        Analysis analysis = new Analysis();
        analysis.RunAnalysis();

        String[] Algorithms = {"BFS", "Bellman-Ford", "Dijkstra", "Floyd-Warshall"};
        
        try {
            FileWriter fileWriter = new FileWriter("output.txt");
            BufferedWriter bufferedWriter = new BufferedWriter(fileWriter);

            // Escribir los tiempos de ejecución
            for (int i = 0; i < analysis.ExecutionTimes.length; i++) {
                String time = Integer.toString(analysis.ExecutionTimes[i]);
                bufferedWriter.write(time);
                bufferedWriter.newLine();
            }

            for (String algorithm : Algorithms) {
                bufferedWriter.write(algorithm);
                bufferedWriter.newLine();
            }

            // Cerrar el archivo
            bufferedWriter.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
