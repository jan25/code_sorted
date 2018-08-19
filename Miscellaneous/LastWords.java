/*
** https://code.google.com/codejam/contest/dashboard?c=4304486
** level: Med
** N^2 solution. can be done in N? or NlogN using sort? Yea, Think so..
*/

import java.util.*;
import java.lang.*;
import java.io.*;

/*
 * idea: lastword == one subseq(x) + mirror of remaining subseq(x)
 */
public class LastWords {
	
	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		int N = in.nextInt();
		for (int i = 1; i <= N; ++i) {
			System.out.println("Case #" + i + ": " + new Task().input(in).getLastWord());
		}
		in.close();
	}

	static class Task {
		String x;

		Task input(Scanner in) {
			this.x = in.next().trim();
			return this;
		}
		
		String getLastWord() {
			TreeMap<Integer, Boolean> map = new TreeMap<>();
			StringBuilder y = new StringBuilder();
			int maxIndex = x.length() - 1;
			char maxChar = '-';
			while (maxIndex >= 0) {
				int nextMaxIndex = this.getMaxIndexLeft(maxIndex);
				maxChar = x.charAt(nextMaxIndex);
				y.append(maxChar);
				map.put(nextMaxIndex, true);
				maxIndex = nextMaxIndex - 1;
			}
			for (int i = 0; i < x.length(); ++i) {
				if (!map.containsKey(i)) {
					y.append(x.charAt(i));
				}
			}
			return y.toString();
		}
		
		int getMaxIndexLeft(int r) {
			int maxIndex = r;
			while (r-- > 0) {
				if (x.charAt(r) > x.charAt(maxIndex))
					maxIndex = r;
			}
			return maxIndex;
		}
	}
}