import java.util.*;
class Solution{
    public String decodeString(String s){
        int n = s.length();
        Stack<Character> stack = new Stack<>();
        for (int i = 0; i < n; i++){
            char c = s.charAt(i);
            if (c != ']') stack.push(c);
            else {
                String st = "";
                while (!stack.isEmpty() && Character.isLetter(stack.peek()))
                    st = stack.pop() + st; // the most inificient part of the algorithm
                    // adding eats time
                stack.pop(); // remove the '[' from the stack
                int num = 0;
                int exp= 0;
                while ( !stack.isEmpty() && Character.isDigit(stack.peek())){
                    num += Integer.parseInt("" + stack.pop()) * Math.pow(10, exp++);  
                }
                                                              
                while (num > 0){
                     for (char currChar : st.toCharArray())
                         stack.push(currChar);
                    num--;
                }
                                                              
                                                             
   
            }
}
                                                                     
    StringBuilder ans = new StringBuilder();
        while (!stack.isEmpty()) ans.append(stack.pop());
        return ans.reverse().toString();
                                                                
    }
}
