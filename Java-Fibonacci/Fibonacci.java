import java.util.ArrayList;

public class Fibonacci {
private ArrayList<Integer> sequence = new ArrayList();

  public ArrayList<Integer> generateFibonacci (int number) {
    int number1 = 0;
    int number2 = 1;
    // add the starting zero directly to avoid writing logic for it
    sequence.add(0);
    // if only 1 fibonacci number should be generated, its simply 0.
    // if more are wanted, we need to start the sequence by adding a 1.
    if (number > 1){
      sequence.add(1);
    }
    int numberToAdd = 0;
    // as we have already added two numbers to the sequence, we can start the loop
    // at 2.
    for (int i = 2; i <= number -1 ; i++){
      // calculate next element and add it to the ArrayList
      numberToAdd = number1 + number2;
      sequence.add(numberToAdd);

      // Shift the numbers one step to the right as the next number to calculate
      // depends on the last two numbers
      number1 = number2;
      number2 = numberToAdd;
    }
    return sequence;
  }
}
