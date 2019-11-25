import time

width = 40
height = 20
border_char = "*"

def run():
    t = time.time()
    output = "The time is"+str(t)
    output_len = len(output)
    
    print(border_char*width, end="\n")
    
    print(border_char, end="")
    print(" "*(width-2), end="")
    print(border_char, end="\n")
    
    print(border_char, end="")
    print(" ", end="")
    print('The time is '+str(t), end="")
    print(" "*(width-2-2-1-output_len), end="")
    print(" ", end="")
    print(border_char, end="\n")
    
    print(border_char, end="")
    print(" "*(width-2), end="")
    print(border_char, end="\n")
    
    print(border_char*width, end="\n")


if __name__ == '__main__':
    run()
