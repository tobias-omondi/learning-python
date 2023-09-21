# ask user their name 
name = input("what is your name ?").strip().title().split()

# # remove white space from str and caps   
# # name = name.strip().title()

# # capitalize Name
# name = name.title() 

# split user name into first name and last name
# first , last = name.split("")  

# say hello to user
print(f"Hello, {name}")



def hello(to= "world"):
    print("hello,", to )

hello()
name = input ("what is your dog name ?").strip().title()
hello (name)