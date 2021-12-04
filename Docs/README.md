## Table of Contents

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

## Default settings

![ds001](https://raw.githubusercontent.com/dprojects/getDimensions/master/Screenshots/ds001.png)

## Quickstart

* Go to `FreeCAD > Part > Create a cube solid > Cube data (tab)`
* Set `Length` to e.g. 500
* Set `Width` to e.g. 500
* Set `Height` to e.g. 18

  **NOTE**: Now you should have chipboard `500mm x 500mm x 18mm`. You can create whatever you like using such chipboards. Even group them in folders.

* Run macro.

## Printing

TechDraw page is automatically created and it is named `toPrint`. You can print directly from the page named `toPrint` or just export this page to pdf file and print it later. 

## Known issues

* Special characters (Polish) for chipboards (object cube names) not supported. However, you can change the names later manually within the spreadsheet and the TechDraw view will be automatically updated with new names. 

## Features

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

  **Result:** Now you can create any report you want just by toggling visibility items or groups of items.

    ![tvf001](https://raw.githubusercontent.com/dprojects/getDimensions/master/Screenshots/tvf001.png)

    ![tvf002](https://raw.githubusercontent.com/dprojects/getDimensions/master/Screenshots/tvf002.png)

* **Note:** You can generate different reports at the same furniture project. Just rename the TechDraw page `toPrint` to store it and prevent it from an overwrite.

### Group objects

* Search `Label Type Feature` part in the `default settings` section within the macro code.
* Set `sLTF` variable to the exact value you want.

#### Name report

To create list of names just set `sLTF` variable to `n` and run the macro:

  ![ltf001](https://raw.githubusercontent.com/dprojects/getDimensions/master/Screenshots/ltf001.png)

#### Quantity report

To create quantity report just set `sLTF` variable to `q` and run macro:

  ![ltf002](https://raw.githubusercontent.com/dprojects/getDimensions/master/Screenshots/ltf002.png)
    
#### Group report

For group mode `g`, you'll need to have the exact folder tree structure in your furniture project. The idea behind this is that each element needs to have both a  'parent' folder and a 'grandparent' folder. For example, an element named `Foot L` needs to be in the parent folder (e.g. named `Foot`). Also the `Foot` folder needs to be in the grandparent folder (e.g. named `White color`). 

See the screenshot tree demonstrating this:

  ![ltf003](https://raw.githubusercontent.com/dprojects/getDimensions/master/Screenshots/ltf003.png)
    
Now you'll be able to generate the TechDraw page `toPrint` with the macro:

  ![ltf004](https://raw.githubusercontent.com/dprojects/getDimensions/master/Screenshots/ltf004.png)
    
### Edge size

* Search `Toggle Visibility Feature` part in the "default settings" section in the macro code.
* Set `sTVF` variable to `edge`.
* By default the feature `Summary for Edge Size Feature` calculates the whole edge and doesn't have to be enabled. But in the real world the edge size that needs to be covered is very often much smaller. For example, you can skip any parts to calculate costs better. To do this, just organize your project tree with better visibility management in mind.  This can be done for Array as well:

    ![sesf001](https://raw.githubusercontent.com/dprojects/getDimensions/master/Screenshots/sesf001.png)
    
    ![sesf002](https://raw.githubusercontent.com/dprojects/getDimensions/master/Screenshots/sesf002.png)
    
* Hide parts you do not wish to calculate (e.g. press the `Spacebar` key while on the `Array` group) as demonstrated in:

    ![sesf003](https://raw.githubusercontent.com/dprojects/getDimensions/master/Screenshots/sesf003.png)
    
* Run the macro
  **Result:** the edge size is different now):
    
    ![sesf004](https://raw.githubusercontent.com/dprojects/getDimensions/master/Screenshots/sesf004.png)

    
### Pads and Sketches

* Create any furniture using Pads and Sketches. 

    ![pads001](https://raw.githubusercontent.com/dprojects/getDimensions/master/Screenshots/pads001.png)
 
* Make sure all your folder tree have the correct structure. The Sketch object must be in the Pad folder:

    ![pads002](https://raw.githubusercontent.com/dprojects/getDimensions/master/Screenshots/pads002.png)
    
* You can also create global furniture dimensions in a separate spreadsheet that gives you the ability to change the global furniture size later:
    ![pads003](https://raw.githubusercontent.com/dprojects/getDimensions/master/Screenshots/pads003.png)
    
* Now you can create a report with all necessary dimensions to cut:
    
    ![pads004](https://raw.githubusercontent.com/dprojects/getDimensions/master/Screenshots/pads004.png)


  **Important note:** This is an experimental feature, so advanced features like mirror are not working. See the demo for pads to see the correct directory tree in the [Demo folder](https://github.com/dprojects/getDimensions/tree/master/Demo)
