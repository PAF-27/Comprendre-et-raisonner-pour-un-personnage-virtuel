import org.tartarus.snowball.ext.englishStemmer;

/**
 */
public class WordRootTest {

    public static void main(String[] args) {
        englishStemmer stemmer = new englishStemmer();
        stemmer.setCurrent("");
        if (stemmer.stem()){
            System.out.println(stemmer.getCurrent());
        }
    }
}
