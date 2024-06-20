#dictionary of morze alphabet
azbuca = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    'Q': '--.-',
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----."
}
#we input a string value and transforming it into uppercase , as are the keys in the dictionary
#also we delete each gap in sentence if it is a sentence , if it will be just a word , the morse 
# values will be separated by one gap
n = str(input().replace(" ", "").upper())
for s in n:
    if s in azbuca:
        if s == " ":
            print(" ", end="")
        else:
            s1 = azbuca[s]
            print(s1, end=" ")