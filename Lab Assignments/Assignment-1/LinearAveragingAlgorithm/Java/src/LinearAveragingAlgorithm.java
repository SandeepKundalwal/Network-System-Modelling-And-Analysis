import java.text.DecimalFormat;
import java.util.Arrays;

public class LinearAveragingAlgorithm {
    public static final DecimalFormat decimalFormat = new DecimalFormat("0.00000");
    public static void linearAveragingAlgorithm(double[] state, double[][] adjacencyMatrix) {
        int iteration = 0;
        while(true){
            double nextState[] = findLinearAverage(state, adjacencyMatrix);
            if(repeatedIteration(state, nextState)){
                break;
            }
            state = nextState.clone();
            iteration++;
        }

        System.out.println("Consensus reached at: " + (iteration + 1) + " iteration");
        System.out.println(Arrays.toString(state));
    }

    public static double[] findLinearAverage(double state[], double adjacencyMatrix[][]){
        int n = state.length;
        int decimalPlaces = 5;
        double nextState[] = new double[n];

        for(int i = 0; i < n; i++){
            double sum = 0;
            for(int j = 0; j < n; j++){
                double multiply = Math.round(Double.parseDouble(decimalFormat.format(state[j] * adjacencyMatrix[i][j])) * Math.pow(10, decimalPlaces)) / Math.pow(10, decimalPlaces);
                sum += multiply;
            }
            nextState[i] = sum;
        }

        return nextState;
    }

    public static boolean repeatedIteration(double state[], double nextState[]){
        int n = state.length;
        for(int i = 0; i < n; i++){
            if(Double.compare(state[i], nextState[i]) != 0){
                return false;
            }
        }
        return true;
    }
}
