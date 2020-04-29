
public class ConcatenatedWords {
    public List<String> findAllConcatenatedWordsInADict(String[] words) {

        // we sort the words array by length of the words
        Arrays.sort(words, (w1, w2) -> w1.length() - w2.length());

        // we maintain a set of words already seen so that it is easy for us to chek the
        // prefix and see if the word can be made
        Set<String> set = new HashSet<>();
        List<String> res = new ArrayList<>();

        // we check every word if it can be made by the other words if yes then we add
        // to res
        // we add every word to set to check if it can be used to make other word

        for (String word : words) {
            if (canBeFormed(word, set)) {
                res.add(word);
            }
            // add every word in the prefix set
            set.add(word);
        }

        return res;
    }

    public boolean canBeFormed(String word, Set<String> set) {

        // if word is already present in the set then return
        if (set.contains(word))
            return true;

        // else check each substring on the word,
        // starting from 0-1 if it is present then check if rest substring is present
        // if both are present that means the word can be formed by using the prefixes
        // in the string

        for (int i = 1; i <= word.length(); i++) {

            if (set.contains(word.substring(0, i))) {

                // then check if the set has rest of the substing
                if (canBeFormed(word.substring(i), set)) {
                    return true;
                }

            }

        }
        return false;
    }
}