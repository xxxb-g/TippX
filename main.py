# All rights reserved for now.
from argparse import ArgumentParser
import gettext
from pathlib import Path as _Path
import json

_localedir = _Path(_Path(__file__).parent, "locales")
_translation = gettext.translation("tippx", localedir=_localedir, fallback=True)
_ = _translation.gettext

parser = ArgumentParser(prog="TippX", description=_("Ein Programm, um das deutsche Zehnfinger-Schreibsystem zu trainieren."))
parser.add_argument("--debug", action="store_true", help=_("Debugging-Nachrichten zeigen"))
parser.add_argument("--dark_mode", action="store_true", help=_("aktiviere Dark Mode"))
args = parser.parse_args()
# globale Variable setzen
debugging = args.debug
dark_mode = args.dark_mode
print("Made by xxxb. All rights reserved.\n##################################\n")

from random import choice
from time import time
import pygame
from pathlib import Path
from requests import get
import threading
import webbrowser
import platform
import subprocess

# Initialize Pygame
pygame.init()

Fensterbreite = 1000
Fensterhöhe = 750
Version = "v1.1.3"
# Set up the game window
screen = pygame.display.set_mode((Fensterbreite, Fensterhöhe), pygame.RESIZABLE | pygame.DOUBLEBUF)
clock = pygame.time.Clock()
font = pygame.font.Font(Path(Path(__file__).parent, "xxxb-Font.otf"), 48)
pygame.display.set_caption("TippX")
UpdateCheckComplete = False
# Funktionen
latest_tag = Version

def popup(message, title=_("Bestätigung")):
    system = platform.system()

    if system == "Linux":
        try:
            result = subprocess.run(
                [
                    "zenity",
                    "--question",
                    f"--title={title}",
                    f"--text={message}",
                    "--ok-label=" + _("Ja"),
                    "--cancel-label=" + _("Nein"),
                ],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
            )
        except Exception as e:
            print(_("Folgender Fehler trat auf: ")+ str(e))
            raise RuntimeError(_("Folgender Fehler trat auf: ")+str(e))

        return result.returncode == 0

    elif system == "Windows":
        import ctypes
        result = ctypes.windll.user32.MessageBoxW(
            0,
            message,
            title,
            4 | 32,  # MB_YESNO | MB_ICONQUESTION
        )
        return result == 6  # 6 = Ja, 7 = Nein
    elif system == "Darwin":
        # macOS über AppleScript.
        nein_label = _("Nein")
        ja_label = _("Ja")
        script = f'''
display dialog "{message.replace('"', '\\"')}" with title "{title.replace('"', '\\"')}" buttons {{"{nein_label}", "{ja_label}"}} default button "{ja_label}"
'''

        result = subprocess.run(
            ["osascript", "-e", script],
            capture_output=True,
            text=True,
        )

        return f"button returned:{ja_label}" in result.stdout

    else:
        raise RuntimeError(_("Nicht unterstütztes Betriebssystem: ") + system)

def update_check():
    global latest_tag
    global Version
    global UpdateCheckComplete

    try:
        API_URL = "https://codeberg.org/api/v1/repos/xxxb/TippX/releases"
        response = get(API_URL, timeout=30)
        releases = response.json()

        latest = releases[0]

        latest_tag = latest["tag_name"]

        current_version = tuple(map(int, Version.lstrip("v").split(".")))
        newest_version = tuple(map(int, latest_tag.lstrip("v").split(".")))

        if newest_version > current_version:
            print({
                _("neueste Version:"): latest_tag,
                _("Veröffentlicht am"): latest["published_at"],
            })
            UpdateCheckComplete = True

        elif newest_version < current_version:
            print(_("Neuster offizieller Tag: {tag}. Du nutzt eine neuere Version.").format(tag=latest_tag))
            UpdateCheckComplete = False
        elif newest_version == current_version:
            UpdateCheckComplete = False
    except Exception as e:
        print(e)
threading.Thread(target=update_check, daemon=True).start()

if dark_mode:
    BLACK = (255,255,255)
    Hintergrund = (0, 0, 0)
else:
    BLACK = (1,1,1) #Das ist nicht (0,0,0), weil ich das lustig finde. Nicht, weil es eine Bedeutung hätte oder so.
    Hintergrund = (255,240,200)

