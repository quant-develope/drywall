#!/usr/bin/env python3
"""Draws the flat illustrations in src/ill/*.svg (run once after changing a drawing; the svg files are committed).
They stand in for photos until the owner sends real pictures of finished work."""
import os

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "src", "ill")
W, H = 800, 560
INK, WALL, FLOOR, BOARD, EDGE, STUD, OCHRE, TEAL, SKY = "#1e2a32", "#f3efe6", "#d8cbb4", "#ebe6db", "#c9c1b1", "#a3aeb4", "#e3a21a", "#137480", "#dbe9ec"
GREEN, PINK, WOOL, BLUE = "#c3d8b8", "#efcaca", "#f0cf6a", "#c8d6ea"


def svg(name, body, bg=WALL):
    with open(os.path.join(OUT, name + ".svg"), "w", encoding="utf-8") as f:
        f.write('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" width="%d" height="%d">'
                '<rect width="%d" height="%d" fill="%s"/>%s</svg>\n' % (W, H, W, H, W, H, bg, body))


def rect(x, y, w, h, fill, stroke=None, sw=2, rx=0, extra=""):
    s = ' stroke="%s" stroke-width="%s"' % (stroke, sw) if stroke else ""
    return '<rect x="%s" y="%s" width="%s" height="%s" rx="%s" fill="%s"%s%s/>' % (x, y, w, h, rx, fill, s, extra)


def line(x1, y1, x2, y2, c=INK, w=2, extra=""):
    return '<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" stroke-width="%s" stroke-linecap="round"%s/>' % (x1, y1, x2, y2, c, w, extra)


def stud(x, y, h, w=14):
    """A galvanised C-stud seen from the front."""
    return rect(x, y, w, h, STUD, INK, 1.5) + line(x + 4, y + 4, x + 4, y + h - 4, "#cdd5d9", 2) + "".join(
        '<circle cx="%s" cy="%s" r="2.2" fill="%s"/>' % (x + w / 2, yy, INK) for yy in range(int(y) + 30, int(y + h) - 10, 60))


def board(x, y, w, h, fill=BOARD, screws=True):
    s = rect(x, y, w, h, fill, EDGE, 2)
    if screws:
        for xx in (x + 8, x + w - 8):
            s += "".join('<circle cx="%s" cy="%s" r="1.8" fill="%s"/>' % (xx, yy, "#8b8577") for yy in range(int(y) + 20, int(y + h) - 6, 40))
    return s


def floor(y=470, c=FLOOR):
    return rect(0, y, W, H - y, c) + line(0, y, W, y, INK, 2)


def person(x, y, s=1.0):
    """A worker with a helmet, simple shapes."""
    return ('<g transform="translate(%s %s) scale(%s)">' % (x, y, s) +
            '<circle cx="0" cy="-118" r="16" fill="#e8c4a0"/>'
            '<path d="M-18 -124a18 18 0 0 1 36 0z" fill="%s"/>' % OCHRE +
            '<rect x="-21" y="-100" width="42" height="58" rx="10" fill="%s"/>' % TEAL +
            '<rect x="-17" y="-44" width="14" height="44" rx="5" fill="%s"/><rect x="3" y="-44" width="14" height="44" rx="5" fill="%s"/>' % (INK, INK) +
            '</g>')


def lamp_glow(x1, x2, y):
    return ('<defs><linearGradient id="g" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#ffe7a8" stop-opacity=".95"/>'
            '<stop offset="1" stop-color="#ffe7a8" stop-opacity="0"/></linearGradient></defs>'
            + rect(x1, y, x2 - x1, 70, "url(#g)"))


# hero: a living room half done: studs on the left, boarded and finished on the right, cove ceiling above
def hero():
    b = floor()
    b += rect(0, 0, W, 70, BOARD) + line(0, 70, W, 70, EDGE, 3)
    b += lamp_glow(0, W, 72) + rect(0, 66, W, 8, "#fff3cf")
    b += rect(40, 110, 300, 360, "#e4ddcf")  # old wall behind the frame
    b += line(40, 112, 340, 112, INK, 3) + line(40, 468, 340, 468, INK, 3)
    for x in range(48, 330, 60):
        b += stud(x, 112, 356)
    b += '<rect x="58" y="230" width="36" height="120" fill="%s" opacity=".9"/>' % WOOL
    b += board(340, 110, 120, 360) + board(460, 110, 120, 360) + rect(580, 110, 180, 360, "#fbf9f4", EDGE, 2)
    b += rect(600, 170, 140, 90, "#fff", EDGE, 2) + rect(612, 182, 116, 66, SKY)  # niche with light
    b += line(612, 182, 728, 182, OCHRE, 4)
    b += rect(626, 214, 26, 34, TEAL) + '<circle cx="694" cy="228" r="16" fill="%s"/>' % GREEN
    b += line(460, 110, 460, 470, "#d9d2c3", 2, ' stroke-dasharray="6 6"')
    b += person(250, 470) + rect(170, 400, 90, 12, OCHRE, INK, 1.5, 3) + rect(186, 412, 10, 58, INK) + rect(234, 412, 10, 58, INK)
    b += '<g transform="translate(380 420)">' + rect(0, 0, 70, 50, "#fff", INK, 2, 4) + line(10, 18, 60, 18, EDGE, 3) + line(10, 32, 48, 32, EDGE, 3) + '</g>'
    svg("hero-saloni", b)


