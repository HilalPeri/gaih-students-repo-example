#Day5 Final Project
#Knowledge Competition
points = 0
answer1 = str(input("A. Schreibe das Datum in Deutsch.\n "
                    "1) Republic Day: "))
if answer1 == "Tag der Republik":
    points=points + 10

answer2 = str(input("2) Mother’s Day: "))
if answer2 == "Muttertag":
    points = points + 10

answer3 = str(input("3) Christmas: "))
if answer3 == "Weihnachten":
    points = points + 10
answer4 = str(input("B. Schreibe die Jehreszeiten und  die Monate mit Artikeln.\n "
                    "4)	März, April, Mai: "))
if answer4 == "der Frühling":
    points = points + 10

answer5 = str(input("5) im Winter: "))
if answer5 == "der Dezember, der Januar, der Februar":
    points = points + 10

answer6 = str(input("6)	September, Oktober, November: "))
if answer6 == "der Herbst":
    points = points + 10

answer7 = str(input("der Sommer: "))
if answer7 == "der Juni, der Juli, der August":
    points = points + 10
answer8 = str(input("C.	Beantworten Sie die folgenden Fragen entsprechend der angegebenen Dialog.\n"
                    "+Guten Tag, was darf es sein?\n"
                    "-Ich hatte gern ein Kilo Kartoffeln.\n"
                    "+Gern, sonst noch etwas?\n"
                    "-Wie viel kostet der Salat?\n"
                    "+Nur 1,20 Euro\n"
                    "-Dann, nehme ich noch einen Salat und zwei Orangen. Das ist dann alles.\n "
                    "+Das macht zusammen 3,75 Euro.\n"
                    "8)	Wie viel kostet der Salat?\n"))
if answer8 == "1,20 Euro":
    points = points + 10

answer9 = str(input("9)	Was hat der Kunde gekauft? (Screiben Sie in der richtigen Reihenfolge und Menge.)\n"))
if answer9 == "ein Kilo Kartoffeln, einen Salat, zwei Orangen":
    points = points + 10

answer10 = str(input("10) Wie viele Euro hat der Kunde insgesamt bezahlt?\n"))
if answer10 == "3,75 Euro":
    points = points + 10

if points >= 60:
    print("Congratulations, you are successful. Your score is " , points)
else:
    print("You are unsuccessful. You have to practise more. Your score is ", points)