# Default settings

![ds001](https://raw.githubusercontent.com/dprojects/getDimensions/master/Screenshots/ds001.png)

# Usage - quickstart

* Go to FreeCAD -> Part -> Create a cube solid -> Cube data (tab):
* Set "Length" to e.g. 500
* Set "Width" to e.g. 500
* Set "Height" to e.g. 18

**NOTE**: Now you should have chipboard 500 mm x 500 mm x 18 mm. You can create whatever you like using such chipboards. Even group them in folders.

* Run macro.

# Printing

TechDraw page is automatically created and it is named "toPrint". You can print directly from the page named "toPrint" or just export this page to pdf file and print it later. 

# Known issues

* Special characters (Polish) for chipboards (object cube names) not supported. However, You can change the names later manually in spreadsheet and the TechDraw view will be automatically updated with new names. 

# Features

### Arrays:

* This macro supports arrays made of cube (thanks [jaisejames](https://forum.freecadweb.org/memberlist.php?mode=viewprofile&u=10269)).
* Project example (3D model view):

    ![arrays001](https://raw.githubusercontent.com/dprojects/getDimensions/master/Screenshots/arrays001.png)

* Project example (objects view):

    ![arrays002](https://raw.githubusercontent.com/dprojects/getDimensions/master/Screenshots/arrays002.png)

* Automatically generated report "toPrint" for project above:
    
    ![arrays003](https://raw.githubusercontent.com/dprojects/getDimensions/master/Screenshots/arrays003.png)
    
    ![arrays004](https://raw.githubusercontent.com/dprojects/getDimensions/master/Screenshots/arrays004.png)

### Toggle Visibility Feature:

* Search "Toggle Visibility Feature" part in the "default settings" section in the macro code.
* Set "sTVF" variable to "on".
* Now You can create any report You want just by toggle visibility items or group of items.

    ![tvf001](https://raw.githubusercontent.com/dprojects/getDimensions/master/Screenshots/tvf001.png)

    ![tvf002](https://raw.githubusercontent.com/dprojects/getDimensions/master/Screenshots/tvf002.png)

* You can generate different reports at the same furniture project. Just rename the TechDraw page "toPrint" to store it and prevent from overwrite.

### Label Type Feature:

* Search "Label Type Feature" part in the "default settings" section in the macro code.
* Set "sLTF" variable to exact value You want.

#### Create name list

* To create list of names just set "sLTF" variable to "n" and run macro:

    ![ltf001](https://raw.githubusercontent.com/dprojects/getDimensions/master/Screenshots/ltf001.png)

#### Create quantity report

* To create quantity report just set "sLTF" variable to "q" and run macro:

    ![ltf002](https://raw.githubusercontent.com/dprojects/getDimensions/master/Screenshots/ltf002.png)
    
#### Create group report

* For group mode "g", You need to have exact folder tree structure in Your furniture project. The idea behind it is that each element need to has parent folder and also grandparent folder. For exaple element named "Foot L" need to be in parent folder (e.g. named "Foot"). Also the "Foot" folder need to be in grandparent folder (e.g. named "White color"). See example:

    ![ltf003](https://raw.githubusercontent.com/dprojects/getDimensions/master/Screenshots/ltf003.png)
    
* Now You can generate TechDraw page "toPrint" with the macro:

    ![ltf004](https://raw.githubusercontent.com/dprojects/getDimensions/master/Screenshots/ltf004.png)
    
### Summary for Edge Size Feature:

* Search "Toggle Visibility Feature" part in the "default settings" section in the macro code.
* Set "sTVF" variable to "edge".
* By default the feature "Summary for Edge Size Feature" calculate the whole edge and do not have to be turned on. But in the real world the edge size that needs to be covered is very often much smaller. For example You can skip any parts to calculate costs better. To do it, just make Your project Tree for better visibility management, e.g. You can do it for Array as well:

    ![sesf001](https://raw.githubusercontent.com/dprojects/getDimensions/master/Screenshots/sesf001.png)
    
    ![sesf002](https://raw.githubusercontent.com/dprojects/getDimensions/master/Screenshots/sesf002.png)
    
* Turn off parts You do not want to calculate (e.g. press "space" on "Array" group):

    ![sesf003](https://raw.githubusercontent.com/dprojects/getDimensions/master/Screenshots/sesf003.png)
    
* and run the macro (the edge size is different now):
    
    ![sesf004](https://raw.githubusercontent.com/dprojects/getDimensions/master/Screenshots/sesf004.png)

    
### Pads and Sketches:

* Create any furniture using Pads and Sketches. 

    ![pads001](https://raw.githubusercontent.com/dprojects/getDimensions/master/Screenshots/pads001.png)
 
* Make sure all your folder tree has correct structure. The Sketch object must be in the Pad folder:

    ![pads002](https://raw.githubusercontent.com/dprojects/getDimensions/master/Screenshots/pads002.png)
    
* You can also create global furniture dimensions in seprate spreadsheet to be able to change the global furniture size later:
    
    ![pads003](https://raw.githubusercontent.com/dprojects/getDimensions/master/Screenshots/pads003.png)
    
* Now you can create report with all needed dimensions to cut:
    
    ![pads004](https://raw.githubusercontent.com/dprojects/getDimensions/master/Screenshots/pads004.png)

    
This is experimental feature, so advanced features like mirror not working. See the demo for pads to see the correct directory tree: [here](https://github.com/dprojects/getDimensions/tree/master/Demo)
