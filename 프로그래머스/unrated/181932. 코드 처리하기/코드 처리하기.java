class Solution {
    // mode idx char ans 
    // 0   0   a   a
    // 0   1   b   s
    // 0   0   c   
    
    public String solution(String code) {
        String answer = "";
        char[] Acode = code.toCharArray();
        boolean mode = false;

        for(int i=0; i < Acode.length; i++) {   
            if(!mode) {
                if(Acode[i] != '1') {
                    if(i%2 == 0) {
                        answer += Acode[i];
                    }
                } else {
                    mode = true;
                }
            } else {
                if(Acode[i] != '1') {
                    if(i%2 != 0) {
                        answer += Acode[i];
                    }
                } else {
                    mode = false;
                }
            }
        }
        
        if (answer.isEmpty()) {
            answer = "EMPTY";
        }
        
        return answer;
    }
}