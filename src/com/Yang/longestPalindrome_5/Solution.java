package com.Yang.longestPalindrome_5;

public class Solution {
    public static String longestPalindrome(String s) {
        int len = s.length();
        if(len < 2){
            return s;
        }
        int begin = 0,maxLen = 1;

        boolean[][] huiWen =new boolean[len][len];
        for(int i = 0;i < len; i++){
            huiWen[i][i] = true;
        }

        char[] charArray = s.toCharArray();

        //子串长度
        for (int L = 2;L <= len; L++){
            for (int i = 0;i < len;i++){ //左边界
                int j = i + L - 1;
                if(j >= len){
                    continue;
                }
                if (charArray[i] != charArray[j]) {
                    huiWen[i][j] = false;
                }else{
                    if (L <= 2){
                        huiWen[i][j] = true;
                        if (L > maxLen){
                            maxLen = L;
                            begin = i;
                        }
                        continue;
                    }
                    if (huiWen[i+1][j-1] == true){
                        huiWen[i][j] = true;
                        if (L > maxLen){
                            maxLen = L;
                            begin = i;
                        }
                    }
                    else{
                        huiWen[i][j] = false;
                    }
                }
            }
        }

        return s.substring(begin,begin + maxLen);
    }
}