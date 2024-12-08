#!/usr/bin/python
import cgi
import cgitb
cgitb.enable()

form = cgi.FieldStorage()


print( "Content-type: text/html\n\n" )
print( "<html>")
print( "<head>")
print( "<title>LAB 7</title>")
print( "</head>")
print( "<title>py + css test</title>" )
print( """<script src='chart.js' type="text/javascript"></script>""")
print( """<link rel="stylesheet" href="chart.css" type="text/css">""")
print( """<h1 onClick='toggle()'>Rachel Koo</h1>""")
print( """<table class='visible' id="table" >""") 
print("<tr><th>x</th> <th>y</th> <th>dy</th> <th>sumy</th></tr>")

h=3

def f(x):
    return int(form["a"].value)*x*x*x-int(form["b"].value)*x*x+int(form["c"].value)*x

def fprime(x):
    return ( f(x) - f(x-h))/h

def fint(x):
    return (f(x)+f(x-h))*h/2



def fdoubleprime(x):
    return ( fprime(x) - fprime(x-h))/h
ys=0
for x in range(-100,100):
    y=f(x)
    yp=fprime(x)
    yi=fint(x)
    ys+=yi
    yd=fdoubleprime(x)
    if x%2==0:
     print("<tr class='d'><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>"%( x,y,yp,ys))
    else:
     print("<tr class='c'><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>"%( x,y,yp,ys))


print("</table>")
print("</body>")
print("</html>")
