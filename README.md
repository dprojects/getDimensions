# Description

<img align="left" src="https://raw.githubusercontent.com/dprojects/Woodworking/master/Icons/getDimensions.png"> This FreeCAD macro gets dimensions of furniture parts. It has been designed for my private woodworking projects (hobby), especially for chipboards 18 mm of thickness (they are the most common in Poland). This macro creates a spreadsheet named `toCut` and also a TechDraw page `toPrint` with all needed furniture parts to cut for woodworking project. 

**Note:** This tool is also part of [Woodworking workbench](https://github.com/dprojects/Woodworking).

<br><br>

![pl](https://raw.githubusercontent.com/dprojects/getDimensions/master/Screenshots/lang_pl.png)

![en](https://raw.githubusercontent.com/dprojects/getDimensions/master/Screenshots/lang_en.png)

# Main features

* **Languages:** Polish, English.
* **Units:** millimeters, meters, inches.
* **Report types:**
	* quick, quantity first (q - report type),
	* names, objects listing (n - report type),
	* group, grandparent or parent folder name first (g - report type),
	* edgeband, extended edge (e - report type),
	* detailed, edgeband, drill holes, countersinks (d - report type),
	* constraints names, totally custom report (c - report type),
	* pads, all constraints (p - report type),
	* approximation of needed material (a - report type).
* **Additional reports:**
	* Custom measurements:
		* App :: MeasureDistance.
	* Dowels and Screws - dowels made from:
		* Part :: Cylinder.
	* Profiles - metal construction elements made from: 
		* PartDesign :: Thickness, 
		* Dodo workbench profiles.
	* Decoration - decoration elements e.g. drawer handle:
		* PartDesign :: Fillet, 
		* PartDesign :: Chamfer, 
		* Part :: Sphere, 
		* Part :: Cone, 
		* Part :: Torus.
* **Woodworking usage:**
	* wood properties - grain direction, type of wood, color of wood,
	* edgeband (quick way, described, detailed by selection),
	* dowels, pilot holes, countersinks,
	* custom furniture part,
	* 32 mm cabinetmaking system.
* **Calculations:** quantity, thickness, area, edge size, edgeband.
* **Supported furniture parts:**
    * Part :: Cube,
    * PartDesign :: Pad.
* **Supported transformations:**
    * Part :: Mirroring,
    * Draft :: Array,
    * Draft :: Array Polar,
    * Draft :: Clone,
    * PartDesign :: Pocket,
    * PartDesign :: Hole,
    * PartDesign :: LinearPattern,
    * PartDesign :: Mirrored,
    * PartDesign :: MultiTransform,
    * App :: Link,
	* App :: LinkGroup,
	* Part :: Compound,
	* Part :: Cut.
* **Settings by:** Qt Graphical User Interface (GUI), code variables.
* **Outputs:** Spreadsheet, TechDraw page, Spreadsheet multi-page export by [sheet2export](https://github.com/dprojects/sheet2export).

![en2](https://raw.githubusercontent.com/dprojects/getDimensions/master/Screenshots/lang_en2.png)

For more details see documentation page: [in Docs folder](https://github.com/dprojects/getDimensions/tree/master/Docs).

# Screenshots

|   |   |
|---|---|
| [![c1r1](https://raw.githubusercontent.com/dprojects/getDimensions/master/Screenshots/matrix/c1r1.png)](https://raw.githubusercontent.com/dprojects/getDimensions/master/Screenshots/matrix/c1r1.png) | [![c2r1](https://raw.githubusercontent.com/dprojects/getDimensions/master/Screenshots/matrix/c2r1.png)](https://raw.githubusercontent.com/dprojects/getDimensions/master/Screenshots/matrix/c2r1.png) |
| [![c1r2](https://raw.githubusercontent.com/dprojects/getDimensions/master/Screenshots/matrix/c1r2.png)](https://raw.githubusercontent.com/dprojects/getDimensions/master/Screenshots/matrix/c1r2.png) | [![c2r2](https://raw.githubusercontent.com/dprojects/getDimensions/master/Screenshots/matrix/c2r2.png)](https://raw.githubusercontent.com/dprojects/getDimensions/master/Screenshots/matrix/c2r2.png) |
| [![c1r3](https://raw.githubusercontent.com/dprojects/getDimensions/master/Screenshots/matrix/c1r3.png)](https://raw.githubusercontent.com/dprojects/getDimensions/master/Screenshots/matrix/c1r3.png) | [![c2r3](https://raw.githubusercontent.com/dprojects/getDimensions/master/Screenshots/matrix/c2r3.png)](https://raw.githubusercontent.com/dprojects/getDimensions/master/Screenshots/matrix/c2r3.png) |
| [![c1r4](https://raw.githubusercontent.com/dprojects/getDimensions/master/Screenshots/matrix/c1r4.png)](https://raw.githubusercontent.com/dprojects/getDimensions/master/Screenshots/matrix/c1r4.png) | [![c2r4](https://raw.githubusercontent.com/dprojects/getDimensions/master/Screenshots/matrix/c2r4.png)](https://raw.githubusercontent.com/dprojects/getDimensions/master/Screenshots/matrix/c2r4.png) |
| [![c1r5](https://raw.githubusercontent.com/dprojects/getDimensions/master/Screenshots/matrix/c1r5.png)](https://raw.githubusercontent.com/dprojects/getDimensions/master/Screenshots/matrix/c1r5.png) | [![c2r5](https://raw.githubusercontent.com/dprojects/getDimensions/master/Screenshots/matrix/c2r5.png)](https://raw.githubusercontent.com/dprojects/getDimensions/master/Screenshots/matrix/c2r5.png) |

# Contact

Please add all comments and questions to the dedicated
[FreeCAD forum thread](https://forum.freecadweb.org/viewtopic.php?f=22&t=21127).

# License

MIT
