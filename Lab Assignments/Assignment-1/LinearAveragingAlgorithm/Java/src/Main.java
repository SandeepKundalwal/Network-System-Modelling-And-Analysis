public class Main {
    public static void main(String[] args) {
        double initialStates[] = {1.00000, -1.00000, 1.00000, -1.00000, 1.00000};

        double completeGraph[][] = {
                {0.20000,0.20000,0.20000,0.20000,0.20000},
                {0.20000,0.20000,0.20000,0.20000,0.20000},
                {0.20000,0.20000,0.20000,0.20000,0.20000},
                {0.20000,0.20000,0.20000,0.20000,0.20000},
                {0.20000,0.20000,0.20000,0.20000,0.20000}
        };

        double cycleGraph[][] = {
                {0.33333,0.33333,0,0,0.33333},
                {0.33333,0.33333,0.33333,0,0},
                {0,0.33333,0.33333,0.33333,0},
                {0,0,0.33333,0.33333,0.33333},
                {0.33333,0,0,0.33333,0.33333}
        };

        double starGraph[][] = {
                {0.20000,0.20000,0.20000,0.20000,0.20000},
                {0.50000,0.50000,0,0,0},
                {0.50000,0,0.50000,0,0},
                {0.50000,0,0,0.50000,0},
                {0.50000,0,0,0,0.50000}
        };

        System.out.println("Complete Graph: ");
        LinearAveragingAlgorithm.linearAveragingAlgorithm(initialStates, completeGraph);
        System.out.println("Cycle Graph: ");
        LinearAveragingAlgorithm.linearAveragingAlgorithm(initialStates, cycleGraph);
        System.out.println("Star Graph: ");
        LinearAveragingAlgorithm.linearAveragingAlgorithm(initialStates, starGraph);
    }
}