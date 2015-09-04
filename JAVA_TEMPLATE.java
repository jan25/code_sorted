package codeforces;


import java.io.*;
import java.util.*;


public class Code1 {
	
    public static void main(String[] args) throws FileNotFoundException {
    	InputStream inputStream = new FileInputStream(new File("src/input.txt"));
//        InputStream inputStream = System.in;
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

    	public void solve() {

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
