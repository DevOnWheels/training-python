# Dies ist ein Kommentar. Jeder Text, der mit einer Raute beginnt, wird von Python nicht ausgeführt und als
# Kommentar behandelt. Ich empfehle dir dringend, deinen Python Code gut zu kommentieren. Es ist wesentlich einfacher,
# nach einer längeren Pause deinen Code wieder zu verstehen, wenn er verständlich kommentiert ist. Es ist Python
# Standard, zwischen dem Text und der Raute ein Leerzeichen zu schreiben.

# Die erste Anweisung, die in deinem Python Script stehen muss (jedenfalls für den Anfang), ist folgende Zeile.
# Sie sorgt dafür, dass Python den Einstieg in dein Programm findet.

if __name__ == "__main__":

    # Um diesen Code ausführen zu lassen, öffne das Terminal (das vierte Symbol von oben, unten links in der Leiste)
    # und tippe den Befehl "python 01_datentypen\main.py" und drücke Enter. Es wird nun der unten stehende Code ausgeführt.

    # Als Erstes wollen wir etwas Text im Terminal ausgeben. Dazu gibt es den Befehl print(). Zwischen den Klammern
    # kannst du in Anführungszeichen beliebig langen Text schreiben, der dann im Terminal ausgegeben wird.

    print("Herzlich Willkommen im ersten Kapitel!")

    # Ein wichtiger Bestandteil von Python Code sind Variablen. Sie speichern Informationen wie z. B. Texte. Ein
    # Vorteil bei der Verwendung von Variablen ist, dass sie immer wieder verwendet werden können. Eine Variable
    # besteht immer aus ihrem Namen, gefolgt von einem Gleichheitszeichen und dem Wert. Name, Gleichheitszeichen und
    # Wert zusammen nennt man die Deklaration einer Variablen.

    # Als Beispiel deklarieren wir nun die Variable dein_name. Dabei ist "dein_name" ist der Variablenname, "Du" der
    # Variablenwert. Guter Python Standard ist es, das Variablennamen immer kleingeschrieben und Worte innerhalb des
    # Variablennamens mit einem Unterstrich getrennt werden.

    dein_name = "Du"

    # Du kannst die Variable nun in einem Text verwenden, indem du sie mit einem Pluszeichen an einen anderen Text
    # anhängst. Dabei ist es egal, wo du die Variable an einen Text anhängst. Auch mitten im Text ist möglich.

    print("Hallo " + dein_name + "! Schön, dass du an diesem Training teilnimmst.")

    # Als Nächstes wollen wir uns anschauen, wie man Texte bzw. Zeichenketten in Python verwendet und manipulieren
    # kann. Zeichenketten werden in Programmiersprachen als Strings bezeichnet. Ab sofort werden wir daher nur noch
    # von Strings reden. Öffne nun für die weiteren Übungen die Datei 01_datentypen\01_strings.py!
