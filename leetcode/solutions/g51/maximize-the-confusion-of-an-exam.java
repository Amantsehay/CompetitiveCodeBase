class Solution {

    //this is all about the sliding windows problems
    public int maxConsecutiveAnswers(String answerKey, int k) {
        int start=0, end=0,fcount=0, tcount=0, len=answerKey.length();
        int sub=0;
        while (end<len){
            if (answerKey.charAt(end)=='F'){
                fcount++;
            }
            else{
                tcount++;
            }
            while (Math.min(tcount, fcount)>k){
                if (answerKey.charAt(start)=='F'){
                    fcount--;
                }
                else {
                    tcount--;
                }
                start++;

            }
            sub=Math.max(sub, end-start+1);
            end++;




            //this will keep track of the f and the t counts

        }
        return sub;
        //
    }


}