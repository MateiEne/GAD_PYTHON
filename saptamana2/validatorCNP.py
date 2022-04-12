CNP = input("introduceti CNP: ")

sex = CNP[0]
an = CNP[1:3]
luna = CNP[3:5]
ziua = CNP[5:7]
judet = CNP[7:9]
nnn = CNP[9:12]
cifra_control = CNP[-1]

validator = "279146358279"


def e_cifra_control_buna(c):
    sum = 0

    for i in range(len(validator)):
        p = int(validator[i]) * int(CNP[i])
        sum += p

    if sum % 11 is int(c):
        return True

    return False


if len(CNP) < 13 or len(CNP) > 13:
    print("lungimea CNP ului nu este valida")
elif sex > '9':
    print("sexul nu este valid")
elif an > '99':
    print("anul este invalida")
elif luna > '12':
    print("luna este invalida")
elif ziua > '31':
    print("ziua este invalida")
elif '46' < judet < '51' or judet > '52':
    print("judetul este invalid")
elif nnn > '999':
    print("nnn este invalid")
elif not e_cifra_control_buna(cifra_control):
    print("cifra de control nu este valida")
else:
    print("CNP valid")