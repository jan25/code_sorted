package codeforces;

import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class VitallyAndString {
	
	public static void main(String[] args) throws FileNotFoundException {
		Scanner input = new Scanner(new FileInputStream(new File("src/input.txt")));
		solve(input);
		input.close();
	}
	
	static void solve(Scanner input) {
		new Zalgo(input.next().toCharArray(), input.next().toCharArray());
	}
	
	static class KMP {
		
		char[] text, pat;
		int[] lps;
		
		KMP (char[] t, char[] p) {
			text = t;
			pat = p;
			preProcess();
			doMatch();
		}
		
		void preProcess() {
			lps = new int[pat.length];
			lps[0] = 0;
			int len = 0;
			int i = 1;
			while (i < pat.length) {
				if (pat[i] == pat[len]) {
					++len;
					lps[i] = len;
					++i;
				}
				else {
					if (len != 0) {
						len = lps[len - 1];
					}
					else {
						lps[i] = 0;
						++i;
					}
				}
			}
		}
		
		void doMatch() {
			int pi = 0, ti = 0;
			while (ti < text.length) {
				if (pat[pi] == text[ti]) {
					++pi;
					++ti;
				}
				if (pi == pat.length) {
					System.out.println("found at: " + (ti - pi + 1));
					pi = lps[pi - 1];
				}
				else {
					if (ti < text.length && text[ti] != pat[pi]) {
						if (pi != 0) {
							pi = lps[pi - 1];
						}
						else {
							++ti;
						}
					}
				}
			}
		}
		
	}
	
	
	static class Zalgo {
		
		char[] s;
		int[] zarray;
		
		Zalgo(char[] t, char[] p) {
			s = new char[t.length + p.length + 1];
			int i = 0;
			int j = 0;
			while (j < p.length) {
				s[i] = p[j];
				++j; ++i;
			}
			s[i] = '$'; ++i;
			j = 0;
			while (j < t.length) {
				s[i] = t[j];
				++j; ++i;
			}
			fillZ();
			for (int ix = 0; ix < s.length; ++ix) {
				if (zarray[ix] == p.length) {
					System.out.println("found at: " + (ix - p.length - 1));
				}
			}
		}
		
		void fillZ() {
			zarray = new int[s.length];
			int l = 0, r = 0;
			int i = 1;
			while (i < s.length) {
				if (i > r) {
					l = r = i;
					while (r < s.length && s[r - l] == s[r])
						++r;
					zarray[i] = r - l;
					--r;
				}
				else {
					if (zarray[i - l] < r - l + 1) {
						zarray[i] = zarray[i - l];
					}
					else {
						l = i;
						while (r < s.length && s[r - l] == s[r]) 
							++r;
						zarray[i] = r - l;
						--r;
					}
				}
				System.out.print(zarray[i] + " ");
				if (s[i] == '$') System.out.print(" ");
				++i;
			}
		}
	}
	
}
