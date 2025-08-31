def encrypt(message):
    a=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    encrypted = ""
    for i in message:
        encrypted += a[a.index(i)+3]
    print(f"your message has been encrypted successfully {encrypted}")
def decrypt(encryption):
    a = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
         "w", "x", "y", "z"]
    decrypted = ""
    for i in encryption:
        decrypted += a[a.index(i) - 3]
    print(f"your message has been decrypted successfully {decrypted}")

encrypt("helloworld")
decrypt("khoorzruog")