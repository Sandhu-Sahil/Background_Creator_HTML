#!/usr/bin/env python3
'''Assignment 4 Part 1 template'''
print(__doc__)

from typing import IO

class Circle:
    '''Circle class'''
    def __init__(self, cir: tuple, col: tuple):
        self.cx: int = cir[0]
        self.cy: int = cir[1]
        self.rad: int = cir[2]
        self.red: int = col[0]
        self.green: int = col[1]
        self.blue: int = col[2]
        self.op: float = col[3]


class Rectangle:
    '''Rectangle class'''
    def __init__(self, cir: tuple, col: tuple):
        self.cx: int = cir[0]
        self.cy: int = cir[1]
        self.width: int = cir[2]
        self.height: int = cir[3]
        self.red: int = col[0]
        self.green: int = col[1]
        self.blue: int = col[2]
        self.op: float = col[3]

class ProEpiloge:
    '''Html Class'''
    
def writeHTMLcomment(f: IO[str], t: int, com: str):
    '''writeHTMLcomment method'''
    ts: str = "   " * t
    f.write(f'{ts}<!--{com}-->\n')
        
def drawCircleLine(f: IO[str], t: int, c: Circle):
    '''drawCircle method'''
    ts: str = "   " * t
    line: str = f'<circle cx="{c.cx}" cy="{c.cy}" r="{c.rad}" fill="rgb({c.red}, {c.green}, {c.blue})" fill-opacity="{c.op}"></circle>'
    f.write(f"{ts}{line}\n")

def drawRectLine(f: IO[str], t: int, c: Rectangle):
    '''drawCircle method'''
    ts: str = "   " * t
    line: str = f'<rect x="{c.cx}" y="{c.cy}" width="{c.width}" height="{c.height}" fill="rgb({c.red}, {c.green}, {c.blue})" fill-opacity="{c.op}"></rect>'
    f.write(f"{ts}{line}\n")
        
def genArtRect(f: IO[str], t: int):
   '''genART method'''
   drawRectLine(f, t, Rectangle((50,50,60,40), (255,0,0,1.0)))
   drawRectLine(f, t, Rectangle((150,50,60,40), (255,0,0,1.0)))
   drawRectLine(f, t, Rectangle((250,50,60,40), (255,0,0,1.0)))
   drawRectLine(f, t, Rectangle((350,50,60,40), (255,0,0,1.0)))
   drawRectLine(f, t, Rectangle((450,50,60,40), (255,0,0,1.0)))
   drawRectLine(f, t, Rectangle((50,250,60,40), (0,0,255,1.0)))
   drawRectLine(f, t, Rectangle((150,250,60,40), (0,0,255,1.0)))
   drawRectLine(f, t, Rectangle((250,250,60,40), (0,0,255,1.0)))
   drawRectLine(f, t, Rectangle((350,250,60,40), (0,0,255,1.0)))
   drawRectLine(f, t, Rectangle((450,250,60,40), (0,0,255,1.0)))
        
def genArt(f: IO[str], t: int):
   '''genART method'''
   drawCircleLine(f, t, Circle((50,50,50), (255,0,0,1.0)))
   drawCircleLine(f, t, Circle((150,50,50), (255,0,0,1.0)))
   drawCircleLine(f, t, Circle((250,50,50), (255,0,0,1.0)))
   drawCircleLine(f, t, Circle((350,50,50), (255,0,0,1.0)))
   drawCircleLine(f, t, Circle((450,50,50), (255,0,0,1.0)))
   drawCircleLine(f, t, Circle((50,250,50), (0,0,255,1.0)))
   drawCircleLine(f, t, Circle((150,250,50), (0,0,255,1.0)))
   drawCircleLine(f, t, Circle((250,250,50), (0,0,255,1.0)))
   drawCircleLine(f, t, Circle((350,250,50), (0,0,255,1.0)))
   drawCircleLine(f, t, Circle((450,250,50), (0,0,255,1.0)))

def openSVGcanvas(f: IO[str], t: int, canvas: tuple):
     '''openSVGcanvas method'''
     ts: str = "   " * t
     writeHTMLcomment(f, t, "Define SVG drawing box Circle")
     f.write(f'{ts}<svg width="{canvas[0]}" height="{canvas[1]}">\n')

def openSVGcanvasRect(f: IO[str], t: int, canvas: tuple):
     '''openSVGcanvas method'''
     ts: str = "   " * t
     writeHTMLcomment(f, t, "Define SVG drawing box Rectangle")
     f.write(f'{ts}<svg width="{canvas[0]}" height="{canvas[1]}">\n')


def closeSVGcanvasRect(f: IO[str], t: int):
    '''closeSVGcanvas method'''
    ts: str = "   " * t
    f.write(f'{ts}</svg>\n')


def closeSVGcanvas(f: IO[str], t: int):
    '''closeSVGcanvas method'''
    ts: str = "   " * t
    f.write(f'{ts}</svg>\n')
    f.write(f'</body>\n')
    f.write(f'</html>\n')

def writeHTMLline(f: IO[str], t: int, line: str):
     '''writeLineHTML method'''
     ts = "   " * t
     f.write(f"{ts}{line}\n")

def writeHTMLHeader(f: IO[str], winTitle: str):
    '''writeHeadHTML method'''
    writeHTMLline(f, 0, "<html>")
    writeHTMLline(f, 0, "<head>")
    writeHTMLline(f, 1, f"<title>{winTitle}</title>")
    writeHTMLline(f, 0, "</head>")
    writeHTMLline(f, 0, "<body>")

def writeHTMLfile():
    '''writeHTMLfile method'''
    fnam: str = "myPart1Art.html"
    winTitle = "My Art"
    f: IO[str] = open(fnam, "w")
    writeHTMLHeader(f, winTitle)
    openSVGcanvasRect(f, 1, (500,300))
    genArtRect(f, 2)
    closeSVGcanvasRect(f, 1)
    openSVGcanvas(f, 1, (500,300))
    genArt(f, 2)
    closeSVGcanvas(f, 1)
    f.close()

def main():
    '''main method'''
    writeHTMLfile()

main()

                                                                                                                                                                                                                                                                                                        
