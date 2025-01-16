def interval_decrypt(encrypted_message, interval):
    message = ''
    for i in range(0, len(encrypted_message), interval):
        message += encrypted_message[i]
    return message

print(interval_decrypt('Hfeelfllov yWdojrulwdi', 2)) #output: Hello World