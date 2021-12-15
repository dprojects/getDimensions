# Table of Contents

1. [Default settings](#default-settings)
2. [Furniture parts](#furniture-parts)
	1. [Cube - quickstart](#cube---quickstart)
	2. [Pad - basic](#pad---basic)
3. [Transformations](#transformations)
	1. [Cube Array](#cube-array)
	2. [Cube Array Polar](#cube-array-polar)
	3. [Pad Single Mirror](#pad-single-mirror)
	4. [Pad MultiTransform Mirror](#pad-multitransform-mirror)
	5. [Pad Mirror - usage example](#pad-mirror---usage-example)
4. [Report customization](#report-customization)
	1. [Toggle Visibility](#toggle-visibility)
	2. [Group objects](#group-objects)
		1. [Name report](#name-report)
		2. [Quantity report](#quantity-report)
		3. [Group report](#group-report)
	3. [Edge size](#edge-size)
5. [Known issues](#known-issues)
6. [Special thanks](#special-thanks)

# Default settings

![ds001](https://raw.githubusercontent.com/dprojects/getDimensions/master/Screenshots/ds001.png)

# Furniture parts

Furniture parts are base objects for building furniture. Each object needs to have three dimensions (`Width`, `Height`, `Length`) to be considered as furniture part. Also it needs to have squared shape and four edges, to calculate area and edge size. You can consider furniture part as wood board or even better, the squared chipboard. 

## Cube - quickstart

Cube is the easiest way to create furniture. You can create it just by single button click. To do that, just follow steps:

* Go to `FreeCAD > Part > Create a cube solid > Cube data (tab)`
* Set `Length` to e.g. 300
* Set `Width` to e.g. 600
* Set `Height` to e.g. 18

	![cubes001](https://raw.githubusercontent.com/dprojects/getDimensions/master/Screenshots/cubes001.png)

	**Note**: Now You should have chipboard `300 mm x 600 mm x 18 mm`. You can create whatever You like using such chipboards. Even group them in folders.

* Now, just run the macro, to get report `toPrint`:
	
	![cubes002](https://raw.githubusercontent.com/dprojects/getDimensions/master/Screenshots/cubes002.png)

## Pad - basic

Pad is not base object. In fact it is transformation on the Sketch object. However, for the macro purposes it is considered as base element for furniture building, furniture part. Mostly because th Sketch is not real-life object, because it has only two dimensions. To start with Pad furniture part, just follow the steps below: 

* Create any furniture using Pads and Sketches.

    ![pads001](https://raw.githubusercontent.com/dprojects/getDimensions/master/Screenshots/pads001.png)
 
* Make sure all Your folders tree have the correct structure. 

    ![pads002](https://raw.githubusercontent.com/dprojects/getDimensions/master/Screenshots/pads002.png)
    
    **Note:** Normally, when You are creating Pad object, the related Sketch object should be in the "Pad folder" (object content). If You do not have such tree structure, please make sure each Pad object has the correct reference in the `Profile` structure. Sketch dimensions are getting from Pad, exactly from `.Profile[0].Shape.OrderedEdges[0].Length` and `.Profile[0].Shape.OrderedEdges[1].Length`. The last dimension is getting from Pad as well, but this time, exactly from `.Length.Value`. So, the key point it that, the values need to be accessible and correct to get it to work.
    
* You can also create global furniture dimensions in a separate spreadsheet that gives You the ability to change the global furniture size later:
    
    ![pads003](https://raw.githubusercontent.com/dprojects/getDimensions/master/Screenshots/pads003.png)
    
* Now you can create the desired report with all necessary dimensions to cut:
    
    ![pads004](https://raw.githubusercontent.com/dprojects/getDimensions/master/Screenshots/pads004.png)

# Transformations

Transformation on furniture part is any FreCAD operation that creates new object and simplify furniture design process.

## Cube Array

To start with `Cube Array` transformation You need to create furniture part for transformation first. In this case this will be `Cube` furniture part. If You already have the `Cube` created, just follow steps: 

* Click the `Cube` furniture part and create `Array` like it is shown below:

	![arrays001](https://raw.githubusercontent.com/dprojects/getDimensions/master/Screenshots/arrays001.png)

* Run the macro:
	
	![arrays002](https://raw.githubusercontent.com/dprojects/getDimensions/master/Screenshots/arrays002.png)

## Cube Array Polar

To start with `Cube Array Polar` transformation You need to create furniture part for transformation first. In this case this will be `Cube`. If You already have the `Cube` created, just follow steps: 

* Click the `Cube` furniture part and create `Array Polar` like it is shown below:

	![arrays003](https://raw.githubusercontent.com/dprojects/getDimensions/master/Screenshots/arrays003.png)

* Run the macro:
	
	![arrays004](https://raw.githubusercontent.com/dprojects/getDimensions/master/Screenshots/arrays004.png)

## Pad Single Mirror

FreCAD allows You to create Mirror for the Pad. One way is to use `Single Mirror` option. By the `Single Mirror`, I mean, the icon bordered in red at the screenshot below. The icon is also zoomed at the image. This kind of `Mirror` creates new Pad object at the 3D model but both objects are visible as single object in the folder tree structure and it is named `Mirrored`.

![padsSM001](https://raw.githubusercontent.com/dprojects/getDimensions/master/Screenshots/padsSM001.png)

## Pad MultiTransform Mirror

There is also another way for `Pads Mirror` creation. This is named by FreeCAD `MultiTransform`. The `MultiTransform` allows for many transformations at the single step. The `MultiTransform` icon is bordered in red at the screenshot below. The icon is also zoomed at the image.

![padsMT001](https://raw.githubusercontent.com/dprojects/getDimensions/master/Screenshots/padsMT001.png)

## Pad Mirror - usage example

To use any mirror type of feature with Your furniture projects just follow the steps:

* Create any furniture using Pads and Sketches. You can use `Single Mirror` and `MultiTransform Mirror` at the same project. For example legs are four so You can use `MultiTransform Mirror` from single leg and `Single Mirror` for each pair of supporters between them:

	![pads005](https://raw.githubusercontent.com/dprojects/getDimensions/master/Screenshots/pads005.png)
	
* You can also create global furniture dimensions in a separate spreadsheet that gives You the ability to change the global furniture size later:
    
	![pads006](https://raw.githubusercontent.com/dprojects/getDimensions/master/Screenshots/pads006.png)
        
* Now you can create the desired report with all necessary dimensions to cut. However, if You want calculate the edge correctly, just use the visibility to show e.g. top and hide legs and other parts:

	![pads007](https://raw.githubusercontent.com/dprojects/getDimensions/master/Screenshots/pads007.png)

# Report customization

## Toggle Visibility

* Search `Toggle Visibility Feature` part in the `Default Settings` section in the macro code.
* Set `sTVF` variable to `on`.
* Now You can create any report You want just by toggle visibility items or group of items.

    ![tvf001](https://raw.githubusercontent.com/dprojects/getDimensions/master/Screenshots/tvf001.png)

    ![tvf002](https://raw.githubusercontent.com/dprojects/getDimensions/master/Screenshots/tvf002.png)

    **Note:** You can generate different reports at the same furniture project. Just rename the TechDraw page `toPrint` to store it and prevent it from an overwrite.

## Group objects

* Search `Label Type Feature` part in the `Default Settings` section in the macro code.
* Set `sLTF` variable to the exact value You want.

### Name report

* To create list of names just set `sLTF` variable to `n` and run macro:

    ![ltf001](https://raw.githubusercontent.com/dprojects/getDimensions/master/Screenshots/ltf001.png)

### Quantity report

* To create quantity report just set `sLTF` variable to `q` and run macro:

    ![ltf002](https://raw.githubusercontent.com/dprojects/getDimensions/master/Screenshots/ltf002.png)
    
### Group report

* To create quantity report just set `sLTF` variable to `g` and run macro. However, for group mode, You need to have exact folder tree structure in Your furniture project. The idea behind this is that each element needs to have parent folder and also grandparent folder. For example, an element named `Foot L` needs to be in the parent folder (e.g. named `Foot`). Also the `Foot` folder needs to be in the grandparent folder (e.g. named `White color`). See the screenshot tree:

    ![ltf003](https://raw.githubusercontent.com/dprojects/getDimensions/master/Screenshots/ltf003.png)
    
* Now You can generate TechDraw page `toPrint` with the macro:

    ![ltf004](https://raw.githubusercontent.com/dprojects/getDimensions/master/Screenshots/ltf004.png)
    
## Edge size

* Search `Toggle Visibility Feature` part in the `Default Settings` section in the macro code.
* By default the feature `Toggle Visibility Feature` is set to `edge` because in the real world the edge size that needs to be covered is very often much smaller. For example You can skip any parts to calculate costs better. To do this, just organize your project tree with exact visibility, because this feature works for any folder and transformation like `Array`:

    ![edge001](https://raw.githubusercontent.com/dprojects/getDimensions/master/Screenshots/edge001.png)
    
    ![edge002](https://raw.githubusercontent.com/dprojects/getDimensions/master/Screenshots/edge002.png)
    
* Hide parts You do not wish to calculate (e.g. press the `Spacebar` key while on the `Array`) as demonstrated in:

    ![edge003](https://raw.githubusercontent.com/dprojects/getDimensions/master/Screenshots/edge003.png)
    
* Run the macro. 
    
    ![edge004](https://raw.githubusercontent.com/dprojects/getDimensions/master/Screenshots/edge004.png)

    **Note:** The edge size should be different now.

* If You want to calculate the edge size for all furniture parts just set `sTVF` to `off`:
	
	![edge005](https://raw.githubusercontent.com/dprojects/getDimensions/master/Screenshots/edge005.png)

# Known issues

* **Issue**: Special characters (e.g. Polish) for chipboards (objects names) are not supported. 
	**Workaround**: You can change the names later manually in the spreadsheet `toCut` and the TechDraw report named `toPrint` will be automatically updated with new names.

* **Issue**: Units at TechDraw page `toPrint` disappear after open project again.
	**Workaround**: FreeCAD has problem with units generally. The units are still available in the spreadsheet `toCut`. To bring them back to the TechDraw report named `toPrint` You have to run the macro again. To keep them forever just save the TechDraw report named `toPrint` to `pdf` file.

# Special thanks

* Array feature has been suggested to me at the [FreeCAD forum thread by jaisejames](https://forum.freecadweb.org/viewtopic.php?p=164072#p164072), Thanks.

* Pads feature has been suggested to me at the [FreeCAD forum thread by Petert](https://forum.freecadweb.org/viewtopic.php?p=547453#p547453), Thanks.

___
**Note:** For more details see the [Demo folder](https://github.com/dprojects/getDimensions/tree/master/Demo).
