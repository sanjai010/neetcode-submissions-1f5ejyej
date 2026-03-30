class Solution {
    public String mergeAlternately(String word1, String word2) {
        int i=0,j=0;
        StringBuilder mstring= new StringBuilder();
        while(i<word1.length() && j<word2.length()){
            mstring.append(word1.charAt(i));
            mstring.append(word2.charAt(j));

            i++;
            j++; 
        }
            mstring.append(word1.substring(i));
            mstring.append(word2.substring(j));

        
        return mstring.toString();
    }
}