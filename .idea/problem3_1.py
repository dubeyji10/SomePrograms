def problem3_1(txtfilename):
    with open(txtfilename,"r") as asd:
        characters = 0
        for item in asd:
            characters += len(item)
            print(item, end="")
        print("\n\nThere are", characters, "letters in the file.")
        asd.close()

problem3_1("HumptyDumpty.txt")