# Description

This FreeCAD macro gets dimensions of furniture parts. It has been designed for my private woodworking projects (hobby), especially for chipboards 18 mm of thickness (they are the most common in Poland). This macro creates a spreadsheet named `toCut` and also a TechDraw page `toPrint` with all needed furniture parts to cut for woodworking project. 

![pl](https://raw.githubusercontent.com/dprojects/getDimensions/master/Screenshots/lang_pl.png)

![en](https://raw.githubusercontent.com/dprojects/getDimensions/master/Screenshots/lang_en.png)

# Main features

* **Languages:** Polish, English.
* **Units:** millimeters, meters, inches.
* **Settings by:** Qt Graphical User Interface (GUI), code variables.
* **Outputs:** Spreadsheet, TechDraw page.
* **Raport types:**
	* automatic by quantity (dimensions),
	* automatic by objects names (listing),
	* automatic by groups (folder names),
	* custom by objects toggle visibility,
	* custom by constraints names (totally custom report).
* **Calculations:** thickness, area, edge size.
* **Support for wood properties:** grain direction, type of wood, wood color.
* **Supported furniture parts:** 
    * Part :: Cube,
    * PartDesign :: Pad.
* **Supported transformations:** 
    * Part :: Mirroring,
    * Draft :: Array,
    * Draft :: Array Polar,
    * PartDesign :: Mirrored,
    * PartDesign :: MultiTransform.


For more details see documentation page: [in Docs folder](https://github.com/dprojects/getDimensions/tree/master/Docs).

# Screenshots

|   |   |   |
|---|---|---|
| [![c1r1](https://raw.githubusercontent.com/dprojects/getDimensions/master/Screenshots/matrix/c1r1.png)](https://raw.githubusercontent.com/dprojects/getDimensions/master/Screenshots/matrix/c1r1.png) | [![c2r1](https://raw.githubusercontent.com/dprojects/getDimensions/master/Screenshots/matrix/c2r1.png)](https://raw.githubusercontent.com/dprojects/getDimensions/master/Screenshots/matrix/c2r1.png) | [![c3r1](https://raw.githubusercontent.com/dprojects/getDimensions/master/Screenshots/matrix/c3r1.png)](https://raw.githubusercontent.com/dprojects/getDimensions/master/Screenshots/matrix/c3r1.png) |
| [![c1r2](https://raw.githubusercontent.com/dprojects/getDimensions/master/Screenshots/matrix/c1r2.png)](https://raw.githubusercontent.com/dprojects/getDimensions/master/Screenshots/matrix/c1r2.png) | [![c2r2](https://raw.githubusercontent.com/dprojects/getDimensions/master/Screenshots/matrix/c2r2.png)](https://raw.githubusercontent.com/dprojects/getDimensions/master/Screenshots/matrix/c2r2.png) | [![c3r2](https://raw.githubusercontent.com/dprojects/getDimensions/master/Screenshots/matrix/c3r2.png)](https://raw.githubusercontent.com/dprojects/getDimensions/master/Screenshots/matrix/c3r2.png) |

# Contact

Please add all comments and questions to the dedicated
[FreeCAD forum thread](https://forum.freecadweb.org/viewtopic.php?f=22&t=21127).

# License

MIT
