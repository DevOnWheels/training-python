# Eine Übersicht aller Funktionen, mit denen du Listen bearbeiten kannst, findest du auf
# https://docs.python.org/3/tutorial/datastructures.html

if __name__ == "__main__":

    # Listen in Python sind eine Möglichkeit, mehrere Werte in einer Variablen zu speichern. Verwendungsbeispiele
    # für Listen können Aufzählungen sein, Datensätze aus einer Datenbank oder Teile eines Strings. Eine Liste wird
    # wie eine normale Variable deklariert, die einzelnen Werte werden von eckigen Klammern [] umschlossen und durch
    # Kommata getrennt.

    fruechte = ["Apfel", "Banane", "Orange", "Mango"]

    # Du kannst eine Liste über print() ausgeben lassen. Wenn du jedoch nur ein einzelnes Element ausgeben möchtest,
    # so musst du den Index des Elementes mit angeben. Stell dir vor, jedes Listenelement hat eine Nummer, über die
    # du jedes einzelne Element ansprechen kannst. Der Listenindex beginnt mit 0 und gibt das erste Element einer
    # Liste an. Wenn du dir das letzte Element einer Liste ausgeben lassen möchtest, kannst du das über einen
    # negativen Index machen. -1 ist also das letzte Element, -2 das vorletzte und so weiter.

    print("Das erste Element der Liste ist " + fruechte[0])
    print("Das vorletzte Element der Liste ist " + fruechte[-2] + "\n")

    # Es gibt einige nützliche Funktionen für Listen, die du auf jeden Fall kennen solltest. Du solltest wissen, wie
    # man die Länge einer Liste bestimmen und eine Liste in einen String zusammenfassen kann.

    # Wie lang eine Liste ist, kann dir die Funktion len() sagen.
    wie_viele_fruechte = len(fruechte)
    print("Es sind " + str(wie_viele_fruechte) + " Früchte!\n")

    # Fasse eine Liste in einen String zusammen. Verwende ein Trennzeichen, um alle Elemente in einem String
    # aneinander zu reihen. Die Schreibweise ist etwas merkwürdig: als Erstes gibst du das Trennzeichen an, und in
    # der Funktion join() übergibst du dann die Liste, die zusammengefasst werden soll.
    trennzeichen = ", "
    obstsalat = trennzeichen.join(fruechte)
    print("In unseren Obstsalat kommt: " + obstsalat + "\n")

    # append() fügt ein Element der Liste hinzu
    print("Füge Weintrauben zum Obstsalat hinzu!")
    fruechte.append("Weintrauben")
    print(fruechte, "\n")

    # remove() entfernt ein Element aus der Liste
    print("Entferne Mango, wer mag die schon...")
    fruechte.remove("Mango")
    print(fruechte, "\n")
