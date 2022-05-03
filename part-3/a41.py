#!/usr/bin/env python3
'''Assignment 4 Part 3 '''
print(__doc__)

from typing import IO
from random import randint, random
from tkinter import *
from decimal import Decimal

class ArtConfig:
    def __init__(self, n :int):
        self.n = n
        self.sha = []
        self.x = []
        self.y = []
        self.rad = []
        self.rx = []
        self.ry = []
        self.w = []
        self.h =[]
        self.r = []
        self.g = []
        self.b = []
        self.op = []

    def Print(self, i:int):
        #print("CNT\tSHA\tX\tY\tRAD\tRX\tRY\tW\tH\tR\tG\tB\tOP")
        #for i in range(int(self.n)):
        print(f"{i}\t{self.sha[i]}\t{self.x[i]}\t{self.y[i]}\t{self.rad[i]}\t{self.rx[i]}\t{self.ry[i]}\t{self.w[i]}\t{self.h[i]}\t{self.r[i]}\t{self.g[i]}\t{self.b[i]}\t{self.op[i]}")

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


class Ellipse:
    '''Ellipse class'''
    def __init__(self, cir: tuple, col: tuple):
        self.cx: int = cir[0]
        self.cy: int = cir[1]
        self.rx: int = cir[2]
        self.ry: int = cir[3]
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
    '''drawRect method'''
    ts: str = "   " * t
    line: str = f'<rect x="{c.cx}" y="{c.cy}" width="{c.width}" height="{c.height}" fill="rgb({c.red}, {c.green}, {c.blue})" fill-opacity="{c.op}"></rect>'
    f.write(f"{ts}{line}\n")

def drawEllipseLine(f: IO[str], t: int, c: Ellipse):
    '''drawEllipse method'''
    ts: str = "   " * t
    line: str = f'<ellipse cx="{c.cx}" cy="{c.cy}" rx="{c.rx}" ry="{c.ry}" fill="rgb({c.red}, {c.green}, {c.blue})" fill-opacity="{c.op}"></ellipse>'
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

def writeHTMLfile(x : int, y :int, a: ArtConfig):
    '''writeHTMLfile method'''
    fnam: str = "myPart1Art.html"
    winTitle = "My Art"
    f: IO[str] = open(fnam, "w")
    writeHTMLHeader(f, winTitle)
    openSVGcanvas(f, 1, (x,y))
    for i in range(int(a.n)):
        if int(a.sha[i]) == 0:
            drawCircleLine(f, 2, Circle((a.x[i],a.y[i],a.rad[i]), (a.r[i],a.g[i],a.b[i],a.op[i])))
        elif int(a.sha[i]) == 1:
            drawRectLine(f, 2, Rectangle((a.x[i],a.y[i],a.w[i],a.h[i]), (a.r[i],a.g[i],a.b[i],a.op[i])))
        elif int(a.sha[i]) == 2:
            drawEllipseLine(f, 2, Ellipse((a.x[i],a.y[i],a.rx[i],a.ry[i]), (a.r[i],a.g[i],a.b[i],a.op[i])))
    
    closeSVGcanvas(f, 1)
    f.close()


class GenRandom:
    def addData(self, a : ArtConfig):
        a.sha.append(randint(0,2))

        win = Tk()
        width = win.winfo_screenwidth()
        height= win.winfo_screenheight()

        a.x.append(randint(0,width))
        a.y.append(randint(0,height))
        a.rad.append(randint(0,100))
        a.rx.append(randint(10,30))
        a.ry.append(randint(10,30))
        a.w.append(randint(10,100))
        a.h.append(randint(10,100))
        a.r.append(randint(0,255))
        a.g.append(randint(0,255))
        a.b.append(randint(0,255))
        a.op.append(round(random(),1))

    def fillData(self, a:ArtConfig):
        n = a.n
        for i in range(int(n)):
            self.addData(a)
            a.Print(i)



def main():
    '''main method'''
    #writeHTMLfile()
    print("Input Dimensions of SVG")
    x = input("x = ")
    y = input("y = ")
    n = input("No of shapes = ")

    art = ArtConfig(n)
    add = GenRandom()
    add.fillData(art)
    #art.Print()
    writeHTMLfile(x,y,art)


main()

                                                                                                                                                                                                                                                                                                        
