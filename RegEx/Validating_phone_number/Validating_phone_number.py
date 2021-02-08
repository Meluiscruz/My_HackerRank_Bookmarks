import re

def pn_validator(phn):
    rex_p = r"^[789]\d{9}$"

    if re.match(rex_p,phn):
        return  "YES"
    else:
        return  "NO"
    
if __name__ == "__main__":
    
    n = int(input())
    list_of_pn = []
    
    for _ in range(n):
        list_of_pn.append(str(input()))
    
    for _ in list_of_pn:
        print(pn_validator(_))