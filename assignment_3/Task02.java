package assignment_3;

public class Task02 implements Runnable {
    private String houseName;

    public Task02(String name) {
        this.houseName = name;
    }

    @Override
    public void run() {
        System.out.printf("The house is : %s\n", houseName);

        // String threadName = Thread.currentThread().getName();
        if (houseName == "House Stark" || houseName == "House Targaryen") {
            sleep(1000);
        } else if (houseName == "House Lannister" || houseName == "House Bolton") {
            sleep(3000);
        } else {
            sleep(5000);
        }
    }

    private void sleep(int millis) {
        try {
            Thread.sleep(millis);
        } catch (Exception e) {
            // e.printStackTrace();
        }
    }
}