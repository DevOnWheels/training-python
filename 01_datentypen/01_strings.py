# In diesem Teil des Python-Trainings lernen wir, wie wir String-Funktionen verwenden.
# Ich werde nicht alle Funktionen, die es gibt, erklären. Falls es dich interessiert, findest du hier eine
# Gesamtübersicht über alle String-Funktionen: https://docs.python.org/3/library/stdtypes.html#string-methods

if __name__ == "__main__":

    # Mehrzeiligen Text schreibt man in Python in runden Klammern (). Die Klammern signalisieren Python: "Diese Zeilen
    # gehören zum gleichen Text". Innerhalb eines Textes kannst du Steuerzeichen (Escape Sequences genannt) wie z. B.
    # einen Zeilenumbruch (das \n im Text) verwenden. Eine Liste (auf Englisch) aller Escape Sequences findest du in
    # der Python Dokumentation: https://docs.python.org/3/reference/lexical_analysis.html#escape-sequences

    greeting = ("Willkommen zurück zum ersten Teil des Python-Trainings.\nWie man Variablen deklariert und ausgibt, "
                "hast du ja bereits in der main.py Datei gelernt.\nNun schauen wir uns an, wie man Strings in Python "
                "verwenden und manipulieren kann.\n")

    print(greeting)

    # In Python wird es immer mal nötig sein, Eingaben des Benutzers abzufragen. Dazu gibt es den Befehl input().
    # input() erwartet als Parameter einen String, der sozusagen die Eingabeaufforderung formuliert. In der main.py
    # Datei habe ich dich noch mit "Du" angesprochen. Mithilfe der input() Funktion kann ich dich nun auffordern, mir
    # deinen Namen zu verraten. Deine Eingabe speichere ich wieder in der Variable dein_name und gebe sie aus.

    dein_name = input("Verrate mir bitte deinen Namen: ")
    print("Vielen Dank, " + dein_name + "! Jetzt können wir weitermachen.\n")

    # Beginnen wir mit ein paar einfachen String-Manipulationen. Wie man Strings aneinander ketten kann, habe ich ja
    # bereits erklärt. Strings bieten eine Reihe von Funktionen an, die den String verändern können. Sie können ihn in
    # Klein- und Großbuchstaben umwandeln oder jedes Wort mit einem Großbuchstaben beginnen lassen.
    # Hier sind ein paar Beispiele.

    # lower() wandelt einen String in Kleinbuchstaben um
    kleinbuchstaben = "Als erstes testen wir Kleinbuchstaben..."
    kleinbuchstaben = kleinbuchstaben.lower()
    print(kleinbuchstaben)

    # upper() ist das Gegenteil zu lower() und wandelt einen String in Großbuchstaben um
    grossbuchstaben = "... und dann kommen Großbuchstaben dran."
    grossbuchstaben = grossbuchstaben.upper()
    print(grossbuchstaben)

    # title() wandelt den ersten Buchstaben eines jeden Wortes in einen Großbuchstaben um
    titel = "Dies ist ein besonderer Moment.\n"
    titel = titel.title()
    print(titel)

    # Kommen wir nun zu ein paar aufwändigeren, aber auch nützlicheren Funktionen. Meist muss man Daten verarbeiten,
    # die nicht dem Format entsprechen, das man erwartet. Du solltest in der Lage sein, Strings in Teile zu splitten,
    # Ersetzungen vornehmen zu können oder mit Teilen des Strings zu arbeiten.

    # replace(alt, neu) ersetzt in einem String einen alten Wert gegen einen neuen Wert
    ersetzung = "Hello World"
    ersetzung = ersetzung.replace("World", dein_name)
    print(ersetzung + " (es wurde World durch " + dein_name + " ersetzt)\n")

    # split(trennzeichen) zerteilt einen String in eine Liste
    langer_string = "Dies ist ein langer String"
    print(langer_string)

    einzelne_worte = langer_string.split(" ")
    print(einzelne_worte)
    print("Hinweis: wie wir Listen [...] behandeln, schauen wir uns demnächst an!\n")

    # Wenn wir genauer wissen wollen, an welcher Stelle ein String in einem anderen String enthalten ist,
    # liefert index() uns die Position. Denke daran, das in der Programmierung die Zählung bei 0 anfängt!
    pruef_string = "dolor"
    test_string = "Lorem ipsum dolor sit amet"
    pruef_position = test_string.index(pruef_string)
    print("\"" + pruef_string + "\" steht in \"" + test_string + "\" an folgender Stelle:", pruef_position)
    print("Hinweis: wie wir mit Zahlen (Ganz- und Kommazahlen) umgehen, schauen wir uns demnächst an!\n")

    # Du kannst mit dem Schlüsselwort "in" prüfen, ob ein String in einem anderen String enthalten ist
    pruef_string = "dolor"
    test_string = "Lorem ipsum dolor sit amet"
    ist_enthalten = pruef_string in test_string
    print("Ist \"" + pruef_string + "\" in \"" + test_string + "\" enthalten?", ist_enthalten)
    print("Hinweis: wie wir mit boolschen Werten (True / False) umgehen, schauen wir uns im nächsten Kapitel an!\n")

    print("Lasst uns mit dem nächsten Datentyp weitermachen: Zahlen. Viel Spaß!")