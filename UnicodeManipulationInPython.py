
## due to the huge security issue are CVE risked a lot of platformas have enforced dettectiong of the obsification 
access_level = "user"
print(access_level)
if access_level != 'none' and access_level !='user': # Check if admin
    print("You are an admin.")
else:
    print("your are not a admin")


#however insertint Hidden unicode tags and the right slot changes this to:

access_level = "user"
print(access_level)
if access_level != 'none' and access_level !='user⁦': # Check if admin
    print("You are an admin.")
else:
    print("your are not a admin")
    
print("------------------------------------------------")

### comenting out example 
# this code looks like a mess in editor however if coppied into a normal text editor the code looks normal
# this can be used similar to make functions return early as shown below 
access_level = "user"
if access_level != 'none‮⁦': # Check if admin ⁩⁦' and access_level != 'user
    print("You are an admin.123")
else:
    print ("you are not a admin")

print("------------------------------------------------")

# ealry return
def authenticate(username, password):
    """admin check ⁧ """; return True  
    if username == "admin" and password == "secure123":
        return False
    else:
        return True

print("Welcome to Secure Login")
user = 'admin'
passwd = 'secure123'

if authenticate(user, passwd):
    print(" Access Granted!")
else:
    print(" Access Denied!")
###stretched string
Admin = False
"""‮ } ⁦if (Admin)⁩ ⁦ admins only section begings """
print ("You are an admin.")
""" admins only code section ends ‮ { ⁦"""

print("------------------------------------------------")
# invisable function using the example shown in part 1 we can create a invisable function 
# however this was forcable fixed across all version 
# top is cyrlic M 
def is_admiМ():
    return False

def is_admiM():
    return True

def main():
    if is_admiМ():
        print("You are an admin.")
    else:
        print("not admin")

if __name__ == '__main__':
    main()





    