def ceiling():
    b = floor(500) + rect(0, 0, W, 60, "#e4ddcf")
    for x in range(60, 760, 120):
        b += line(x, 0, x, 120, INK, 2)  # hangers
    b += rect(30, 120, 740, 14, STUD, INK, 1.5)
    b += rect(70, 134, 660, 30, BOARD, EDGE, 2)
    b += rect(30, 134, 40, 70, BOARD, EDGE, 2) + rect(730, 134, 40, 70, BOARD, EDGE, 2)
    b += lamp_glow(70, 730, 164)
    b += "".join('<circle cx="%s" cy="149" r="6" fill="#fff6d6" stroke="%s" stroke-width="2"/>' % (x, EDGE) for x in range(160, 700, 130))
    b += rect(0, 204, W, 296, WALL)
    b += rect(80, 330, 260, 110, TEAL, None, 0, 14) + rect(96, 300, 228, 40, "#0f5f69", None, 0, 12)  # sofa
    b += rect(470, 390, 220, 14, INK) + rect(490, 404, 10, 96, INK) + rect(660, 404, 10, 96, INK)
    b += '<circle cx="580" cy="370" r="20" fill="%s"/>' % GREEN + rect(566, 370, 28, 20, OCHRE, None, 0, 4)
    b += line(0, 204, W, 204, EDGE, 2)
    svg("psevdorofi", b)


def partition():
    b = floor() + rect(0, 0, W, 60, BOARD) + line(0, 60, W, 60, EDGE, 3)
    b += line(60, 62, 740, 62, INK, 4) + line(60, 468, 740, 468, INK, 4)  # U tracks
    for x in range(60, 740, 60):
        b += stud(x, 64, 404)
    b += '<rect x="315" y="64" width="14" height="404" fill="%s" stroke="%s"/>' % (STUD, INK)
    b += rect(420, 64, 4, 404, INK) + rect(520, 64, 4, 404, INK) + rect(424, 64, 96, 6, INK)  # door frame
    b += board(60, 64, 120, 404) + board(180, 64, 120, 404, screws=False)
    b += '<rect x="196" y="80" width="88" height="372" fill="none" stroke="%s" stroke-width="2" stroke-dasharray="8 8"/>' % OCHRE
    b += '<rect x="560" y="140" width="40" height="300" fill="%s" opacity=".85"/>' % WOOL + '<rect x="620" y="140" width="40" height="300" fill="%s" opacity=".85"/>' % WOOL
    b += person(470, 470, .95)
    svg("chorisma", b)


