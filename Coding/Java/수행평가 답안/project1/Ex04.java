// 4���� ����(1,2,3,4)�� ����� �ִ� 4�ڸ��� �ڿ��� ��θ� ����ϰ�, �� ����� ���� ���Ͻÿ�.
package project1;

public class Ex04 {

	public static void main(String[] args) {
		int[] nums = {1,2,3,4};
		int length = nums.length;
		int count = 0;
		
		for(int i=0; i < length; i++)
		{
			for(int j=0; j < length; j++)
			{
				for(int k=0; k < length; k++)
				{
					for( int l=0; l < length; l++)
					{
						if ( i != j && i != k && i != l && j != k && j != l && k != l )
						{
							System.out.println((count+1) + " : " + nums[i]+nums[j]+nums[k]+nums[l]);
							count++;
						}
					}
				}
			}
		}
		System.out.println("�� " + count + "����");

	}

}
