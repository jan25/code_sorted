use std::io::{self, BufRead};
use std::collections::HashMap;

fn main() {
    let stdin = io::stdin();
    let mut map = HashMap::new();
    for line in stdin.lock().lines() {
        let num: i32 = line.unwrap().parse().unwrap();
        match map.get(&(2020 - num)) {
            Some(&_) => println!("{}", (2020 - num) * num),
            _ => () 
        }
        map.insert(num, true);
    }
}