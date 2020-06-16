import java.util.Scanner;
import java.util.ArrayList;
import java.nio.file.Paths;
import java.util.Random;
public class Main{



public static void main ( String[] args ){
    ArrayList<String> listOfWords = new ArrayList<>();
      try (Scanner scanner = new Scanner(Paths.get("Words.txt"));) {
          while (scanner.hasNextLine()){
            String line = scanner.nextLine();
            listOfWords.add(line);

          }
      // randomly select one of the words that have been read from file



      } catch (Exception e){
        System.out.println("Error reading file.");
      }
      System.out.println(listOfWords);
      Random rand = new Random();
      int randomNumber = rand.nextInt(listOfWords.size());
      StateOfGame gameState = new StateOfGame();
      Word word = new Word(listOfWords.get(randomNumber));
      word.maskTheWord(gameState);


      System.out.println(word.getWord());
      System.out.println(word.getMaskedWord());
      while (true){
      Scanner inputReader = new Scanner(System.in);
      System.out.println("Guess a letter. Empty to stop.");
      String guess = inputReader.nextLine();
      if (guess.equals("")){
        break;
      }
      gameState.addLetter(guess);
      System.out.println(gameState.getLetters());
      word.maskTheWord(gameState);
      System.out.println(word.getMaskedWord());
    }
  }

}
