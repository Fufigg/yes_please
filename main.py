import yes_please

s = input()
"""
encrypted = yes_please.encrypt_string_to_string(s)
print(encrypted)

"""
yes_please.encrypt_string_to_file(s, 'encrypt_string.txt', show_process=True)

text = yes_please.decrypt_file_to_string('encrypt_string.txt')
print(text)

"""
decrypted = yes_please.decrypt_string_to_string(encrypted)
print(decrypted)

"""