# Table of Contents

1. [Default settings](#default-settings)
2. [Furniture parts](#furniture-parts)
	1. [Cube - quickstart](#cube---quickstart)
	2. [Pad - quickstart](#pad---quickstart)
	3. [Which one should I choose?](#which-one-should-i-choose)
	4. [Basic furniture example](#basic-furniture-example)
3. [Transformations](#transformations)
	1. [Array - Cube](#array---cube)
	2. [Array - Pad](#array---pad)
	3. [Array Polar - Cube](#array-polar---cube)
	4. [Array Polar - Pad](#array-polar---pad)
	5. [Single Mirror - Pad](#single-mirror---pad)
	6. [MultiTransform Mirror - Pad](#multitransform-mirror---pad)
	7. [Advanced furniture example](#advanced-furniture-example)
4. [Report customization](#report-customization)
	1. [Visibility](#visibility)
	2. [Group furniture parts](#group-furniture-parts)
		1. [Name report](#name-report)
		2. [Quantity report](#quantity-report)
		3. [Group report](#group-report)
	3. [Edge size](#edge-size)
5. [Known issues](#known-issues)
6. [Special thanks](#special-thanks)
7. [Feature requests](#feature-requests)

# Default settings

![ds001](https://raw.githubusercontent.com/dprojects/getDimensions/master/Screenshots/ds001.png)

**Note:** Most of all `toPrint` reports screenshots are made with `sLTF` variable set to `n`, for better readability.

# Furniture parts

Furniture parts are base objects for building furniture, base construction element. Each object needs to have three dimensions (`Width`, `Height`, `Length`) to be considered as furniture part. Also it needs to have rectangular shape (four edges), to calculate area and edge size. You can consider furniture part as wood board, or even better, the rectangular chipboard. 

## Cube - quickstart

Cube is the easiest way to create furniture. You can create it just by single button click. To do that, just follow steps:

* Go to `FreeCAD > Part > Create a cube solid > Cube data (tab)`
* Set `Length` to e.g. 300
* Set `Width` to e.g. 600
* Set `Height` to e.g. 18

	![cubes001](https://raw.githubusercontent.com/dprojects/getDimensions/master/Screenshots/cubes001.png)

	**Note**: Now You should have furniture part `300 mm x 600 mm x 18 mm`. You can create any furniture You like using such furniture part, even group them in folders.

* Now, just run the macro, to get report `toPrint`:
	
	![cubes002](https://raw.githubusercontent.com/dprojects/getDimensions/master/Screenshots/cubes002.png)

## Pad - quickstart

Pad is not base object. In fact, it is transformation on the Sketch object. However, for the macro purposes it is considered as base element for furniture building, furniture part. Mostly because the Sketch is not real-life object, because it has only two dimensions. 

* To start with Pad furniture part, You have to create Sketch object first. If You have the Sketch created already, just click the Sketch object and then the icon bordered in red at the screenshot below. The icon is also zoomed at the image:

	![pads001](https://raw.githubusercontent.com/dprojects/getDimensions/master/Screenshots/pads001.png)

	**Note**: Now You should have furniture part `300 mm x 600 mm x 18 mm`. You can create any furniture You like using such furniture part, even group them in folders.
	
* Now, just run the macro, to get report `toPrint`:

	![pads002](https://raw.githubusercontent.com/dprojects/getDimensions/master/Screenshots/pads002.png)

	**Note:** Normally, when You are creating Pad object, the related Sketch object should be in the "Pad folder" (object content). If You do not have such tree structure, please make sure each Pad object has the correct reference in the `Profile` structure. Sketch dimensions are getting from Pad, exactly from `.Profile[0].Shape.OrderedEdges[0].Length` and `.Profile[0].Shape.OrderedEdges[1].Length`. The last dimension is getting from Pad as well, but this time, exactly from `.Length.Value`. So, the key point it that, the values need to be accessible and correct to get it to work.

## Which one should I choose?

Personally, I used to design everything with `Cube` furniture part. With calculator and `Placement` option I was able to design any furniture I needed, even some tools like doweling jig. Designing simple furniture with `Cube` takes about 5 minutes and You can just use `CTRL-C` and `CTRL-V` keys to multiply `Cube` furniture part quickly, move it and change some dimensions if needed.

However, I see the power of `Pad`. The `Pad` furniture part is better supported by FreeCAD. I would say, this is how it should be designed under the FreeCAD. First You should create `Sketch` object, make it fully constrained and use `Pad` option on the fully constrained `Sketch`. It takes more time and effort but You can use more transformations then and such furniture is more compliant with FreeCAD point of view.

However, if You are new FreeCAD user and You want design single furniture, I would recommend to start with `Cube`. Later You can extend Your knowledge, use `Pad` and You will be able to use the full power of FreeCAD.

## Basic furniture example

* Create any furniture using Pads and Sketches:

    ![pads003](https://raw.githubusercontent.com/dprojects/getDimensions/master/Screenshots/pads003.png)
 
* Make sure all Your folders tree have the correct structure:

    ![pads004](https://raw.githubusercontent.com/dprojects/getDimensions/master/Screenshots/pads004.png)
    
* You can also create global furniture dimensions in a separate spreadsheet that gives You the ability to change the global furniture size later:
    
    ![pads005](https://raw.githubusercontent.com/dprojects/getDimensions/master/Screenshots/pads005.png)
    
* Now, just run the macro, to get report `toPrint`:
    
    ![pads006](https://raw.githubusercontent.com/dprojects/getDimensions/master/Screenshots/pads006.png)

# Transformations

The transformation of a furniture part is any FreeCAD operation that creates a new object and simplifies the process of furniture design.

**Note:** FreeCAD allows for many objects transformations but some are not supported e.g.: `Single Mirror` or `MultiTransform Mirror` of `Cube` furniture part. However, this macro support each transformation of any furniture part. 

## Array - Cube

To start with `Array` transformation of `Cube` furniture part, You have to create the furniture part for transformation first. In this case this will be `Cube` furniture part. If You already have the `Cube` created, just follow steps: 

* Click the `Cube` furniture part and create `Array` as it is demonstrated below:

	![arrays001](https://raw.githubusercontent.com/dprojects/getDimensions/master/Screenshots/arrays001.png)

* Now, just run the macro, to get report `toPrint`:
	
	![arrays002](https://raw.githubusercontent.com/dprojects/getDimensions/master/Screenshots/arrays002.png)

## Array - Pad

To start with `Array` transformation of `Pad` furniture part, You have to create the furniture part for transformation first. In this case this will be `Pad` furniture part. If You already have the `Pad` created, just follow steps: 

* Click the `Pad` furniture part and create `Array` as it is demonstrated below:

	![arrays003](https://raw.githubusercontent.com/dprojects/getDimensions/master/Screenshots/arrays003.png)

* Now, just run the macro, to get report `toPrint`:
	
	![arrays004](https://raw.githubusercontent.com/dprojects/getDimensions/master/Screenshots/arrays004.png)
	
* FreeCAD transformations have hidden base elements. Only the final transformed object is visible. Hovewer, it is not the issue, to have the `edge size` calculated as well just e.g. press the `Spacebar` key while on the `Pad` to make it visible and run the macro again:
	
	![arrays005](https://raw.githubusercontent.com/dprojects/getDimensions/master/Screenshots/arrays005.png)
	
	**Note:** Now You should see the `edge size` is calculated correctly.

## Array Polar - Cube

To start with `Array Polar` transformation of `Cube` furniture part, You have to create the furniture part for transformation first. In this case this will be `Cube` furniture part. If You already have the `Cube` created, just follow steps: 

* Click the `Cube` furniture part and create `Array Polar` as it is demonstrated below:

	![arrays006](https://raw.githubusercontent.com/dprojects/getDimensions/master/Screenshots/arrays006.png)

* Now, just run the macro, to get report `toPrint`:
	
	![arrays007](https://raw.githubusercontent.com/dprojects/getDimensions/master/Screenshots/arrays007.png)

## Array Polar - Pad

To start with `Array Polar` transformation of `Pad` furniture part, You have to create the furniture part for transformation first. In this case this will be `Pad` furniture part. If You already have the `Pad` created, just follow steps: 

* Click the `Pad` furniture part and create `Array Polar` as it is demonstrated below:

	![arrays008](https://raw.githubusercontent.com/dprojects/getDimensions/master/Screenshots/arrays008.png)

* Now, just run the macro, to get report `toPrint`:
	
	![arrays009](https://raw.githubusercontent.com/dprojects/getDimensions/master/Screenshots/arrays009.png)

## Single Mirror - Pad

To start with `Single Mirror` transformation of `Pad` furniture part, You have to create the furniture part for transformation first. In this case this will be `Pad` furniture part. If You already have the `Pad` created, just follow steps: 

* Click the `Pad` furniture part and create `Single Mirror` as it is demonstrated below:

	![padsSM001](https://raw.githubusercontent.com/dprojects/getDimensions/master/Screenshots/padsSM001.png)

* Now, just run the macro, to get report `toPrint`:
	
	![padsSM002](https://raw.githubusercontent.com/dprojects/getDimensions/master/Screenshots/padsSM002.png)

## MultiTransform Mirror - Pad

The `MultiTransform` allows for many transformations at the single step. To start with `MultiTransform Mirror` transformation of `Pad` furniture part, You have to create the furniture part for transformation first. In this case this will be `Pad` furniture part. If You already have the `Pad` created, just follow steps: 

* Click the `Pad` furniture part and create `MultiTransform Mirror` as it is demonstrated below:

	![padsMT001](https://raw.githubusercontent.com/dprojects/getDimensions/master/Screenshots/padsMT001.png)

* Now, just run the macro, to get report `toPrint`:
	
	![padsMT002](https://raw.githubusercontent.com/dprojects/getDimensions/master/Screenshots/padsMT002.png)

## Advanced furniture example

To use any mirror type of feature part with Your furniture project just follow the steps:

* Create any furniture using Pads and Sketches. You can use `Single Mirror` and `MultiTransform Mirror` at the same project. For example legs are four, so You can use `MultiTransform Mirror` from the single leg and `Single Mirror` for each pair of supporters between them:

	![pads007](https://raw.githubusercontent.com/dprojects/getDimensions/master/Screenshots/pads007.png)
	
* You can also create global furniture dimensions in a separate spreadsheet that gives You the ability to change the global furniture size later:
    
	![pads008](https://raw.githubusercontent.com/dprojects/getDimensions/master/Screenshots/pads008.png)
        
* Now, just run the macro, to get report `toPrint`:

	![pads009](https://raw.githubusercontent.com/dprojects/getDimensions/master/Screenshots/pads009.png)
	
	**Note:** If You want to calculate the `edge size` correctly, You have to use the visibility to show e.g. top and hide legs and other parts.

# Report customization

## Visibility

* Search `Toggle Visibility Feature` part in the `Default Settings` section in the macro code.
* Set `sTVF` variable to `on`.
* Now You can create any report You want just by toggle visibility items or group of items.

    ![tvf001](https://raw.githubusercontent.com/dprojects/getDimensions/master/Screenshots/tvf001.png)

    ![tvf002](https://raw.githubusercontent.com/dprojects/getDimensions/master/Screenshots/tvf002.png)

    **Note:** You can generate different reports at the same furniture project. Just rename the TechDraw page `toPrint` to store it and prevent it from an overwrite or save it as `pdf` file.

## Group furniture parts

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
    
* Now, just run the macro, to get report `toPrint`:

    ![ltf004](https://raw.githubusercontent.com/dprojects/getDimensions/master/Screenshots/ltf004.png)
    
## Edge size

* Search `Toggle Visibility Feature` part in the `Default Settings` section in the macro code.
* By default the feature `Toggle Visibility Feature` is set to `edge` because in the real world the `edge size` that needs to be covered is very often much smaller. For example You can skip any parts to calculate costs better. To do this, just organize Your project tree with exact visibility, because this feature works for any folder and transformation like `Array`:

    ![edge001](https://raw.githubusercontent.com/dprojects/getDimensions/master/Screenshots/edge001.png)
    
    ![edge002](https://raw.githubusercontent.com/dprojects/getDimensions/master/Screenshots/edge002.png)
    
* Hide parts You do not wish to calculate (e.g. press the `Spacebar` key while on the `Array`) as it is demonstrated below:

    ![edge003](https://raw.githubusercontent.com/dprojects/getDimensions/master/Screenshots/edge003.png)
    
* Now, just run the macro, to get report `toPrint`:
    
    ![edge004](https://raw.githubusercontent.com/dprojects/getDimensions/master/Screenshots/edge004.png)

    **Note:** The `edge size` should be different now.

* If You want to calculate the `edge size` for all furniture parts just set `sTVF` to `off`:
	
	![edge005](https://raw.githubusercontent.com/dprojects/getDimensions/master/Screenshots/edge005.png)

# Known issues

* **Issue**: Special characters (e.g. Polish) for chipboards (objects names) are not supported. 
	* **Workaround**: You can change the names later manually in the spreadsheet `toCut` and the TechDraw report named `toPrint` will be automatically updated with new names.

* **Issue**: Units at TechDraw page `toPrint` disappear after open project again.
	* **Workaround**: FreeCAD has problem with units generally. The units are still available in the spreadsheet `toCut`. To bring them back to the TechDraw report named `toPrint` You have to run the macro again. To keep them forever just save the TechDraw report named `toPrint` to `pdf` file.

# Special thanks

* `Array` feature has been suggested to me at the [FreeCAD forum thread by jaisejames](https://forum.freecadweb.org/viewtopic.php?p=164072#p164072), Thanks.

* `Inches` feature has been suggested to me at the [FreeCAD forum thread by acousticguy](https://forum.freecadweb.org/viewtopic.php?p=286030#p286030), Thanks.

* `Pads` feature has been suggested to me at the [FreeCAD forum thread by Petert](https://forum.freecadweb.org/viewtopic.php?p=547453#p547453), Thanks.

# Feature requests

Best way to ask for new feature is [FreeCAD forum thread](https://forum.freecadweb.org/viewtopic.php?f=22&t=21127). However, You need to be convincing and provide an argument and concrete examples of the use of this functionality in the furniture design process. You have to keep in mind that FreeCAD has a lot of possibilities and not everything has to be implemented. 

___
**Note:** For more details see the [Demo folder](https://github.com/dprojects/getDimensions/tree/master/Demo).
