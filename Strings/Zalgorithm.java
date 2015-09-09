/* Z algorithm */
/* longest common prefix for S ans suffix(S) */
/* O(len(s)) */

//package codeforces;


import java.io.*;
import java.util.*;


class Sept7 {
	
    public static void main(String[] args) throws FileNotFoundException {
//    	InputStream inputStream = new FileInputStream(new File("src/input.txt"));
        InputStream inputStream = System.in;
    	OutputStream outputStream = System.out;
    	InputReader in = new InputReader(inputStream);
    	PrintWriter out = new PrintWriter(outputStream);
        new Task(in, out).solve();
        out.close();
    }

    static class Task {
    	InputReader in;
    	PrintWriter out;
    	public Task(InputReader in, PrintWriter out) {
    		this.in = in;
    		this.out = out;
    	}

    	int[] z;
    	
    	public void solve() {
    		int tc = in.nextInt();
    		while (tc-- > 0) {
    			String s = in.next();
    			int len = s.length();
    			z = new int[len];
    			fillz(s, len);
    			int q = in.nextInt();
    			while (q-- > 0) {
    				int i = in.nextInt();
    				--i;
    				out.println(z[revi(i, len)]);
    			}
    		}
    	}
    	
    	public int revi(int i, int len) {
    		return len - i - 1;
    	}
    	
    	public void fillz(String s, int len) {
    		char[] ar = s.toCharArray();
    		for (int i = 0, j = len-1; i < j; ++i, --j) {
    			char c = ar[i];
    			ar[i] = ar[j];
    			ar[j] = c;
    		}
    		int l = 0, r = 0;
    		z[0] = len;
    		for (int i = 1; i < len; ++i) {
    			if (i > r) {
    				l = i; r = i;
    				while (r < len && ar[r - l] == ar[r]) ++r;
    				z[i] = r - l;
    				--r;
    			}
    			else {
    				int k = i - l;
    				if (z[k] < r - i + 1) {
    					z[i] = z[k];
    				}
    				else {
    					l = i;
    					while (r < len && ar[r - l] == ar[r]) ++r;
    					z[i] = r - l;
    					--r;
    				}
    			}
    		}
    		
    	}
    	
    }

    static class InputReader {
        public BufferedReader reader;
        public StringTokenizer tokenizer;

        public InputReader(InputStream stream) {
            reader = new BufferedReader(new InputStreamReader(stream), 32768);
            tokenizer = null;
        }

        public String next() {
            while (tokenizer == null || !tokenizer.hasMoreTokens()) {
                try {
                    tokenizer = new StringTokenizer(reader.readLine());
                } catch (IOException e) {
                    throw new RuntimeException(e);
                }
            }
            return tokenizer.nextToken();
        }

        public int nextInt() {
            return Integer.parseInt(next());
        }
        
        public long nextLong() {
        	return Long.parseLong(next());
        }

    }
}
