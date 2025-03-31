#Made by xxxb
#importieren
import random
import time
import math
import os
#Bildschirm leeren
os.system('clear')
#Windoof Variante:
#os.system("cls")
#für jedes LevelListe von Sätzen definieren
Sätze1 = ["falls", "kalk", "saal", "dallas", "als", "klös", "alaska", "das", "las", "kafka", "öl", "aal", "fkk", "kajak", "lass das", "fass", "alfa", "salsa", "fall"]
Sätze2 = [" enden jenen kenne den denken senden senken","lenken jens elan senf ölen allen danke dekan faden","nadel laken lösen laden fassen lassen fallen","klaffen allenfalls denen kennen nennen denn ende","jene enkel essen denke jenes könne jeden lesen","nasen dessen essens öffnen landen fanden fallendes","jedenfalls können seele dann es an kann je jede jedes","edles des ans elf and alle fand dank sank sense","nelke esel lesende danken flennen nase ekeln","ölkanne klassen flanke löffel jeans köln kassen","skandalös kekse kaskade dösen edel fesseln kasse dösen","enden fesseln senden senf faden fassen denen jene","könne essens jedenfalls an edles alle skandalös","danken ekeln jenen senken ölen nadel lassen kennen","enkel jeden öffnen können kann des fand sense","flennen ölkanne löffel jeans edel kenne kasse lenken","allen laken fallen nennen essen lesen landen seele","je ans dank kekse nelke klassen köln den jens","danke lösen klaffen denn denke nasen fanden dann","jede elf sank kaskade esel nase flanke kassen","denken elan dekan laden allenfalls ende jenes","dessen fallendes es jedes and lesende"]
Sätze3 = ["frei drei rein rief drin einer kreis darin","reise risse freie reine realisieren deiner dieser","kinder lieder seiner keiner leider friede freien","rinnen kreise leiser feiern nieder innere reinen","reisen riefen derlei inneren kleiner kindern","frieden liefern radikal einander niederen friedens","allerlei kleinere radikale kleineren radikalen","kassieren aneinander dir irre freier erinnere erinnern","keinerlei definieren kandidieren in er derer die der","nie ein sie ins redner rinnen dar irren klarer","anderer fördern fiel ideal niesen eid iris riss","reifen seife fieser diesel kreisel jener ranken","inder föderal fernreise frieren frisieren drinnen","feiner erde irland klirren erlösen riese denkerin","franken körner karin sören reis siri senfei kreisend","krise rinne rinnsal ski keller eile sissi filiale","frei einer freie kinder friede feiern riefen","frieden friedens radikalen freier kandidieren der","redner anderer rinne riss diesel inder frieren","irland denkerin franken senfei filiale drei kreis","reine lieder freien nieder derlei liefern allerlei","kassieren erinnere in nie rinnen fördern rinnsal ski","keller reifen frisieren klirren körner reis","kreisend rein darin realisieren seiner rinnen innere","inneren radikal kleinere aneinander erinnern er ein","dar niesen seife kreisel drinnen karin siri","krise eile rief reise deiner keiner kreise fiel","reinen kleiner einander radikale dir keinerlei","derer sie irren jener föderal feiner erlösen sören","sissi drin risse dieser leider leiser ideal reisen","kindern niederen kleineren irre definieren die ins","klarer eid iris fieser ranken fernreise erde riese"]
Sätze18 = ["Grund der Störung: defekte Leitung.","In guter Erinnerung.","Ein Grad Celsius.","Es ist alles fertig.","Es stand nicht dran.","Gut ist nicht gut genug.","Geniale Köche grillen Grillgut.","Sein Gang ist gestört durch defekte Gelenke.","Der Mann eilte mutig aus dem Ort.","Auf dem Kirchhof.","Dann kamen die Masern.","Die Anforderungen an das Fundament.","Dummheit möge angenehm sein.","Das ist mal nett.","Und an Mahnungen hat es nicht gefehlt.","Momos Oma kommt.","Wir wollen nach Buenos Aires.","Bitte wie gewöhnlich an die alte Adresse.","Aber der Bau ist eben nicht nur ein Rettungsloch.","Die Chinesische Mauer ist an ihrer nördlichsten Stelle beendet worden.","Die Wall Street meldet Wachstum.","Marion wurde immer röter.","Ein schwaches Kichern entstand.","Ich bin ein Berliner.","Der Zoll zollte.","Der Zahnarzt zog den Zahn.","Das wird jetzt anders werden, hoffe ich.","Lange horchte ich ihm noch in die Stille nach, ehe ich wieder zu arbeiten begann.","Setz deinen Hut auf.","Und er war es in der Tat;","Das bezog sich auf Gedanken so gut wie auf Menschen.","Ich denke, sie werden diese Nacht den alten Huber holen.","Die Königin sagte: Ganz gut gelungen.","Der Zug hatte zig Waggons.","Der Zirkusdirektor zeigte stolz seine Zirkuszelte.","Mein Partner ist vor Ort.","Er rappelte sich auf.","Es spricht manches dagegen.","Sie hob stolz den Kopf.","Dann aber empfand sie doch Reue.","Ich rede hier nicht von irgendwelchen hohen Gedanken, sondern von jedem kleinen Unternehmen der Kinderzeit.","Da stand sie schon mit den Koffern vor ihrem Haus.","Peter nahm seinen Preis in Empfang.","Papa verpasste den Zug.","Er verklagte praktisch jede und jeden.","Der Vater packte die prallvolle Picknicktasche.","Übrigens fahre ich nächste Woche in Urlaub.","Übrigens besteht zwischen uns dieser Unterschied heute noch ähnlich.","In dieser Weise bewegten sich nicht die Überlegungen, aber das Gefühl des Kindes.","Es ist eine neue Welt, die neue Kräfte gibt, und was oben Müdigkeit ist, gilt hier nicht als solche.","Lieber hielt ich mich ans Tatsächliche und Fortwährende.","Ich war unbeständig, zweifelhaft.","Und er machte sich nochmal darüber.","Das ist merkwürdig, ich sehe hier auch nicht ganz klar.","Es ist, wie wenn einer gehängt werden soll.","Und noch weitere unnütze Entdeckungen mache ich.","Nicht anders dürfte es sich mit der Religion verhalten.","Irgendeine Ahnung dessen, was ich sagen will, hast du merkwürdigerweise.","Ich gehe deshalb den Gang abwärts bis zum Burgplatz und beginne dort zu horchen.","Quietscht es regelmäßig?","Es war wohl ziemlich heiß in der Schule?","Hüpfen die?","Warum denn küssen?","Wer hindert dich denn?","Unter dir lag schließlich am meisten.","Gehst du zum Essen nach Haus?","Die Ausreißer kehrten vergnügt zurück.","Und je höher die Leistung, desto größer die Anforderungen.","Nun ist es keine Arbeit mehr, nun rollt und fließt das Ganze fast von selbst hinab.","Ein quengelndes Kind quetscht die Quietscheente.","Berechne die Größe der Quadratwurzel.","Xylophon spielen ist schwer - ich lerne es fix.","Das Saxophon zischt nur - es ist verflixt.","Der DAX-Wert stieg um zwölf Punkte.","Methan/Ethan/Propan/Truthahn","Eine Hexe namens Lili?","Tausend Yen kostete die Vase.","Lydia pickte auf ihrem Teller herum, mir sah sie bewundernd zu.","Im Training übte er mit seinen Trainerinnen Xena und Yara.","Achtung! Abstand halten! (wegen des Unfallrisikos)","Sie nannte den Stadtteil immer Prenzl'berg!","Ach Unsinn!","Garstiger Junge!","Man müsse es doch als 'Schiff' betrachten.","Welch ein Held war Udo geworden!","Nach dem Zitat 'Nicht drunter, sondern drüber'.","Rufst Du mich an? (Meine Nummer lautet 67584930)","In den 80er Jahren; ich war ungefähr 40.","Wahnsinn, bei dem Konzert waren über 10 000 Personen!","Sagt die 0 zur 8: 'Schicker Gürtel!'","Sie hat im Lotto gewonnen - 1,5 Millionen. Man glaubt es nicht!","Mit einer 6 in Mathe braucht er gar nicht erst nach Hause zu kommen!","Ich arbeite nun schon 50 % meines bisherigen Lebens bei Schmidt & Söhne.","20 € sind mir zu viel!","Heißa! Ich hab 144 € gewonnen.","Merke Dir unbedingt diesen Sicherheitscode: #1234","Bitte senden Sie eine E-Mail an Herrn Mustermann (mustermann@beispielfirma.com).","Sie sagte: Genau das ist es.","Er rechtfertigte: Er hat Schaden ertragen.","In der Regel."]
#Willkommensbotschaft/Einführung senden
print("Willkommen zu Tipp X! Du wirst aufgefordert werden, Zahlen, Buchstaben, Wörter und Sätze einzugeben. Du musst jede Eingabe mit der Entertaste bestätigen. Viel Spaß!")
#Level abfragen
Level = input("ÜBERSICHT LEVEL:\nJedes Level beinhaltet alle Zeichen aus dem vorherigen Level!\n1: Grundstellung\n2:e,n\n3:r,i\n18: Alle Zeichen\nWelches Level möchtest du trainieren? ")
#Failsafe
while Level != "1" and Level != "2" and Level != "3" and Level != "18":
    Level = input("Ungültige Eingabe. Bitte tippe die entsprechende Nummer! ")
