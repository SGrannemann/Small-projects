public class Word {
  private String word;
  private String maskedWord;


  public Word (String word) {
    this.word = word;
    maskTheWord();
  }

  public String getWord() {
    return this.word;
  }

  public void maskTheWord() {
    char[] maskedWordArray = word.toCharArray();
    for (int i = 0; i < maskedWordArray.length; i++){
      //if ( Character.isWhitespace(maskedWordArray[i])){
      if (maskedWordArray[i] == ' '){
        continue;
      }
        maskedWordArray[i] = '*';
  }
    maskedWord = String.valueOf(maskedWordArray);

  }

  public String getMaskedWord() {
    return this.maskedWord;
  }


}
