# Table of Contents

1. [Default settings](#default-settings)
2. [Quickstart](#quickstart)
3. [Printing](#printing)
4. [Known issues](#known-issues)
5. [Arrays](#arrays)
6. [Toggle Visibility](#toggle-visibility)
7. [Group objects](#group-objects)
    1. [Name report](#name-report)
    2. [Quantity report](#quantity-report)
    3. [Group report](#group-report)
8. [Edge size](#edge-size)
9. [Pads and Sketches](#pads-and-sketches)
	1. [Pads Basic](#pads-basic)
	2. [Pads Single Mirror](#pads-single-mirror)
    3. [Pads MultiTransform Mirror](#pads-multitransform-mirror)
    4. [Pads Mirror - usage example](#pads-mirror---usage-example)

# Default settings

![ds001](https://raw.githubusercontent.com/dprojects/getDimensions/master/Screenshots/ds001.png)

# Quickstart

* Go to `FreeCAD > Part > Create a cube solid > Cube data (tab)`
* Set `Length` to e.g. 500
* Set `Width` to e.g. 500
* Set `Height` to e.g. 18

	**Note**: Now you should have chipboard `500 mm x 500 mm x 18 mm`. You can create whatever you like using such chipboards. Even group them in folders.

* Run macro.

# Printing

TechDraw page is automatically created and it is named `toPrint`. You can print directly from the page named `toPrint` or just export this page to `pdf` file and print it later. 

# Known issues

* Special characters (e.g. Polish) for chipboards (objects names) are not supported. However, You can change the names later manually in the spreadsheet `toCut` and the TechDraw report named `toPrint` will be automatically updated with new names. 

# Arrays

This feature has been suggested to me at the [FreeCAD forum thread by jaisejames](https://forum.freecadweb.org/viewtopic.php?p=164072#p164072), Thanks.

* Project example (3D model view):

    ![arrays001](https://raw.githubusercontent.com/dprojects/getDimensions/master/Screenshots/arrays001.png)

* Project example (objects view):

    ![arrays002](https://raw.githubusercontent.com/dprojects/getDimensions/master/Screenshots/arrays002.png)

* Automatically generated report `toPrint` for project above:
    
    ![arrays003](https://raw.githubusercontent.com/dprojects/getDimensions/master/Screenshots/arrays003.png)
    
    ![arrays004](https://raw.githubusercontent.com/dprojects/getDimensions/master/Screenshots/arrays004.png)

# Toggle Visibility

* Search `Toggle Visibility Feature` part in the `default settings` section in the macro code.
* Set `sTVF` variable to `on`.
* Now You can create any report You want just by toggle visibility items or group of items.

    ![tvf001](https://raw.githubusercontent.com/dprojects/getDimensions/master/Screenshots/tvf001.png)

    ![tvf002](https://raw.githubusercontent.com/dprojects/getDimensions/master/Screenshots/tvf002.png)

    **Note:** You can generate different reports at the same furniture project. Just rename the TechDraw page `toPrint` to store it and prevent it from an overwrite.

# Group objects

* Search `Label Type Feature` part in the `default settings` section in the macro code.
* Set `sLTF` variable to the exact value You want.

## Name report

* To create list of names just set `sLTF` variable to `n` and run macro:

    ![ltf001](https://raw.githubusercontent.com/dprojects/getDimensions/master/Screenshots/ltf001.png)

## Quantity report

* To create quantity report just set `sLTF` variable to `q` and run macro:

    ![ltf002](https://raw.githubusercontent.com/dprojects/getDimensions/master/Screenshots/ltf002.png)
    
## Group report

* To create quantity report just set `sLTF` variable to `g` and run macro. However, for group mode, You need to have exact folder tree structure in Your furniture project. The idea behind this is that each element needs to have parent folder and also grandparent folder. For example, an element named `Foot L` needs to be in the parent folder (e.g. named `Foot`). Also the `Foot` folder needs to be in the grandparent folder (e.g. named `White color`). See the screenshot tree:

    ![ltf003](https://raw.githubusercontent.com/dprojects/getDimensions/master/Screenshots/ltf003.png)
    
* Now You can generate TechDraw page `toPrint` with the macro:

    ![ltf004](https://raw.githubusercontent.com/dprojects/getDimensions/master/Screenshots/ltf004.png)
    
# Edge size

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
    
# Pads and Sketches

This feature has been suggested to me at the [FreeCAD forum thread by Petert](https://forum.freecadweb.org/viewtopic.php?p=547453#p547453), Thanks.

## Pads Basic

* Create any furniture using Pads and Sketches. 

    ![pads001](https://raw.githubusercontent.com/dprojects/getDimensions/master/Screenshots/pads001.png)
 
* Make sure all Your folders tree have the correct structure. 

    ![pads002](https://raw.githubusercontent.com/dprojects/getDimensions/master/Screenshots/pads002.png)
    
    **Note:** Normally, when You are creating Pad object, the related Sketch object should be in the "Pad folder" (object content). If You do not have such tree structure, please make sure each Pad object has the correct reference in the `Profile` structure. Sketch dimensions are getting from Pad, exactly from `.Profile[0].Shape.OrderedEdges[0].Length` and `.Profile[0].Shape.OrderedEdges[1].Length`. The last dimension is getting from Pad as well, but this time, exactly from `.Length.Value`. So, the key point it that, the values need to be accessible and correct to get it to work.
    
* You can also create global furniture dimensions in a separate spreadsheet that gives You the ability to change the global furniture size later:
    
    ![pads003](https://raw.githubusercontent.com/dprojects/getDimensions/master/Screenshots/pads003.png)
    
* Now you can create the desired report with all necessary dimensions to cut:
    
    ![pads004](https://raw.githubusercontent.com/dprojects/getDimensions/master/Screenshots/pads004.png)

## Pads Single Mirror

FreCAD allows You to create Mirror for the Pad. One way is to use Single Mirror option. By the Single Mirror, I mean, the icon bordered in red at the screenshot below. The icon is also resized at the image. This kind of Mirror just creates new Pad object at the 3D model but the 2 elements created are named in folder tree structure `Mirrored`.

![padsSM001](https://raw.githubusercontent.com/dprojects/getDimensions/master/Screenshots/padsSM001.png)


## Pads MultiTransform Mirror

There is also another way of Mirror creation. This is named by FreeCAD `MultiTransform`. The `MultiTransform` allows for many transformations at single step. However, the Mirror is supported by the macro. The The `MultiTransform` icon is bordered in red at the screenshot below. The icon is also resized at the image.

![padsMT001](https://raw.githubusercontent.com/dprojects/getDimensions/master/Screenshots/padsMT001.png)

## Pads Mirror - usage example

To use any mirror type of feature with Your furniture projects just follow the steps:

* Create any furniture using Pads and Sketches. You can use `Single Mirror` and `MultiTransform Mirror` at the same project. For example legs are four so You can use `MultiTransform Mirror` from single leg and `Single Mirror` for each pair of supporters between them:

	![pads005](https://raw.githubusercontent.com/dprojects/getDimensions/master/Screenshots/pads005.png)
	
* You can also create global furniture dimensions in a separate spreadsheet that gives You the ability to change the global furniture size later:
    
	![pads006](https://raw.githubusercontent.com/dprojects/getDimensions/master/Screenshots/pads006.png)
        
* Now you can create the desired report with all necessary dimensions to cut. However, if You want calculate the edge correctly, just use the visibility to show e.g. top and hide legs and other parts:

	![pads007](https://raw.githubusercontent.com/dprojects/getDimensions/master/Screenshots/pads007.png)

**Note:** For more details see the [Demo folder](https://github.com/dprojects/getDimensions/tree/master/Demo).
