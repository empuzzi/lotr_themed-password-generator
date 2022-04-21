from random import randint

# List for Lord of The Rings themed words

lotr_words = ["bard the bowman", "eowyn", "the ring", "faramir", "boromir", "hobbits to isengard", "isengard", "orcs", "the hobbit", "return of the king", "fellowship of the ring", "two towers", "shire", "middle-earth", "frodo baggins", "sauron", "hobbit", "silmarillion", "one ring", "samwise gamgee", "lord of the rings", "ent", "tom bombadil", "aragorn", "misty mountains", "minas tirith", "pipe-weed", "helms deep", "moria", "gollum", "smaug", "bilbo baggins", "gimli", "river anduin", "paths of the dead", "saruman", "gandalf", "galadriel", "elrond", "fangorn", "dark lord","battle of evermore", "where was gondor?!", "gondor", "theoden", "pippin", "merry brandybuck", "dead marshes", "battle of pelennor fields", "arwen", "halfling", "treebeard", "mellon", "speak friend and enter", "tolkien"  ]
password_length = ""

# User specified password length
specify_length = input("Would you like to specify the length of your new password? Type \"y\" for yes or \"n\" for no.")

if specify_length == "y":
    password_length = input("Specify the length of your password: " )
elif specify_length == "n":
    password_length = randint(5, 16)

# User specified special characters
special_ch = "!#%&?*¤$£@+-"
user_special_ch = input("How many special characters would you like to have in your password?")
ch_count = len(special_ch)

# Function for generating the password
def password_generator(password_length):
    suitable_passwords = []
    for word in lotr_words:
        if len(word) < int(password_length):
            suitable_passwords.append(word)

    suitable_length = len(suitable_passwords)
    password = suitable_passwords[randint(0, len(suitable_passwords))]
    password.strip(" ")

    #Loop for special characters
    count = 0
    while count < int(user_special_ch):
        password += str(special_ch[randint(0, ch_count)])
        count += 1
    
    # Loop for numbers in password

    while len(password) < int(password_length):
        password +=  str(randint(0, 9))
    return password.capitalize()

print("Your new password is: " + password_generator(password_length))