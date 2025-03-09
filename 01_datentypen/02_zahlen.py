if __name__ == "__main__":

    # Als Erstes deklarieren wir uns zwei Variablen, mit denen wir rechnen wollen. Wir beginnen mit Ganzzahlen,
    # in der Programmierung auch Integer (kurz int) genannt.

    a = 10
    b = 5

    # Einfache Grundrechenarten wie Addition, Subtraktion, Multiplikation, Division und Potenzen können mit dem
    # jeweiligen Rechenzeichen dargestellt werden. Für komplexere mathematische Rechenarten gibt es Funktionen in
    # speziell dafür angelegten Python Bibliotheken. Diese lernen wir später kennen.

    print(a + b)
    print(a - b)
    print(a * b)
    print(a / b)
    print(a ** b)

    # Hinweis: wenn du eine Zahl allein in print() ausgeben willst, ist das kein Problem. Möchtest du aber, dass die
    # Zahl in einem String steht, musst du den Integer zu einem String machen. Das erledigt die Funktion str().
    # Versuche, die Umwandlung durch str() zu entfernen und schau, was passiert!

    print("Die Zahl " + str(b) + " kannst du nur mit Text zusammen ausgeben, wenn du sie zu einem String umwandelst.\n")

    # Neben Integer gibt es auch noch Kommazahlen. Der Zahlentyp wird in der Programmierung float ("Fließkommazahl")
    # genannt. Mit floats kannst du die gleichen Berechnungen anstellen wie mit Integer. Deklariert werden sie so:

    g = 9.801
    pi = 3.1415
    e = 2.7182

    # Zahlen runden kann man mit der Funktion round(). Als zweiten Parameter kann man der Funktion die Anzahl der
    # Nachkommastellen mit übergeben.

    g_gerundet = round(g)
    pi_gerundet = round(pi)
    e_gerundet = round(e, 2)

    print(str(g) + " gerundet ist " + str(g_gerundet))
    print(str(pi) + " gerundet ist " + str(pi_gerundet))
    print(str(e) + " auf zwei nachkommestellen gerundet ist " + str(e_gerundet))
