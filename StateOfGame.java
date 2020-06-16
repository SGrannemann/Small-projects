import java.util.ArrayList;

public class StateOfGame {
  private ArrayList<String> lettersGuessed = new ArrayList<>();

  public StateOfGame () {

  }

  public void addLetter(String letter) {
    if (!(lettersGuessed.contains(letter))){
    lettersGuessed.add(letter);
  } else {
    System.out.println("You already guessed that letter.");
  }
}

  public ArrayList<String> getLetters () {
    return lettersGuessed;
  }
}
