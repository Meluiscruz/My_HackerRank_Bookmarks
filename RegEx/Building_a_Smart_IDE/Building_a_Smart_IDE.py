# Enter your code here. Read input from STDIN. Print output to STDOUT

import re
import sys

def Code_Detector(Text):
    
    if "#include" in Text:
        return "C"
    elif "import java.io." in Text:
        return "Java"
    else :
        return "Python"

if __name__ == "__main__":
    
    Text = sys.stdin.read()
    print(Code_Detector(Text))