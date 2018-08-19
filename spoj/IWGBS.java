/*
**	Date: 26.04.2015
**
*/
// Using BigInteger class of java
import java.util.*;
import java.lang.*;
import java.io.*;
import java.math.*;

class UsingBigInt {
	public static void main (String[] args) throws java.lang.Exception {
		int N = 10001;
		BigInteger[] zero = new BigInteger[N];
		BigInteger[] one = new BigInteger[N];

		zero[1] = new BigInteger("1");
		one[1] = new BigInteger("1");
		for (int i = 2; i < N; ++i) {
			one[i] = one[i-1].add(zero[i-1]);
			zero[i] = one[i-1].add(new BigInteger("0"));
		}
		Scanner in = new Scanner(System.in);
		int n = in.nextInt();
		System.out.println(zero[n].add(one[n]));
	}
}
