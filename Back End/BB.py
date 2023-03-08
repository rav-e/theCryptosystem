from decimal import Decimal
import hashlib


selection = input("Type STRAT if you want to start program ")

if selection == 'START':
    ty = input("Press t for text Encryption/Decryption or f if you want to encrypt file : ")
    if ty == 't':
       level = input('''\nSelelct level of Encryption : \n 1.script kiddie\n 2.programming\n 3.black hat\n\nYour Choice:''')
       if level == '1':
          def VernamCipherFunction(text,key):
              answer = ""
              p = 0 
              for char in text:
                  answer += chr(ord(char) ^ ord(key[p]))
                  p += 1
                  if p == len(key):
                     p == 0
              return answer
          my_key = "cvwopslweinedvq9fnasdlkfn2"
          while True:
                     plaintext = input("\nYour Text : ")
                     cypher = VernamCipherFunction(plaintext,my_key)
                     print("Cipher Text : " +cypher)
                     decrypt = VernamCipherFunction(cypher,my_key)
                     print("plain text: "+decrypt) 
       elif level == '2':
            def gcd(a,b):
               if b == 0:
                  return a
               else:
                   return gcd(b,a%b)
            s = int(input('Enter the value of p = ')) 
            q = int(input('Enter the value of q = '))
            no = int(input('Enter the Text = '))
            n = s * q
            tt = (s-1) * (q -1)
            for f in range (2,tt):
                 if gcd(f,tt) == 1:
                    break
            for i in range (1,10):
                 x = 1 + i*tt 
                 if x%f == 0:
                    d = int(x/f)
                    break
            ctt = Decimal(0)
            ctt = pow(no,f)
            ct = ctt%n
            dtt = Decimal(0)
            dtt = pow(ct,d)
            dt = dtt%n
             
             
            print("Cipher Text :  " +str(ct) )
            print("Your Text : " +str(dt))        
       elif level == '3':
             str = input("Your text : ")
             result = hashlib.sha256(str.encode())
             print("Hash Digest of Your Text : ")
             print(result.hexdigest())
       else :
              print("invalid input!")
    elif ty == 'f':
       try:
                import pyAesCrypt
       except ImportError:
                import subprocess
                subprocess.check_call(["python", '-m', 'pip', 'install', 'pyAesCrypt'])
       def print_menu():
            print("""
                         1) Encrypt files
                         2) Decrypt files
                         0) Exit
                           """)
       loop = True
       while loop:
                   print_menu()
                   menu = int(input("Your Choice :"))
                   passw = input("Enter Password to Encrypt this File : ")
                   file = input("Enter your File Name or Path here: ")
                   bufferSize = 64 * 1024
                   if menu == 1:
                        pyAesCrypt.encryptFile(file, file+".txt.aes", passw, bufferSize)

   
                   elif menu == 2:
                          pyAesCrypt.decryptFile(file, file+".txt", passw, bufferSize)
       print_menu()
    else:
           print("invalid input!")
else:
       print("BYE BYE")
                                          
                     
              
     
