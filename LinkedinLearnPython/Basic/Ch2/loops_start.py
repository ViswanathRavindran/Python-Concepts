#
# Example file for working with loops
#

def main():
  # x = 0

  # # define a while loop
  # while(x<5):
  #   print("x:", x)
  #   x += 1

  # # define a for loop
  # for x in range(5,10):
  #   print(x)

  # # use a for loop over a collection
  # days = ["Mon", "Tue", "Wed", "Thur", "Fri", "Sat", "Sun"]
  # for d in days:
  #   print(d)
  
  # # use the break and continue statements
  # for x in range(5,11):
  #   if (x==9): break
  #   if (x%2 == 0): continue
  #   print(x)

  # using the enumerate() function to get index
  days = ["Mon", "Tue", "Wed", "Thur", "Fri", "Sat", "Sun"]
  for i,d in enumerate(days):
    print(i, d)

  # def countDigit(n):
  #   count = 0
  #   while n != 0:
  #       n //= 10
  #       count += 1
  #   return count
  
  # print("Number of digits : % d" % (countDigit(23490)))
  
if __name__ == "__main__":
  main()

