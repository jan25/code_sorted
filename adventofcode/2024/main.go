package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strings"
)

func main() {
    args := os.Args
    // First arg is the binary being run.
    if len(args) == 1 {
        panic(fmt.Sprintf("Expected atleast 1 arg. Usage:\ngo run main.go <target> [input.file]\n Provided %v", args))
    }
    name := args[1]
    var inp string
    if len(args) > 2 {
        inp = args[2]
    } else {
        inp = "input.txt"
    }
    fmt.Printf("Target: %s\nInput file: %s\n", name, inp)
    
    lines := parse(inp)
    fmt.Println(fmt.Printf("Executing %s..\n", name))
    prob1a(lines)
}

// Parses given file into list of list of words
// Top level list represents a line
// Within each level words are from same line
func parse(f string) [][]string {
    file, err := os.Open(f)
    if err != nil {
        log.Fatal(err)
    }
    scanner := bufio.NewScanner(file)
    const lineLen int = 10000
    buf := make([]byte, lineLen)
    scanner.Buffer(buf, lineLen)
    var lines [][]string
    for scanner.Scan() {
        line := scanner.Text()
        lines = append(lines, strings.Fields(line))
    }
    return lines
}
