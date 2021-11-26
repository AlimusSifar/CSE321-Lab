package assignment_3;

public class Task03 implements Runnable {
    private long[] fibonacci;
    private String type;
    private int part;
    private long average;
    private long[] mean;
    private boolean skipAverage = false;

    public Task03(long[] fibonacci, String type, int part) {
        this.fibonacci = fibonacci;
        this.type = type;
        this.part = part;
    }

    public Task03(long[] mean) {
        this.mean = mean;
        this.skipAverage = true;
    }

    @Override
    public void run() {
        if (skipAverage) {
            calculateMean(mean, 0, mean.length, 1);
        } else {
            if (part == 1 && type == "odd") {
                calculateMean(fibonacci, 1, 1 + fibonacci.length / 2, 2);

            } else if (part == 1 && type == "even") {
                calculateMean(fibonacci, 2, 1 + fibonacci.length / 2, 2);

            } else if (part == 2 && type == "odd") {
                calculateMean(fibonacci, 26, fibonacci.length, 2);

            } else if (part == 2 && type == "even") {
                calculateMean(fibonacci, 27, fibonacci.length, 2);
            }
        }
    }

    private void calculateMean(long[] array, int ini, int len, int step) {
        long sum = 0;
        int count = 0;

        for (int i = ini; i < len; i += step, count++) {
            sum += array[i];
        }

        this.average = sum / count;
    }

    public long getMean() {
        return this.average;
    }
}