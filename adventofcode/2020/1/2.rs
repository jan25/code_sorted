use std::io::{self, BufRead};
use std::collections::HashMap;

fn main() {
    let stdin = io::stdin();
    let mut nums = vec![];
    for line in stdin.lock().lines() {
        let num: i32 = line.unwrap().parse().unwrap();
        nums.push(num);
    }
    
    let mut map = HashMap::new();
    for a in &nums {
        for b in &nums {
            map.insert(a + b, a * b);
        }
    }

    for a in &nums {
        match map.get(&(2020 - a)) {
            Some(&pair) => println!("{}", a * pair),
            _ => ()
        }
    }
}