# Description

This is FreeCAD macro that gets chipboards dimensions to cut (or any other wood parts but has been designed for chipboards 18 mm thickness). This macro creates spreadsheet named "toCut" with all needed things to cut chipboards for your woodworking project.

Project example (3D model view): 

![screen1](https://raw.githubusercontent.com/dprojects/getDimensions/master/screenshot1.png)

Project example (objects view):

![screen2](https://raw.githubusercontent.com/dprojects/getDimensions/master/screenshot2.png)

Automatically generated spreadsheet "toCut" for project above:

![screen3](https://raw.githubusercontent.com/dprojects/getDimensions/master/screenshot3.png)

# Download

* Polish version (originally designed): [getDimesions.py](https://raw.githubusercontent.com/dprojects/getDimensions/master/getDimensions.py)
* English version (ported): [getDimesionsEN.py](https://raw.githubusercontent.com/dprojects/getDimensions/master/getDimensionsEN.py)

# Install

1. Create new macro in FreeCAD named e.g. "getDimensions".
2. Copy exact language version of macro (e.g. getDimensionsEN.py) and paste it to your new empty macro.

# Usage

* Create chipboards:
 * Go to FreeCAD -> Part -> Create a cube solid -> Cube data (tab):
 * Set "Length" to e.g. 500
 * Set "Width" to e.g. 500
 * Set "Height" to e.g. 18
 
**NOTE**: Now you should have chipboard 500 mm x 500 mm x 18 mm. You can create whatever you like using such chipboards. Even group them in folders.

* Run macro.

**NOTE**: Now you should have spreadsheet named "toCut" with all needed dimensions. If you have already "toCut" spreadsheet it will be overwritten (read: updated).

Maybe someone will make any YouTube video tutorial about it?

# Printing

FreeCAD not support direct printing for spreadsheets ([issue: #0002957](http://freecadweb.org/tracker/view.php?id=2957)). So you have to:

1. Export your spreadsheet to CSV.
2. Copy the CSV data to LibreOffice.
3. Convert text with tabulators in LibreOffice to the table.
4. Make some corrections (add mm and adjust table columns).
5. Print it.
6. Go and cut your chipboards to market or any other woodworking service that provide wood cutting :-)

# Make a note

* Special characters (Polish) for chipboards (object cube names) not supported.

# Additional features

### Support for arrays

This macro supports arrays made of cube (thanks [jaisejames](https://forum.freecadweb.org/memberlist.php?mode=viewprofile&u=10269)). 

Project example (3D model view): 

![screen4](https://raw.githubusercontent.com/dprojects/getDimensions/master/screenshot4.png)

Project example (objects view):

![screen5](https://raw.githubusercontent.com/dprojects/getDimensions/master/screenshot5.png)

Automatically generated spreadsheet "toCut" for project above:

![screen6](https://raw.githubusercontent.com/dprojects/getDimensions/master/screenshot6.png)


# Contact

Please add all comments and questions in FreeCAD forum topic related to this project available at: 
[https://forum.freecadweb.org/viewtopic.php?f=22&t=21127](https://forum.freecadweb.org/viewtopic.php?f=22&t=21127)

You can also send me private message on FreeCAD forum. Maybe I will set up dedicated website for this project in the future, who knows.

# License

MIT
