package assignment_3;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner keyboard = new Scanner(System.in);

        // /***** TASK 01 *****/
        // System.out.println("----- Task 01 -----");

        // /* Test vriables */
        // var num1 = 12;
        // var num2 = 7;

        // // System.out.print("Enter 1st integer: ");
        // // var num1 = keyboard.nextInt();
        // // System.out.print("Enter 2nd integer: ");
        // // var num2 = keyboard.nextInt();

        // Task01 runs1 = new Task01(num1, num2, "add");
        // Task01 runs2 = new Task01(num1, num2, "sub");
        // Task01 runs3 = new Task01(num1, num2, "mul");
        // Task01 runs4 = new Task01(num1, num2, "div");
        // Task01 runs5 = new Task01(num1, num2, "oth");

        // Thread add = new Thread(runs1, "Addition Thread");
        // Thread sub = new Thread(runs2, "Subtraction Thread");
        // Thread mul = new Thread(runs3, "Multiplication Thread");
        // Thread div = new Thread(runs4, "Division Thread");
        // Thread oth = new Thread(runs5, "Other Threads");

        // add.start();
        // sub.start();
        // mul.start();
        // div.start();
        // oth.start();

        // try {
        // add.join();
        // sub.join();
        // mul.join();
        // div.join();
        // oth.join();
        // } catch (InterruptedException e) {
        // // e.printStackTrace();
        // }
        // System.out.println("----- Task 01 Completed -----\n");

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
        // System.out.println("----- Task 03 -----");

        // System.out.println("----- Task 03 Completed -----\n");
        keyboard.close();
    }
}