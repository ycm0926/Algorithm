class Solution {
    public String solution(String str1, String str2) {
        String answer = "";
        char[] a = str1.toCharArray();
        char[] b = str2.toCharArray();
        int c = 0;
        
        if (a.length >= b.length ) {
            c = a.length;
        } else {
            c = b.length;
        }
        
        for(int i=0; i<c; i++){
            answer += a[i];
            answer += b[i];
        }
        
        return answer;
    }
}