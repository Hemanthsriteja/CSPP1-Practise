'''Exercise : Function and Objects Exercise-1'''
#testList = [1, -4, 8, -9] into [1, 4, 8, 9]


def apply_to_each(L, f):
   for i in range(0,len(L)):
       L[i] = f(L[i])
   return L
def main():
   data = input()
   data = data.split()
   list1 = []
   for j in data:
       list1.append(int(j))
   apply_to_each(list1, abs)
   print(list1)
if __name__ == "__main__":
   main()