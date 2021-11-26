package assignment_3;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner keyboard = new Scanner(System.in);

        /***** TASK 01 *****/
        System.out.println("----- Task 01 -----");

        System.out.print("Enter 1st integer: ");
        var num1 = keyboard.nextInt();
        System.out.print("Enter 2nd integer: ");
        var num2 = keyboard.nextInt();

        Task01 runs1 = new Task01(num1, num2, "add");
        Task01 runs2 = new Task01(num1, num2, "sub");
        Task01 runs3 = new Task01(num1, num2, "mul");
        Task01 runs4 = new Task01(num1, num2, "div");
        Task01 runs5 = new Task01(num1, num2, "oth");

        Thread add = new Thread(runs1, "Addition Thread");
        Thread sub = new Thread(runs2, "Subtraction Thread");
        Thread mul = new Thread(runs3, "Multiplication Thread");
        Thread div = new Thread(runs4, "Division Thread");
        Thread oth = new Thread(runs5, "Other Threads");

        add.start();
        sub.start();
        mul.start();
        div.start();
        oth.start();

        try {
            add.join();
            sub.join();
            mul.join();
            div.join();
            oth.join();
        } catch (InterruptedException e) {
            // e.printStackTrace();
        }
        System.out.println("----- Task 01 Completed -----\n");

        /***** TASK 02 *****/
        System.out.println("----- Task 02 -----");

        Thread houseStark = new Thread(new Task02("House Stark"));
        Thread houseTargaryen = new Thread(new Task02("House Targaryen"));
        Thread houseBolton = new Thread(new Task02("House Bolton"));
        Thread houseLannister = new Thread(new Task02("House Lannister"));
        Thread houseTyrell = new Thread(new Task02("House Tyrell"));

        houseStark.setPriority(Thread.MAX_PRIORITY);
        houseBolton.setPriority(Thread.MIN_PRIORITY);

        System.out.println("~ Single Threaded Mode ~");
        houseStark.run();
        houseTargaryen.run();
        houseLannister.run();
        houseBolton.run();

        System.out.println("~ Multi Threaded Mode ~");
        houseStark.start();
        houseLannister.start();
        houseBolton.start();
        houseTyrell.start();

        try {
            houseStark.join();
            houseTargaryen.join();
            houseLannister.join();
            houseBolton.join();
            houseTyrell.join();
        } catch (InterruptedException e) {
            // e.printStackTrace();
        }

        System.out.println("----- Task 02 Completed -----\n");

        /***** TASK 03 *****/
        System.out.println("----- Task 03 -----");

        long[] fibonacci = new long[51];
        fibonacci[0] = 1;
        fibonacci[1] = 1;

        for (int i = 2; i < fibonacci.length; i++) {
            fibonacci[i] = fibonacci[i - 1] + fibonacci[i - 2];
        }

        Task03[] runs = new Task03[4];

        runs[0] = new Task03(fibonacci, "odd", 1);
        runs[1] = new Task03(fibonacci, "even", 1);
        runs[2] = new Task03(fibonacci, "odd", 2);
        runs[3] = new Task03(fibonacci, "even", 2);

        Thread[] th = new Thread[runs.length];

        for (int i = 0; i < th.length; i++) {
            th[i] = new Thread(runs[i], "Thread " + i);
        }

        th[0].start();
        th[1].start();
        th[2].start();
        th[3].start();

        try {
            th[0].join();
            th[1].join();
            th[2].join();
            th[3].join();
        } catch (InterruptedException e) {
            // e.printStackTrace();
        }

        long[] mean = new long[runs.length];

        for (int i = 0; i < mean.length; i++) {
            mean[i] = runs[i].getMean();
        }

        Task03 run = new Task03(mean);
        Thread th5 = new Thread(run, "Thread 4");
        th5.start();

        try {
            th5.join();
        } catch (InterruptedException e) {
            // e.printStackTrace();
        }

        System.out.println("PIN: " + run.getMean());

        System.out.println("----- Task 03 Completed -----\n");

        keyboard.close();
    }
}