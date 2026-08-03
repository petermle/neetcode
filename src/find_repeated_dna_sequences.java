import java.util.List;
import java.util.HashSet;
import java.lang.String;
import java.util.ArrayList;

public class find_repeated_dna_sequences
{
    public static List<String> findRepeatedDnaSequences(String s)
    {
        HashSet<String> seen = new HashSet<>();
        HashSet<String> result = new HashSet<>();
        int lastViableIndex = s.length() - 9;

        for (int i = 0; i < lastViableIndex; ++i)
        {
            String currentString = s.substring(i, i + 10);
            if (seen.contains(currentString))
                result.add(currentString);
            else
                seen.add(currentString);
        }
        return new ArrayList<>(result);
    }
    public static void main(String[] args)
    {
        String test = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT";
        List<String> result = findRepeatedDnaSequences(test);
        result.forEach(string -> System.out.println(string));
    }
}