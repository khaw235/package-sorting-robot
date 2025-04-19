def sort(uidth, height, length, mass):
    volume = uidth * height * length
    is_bulky = (volume >= 1000000) or (uidth >= 150 or height >= 150 or length >= 150)
    is_heavy = mass >= 20
    return "REJECTED" if is_bulky and is_heavy else "SPECIAL" if is_bulky or is_heavy else "STANDARD"

print(sort(200, 150, 180, 25))