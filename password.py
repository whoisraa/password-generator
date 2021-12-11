import random
import string

lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
digits = string.digits
symbols = string.punctuation
format = lowercase + uppercase + digits + symbols
length = 20
password = "".join(random.sample(format, length))

print(password)
