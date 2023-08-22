import requests

class main:

    def read_payload():
        file_path = "XSS-Latest.txt"

        with open(file_path, "r") as file1:
            Lines = file1.readlines()
            for line in Lines:
                return Lines
                 

     

print(main.read_payload())
