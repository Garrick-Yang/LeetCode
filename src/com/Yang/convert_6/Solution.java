package com.Yang.convert_6;

import java.util.ArrayList;

public class Solution {
    public static String convert(String s,int numRows){
        if(numRows == 1){
            return s;
        }
        ArrayList<StringBuffer> list = new ArrayList<>();
        for (int i = 0; i < numRows; i++) {
            list.add(new StringBuffer());
        }
        int temp = 0,flag = -1;
        for (char c:
             s.toCharArray()) {
            list.get(temp).append(c);
            if (temp == 0 || temp == numRows - 1){
                flag = -flag;
            }
            temp += flag;
        }
        StringBuffer reslut = new StringBuffer();
        for (StringBuffer num:
             list) {
            reslut.append(num);
        }
        return reslut.toString();
    }
}
