N=input()
if(N.isalpha()):
    if(N=='a' or N=='e' or N=='i' or N=='o' or N=='u' or N=='A' or N=='E' or N=='I' or N=='O' or N=='U'):
        print("Vowel")
    else:
        print("Consnant")
else:
    print("Invalid")
