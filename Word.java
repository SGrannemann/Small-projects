public class Word {
  private String word;
  private String maskedWord;


  public Word (String word) {
    this.word = word;

  }

  public String getWord() {
    return this.word;
  }



  public void maskTheWord(StateOfGame gameState) {
    char[] maskedWordArray = word.toCharArray();
    for (int i = 0; i < maskedWordArray.length; i++){
      //if ( Character.isWhitespace(maskedWordArray[i])){
      if (maskedWordArray[i] == ' ' ){
        continue;
      }
      if (gameState.getLetters().contains(String.valueOf(maskedWordArray[i]))) {
        continue;
      }

        maskedWordArray[i] = '*';
  }
    maskedWord = String.valueOf(maskedWordArray);

  }

  public boolean letterContained (char letter) {
    if (word.indexOf(letter) == -1){
      return false;
    }

    return true;
  }



  public String getMaskedWord() {
    return this.maskedWord;
  }


}
