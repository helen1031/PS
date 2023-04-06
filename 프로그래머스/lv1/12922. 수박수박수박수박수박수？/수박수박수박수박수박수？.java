class Solution {
    public String solution(int n) {
        String keyString = "수박";
        int iteration = n / 2;
        int odd = n % 2;
        
        String answer = "";
        
        for(int i = 0; i < iteration; i ++ ){
            answer += keyString;
        }
        if (odd == 1) {
            answer += "수";
        }
        return answer;
    }
}