def reset():
    # Fenstergröße ermitteln
    global Fensterbreite, Fensterhöhe
    Fensterbreite, Fensterhöhe = screen.get_size()
    if Stage <= 2: # Gets called every tick bc my code is spagethi (nevím jak se to píše).
        # Darkmode
        global BLACK
        global Hintergrund
        global anweisung_color
        global latest_tag
        global UpdateCheckComplete
        if dark_mode:
            BLACK = (255, 255, 255)
            Hintergrund = (0, 0, 0)
            anweisung_color = (145,240,55)
        else:
            BLACK = (1, 1,1)  # Das ist nicht (0,0,0), weil ich das lustig finde. Nicht, weil es eine Bedeutung hätte oder so.
            Hintergrund = (255, 240, 200)
            anweisung_color = (10, 10, 200)
        # Update
        if UpdateCheckComplete and Stage<=2:
            updaten = popup(_("Es ist ein Update verfügbar. Willst du es herunterladen?"), _("Update"))
            while UpdateCheckComplete:
                if updaten:
                    latest_tag = Version
                    webbrowser.open("https://codeberg.org/xxxb/TippX/releases/latest")
                    UpdateCheckComplete = False
                elif not updaten:
                    UpdateCheckComplete= False
                else:
                    time.sleep(0.01)
    screen.fill(Hintergrund)
def pgprint(text, font=pygame.font.Font(Path(Path(__file__).parent, "xxxb-Font.otf"), 48), color = (-1,-2,-3)):
    if color == (-1,-2,-3):
        global BLACK
        color = BLACK
    if type(text) != str:
        return("No String")
    else:
        return(font.render(text, True, color))
def isfloat(str):
    try:
        return(float(str))
    except ValueError:
        return(False)
if 'debugging' in locals():
    if not debugging:
        def dprint(text):
            return()
    elif debugging:
        def dprint(text):
            print(text)
else:
    def dprint(text):
            return()

# Setup new variables
try:
    file = open(".highscore.txt")
    highscore = file.read()
except Exception:
    file = open(".highscore.txt", "w")
    file.write("0")
    highscore = "0"
