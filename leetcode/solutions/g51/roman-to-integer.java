class Solution 
{
    public int romanToInt(String s) 
    {
        Map<Character,Integer> map = new HashMap<>();
        map.put('I',1);
        map.put('V',5);
        map.put('X',10);
        map.put('L',50);
        map.put('C',100);
        map.put('D',500);
        map.put('M',1000);

        int result = map.get(s.charAt(s.length()-1));
        for(int i=s.length()-2;i>=0;i--)
        {
            int valueOne = map.get(s.charAt(i));
            int valueTwo = map.get(s.charAt(i+1));
            if( valueOne<valueTwo )
            result-=valueOne;
            else
            result+=valueOne;
        }

        return result;

        
    }
}