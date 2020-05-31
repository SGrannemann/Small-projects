import java.util.ArrayList;

public class Fibonacci {
private ArrayList<Integer> sequence = new ArrayList();

  public ArrayList<Integer> generateFibonacci (int number) {
    int number1 = 0;
    int number2 = 1;
    sequence.add(0);
    if (number > 1){
      sequence.add(1);
    }
    int numberToAdd = 0;

    for (int i = 2; i <= number -1 ; i++){
      numberToAdd = number1 + number2;
      sequence.add(numberToAdd);

      number1 = number2;
      number2 = numberToAdd;
    }
    return sequence;
  }
}
