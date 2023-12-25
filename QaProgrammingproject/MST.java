import java.util.Scanner;
public class MST {
    // Instance variables
    private int[][] costMatrix;
    private int[] visitedNodes;
    private int totalWeight;
    // Constructor to init  variables based on the number of nodes
    public MST(int numberOfNodes) {
        costMatrix = new int[numberOfNodes + 1][numberOfNodes + 1];
        visitedNodes = new int[numberOfNodes + 1];
        totalWeight = 0;
    }
    // Method to calculate the Minimum Spanning Tree using Prim's algorithm
    public void calculateMinimumSpanningTree(int numberOfNodes) {
        int edgeCount = 1;
        int source = 0, destination = 0;
        // Loop until all edges are included in the MST
        while (edgeCount < numberOfNodes) {
            int minWeight = Integer.MAX_VALUE;
            // Iterate through the cost matrix to find the minimum weight edge
            for (int i = 1; i <= numberOfNodes; i++) {
                for (int j = 1; j <= numberOfNodes; j++) {
                    // Check if the current edge weight is smaller than the minimum
                    if (costMatrix[i][j] < minWeight && visitedNodes[i] != 0) {
                        minWeight = costMatrix[i][j];
                        source = i;
                        destination = j;
                    }
                }
            }
            // If the source or destination node is not visited, include the edge in the MST
            if (visitedNodes[source] == 0 || visitedNodes[destination] == 0) {
                System.out.println(source + "\t\t" + destination + "\t\t" + minWeight);
                edgeCount++;
                totalWeight += minWeight;
                visitedNodes[destination] = 1;
                costMatrix[source][destination] = costMatrix[destination][source] = Integer.MAX_VALUE;
            }
        }
        // Display the total weight of the Minimum Spanning Tree
        System.out.println("The total weight of the spanning tree is " + totalWeight);
    }
    public static void main(String[] args) {
            Scanner input = new Scanner(System.in);
            System.out.println("Enter the number of nodes:");
            int numberOfNodes = input.nextInt();
            // Init an instance of MinimumSpanningTree
            MST mst = new MST(numberOfNodes);
            // User input for the cost matrix
            System.out.println("Enter the cost matrix weights:");
            for (int i = 1; i <= numberOfNodes; i++) {
                for (int j = 1; j <= numberOfNodes; j++) {
                    mst.costMatrix[i][j] = input.nextInt();
                    if (mst.costMatrix[i][j] == 0) {
                        mst.costMatrix[i][j] = Integer.MAX_VALUE;
                    }
                }
            }
            // Init the first node as visited and calc the MST
            mst.visitedNodes[1] = 1;
            mst.calculateMinimumSpanningTree(numberOfNodes);
    }
}