# Description

This is FreeCAD macro that gets chipboards dimensions to cut (or any other wood parts but has been designed for chipboards 18 mm thickness). This macro creates spreadsheet named "toCut" with all needed things to cut chipboards for your woodworking project.

Project example (3D model view):

![screen001](https://raw.githubusercontent.com/dprojects/getDimensions/master/screenshots/screenshot001.png)

![screen002](https://raw.githubusercontent.com/dprojects/getDimensions/master/screenshots/screenshot002.png)

### Polish version

Project example (objects view):

![screen003](https://raw.githubusercontent.com/dprojects/getDimensions/master/screenshots/screenshot003.png)

Automatically generated spreadsheet "toCut" for project above:

![screen004](https://raw.githubusercontent.com/dprojects/getDimensions/master/screenshots/screenshot004.png)

### English version

Project example (objects view):

![screen005](https://raw.githubusercontent.com/dprojects/getDimensions/master/screenshots/screenshot005.png)

Automatically generated spreadsheet "toCut" for project above:

![screen006](https://raw.githubusercontent.com/dprojects/getDimensions/master/screenshots/screenshot006.png)

# Download

* You can get this macro here: [getDimensions.py](https://raw.githubusercontent.com/dprojects/getDimensions/master/getDimensions.py)

# Install

Just open the macro under the FreeCAD.

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

**NOTE**: You can also use the TechDraw. Just place the spreadsheet there and print. 

# Make a note

* Special characters (Polish) for chipboards (object cube names) not supported.

# Additional features

### Support for arrays

This macro supports arrays made of cube (thanks [jaisejames](https://forum.freecadweb.org/memberlist.php?mode=viewprofile&u=10269)).

Project example (3D model view):

![screen007](https://raw.githubusercontent.com/dprojects/getDimensions/master/screenshots/screenshot007.png)

Project example (objects view):

![screen008](https://raw.githubusercontent.com/dprojects/getDimensions/master/screenshots/screenshot008.png)

Automatically generated spreadsheet "toCut" for project above:

![screen009](https://raw.githubusercontent.com/dprojects/getDimensions/master/screenshots/screenshot009.png)

### Support for square millimeters

![screen010](https://raw.githubusercontent.com/dprojects/getDimensions/master/screenshots/screenshot010.png)

### Support for square meters

![screen011](https://raw.githubusercontent.com/dprojects/getDimensions/master/screenshots/screenshot011.png)

### Support for square inches

![screen012](https://raw.githubusercontent.com/dprojects/getDimensions/master/screenshots/screenshot012.png)

### Support for custom settings

![screen013](https://raw.githubusercontent.com/dprojects/getDimensions/master/screenshots/screenshot013.png)

![screen014](https://raw.githubusercontent.com/dprojects/getDimensions/master/screenshots/screenshot014.png)

![screen015](https://raw.githubusercontent.com/dprojects/getDimensions/master/screenshots/screenshot015.png)

![screen016](https://raw.githubusercontent.com/dprojects/getDimensions/master/screenshots/screenshot016.png)

# Contact

Please add all comments and questions in FreeCAD forum topic related to this project available at:
[https://forum.freecadweb.org/viewtopic.php?f=22&t=21127](https://forum.freecadweb.org/viewtopic.php?f=22&t=21127)

You can also send me private message on FreeCAD forum. Maybe I will set up dedicated website for this project in the future, who knows.

# License

MIT