#Sätze aus der Liste importieren
if Level == "1":
    Sätze = Sätze1
elif Level == "2":
    Sätze = Sätze2
elif Level == "3":
    Sätze = Sätze3
elif Level == "18":
    Sätze = Sätze18
#Variabeln (zurück)setzen
Richtig = 0
Falsch = 0
Anschläge = 0
Tipp =""
#Trainierungszeit abfragen
Zeit = input("Wie viele Minuten möchtest du trainieren? ")
#Failsafe
while 1 == 1:
    try:
        if float(Zeit) < 1:
            Zeit = input("Ungültige Eingabe! Tippe die Minutenanzahl als Zahl (mindestens 1).  ")
        if float(Zeit)>=1:
            Zeit = float(Zeit)*60
            break
    except ValueError:
        Zeit = input("Ungültige Eingabe! Tippe die Minutenanzahl als Zahl (mindestens 1).  ")
#initialisieren des Satzes
Satz = str((random.choice(Sätze)))
#Startzeit speichern
Startzeit = time.time()
#Satz abtippen lassen
Tipp = input("Tippe diesen Satz:\n" + Satz + "\n")
#Hauptschleife
while time.time() - Startzeit < Zeit: #läuft, solange Die Zeit nicht abgelaufen ist.
    while Tipp != Satz: #solange das getippte falsch ist, nochmal versuchen lassen
        Anschläge += len(str(Tipp)) #Anschläge zählen
        Falsch += 1 #zählen,wie viele Fehler gemacht wurden
        Tipp = input("Falsch. Tippe diesen Satz:\n" + Satz + "\n") #Nochmal versuchen
    Richtig += 1 #Zählen, wie oft es richtig war
    Anschläge += len(str(Tipp)) #Anschläge zählen
    Satz = str((random.choice(Sätze))) #Neuer Satz
    Tipp=input("Richtig. Tippe diesen Satz:\n" + Satz + "\n") #Satz abtippen lassen
#Wenn die Zeit zu Ende ist, den letzten Versuch prüfen
if Tipp != Satz:
    Anschläge += len(str(Tipp))
    Falsch += 1
    print("Falsch.")
if Tipp == Satz:
    Richtig += 1
    Anschläge += len(str(Tipp))
    print("Richtig.")
#Bildschirm leeren
os.system('clear')
#Windoof Variante:
#os.system("cls")
#Resultat ausgeben
print("\nDas Training ist beendet\nRESULTAT\nRichtige Sätze: " + str(Richtig) + "\nFehlgeschlagene Versuche: " +str(Falsch) + "\nFehlerquote: " +(str(round(Falsch/(Falsch+Richtig)*100))+"%") + "\nAnschläge pro Minute: "+str(round((int(Anschläge)/(Zeit/60)))))
