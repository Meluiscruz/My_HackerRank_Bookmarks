import email.utils
import re

def main():
  #pattern = re.compile(r"^[\w\._]{5,30}\+?[\w]{0,10}@[^\d][\w\.\-]{3,}\.\w{2,5}$")
  pattern = re.compile(r"^[a-zA-Z][\w\-.]*@[a-zA-Z]+\.[a-zA-Z]{1,3}$")
  for _ in range(int(input())):
    u_name, u_email = email.utils.parseaddr(input())
    if pattern.match(u_email):
      print(email.utils.formataddr((u_name, u_email)))

if __name__ == "__main__":
  main()