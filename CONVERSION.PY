OS = input("Enter the string that you want to convert to cipher code")
  #k =int(input("Enter the key value"))
char_array = list(OS)
  
  
for i in range(len(char_array)):
    #print(char_array[i])   
    A = ord('A')
    B = ord('a')
    c = char_array[i]
    if 'A' <= c <= 'Z' :
      tempSum = ord(c) - A
      #print(tempSum)
      if tempSum == 23:
         tempSum = -3
      elif tempSum == 24:
         tempSum = -2
      elif tempSum == 25:
         tempSum = -1
      tempSum = tempSum + 3
      t = tempSum + 65
      temp = chr(t)
      print(temp, end=' ')
    elif 'a' <= c <= 'z':
      tempSum = ord(c) - B
      #print(tempSum)
      if tempSum == 25:
         tempSum = -1
      elif tempSum == 24:
         tempSum = -2
      elif tempSum == 23:
         tempSum = -3
      tempSum = tempSum + 3
      t = tempSum + 65
      temp = chr(t)
      print(temp, end=' ')
    elif 0<= c <= 9:
      tempSum  = ord(c) + 65
      temp = chr(tempSum)
      print(temp)
      
      
    else:
      print("invalid character")

input()


