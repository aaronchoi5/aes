Welcome to project2.py! I am excited to present to you an interactive encryption and decryption service!

Specs: Windows 10 pro(I don't think the pro matters) Python 3.4(Don't use Python 2.x and you'll be fine probably) Cryptography(the python library)

How to run: you should run python project2.py(make sure you have Cryptography the library first! Do a python -m pip install cryptography)

How to use: It's pretty easy. I used an almost foolproof prompt system. If you fail to give a proper response you will be punished by having to run python project2.py again. When you run the program, It will prompt you for either Key Generation, Encryption, or Decryption. If you choose Key Generation, it will generate a key and put it in the ../data/key.txt file. I also provide a default key file in case you just want to dive into the encryption and decryption. 

On that note, if you choose encryption you will be prompted for either CBC or ECB. Any other response will be punished by making you run the program again. The resulting ciphertext will be put in the ../data/ciphertext.txt file. If you choose decryption, you will be prompted for CBC or ECB too and then the original message will be put in the ../data/result.txt file. Please don't do a mix of CBC encryption and then ECB decryption or vice versa. You're going to have a bad time. It just doesn't work. I have provided default ciphertext, iv, key, plaintext, and result files. Have fun!(I tried to make it more entertaining since you're grading so many of these. I feel your pain. I used to be a grader too. Sorry. :p)