from itertools import permutations

def decrypt(A, key):
    key_len = len(key)
    A2 = []
    for i in range(len(A)):
        new_value = A[i]^key[i%key_len]
        if 32 <= new_value <= 126:
            A2.append(new_value)
        else:
            A2 = []
            break
    return A2

with open("C:\\Users\\jeremy.doan\\OneDrive - IHS Markit\\Code\\Project Euler\\p059_cipher.txt", "r") as f:
    cypher_string = f.readline()

cypher_values = [int(i) for i in cypher_string.split(',')]
output = []
for key in permutations(range(97,123), 3):
    decrypted_values = decrypt(cypher_values, key)
    if len(decrypted_values) > 0:
        decrypted_text = "".join([chr(i) for i in decrypted_values])
        if "Euler" in decrypted_text:
            output.append([key, decrypted_text, sum(decrypted_values)])
            break

print(output)