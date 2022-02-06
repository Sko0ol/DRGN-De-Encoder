from colorit import *


def clean_the_string_and_decode_it(string):
    """
    Removes any unwanted things in that string like umlaute, special characters, \n and double whitespace.
    :param string: string to clean
    :return: cleaned string
    """

    string = string.replace("ü", "ue")
    string = string.replace("Ü", "Ue")
    string = string.replace("ä", "ae")
    string = string.replace("Ä", "Ae")
    string = string.replace("ö", "oe")
    string = string.replace("Ö", "Oe")
    string = string.replace("ß", "ss")
    string = string.replace(",", " ")
    string = string.replace(".", " ")
    string = string.replace("!", " ")
    string = string.replace("?", " ")
    string = string.replace(":", " ")
    string = string.replace(";", " ")
    string = string.replace("-", " ")
    string = string.replace("_", " ")
    string = string.replace(")", " ")
    string = string.replace("(", " ")
    string = string.replace("\n", " ")
    string = string.replace("  ", " ")
    string = string.replace("  ", " ")

    return string


print(color_front("============================ DRGN DE&ENCODER v1.0 ============================\n\n", 245, 219, 52))

print("Wenn sie die Datei Encoden wollen drücken sie |1|\n")
print("Wenn sie die Datei Decoden wollen drücken sie |2|")
choice = input(">")

if choice == "1":
    txtfile = input("Name of the txt file to Encode\n> ")

    try:
        fh = open(txtfile, encoding="utf-8")

    except:
        print("Die Datei konnte nicht gfunden werden!")
        exit()

    print(fh)

    fhlist = [line for line in fh]

    fh_string = "".join(fhlist)

    clean_fh_string = clean_the_string_and_decode_it(fh_string)

    lowerd_clean_string = clean_fh_string.lower()

elif choice == "2":
    pass


else:
    print("Der eingegebene parameter < " + choice + " > ist nicht valide!")
    exit()
