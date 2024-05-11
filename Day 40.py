import random 
import string

def generate_random_chars():
    return ''.join(random.choice(string.ascii_letters) for _ in range(3))

def encoder(x):

    final = []
    words = x.split(" ")

    for word in words:

        if(len(word) >= 3):
            first_letter = word[0]
            new_str = generate_random_chars() + word[1:] + first_letter + generate_random_chars()
            final.append(new_str)          
        
        else:
            new_str = word[::-1]
            final.append(new_str)

    return final 

def decoder(x):

    final = []
    words = x.split(" ")

    for word in words:
        
        if(len(word) >= 3):
            last_letter = word[-4]
            new_str = last_letter + word[3:-4] 
            final.append(new_str)

        else:
            new_str = word[::-1]
            final.append(new_str)

    return final
    

# data = input("Enter the string you wanna encode : ")
# encoded_data = encoder(data)
# print(f"encoded data : {" ".join(encoded_data)}")

# decoded_data = decoder(encoded_data)
# print(f"decoded data : {" ".join(decoded_data)}")

for i in range(100):

    a = input("Enter encode, decode or exit to perform instruction : ")

    if(a == "encode"):
        data = input("Enter the string you wanna encode : ")
        encoded_data = encoder(data)
        print(f"encoded data : {" ".join(encoded_data)}")

    elif(a == "decode"):
        encoded_data = input("Enter the string you wanna decode : ")
        decoded_data = decoder(encoded_data)
        print(f"decoded data : {" ".join(decoded_data)}")

    else:
        break
