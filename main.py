import yes_please

s = input()
encrypted = yes_please.encrypt_string_to_string(s)
print(encrypted)

decrypted = yes_please.decrypt_string_to_string(encrypted)
print(decrypted)