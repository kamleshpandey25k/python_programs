try:
    10/0
except:
 print()
 raise Exception("UNknown exception")
# try is used for write the risky code
# except is used for write the handler code
# else it comes after except and it it excute , if exception not occure
# raise it is used for generate the exception manually
#finally it is always run , does not matter exception occure or not
