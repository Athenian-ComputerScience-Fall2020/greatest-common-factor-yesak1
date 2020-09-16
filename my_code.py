# Collaborators (including web sites where you got help: (enter none if you didn't need help)
#  I did probably 90% on my own but I didn't exactly know how functions worked so I refreshed my memory by looking it up. I also needed help with while loops
# the website I used for reference was called stackoverflow.com
def find_gcf(x,y): 
    if x > y:
        z=x%y
        if z==0:
            return y
    if x<y:
        z=y%x
        if z==0:
            return x
        else: 
            return find_gcf(x,z)
    if x==y:
        return x
    if x==0:
        return y
    if y==0:
        return x
    while z > 0:
        if x % z == 0 and y % z == 0:
            return z
        z -= 1

          # Do not change function name!
    # User code goes here




if __name__ == '__main__':
    # Test your code with this first
    # Change the argument to try different values
    x = int(input("Enter a number: "))
    y = int(input("Enter another number: "))
    
    print(find_gcf(x,y))

    # After you are satisfied with your results, use input() to prompt the user for two values:
    

