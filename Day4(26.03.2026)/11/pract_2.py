import re


string = "Ты супер редиска, и нехороший человек"

sub = re.sub(r"редиск\D|нехорош\D* человек\D*","*давайте жить дружно*",string)

print(sub)