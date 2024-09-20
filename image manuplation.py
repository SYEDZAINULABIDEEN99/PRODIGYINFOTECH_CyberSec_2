# try block to handle the exception
try:
    while True:
        # ask if the user wants to encrypt or decrypt
        mode = input("Do you want to encrypt or decrypt? (e/d): ").lower()

        if mode not in ['e', 'd']:
            print('Invalid choice! Please enter "e" for encryption or "d" for decryption.')
            continue

        # take path of image as a user input
        path = input("Enter the full path of the image file: ")

        # taking encryption/decryption key as input
        key = int(input('Enter Key for encryption/decryption of the Image: '))

        # print path of image file and decryption key that we are using
        print('The path of file: ', path)
        print('Note: Encryption key and Decryption key must be the same.')
        print(f'Key for {"Decryption" if mode == "d" else "Encryption"}: {key}')

        # open file for reading purpose
        with open(path, 'rb') as fin:
            # storing image data in variable "image"
            image = fin.read()

        # converting image into byte array to perform encryption/decryption easily on numeric data
        image = bytearray(image)

        # performing XOR operation on each value of bytearray
        for index, value in enumerate(image):
            image[index] = value ^ key

        # open file for writing the encrypted/decrypted data back to the same file
        with open(path, 'wb') as fout:
            fout.write(image)

        print(f'{ "Decryption" if mode == "d" else "Encryption" } Done!')

        # ask if the user wants to continue or quit
        choice = input("Do you want to continue? (yes/no): ").lower()
        if choice != 'yes':
            print('Exiting the program.')
            break

except FileNotFoundError:
    print('Error: File not found. Please check the file path.')

except ValueError:
    print('Error: Invalid key entered. Please enter a numeric value.')

except Exception as e:
    print('Error caught: ', str(e))
