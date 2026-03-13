try:
  with open('docs.txt','r') as rd:
         text = rd.readlines()
         if not text:
               raise ValueError("data not available")
  with open('abc.txt','w') as wd:
          wd.writelines(text)
except FileNotFoundError:
      print("File not present")
except ValueError as e:
      print(e)


                 
        
             