// 비밀번호 찾기 
package project1;

public class Ex05 {

	public static void main(String[] args) {
		String key = "129036";  // 129036, 123629, 5918
		int[] keys = {14,18,27};
		int[] strs = {5,2,9};
		String[] oper = {"*","-","+"};
		String[][] key1 = new String[strs.length*oper.length][2];
		String[][] key2 = new String[strs.length*oper.length][2];
		String[][] key3 = new String[strs.length*oper.length][2];
		String temp ="";
		String expression ="";
		// 모든 경우의 수 생성 
		for(int i=0; i < strs.length; i++) {
			key1[0+i*3][0] = keys[0] * strs[i] + "";
			key1[1+i*3][0] = keys[0] - strs[i] + "";
			key1[2+i*3][0] = keys[0] + strs[i] + "";
			key2[0+i*3][0] = keys[1] * strs[i] + "";
			key2[1+i*3][0] = keys[1] - strs[i] + "";
			key2[2+i*3][0] = keys[1] + strs[i] + "";
			key3[0+i*3][0] = keys[2] * strs[i] + "";
			key3[1+i*3][0] = keys[2] - strs[i] + "";
			key3[2+i*3][0] = keys[2] + strs[i] + "";

			key1[0+i*3][1] = keys[0] + "*" + strs[i] + "";
			key1[1+i*3][1] = keys[0] + "-" +  strs[i] + "";
			key1[2+i*3][1] = keys[0] + "+" + strs[i] + "";
			key2[0+i*3][1] = keys[1] + "*" +  strs[i] + "";
			key2[1+i*3][1] = keys[1] + "-" + strs[i] + "";
			key2[2+i*3][1] = keys[1] + "+" + strs[i] + "";
			key3[0+i*3][1] = keys[2] + "*" +  strs[i] + "";
			key3[1+i*3][1] = keys[2] + "-" + strs[i] + "";
			key3[2+i*3][1] = keys[2] + "+" + strs[i] + "";
		}
		
		loop:
		for(int i=0; i < key1.length; i++) {
			for(int j=0; j< key2.length; j++) {
				for(int k=0; k < key3.length; k++) {
					temp = key1[i][0]+key2[j][0]+key3[k][0];
					expression = "("+key1[i][1]+") ("+key2[j][1]+") ("+key3[k][1]+")";
					if ( key.equals(temp) ) {
						System.out.println("비밀번호 : " + key);
						System.out.println("조합식 : " + expression);
						break loop;
					}
				}
			}
		}
	}
}
