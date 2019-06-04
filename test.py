from main import calculate

def main():
    memes = [('rollsafe.jpg', 202, 6),
             ('rollsafe1.jpg', 102, 16),
             ('rollsafe2.jpg', 700, 56),
             ('sad_pepe_compilation.gif', 410, 10),
             ('sad_pepe_compilation1.gif', 410, 30),
             ('sad_pepe_compilation2.gif', 110, 2),
             ('yodeling_kid.avi', 605, 12),
             ('yodeling_kid1.avi', 150, 40)
             ]
    print(calculate(1, memes))


main()