file.close()
anweisung_color = (10, 10, 200)
input_active = True
Level = ''
Duration = ''
duration = ''
Input = ''
Punkte = 0
Fehler = 0
Stage = 0
Backspace = True
CTRL = [False, time()]
pygame.mixer.init()
ding = pygame.mixer.Sound(Path(Path(__file__).parent, "Ding.wav"))
döp = pygame.mixer.Sound(Path(Path(__file__).parent, "Doeng.mp3"))
mute = _("(laut)")
döp.set_volume(0.21)
clock.tick(500)
def load_levels():
    lang = _translation.info().get("language")
    if lang:
        lang_file = _localedir / lang / "levels.json"
        if lang_file.is_file():
            try:
                with open(lang_file, "r", encoding="utf-8") as f:
                    return json.load(f)
            except Exception as e:
                dprint("Fehler beim Laden von " + str(lang_file) + ": " + str(e))
    fallback_file = _localedir / "de" / "levels.json"
    if fallback_file.is_file():
        try:
            with open(fallback_file, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception as e:
            dprint("Fehler beim Laden von " + str(fallback_file) + ": " + str(e))
    return []

Levels = load_levels()
Sätze = [lvl["sentences"] for lvl in Levels]

# Game loop
running = True
dprint("DEBUG: Start game loop")
while running:
    # screen reset
    reset()
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                raise SystemExit
            if event.type == pygame.QUIT:
                raise SystemExit
    if Stage == 0:
        while input_active and Stage == 0:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    raise SystemExit
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                        Stage += 1
                    elif event.key == pygame.K_BACKSPACE:
                        Level = Level[:-1]
                    elif event.key == pygame.K_ESCAPE:
                        raise SystemExit
                    elif event.key == pygame.K_d:
                        dark_mode = not dark_mode
                    elif event.key == pygame.K_m:
                        if mute == _("(stummgeschaltet)"):
                            ding.set_volume(1)
                            mute = _("(laut)")
                        elif mute == _("(laut)"):
                            ding.set_volume(0)
                            mute = _("(stummgeschaltet)")
            reset()
            Text = "TippX" + "\n\n" + _("Willkommen zu TippX!") + "\n" + _("Dies ist ein Trainer für das deutsche Zehnfinger-Schreibsystem.") + "\n" + _("Am Anfang legst du ein Level und eine Zeit fest.") + "\n" + _("Danach erscheinen Wortgruppen, die du so schnell und richtig wie möglich abtippst.") + "\n" + _("Am Ende erscheint eine Auswertung.") + "\n\n" + _("Du kannst mit:") + "\n" + _("- Escape: Abbrechen") + "\n" + _("- D: Dark Mode umschalten (im Menü)") + "\n" + _("- M: Richtig-Geräusch stummschalten {mute}").format(mute=mute) + "\n" + _("- Enter: Eingabe bestätigen.") + "\n" + _("Drücke Enter, um fortzufahren.")
            for i in range(len(Text.split("\n"))):
                if Text.split("\n")[i] == "TippX":
                    text = pgprint(Text.split("\n")[i], pygame.font.Font(Path(Path(__file__).parent, "xxxb-Font.otf"), 40), (200, 100, 0))
                elif i == len(Text.split("\n")) - 1:
                    text = pgprint(Text.split("\n")[i], pygame.font.Font(Path(Path(__file__).parent, "xxxb-Font.otf"), 40), anweisung_color)
                else:
                    text = pgprint(Text.split("\n")[i], pygame.font.Font(Path(Path(__file__).parent, "xxxb-Font.otf"), 20))
                screen.blit(text, (Fensterbreite/10, ((((Fensterhöhe-text.get_height())/len(Text.split("\n")))*i)+text.get_height()) - text.get_height()/2))

            pygame.display.flip()

    if Stage == 1:
        while input_active:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    raise SystemExit
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                        if Level.isdigit():
                            if int(Level) > 0 and int(Level) <= len(Levels):
                                input_active = False
                    elif event.key == pygame.K_BACKSPACE:
                        Level = Level[:-1]
                    elif event.key == pygame.K_ESCAPE:
                        raise SystemExit
                    elif event.key == pygame.K_d:
                        dark_mode = not dark_mode
                    else:
                        if input_active:
                            Level += event.unicode
            level = pgprint(_("Deine Eingabe: ")+Level, pygame.font.Font(Path(Path(__file__).parent, "xxxb-Font.otf"), 20), (200, 0, 0))
            reset()
            level_lines = [f"{idx:2d}: {lvl['name']}" for idx, lvl in enumerate(Levels, start=1)]
            Text = _("ÜBERSICHT LEVEL:") + "\n" + _("Jedes Level beinhaltet alle Zeichen aus allen vorherigen Level!") + "\n" + "\n".join(level_lines) + "\n\n" + _("Welches Level möchtest du trainieren? ")
            for i in range(len(Text.split("\n"))):
                text = pgprint(Text.split("\n")[i], pygame.font.Font(Path(Path(__file__).parent, "xxxb-Font.otf"), 20))
                if i == len(Text.split("\n")) - 1:
                    text = pgprint(Text.split("\n")[i], pygame.font.Font(Path(Path(__file__).parent, "xxxb-Font.otf"), 20), anweisung_color)
                screen.blit(text, (Fensterbreite/10, ((((Fensterhöhe-text.get_height())/len(Text.split("\n")))*i)+text.get_height()) - text.get_height()/2))
            text = pgprint(Text.split("\n")[len(Text.split("\n"))-1], pygame.font.Font(Path(Path(__file__).parent, "xxxb-Font.otf"), 20))
            screen.blit(level, (Fensterbreite / 10, ((((Fensterhöhe - text.get_height()) / len(Text.split("\n"))) * i) + text.get_height() * 2) - text.get_height() / 2))

            pygame.display.flip()
        else:
            Stage += 1
            dprint("DEBUG: Level="+str(Level))

    elif Stage == 2:
        Text = _("Wie viele Minuten lang möchtest du trainieren?")
        for i in range(len(Text.split("\n"))):
            text = pgprint(Text.split("\n")[i], pygame.font.Font(Path(Path(__file__).parent, "xxxb-Font.otf"), 20), anweisung_color)
            screen.blit(text, (Fensterbreite/2 - text.get_width()/2, ((((Fensterhöhe-text.get_height())/len(Text.split("\n")))*i)+text.get_height()) - text.get_height()/2))
        input_active = True
        while input_active:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        raise SystemExit
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                            if isfloat(Duration):
                                if float(Duration) >= 0.01:
                                    input_active = False
                                    start_time = time()
                                    dprint("DEBUG: Duration="+str(Duration))
                                    Duration_time = float(Duration)*60
                                    Stage += 1
                        elif event.key == pygame.K_BACKSPACE:
                            Duration = Duration[:-1]
                        elif event.key == pygame.K_ESCAPE:
                            raise SystemExit
                        elif event.key == pygame.K_g:
                            dark_mode = True
                        else:
                            if input_active:
                                Duration += event.unicode
                duration = pgprint(_("Deine Eingabe: ")+Duration, pygame.font.Font(Path(Path(__file__).parent, "xxxb-Font.otf"), 20), (200, 0, 0))
                screen.blit(duration, (Fensterbreite / 2 - text.get_width() / 2 - pgprint(_("Deine Eingabe: "),pygame.font.Font(Path(Path(__file__).parent, "xxxb-Font.otf"),20),(200, 0, 0)).get_width(), ((((Fensterhöhe - text.get_height()) / len(Text.split("\n"))) * i) + text.get_height() * 2) - text.get_height() / 2))
                screen.blit(text, (Fensterbreite/2 - text.get_width()/2, ((((Fensterhöhe-text.get_height())/len(Text.split("\n")))*i)+text.get_height()) - text.get_height()/2))
                pygame.display.flip()
                reset()
    elif Stage == 3:
        while not float(start_time)+float(Duration_time) <= float(time()):
            input_active = True
            while input_active and not float(start_time)+float(Duration_time) <= float(time()):
                Match = False
                Backspace = False
                current_level = Levels[int(Level)-1]
                Text = str(choice(current_level["sentences"]))
                require_enter = current_level.get("require_enter", len(Text) > 10)
                while not float(start_time)+float(Duration_time) <= float(time()) and input_active and not Match:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            raise SystemExit
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                                dprint("DEBUG: Input= "+Input)
                                dprint("DEBUG: Text= "+Text)
                                if Input == Text:
                                    dprint("DEBUG: Match")
                                    Match = True
                                    Punkte += 1
                                    ding.play()
                                    Input = ''
                            elif event.key == pygame.K_BACKSPACE and Backspace:
                                Input = Input[:-1]
                            elif event.key == pygame.K_ESCAPE:
                                start_time = start_time-Duration_time
                                dprint("DEBUG: Escape")
                            elif event.key == pygame.K_RCTRL:
                                CTRL[0] = True
                                CTRL[1] = float(time())
                                dprint("DEBUG: CTRL")
                            elif CTRL[0]:
                                if CTRL[1]+1.0 <= float(time()):
                                    CTRL[0] = False
                                if event.key == pygame.K_INSERT and CTRL[0]:
                                    Match = True
                                    CTRL[0] = False
                                    dprint("DEBUG: Skipped")
                            else:
                                if input_active:
                                    if (not event.key == pygame.K_BACKSPACE and event.unicode and not Backspace) or len(Input)==0:
                                        Input += event.unicode
                                        Backspace = False
                            if len(Input) <= len(Text) and len(Input) != 0 and Input == Text[:len(Input)]:
                                if event.unicode and event.key != pygame.K_BACKSPACE and event.key != pygame.K_RETURN and event.key != pygame.K_KP_ENTER:
                                    Punkte += 1
                                    ding.play()
                                Backspace = False
                            else:
                                if not event.key == pygame.K_RETURN and not event.key == pygame.K_KP_ENTER:
                                    if not event.key == pygame.K_BACKSPACE and event.unicode and not Backspace:
                                        Fehler += 1
                                        döp.play()
                                    Backspace = True
                            if not require_enter:
                                dprint("DEBUG: Input= " + Input)
                                dprint("DEBUG: Text= " + Text)
                                if Input == Text:
                                    dprint("DEBUG: Match")
                                    Match = True
                                    Punkte += 1
                                    ding.play()
                                    Input = ''
                                text = pgprint(Text, pygame.font.Font(Path(Path(__file__).parent, "xxxb-Font.otf"), 30))
                            else:
                                text = pgprint(Text+"⏎", pygame.font.Font(Path(Path(__file__).parent, "xxxb-Font.otf"), 30))
                    if not require_enter:
                        text = pgprint(Text, pygame.font.Font(Path(Path(__file__).parent, "xxxb-Font.otf"), 30))
                    else:
                        text = pgprint(Text + "⏎", pygame.font.Font(Path(Path(__file__).parent, "xxxb-Font.otf"), 30))
                    input = pgprint(_("Deine Eingabe: ")+Input+("|" if int((time() - start_time) * 2) % 2 == 0 else ""), pygame.font.Font(Path(Path(__file__).parent, "xxxb-Font.otf"), 30), (200, 0, 0))
                    if pgprint(_("Deine Eingabe: "),pygame.font.Font(Path(Path(__file__).parent, "xxxb-Font.otf"), 30),(200, 0, 0)).get_width()*2+text.get_width()> Fensterbreite:
                        text = pgprint(Text, pygame.font.Font(Path(Path(__file__).parent, "xxxb-Font.otf"), 20))
                        input = pgprint(_("Deine Eingabe: ") + Input, pygame.font.Font(Path(Path(__file__).parent, "xxxb-Font.otf"), 20), (200, 0, 0))
                        screen.blit(input, (Fensterbreite / 2 - text.get_width() / 2 - pgprint(_("Deine Eingabe: "),pygame.font.Font(Path(Path(__file__).parent, "xxxb-Font.otf"), 20),(200, 0, 0)).get_width(),((((Fensterhöhe - text.get_height()) / len(Text.split("\n"))) * i) + text.get_height() * 2) - text.get_height() / 2))
                    else:
                        screen.blit(input,  (Fensterbreite/2 - text.get_width()/2 - pgprint(_("Deine Eingabe: "), pygame.font.Font(Path(Path(__file__).parent, "xxxb-Font.otf"), 30), (200, 0, 0)).get_width(), ((((Fensterhöhe-text.get_height())/len(Text.split("\n")))*i)+text.get_height()*2) - text.get_height()/2))
                    screen.blit(text, (Fensterbreite/2 - text.get_width()/2, ((((Fensterhöhe-text.get_height())/len(Text.split("\n")))*i)+text.get_height()) - text.get_height()/2))
                    pygame.display.flip()
                    reset()
        if float(start_time)+float(Duration_time) <= float(time()):
            punkte = pgprint(_("Punkte: ") + str(Punkte), pygame.font.Font(Path(Path(__file__).parent, "xxxb-Font.otf"), 48), (40, 190, 40))
            fehler = pgprint(_("Fehler: ") + str(Fehler), pygame.font.Font(Path(Path(__file__).parent, "xxxb-Font.otf"), 48), (140, 5, 5))
            duration = pgprint(_("Länge: ") + str(Duration) + " " + _("Minuten"))
            ApM = pgprint(_("Anschläge/Minute: ") + str((float(Punkte)) / float(Duration)))
            Score = 0 if round(((float(Punkte - 10 * Fehler) / float(Duration)))) <= 0 else round(
                    ((float(Punkte - 10 * Fehler) / float(Duration))) - (
                        0.01 if dark_mode else 0)) # Das Punkteabziehen ist nur als Spaß und hat keine Auswirkung, aber ich mag halt darkmode nicht. Aber es hat keine Auswirkung auf irgendwas und ist somit nicht diskriminierend.
            score = pgprint("Score: " + str(Score))
            Text = "\n\n" + _("Drücke Enter, um nochmal zu spielen.") + "\n" + _("Drücke Escape, um zu beenden.")
            Titel = _("Auswertung")
            Highscore = pgprint(_("Dein bisheriger Highscore: {score}").format(score=highscore) if Score <= int(highscore) else _("Das ist ein neuer Highscore!"))
            dest_zero = (Fensterbreite / 10, Fensterhöhe / 2)
            if not Score < int(highscore):
                file = open(".highscore.txt", "w")
                file.write(str(Score))
                highscore = str(Score)
                file.close()
            dest = [dest_zero[0], dest_zero[1]]
            while Stage == 3:
                reset()
                dest[1] = dest_zero[1] - 5.2 * punkte.get_height()
                screen.blit(pgprint(Titel, pygame.font.Font(Path(Path(__file__).parent, "xxxb-Font.otf"), 55)), dest)
                dest[1] = dest_zero[1] - 4 * punkte.get_height()
                screen.blit(score, dest)
                dest[1] = dest_zero[1] - 3 * punkte.get_height()
                screen.blit(Highscore, dest)
                dest[1] = dest_zero[1] - 2 * punkte.get_height()
                screen.blit(ApM, dest)
                dest[1] = dest_zero[1] - punkte.get_height()
                screen.blit(punkte, dest)
                dest[1] = dest_zero[1]
                screen.blit(fehler, dest)
                dest[1] = dest_zero[1] + punkte.get_height()
                screen.blit(duration, dest)
                for i in range(len(Text.split("\n"))):
                    text = pgprint(Text.split("\n")[i], font, anweisung_color)
                    dest[1] = dest_zero[1] + (i + 2) * punkte.get_height()
                    screen.blit(text, dest)
                pygame.display.flip()
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            raise SystemExit
                        elif event.key == pygame.K_RETURN:
                            Stage = 1
                            anweisung_color = (10, 10, 200)
                            input_active = True
                            Level = ''
                            Duration = ''
                            duration = ''
                            Input = ''
                            Punkte = 0
                            Fehler = 0
                            Backspace = True
                            CTRL = [False, time()]
                    elif event.type == pygame.QUIT:
                        raise SystemExit
    clock.tick(500)
    pygame.display.flip()

# Quit Pygame
dprint("DEBUG: End Programm")
pygame.quit()
raise SystemExit