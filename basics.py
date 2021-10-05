user_name = input("Enter name")
surname = input("Enter Surname")
quote = input("Enter feeling")
message = f"Hello {user_name} {surname} How may i {quote} you"
message = "Hi %s %s may I %s you" %(user_name,surname,quote) 


types = [1,1.2,34]
types = [i for i in types if isinstance(i,int)]
print(types)