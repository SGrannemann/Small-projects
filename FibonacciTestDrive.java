import java.util.Scanner;
import java.util.ArrayList;
public class FibonacciTestDrive{

  public static void main (String[] args) {
    ArrayList<Integer> list = new ArrayList();
    Scanner scanner = new Scanner(System.in);
    Fibonacci fib = new Fibonacci();
    System.out.println("How many fibonacci numbers to generate?");
    int input = Integer.valueOf(scanner.nextLine());
    list = fib.generateFibonacci(input);
    System.out.println(list);
  }
}
