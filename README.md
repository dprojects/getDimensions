# Description

This is FreeCAD macro that read FreeCAD 3D model and gets chipboards dimensions to cut or any other wood parts but has been designed for chipboards 18 mm of thickness. This macro creates spreadsheet named "toCut" and also TechDraw page "toPrint" with all needed chipboards elements to cut for your woodworking project. They are grouped with same sizes to make cutting more easier. So, You know how many same elements You need to cut and You can easily calculate costs per square area.

### TechDraw report example in English language:

![en](https://raw.githubusercontent.com/dprojects/getDimensions/master/screenshots/lang_en.png)

### TechDraw report example in Polish language:

![pl](https://raw.githubusercontent.com/dprojects/getDimensions/master/screenshots/lang_pl.png)

# Main features

* Support for English and Polish languages.
* Elements can be listed in millimeters, meters or inches.
* Square area can be listed in millimeters, meters or inches.
* Group elements by thickness.
* Toggle Visibility Feature allow turn off elements or even group of elements (folder).
* Summary By Colors Feature allow to group elements by colors to make costs more visible for each color.
* Summary for edge size.
* Support for arrays made of cube.

# Download

* You can get this macro here: [getDimensions.py](https://raw.githubusercontent.com/dprojects/getDimensions/master/getDimensions.py)

# Install

Just open the macro under the FreeCAD.

# Usage

### Sample usage - create chipboards:

* Go to FreeCAD -> Part -> Create a cube solid -> Cube data (tab):
* Set "Length" to e.g. 500
* Set "Width" to e.g. 500
* Set "Height" to e.g. 18

**NOTE**: Now you should have chipboard 500 mm x 500 mm x 18 mm. You can create whatever you like using such chipboards. Even group them in folders.

* Run macro.

### Sample usage - arrays:

This macro supports arrays made of cube (thanks [jaisejames](https://forum.freecadweb.org/memberlist.php?mode=viewprofile&u=10269)).

Project example (3D model view):

![arrays001](https://raw.githubusercontent.com/dprojects/getDimensions/master/screenshots/arrays001.png)

Project example (objects view):

![arrays002](https://raw.githubusercontent.com/dprojects/getDimensions/master/screenshots/arrays002.png)

Automatically generated spreadsheet "toCut" for project above:

![arrays003](https://raw.githubusercontent.com/dprojects/getDimensions/master/screenshots/arrays003.png)

### Sample usage - Toggle Visibility Feature:

If the feature "Toggle Visibility Feature" is set to "on", 

![tvf001](https://raw.githubusercontent.com/dprojects/getDimensions/master/screenshots/tvf001.png)

You can create any TechDraw view You want just by toggle visibility items or group of items. 

![tvf002](https://raw.githubusercontent.com/dprojects/getDimensions/master/screenshots/tvf002.png)

![tvf003](https://raw.githubusercontent.com/dprojects/getDimensions/master/screenshots/tvf003.png)

You can generate different reports at the same furniture project. Just rename the TechDraw page 
to store it and prevent from overwrite.

### Sample usage - Summary By Colors Feature:

By default the feature "Summary By Colors Feature" is set to "off". So, You have to turn it on:

![sbcf001](https://raw.githubusercontent.com/dprojects/getDimensions/master/screenshots/sbcf001.png)

Also You need to have exact folder tree structure in Your furniture project. The idea behind it is 
that each element need to has parent folder and also grandparent folder. For exaple element named 
"Foot L" need to be in parent folder (e.g. named "Foot"). Also the "Foot" folder need to be in 
grandparent folder (e.g. named "Black color"). See example: 

![sbcf002](https://raw.githubusercontent.com/dprojects/getDimensions/master/screenshots/sbcf002.png)

Now You can generate TechDraw page with the macro:

![sbcf003](https://raw.githubusercontent.com/dprojects/getDimensions/master/screenshots/sbcf003.png)

or for all elements:

![sbcf004](https://raw.githubusercontent.com/dprojects/getDimensions/master/screenshots/sbcf004.png)

![sbcf005](https://raw.githubusercontent.com/dprojects/getDimensions/master/screenshots/sbcf005.png)

### Sample usage - Summary for Edge Size Feature:

By default the feature "Summary for Edge Size Feature" calculate the whole edge and do not have 
to be turned on. But in the real world the edge size that needs to be covered is very often 
much smaller. For example You can skip "Back" or "HDF" parts to calculate costs better. To do it, 
just make Your project Tree for better visibility management e.g.:

![sesf001](https://raw.githubusercontent.com/dprojects/getDimensions/master/screenshots/sesf001.png)

Set Your "Toggle Visibility Feature" to "edge":

![sesf002](https://raw.githubusercontent.com/dprojects/getDimensions/master/screenshots/sesf002.png)

Turn off parts You do not want to calculate (e.g. press "space" on "HDF" group):

![sesf003](https://raw.githubusercontent.com/dprojects/getDimensions/master/screenshots/sesf003.png)

and run the macro:

![sesf004](https://raw.githubusercontent.com/dprojects/getDimensions/master/screenshots/sesf004.png)


# Printing

TechDraw page is automatically created and it is named "toPrint". So now You can print directly from the 
page named "toPrint" or just export this page to pdf file and print it later. 

# Screenshots

|   |   |   |
|---|---|---|
| [![001](https://raw.githubusercontent.com/dprojects/getDimensions/master/screenshots/matrix/001.png)](https://raw.githubusercontent.com/dprojects/getDimensions/master/screenshots/matrix/001.png) | [![002](https://raw.githubusercontent.com/dprojects/getDimensions/master/screenshots/matrix/002.png)](https://raw.githubusercontent.com/dprojects/getDimensions/master/screenshots/matrix/002.png) | [![003](https://raw.githubusercontent.com/dprojects/getDimensions/master/screenshots/matrix/003.png)](https://raw.githubusercontent.com/dprojects/getDimensions/master/screenshots/matrix/003.png) |
| [![004](https://raw.githubusercontent.com/dprojects/getDimensions/master/screenshots/matrix/004.png)](https://raw.githubusercontent.com/dprojects/getDimensions/master/screenshots/matrix/004.png) | [![005](https://raw.githubusercontent.com/dprojects/getDimensions/master/screenshots/matrix/005.png)](https://raw.githubusercontent.com/dprojects/getDimensions/master/screenshots/matrix/005.png) | [![006](https://raw.githubusercontent.com/dprojects/getDimensions/master/screenshots/matrix/006.png)](https://raw.githubusercontent.com/dprojects/getDimensions/master/screenshots/matrix/006.png) |

# Known issues

* Special characters (Polish) for chipboards (object cube names) not supported. However, You can change 
the names later manually in spreadsheet and the TechDraw view will be automatically updated with new names. 

# Contact

Please add all comments and questions in FreeCAD forum topic related to this project available at:
[https://forum.freecadweb.org/viewtopic.php?f=22&t=21127](https://forum.freecadweb.org/viewtopic.php?f=22&t=21127)

# License

MIT