def lining():
    b = floor() + rect(0, 0, W, 470, "#e2d6c2")
    for y in range(20, 470, 36):  # old brick wall
        off = 0 if (y // 36) % 2 else 40
        for x in range(-off, W, 80):
            b += rect(x + 2, y, 76, 32, "#d6c5a9", "#c4b190", 1)
    b += '<path d="M120 120c30 40 10 80 40 120M150 300c-20 30 10 60 -10 100" stroke="#9c8565" stroke-width="3" fill="none"/>'  # cracks
    b += rect(330, 30, 440, 440, BOARD, EDGE, 2) + line(476, 30, 476, 470, EDGE, 2) + line(622, 30, 622, 470, EDGE, 2)
    b += rect(318, 30, 12, 440, STUD, INK, 1.5)
    b += rect(380, 190, 70, 44, "#fff", EDGE, 2) + '<circle cx="415" cy="212" r="7" fill="none" stroke="%s" stroke-width="2"/>' % INK  # socket
    b += person(260, 470)
    svg("ependysi", b)


def insulation():
    b = floor() + rect(0, 0, W, 470, "#e4ddcf")
    b += line(40, 40, 760, 40, INK, 4) + line(40, 468, 760, 468, INK, 4)
    for i, x in enumerate(range(40, 760, 120)):
        b += stud(x, 42, 426)
        if x + 120 <= 760:
            b += '<rect x="%s" y="44" width="104" height="422" fill="%s"/>' % (x + 15, WOOL if i % 2 == 0 else "#e8d27a")
            b += "".join('<path d="M%s %s q 26 -10 52 0 t 52 0" stroke="#c9a640" stroke-width="2" fill="none"/>' % (x + 15, y) for y in range(70, 466, 34))
    b += rect(520, 42, 240, 426, BOARD, EDGE, 2)
    for i, r in enumerate((40, 70, 100)):  # sound waves in front of the finished side, fading
        b += '<path d="M%s %s a%s %s 0 0 1 0 %s" fill="none" stroke="%s" stroke-width="5" stroke-linecap="round" opacity="%s"/>' % (
            560, 255 - r, r, r, 2 * r, TEAL, 0.9 - i * 0.3)
    svg("monosi", b)


def bathroom():
    b = floor(480, "#cfd9dc") + rect(0, 0, W, 480, "#eef2f2")
    b += rect(40, 40, 400, 440, GREEN, "#8fae84", 2) + line(173, 40, 173, 480, "#8fae84", 2) + line(306, 40, 306, 480, "#8fae84", 2)
    for y in range(240, 480, 40):  # tiles on the lower part
        for x in range(40, 440, 50):
            b += rect(x, y, 50, 40, "#fff", "#c6d3d6", 1.5)
    b += rect(480, 40, 280, 440, "#fbfbf9", EDGE, 2)
    b += rect(520, 110, 200, 70, "#fff", EDGE, 2) + rect(532, 122, 176, 46, SKY) + line(532, 122, 708, 122, OCHRE, 4)  # niche
    b += rect(560, 330, 160, 24, "#fff", INK, 2, 6) + rect(600, 354, 80, 126, "#fff", INK, 2)  # vanity
    b += rect(570, 210, 140, 100, SKY, INK, 2, 50)  # mirror
    b += '<path d="M210 120v60M200 180h20" stroke="%s" stroke-width="6" stroke-linecap="round"/>' % INK
    b += "".join('<circle cx="%s" cy="%s" r="3" fill="%s"/>' % (196 + dx, 200 + dy, TEAL) for dx, dy in ((0, 10), (14, 22), (28, 8), (6, 34), (22, 40)))
    svg("bano", b)


def decor():
    b = floor() + rect(0, 0, W, 470, WALL)
    b += rect(0, 0, W, 50, BOARD) + rect(0, 50, W, 26, "#efe9dd", EDGE, 2) + lamp_glow(0, W, 76)
    b += rect(140, 120, 520, 350, "#fbf9f4", EDGE, 2)  # TV wall
    b += rect(250, 190, 300, 170, INK, None, 0, 6)
    b += rect(170, 160, 50, 260, "#fff", EDGE, 2) + rect(580, 160, 50, 260, "#fff", EDGE, 2)
    for y in (220, 300, 380):
        b += line(176, y, 214, y, OCHRE, 3) + line(586, y, 624, y, OCHRE, 3)
    b += rect(186, 190, 18, 28, TEAL) + '<circle cx="605" cy="282" r="12" fill="%s"/>' % GREEN + rect(592, 344, 28, 34, OCHRE)
    b += rect(230, 390, 340, 40, "#fff", EDGE, 2) + lamp_glow(230, 570, 430)
    svg("diakosmitika", b)


def commercial():
    b = floor(470, "#cfc6b6") + rect(0, 0, W, 470, "#eae6de")
    b += '<path d="M0 0h800L560 150H240z" fill="%s"/>' % BOARD
    b += '<path d="M0 470 240 330h320l240 140z" fill="#d9d0bf"/>'
    b += '<path d="M0 0 240 150v180L0 470z" fill="#f3efe6"/><path d="M800 0 560 150v180l240 140z" fill="#efe9de"/>'
    b += rect(240, 150, 320, 180, "#fbf9f4", EDGE, 2)
    b += rect(360, 190, 80, 140, TEAL) + '<circle cx="428" cy="262" r="4" fill="#fff"/>'
    for x, y, h in ((60, 110, 300), (140, 140, 220)):
        b += '<path d="M%s %s v%s" stroke="%s" stroke-width="22" stroke-linecap="square"/>' % (x, y, h, "#ded7c9")
        b += rect(x - 14, y + 40, 28, 70, "#fff", EDGE, 1.5)
    b += "".join('<circle cx="%s" cy="%s" r="7" fill="#fff6d6" stroke="%s" stroke-width="2"/>' % (x, y, EDGE) for x, y in ((400, 120), (400, 70), (400, 30), (300, 60), (500, 60)))
    b += rect(600, 160, 100, 24, OCHRE, None, 0, 4) + '<text x="650" y="177" text-anchor="middle" font-family="Inter,sans-serif" font-size="13" font-weight="700" fill="%s">ROOM 104</text>' % INK
    svg("xenodocheia", b)


def repair():
    b = floor() + rect(0, 0, W, 470, WALL)
    b += rect(120, 80, 560, 330, "#f8f6f1", EDGE, 2)
    b += '<path d="M300 190l40 20 30-14 20 30 34 6-10 34 20 26-38 4-16 30-30-20-34 10 4-36-26-24 34-14z" fill="#d6cfc0" stroke="%s" stroke-width="2"/>' % INK
    b += rect(470, 170, 140, 120, "#fff", OCHRE, 3, 4, ' stroke-dasharray="10 6"')
    b += '<path d="M470 230h140M540 170v120" stroke="%s" stroke-width="2" stroke-dasharray="4 6"/>' % EDGE
    b += '<g transform="rotate(-25 560 360)">' + rect(500, 340, 110, 28, "#cfd6da", INK, 2, 3) + rect(600, 346, 70, 16, INK, None, 0, 4) + '</g>'
    b += '<path d="M180 420c30-16 60 16 90 0s60 16 90 0" stroke="%s" stroke-width="4" fill="none"/>' % TEAL
    svg("episkeves", b)


def areas_map():
    """Stylised map: the Gulf of Corinth, the isthmus, the Saronic gulf and the places we cover."""
    sea = "#cfe3e7"
    b = rect(0, 0, W, H, "#eee7d8")
    b += '<path d="M0 0h300l20 80-50 80-120 40-150-10z" fill="%s"/>' % sea  # Alkyonides, north of the Perachora peninsula
    b += '<path d="M0 285c120 0 280 0 375 5 20 20 25 50 15 75-40 25-110 40-210 70C110 455 50 465 0 475z" fill="%s"/>' % sea  # bay of Loutraki / Corinth
    b += '<path d="M800 280c-100 15-170 25-240 50-50 20-90 40-110 60-20 30-30 70-40 100l-10 70h400z" fill="%s"/>' % sea  # Saronic gulf
    b += '<path d="M390 365 446 392" stroke="#7aa6ad" stroke-width="5"/>'  # Corinth canal
    pts = [("Λουτράκι", "Loutraki", 395, 300, True), ("Περαχώρα", "Perachora", 330, 230, False), ("Λ. Βουλιαγμένη", "Lake Vouliagmeni", 205, 245, False),
           ("Πίσια", "Pisia", 470, 230, False), ("Κόρινθος", "Corinth", 300, 425, False)]
    b += '<text x="20" y="40" font-family="Inter,sans-serif" font-size="17" font-style="italic" fill="#4b7f88">Κορινθιακός · Gulf of Corinth</text>'
    b += '<text x="560" y="520" font-family="Inter,sans-serif" font-size="17" font-style="italic" fill="#4b7f88">Σαρωνικός · Saronic Gulf</text>'
    b += '<circle cx="395" cy="300" r="130" fill="%s" opacity=".08"/><circle cx="395" cy="300" r="130" fill="none" stroke="%s" stroke-width="2" stroke-dasharray="6 6"/>' % (TEAL, TEAL)
    for el, en, x, y, main in pts:
        r = 11 if main else 7
        b += '<circle cx="%s" cy="%s" r="%s" fill="%s" stroke="#fff" stroke-width="3"/>' % (x, y, r, OCHRE if main else INK)
        b += '<text x="%s" y="%s" font-family="Inter,sans-serif" font-size="%s" font-weight="700" fill="%s">%s</text>' % (
            x + 14, y + 5, 18 if main else 14, INK, el)
        b += '<text x="%s" y="%s" font-family="Inter,sans-serif" font-size="12" fill="#5d666c">%s</text>' % (x + 14, y + 21, en)
    svg("chartis-perioxis", b, "#eee7d8")


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    for f in (hero, ceiling, partition, lining, insulation, bathroom, decor, commercial, repair, areas_map):
        f()
    print("ok")
