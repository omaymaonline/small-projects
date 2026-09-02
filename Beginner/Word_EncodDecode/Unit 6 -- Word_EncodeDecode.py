print("Welcome to the Secret Message Encoder/Decoder!\n")

message = input("Enter a message: ")

#Split the message into words
words = message.split()

#Reverse each word (slicing)
reversed_words = [word[::-1] for word in words]

#Join them back into a string
encoded = " ".join(reversed_words)

#Reverse the entire string (slicing again)
encoded = encoded[::-1]

print(f"\nEncoded message: {encoded}")

#Reverse the process
decoded = encoded[::-1]
decoded_words = decoded.split()
original = " ".join([word[::-1] for word in decoded_words])  # Reverse words back

print(f"Decoded message: {original}")
