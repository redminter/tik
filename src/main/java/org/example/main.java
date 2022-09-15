package org.example;


import java.util.ArrayList;
import java.util.Collections;
import java.util.Random;


public class main {
    //function for calculating log with foundation 2
    public static double log2(double x) {
        return (Math.log(x) / Math.log(2));
    }

    public static void main(String[] args) {
        Random rand = new Random();
        int n = rand.nextInt((20 - 10) + 1) + 10;//initialization of how many numbers will be
        ArrayList<Integer> numbers = new ArrayList<>();
        ArrayList<Double> posibilities = new ArrayList<>();
        System.out.println(n);

//adding a random number to the numbers array
        for (int i = 0; i < n; i++) {
            numbers.add(rand.nextInt(10));
        }
        System.out.println(numbers);

        double entropy = 0.0;
        for (int i = 0; i < numbers.size(); i++) {
            int occurrences = Collections.frequency(numbers,numbers.get(0));//calculating the amount of occurrences
            numbers.removeAll(Collections.singleton(numbers.get(0)));//remove that number from the list
            double possibility = occurrences/(double)n;//calculating the possibility
            posibilities.add(possibility);
        }
        for (int i = 0; i < posibilities.size(); i++){
            entropy += posibilities.get(i)*log2(posibilities.get(i));//implementing the formula
        }

        System.out.println(-entropy);
    }
}