ilfrom sys import argv

def main() -> None:
  if len(argv)!=3:
    flag_format:str = input("What is the format of the flag:\nExample: HTB{X}\n> ")
    bin_name:str = input("What is the name of the binary?\n> ")
  else:
    flag_format:str = argv[1]
    bin_name:str = argv[2]
  to_find:str = flag_format.split("X")[0]
  trail:str = flag_format.split("X")[1]
  try:
    with open(bin_name, "r") as bin:
      try:
        print(bin.read()[bin_name.index(to_find):bin_name.index(trail)])
      except ValueError:
        print("Flag not found")
        exit()
  except FileNotFoundError:
    print("The binary was not found")
      

if __name__=="__main__":
  main()
