from Crypto.PublicKey import RSA
key = RSA.generate(4096)
f = open('./e-commerce protocol/my_rsa_public.pem', 'wb')
f.write(key.publickey().exportKey('PEM'))
f.close()
f = open('./e-commerce protocol/my_rsa_private.pem', 'wb')
f.write(key.exportKey('PEM'))
f.close()

f = open('./e-commerce protocol/my_rsa_public.pem', 'rb')
f1 = open('./e-commerce protocol/my_rsa_private.pem', 'rb')
key = RSA.importKey(f.read())
key1 = RSA.importKey(f1.read())

x = key.encrypt(b"dddddd",32)

print(x)
z = key1.decrypt(x)
print(z)