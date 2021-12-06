# Table of Contents

1. [Default settings](#default-settings)
2. [Quickstart](#quickstart)
3. [Printing](#printing)
4. [Known issues](#known-issues)
5. [Features](#features)
    1. [Arrays](#arrays)
    2. [Toggle Visibility](#toggle-visibility)
    3. [Group objects](#group-objects)
        1. [Name report](#name-report)
        2. [Quantity report](#quantity-report)
        3. [Group report](#group-report)
    4. [Edge size](#edge-size)
    5. [Pads and Sketches](#pads-and-sketches)

# Default settings

![ds001](https://raw.githubusercontent.com/dprojects/getDimensions/master/Screenshots/ds001.png)

# Quickstart

* Go to `FreeCAD > Part > Create a cube solid > Cube data (tab)`
* Set `Length` to e.g. 500
* Set `Width` to e.g. 500
* Set `Height` to e.g. 18

    **NOTE**: Now you should have chipboard `500 mm x 500 mm x 18 mm`. You can create whatever you like using such chipboards. Even group them in folders.

* Run macro.

# Printing

TechDraw page is automatically created and it is named `toPrint`. You can print directly from the page named `toPrint` or just export this page to pdf file and print it later. 

# Known issues

* Special characters (Polish) for chipboards (object cube names) not supported. However, You can change the names later manually in the spreadsheet `toCut` and the TechDraw report named `toPrint` will be automatically updated with new names. 

# Features

### Arrays

* This macro supports arrays made of cube (thanks [jaisejames](https://forum.freecadweb.org/memberlist.php?mode=viewprofile&u=10269)).
* Project example (3D model view):

    ![arrays001](https://raw.githubusercontent.com/dprojects/getDimensions/master/Screenshots/arrays001.png)

* Project example (objects view):

    ![arrays002](https://raw.githubusercontent.com/dprojects/getDimensions/master/Screenshots/arrays002.png)

* Automatically generated report `toPrint` for project above:
    
    ![arrays003](https://raw.githubusercontent.com/dprojects/getDimensions/master/Screenshots/arrays003.png)
    
    ![arrays004](https://raw.githubusercontent.com/dprojects/getDimensions/master/Screenshots/arrays004.png)

### Toggle Visibility

* Search `Toggle Visibility Feature` part in the `default settings` section in the macro code.
* Set `sTVF` variable to `on`.
* Now You can create any report You want just by toggle visibility items or group of items.

    ![tvf001](https://raw.githubusercontent.com/dprojects/getDimensions/master/Screenshots/tvf001.png)

    ![tvf002](https://raw.githubusercontent.com/dprojects/getDimensions/master/Screenshots/tvf002.png)

    **Note:** You can generate different reports at the same furniture project. Just rename the TechDraw page `toPrint` to store it and prevent it from an overwrite.

### Group objects

* Search `Label Type Feature` part in the `default settings` section in the macro code.
* Set `sLTF` variable to the exact value You want.

#### Name report

* To create list of names just set `sLTF` variable to `n` and run macro:

    ![ltf001](https://raw.githubusercontent.com/dprojects/getDimensions/master/Screenshots/ltf001.png)

#### Quantity report

* To create quantity report just set "sLTF" variable to "q" and run macro:

    ![ltf002](https://raw.githubusercontent.com/dprojects/getDimensions/master/Screenshots/ltf002.png)
    
#### Group report

* For group mode `g`, You need to have exact folder tree structure in Your furniture project. The idea behind this is that each element needs to have parent folder and also grandparent folder. For example, an element named `Foot L` needs to be in the parent folder (e.g. named `Foot`). Also the `Foot` folder needs to be in the grandparent folder (e.g. named `White color`). See the screenshot tree:

    ![ltf003](https://raw.githubusercontent.com/dprojects/getDimensions/master/Screenshots/ltf003.png)
    
* Now You can generate TechDraw page `toPrint` with the macro:

    ![ltf004](https://raw.githubusercontent.com/dprojects/getDimensions/master/Screenshots/ltf004.png)
    
### Edge size

* Search `Toggle Visibility Feature` part in the `default settings` section in the macro code.
* Set `sTVF` variable to `edge`.
* By default the feature `Summary for Edge Size Feature` calculates the whole edge and do not have to be activated. But in the real world the edge size that needs to be covered is very often much smaller. For example You can skip any parts to calculate costs better. To do this, just organize your project tree with exact visibility. This also can be done for `Array` objects:

    ![sesf001](https://raw.githubusercontent.com/dprojects/getDimensions/master/Screenshots/sesf001.png)
    
    ![sesf002](https://raw.githubusercontent.com/dprojects/getDimensions/master/Screenshots/sesf002.png)
    
* Hide parts You do not wish to calculate (e.g. press the `Spacebar` key while on the `Array` group) as demonstrated in:

    ![sesf003](https://raw.githubusercontent.com/dprojects/getDimensions/master/Screenshots/sesf003.png)
    
* Run the macro. 
    
    ![sesf004](https://raw.githubusercontent.com/dprojects/getDimensions/master/Screenshots/sesf004.png)

    **Note:** The edge size should be different now.
    
### Pads and Sketches

* Create any furniture using Pads and Sketches. 

    ![pads001](https://raw.githubusercontent.com/dprojects/getDimensions/master/Screenshots/pads001.png)
 
* Make sure all Your folder tree have the correct structure. 

    ![pads002](https://raw.githubusercontent.com/dprojects/getDimensions/master/Screenshots/pads002.png)
    
    **Note:** Normally, when You are creating Pad object, the related Sketch object should be in the "Pad folder" (object content). If You do not have such tree structure, please make sure each Pad object has the correct reference in the `profile` structure. Sketch dimensions are getting from Pad, exactly from `.Profile[0].Constraints[8].Value` and `.Profile[0].Constraints[9].Value`. The last dimension is getting from Pad as well, but this time, exactly from `.Length.Value`. So, the key point it that, those values needs to be accessible and correct to get it to work.
    
* You can also create global furniture dimensions in a separate spreadsheet that gives You the ability to change the global furniture size later:
    
    ![pads003](https://raw.githubusercontent.com/dprojects/getDimensions/master/Screenshots/pads003.png)
    
* Now you can create the desired report with all necessary dimensions to cut:
    
    ![pads004](https://raw.githubusercontent.com/dprojects/getDimensions/master/Screenshots/pads004.png)

    **Important note:** This is an experimental feature, so advanced features like mirror are not working. See the demo for pads to see the correct directory tree in the [Demo folder](https://github.com/dprojects/getDimensions/tree/master/Demo)
