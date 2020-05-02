package yc.ma.leetcode;

import java.util.HashSet;
import java.util.Map;
import java.util.HashMap;
import java.util.Set;

public class j3 {
    public int lengthOfLongestSubstring(String s) {
        if(s.length()<=1){
            return s.length();
        }
        char[] arr = s.toCharArray();
        int p1 = 0;
        int p2 = 1;
        Set<Character> cache = new HashSet<>();
        cache.add(arr[p1]);
        int currlengthofsubstring = 1;
        int maxlengthofsubstringsofar = 1;
        for (; p2 < arr.length; p2++) {
            if (!cache.contains(arr[p2])) {
                currlengthofsubstring++;
                if (currlengthofsubstring > maxlengthofsubstringsofar) {
                    maxlengthofsubstringsofar = currlengthofsubstring;
                }
                cache.add(arr[p2]);
            }
            else {
                while (arr[p1] != arr[p2]) {
                    cache.remove(arr[p1]);
                    p1++;
                    currlengthofsubstring--;
                }
                p1++;
            }
        }
        return maxlengthofsubstringsofar;
    }
    public int lengthOfLongestSubstring(String s) {
        if (s.length() == 0) {
            return 0;
        }
        int maxlengthofsubstringsofar = 1;
        Map<Character,Integer> m = new HashMap();
        int i;
        for (i = 0; i < s.length(); i++) {
            if (m.containsKey(s.charAt(i)) && m.get(s.charAt(i)) != -1) {
                int ivalue = m.get(s.charAt(i));
                for (Character c : m.keySet()) {
                    int value = m.get(c);
                    if (value <= ivalue && value != -1) {
                        int lengthofsubstring = i - value;
                        if (maxlengthofsubstringsofar < lengthofsubstring) {
                            maxlengthofsubstringsofar = lengthofsubstring;
                        }
                        m.put(c, -1);
                    }
                }
            }
            m.put(s.charAt(i), i);
        }
        for (Integer v: m.values()) {
            if (v != -1 && maxlengthofsubstringsofar < i - v) {
                maxlengthofsubstringsofar = i - v;
            }
        }
        return maxlengthofsubstringsofar;
    }
}
