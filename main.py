import yes_please

s = input()

encrypted = yes_please.encrypt_string_to_string(s)
print(encrypted)


yes_please.encrypt_string_to_file(s, 'encrypt_string.txt', show_process=True)


decrypted = yes_please.decrypt_string_to_string(encrypted)
print(decrypted)