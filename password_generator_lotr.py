from random import randint

# List for Lord of The Rings themed words
lotr_words = ["bardthebowman", "eowyn", "thering", "faramir", "boromir", "hobbitstoisengard", "isengard", "orcs", "thehobbit", "returnoftheking", "fellowshipofthering", "twotowers", "shire", "middle-earth", "frodobaggins", "sauron", "hobbit", "silmarillion", "onering", "samwisegamgee", "lordoftherings", "ent", "tombombadil", "aragorn", "mistymountains", "minastirith", "pipe-weed", "helmsdeep", "moria", "gollum", "smaug", "bilbobaggins", "gimli", "riveranduin", "pathsofthedead", "saruman", "gandalf", "galadriel", "elrond", "fangorn", "darklord","battleofevermore", "wherewasgondor", "gondor", "theoden", "pippin", "merrybrandybuck", "deadmarshes", "pelennorfields", "arwen", "halfling", "treebeard", "mellon", "speakfriendandenter", "tolkien"  ]

# User specified password length option
specify_length = input("Would you like to specify the length of your new password? Type \"y\" for yes or \"n\" for no.")
# Illiterate user debugging
if (specify_length != "y") and (specify_length != "n"):
    raise TypeError("Please only enter \"y\" or \"n\".")

# Password length
if specify_length == "y":
    password_length = int(input("Please specify the length of your password. Use a number between 8 and 24" ))
    # Stupid user debugging
    if not type(password_length) is int:
        raise TypeError("Please enter a number")
    elif (password_length < 8) or (password_length > 24):
        raise Exception("Please enter a number between 8 and 24.")
else:
    password_length = randint(8, 24)

# User specified special characters option
user_special_ch = int(input("How many special characters would you like to have in your password? Choose up to 3"))
# Illiterate user debugging
if not type(user_special_ch) is int:
    raise TypeError("Please enter a number")
elif user_special_ch > 3 or user_special_ch < 1:
    raise Exception("Please enter a number between 1 and 3")

# User specified characters to numbers option
user_customize_ps = input("Would you like to change some characters to similar numbers? Press \"y\" for yes and \"n\" for no.")
# Illiterate user debugging
if user_customize_ps != "y" and user_customize_ps != "n":
    raise Exception("Please only enter \"y\" or \"n\".")

# Special characters for password
special_ch = "!#%&?*¤$£@+-"
# length of scpecial characters string
ch_count = len(special_ch)

# Function for generating lord of the rings string for the password
def password_generator(password_length):
    suitable_passwords = []
    for word in lotr_words:
        if len(word) <= (int(password_length) - 4) and len(word) >= (int(password_length) - 5):
            suitable_passwords.append(word)
    password = suitable_passwords[randint(0, len(suitable_passwords))]
    return str(password)

# Function to capitalize some letters
def capitalize():
    password = password_generator(password_length)
    l_p = len(password)
    count12 = 0
    while count12 < 3:
        indx = randint(0, l_p)
        password = password[:indx] + password[indx].upper() + password[indx + 1:]
        count12 += 1
    return password

# Function for adding special characters and numbers
def specialize():
    password = capitalize()
    #Loop for special characters
    count1 = 0
    while count1 < int(user_special_ch):
        password += str(special_ch[randint(0, ch_count)])
        count1 += 1
    # Loop for numbers in password
    while len(password) < int(password_length):
        password +=  str(randint(0, 9))
    return password

# Function for changing some letters to numbers
def letters_to_numbers():
    password = specialize()
    l_to_n = {"i": "1", "e": "3", "a": "4", "s": "5", "b": "6", "o": "0"}
    keys = list(l_to_n.keys())
    for ch in password:
        if ch in keys:
            password = password.replace(ch, l_to_n[ch])
    return password

# Depending on user choice output the password
if user_customize_ps == "y":
    print("Your new password is:" + str(letters_to_numbers()))
else:
    print("Your new password is: " + specialize())