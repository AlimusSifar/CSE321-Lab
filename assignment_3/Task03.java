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
            this.average = calculateMean(0, mean.length);
        } else {
            if (part == 1) {
                this.average = calculateMean(1, 1 + fibonacci.length / 2);
            } else if (part == 2) {
                this.average = calculateMean(1 + fibonacci.length / 2, fibonacci.length);
            }
        }
    }

    public long getMean() {
        return this.average;
    }

    private long calculateMean(int ini, int len) {
        long sum = 0;
        int count = 0;

        if (skipAverage) {
            for (int i = ini; i < len; i++, count++) {
                sum += mean[i];
            }
        } else {
            for (int i = ini; i < len; i++) {
                if (type == "odd" && fibonacci[i] % 2 == 1) {
                    sum += fibonacci[i];
                    count++;
                } else if (type == "even" && fibonacci[i] % 2 == 0) {
                    sum += fibonacci[i];
                    count++;
                }
            }
        }

        return sum / count;
    }
}