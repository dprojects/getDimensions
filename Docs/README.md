# Table of Contents

1. [Default Settings](#default-settings)
2. [Furniture parts](#furniture-parts)
	1. [Cube - quickstart](#cube---quickstart)
	2. [Pad - quickstart](#pad---quickstart)
	3. [Design furniture not the furniture parts](#design-furniture-not-the-furniture-parts)
	4. [Basic furniture example](#basic-furniture-example)
3. [Transformations](#transformations)
	1. [Part :: Mirroring :: Cube](#part--mirroring--cube)
	2. [Part :: Mirroring :: Pad](#part--mirroring--pad)
	3. [Draft :: Array :: Cube](#draft--array--cube)
	4. [Draft :: Array :: Pad](#draft--array--pad)
	5. [Draft :: Array Polar :: Cube](#draft--array-polar--cube)
	6. [Draft :: Array Polar :: Pad](#draft--array-polar--pad)
	7. [PartDesign :: Mirrored :: Pad](#partdesign--mirrored--pad)
	8. [PartDesign :: MultiTransform :: Pad](#partdesign--multitransform--pad)
	9. [Advanced furniture example](#advanced-furniture-example)
4. [Report customization](#report-customization)
	1. [Visibility](#visibility)
	2. [Group furniture parts](#group-furniture-parts)
		1. [Name report](#name-report)
		2. [Quantity report](#quantity-report)
		3. [Group report](#group-report)
	3. [Edge size](#edge-size)
	4. [Constraints - totally custom report](#constraints---totally-custom-report)
5. [Known issues](#known-issues)
6. [Special thanks](#special-thanks)
7. [Feature requests](#feature-requests)

# Default Settings

This macro supports Qt Graphical User Interface (GUI), so You can quickly change the settings with the help of the mouse wheel:

![ds001](https://raw.githubusercontent.com/dprojects/getDimensions/master/Docs/Screenshots/ds001.png)

If for some reasons would You like to turn the Qt GUI off, just edit the macro code and set the variable `sQT` to `"no"`. All the `Default Settings` will be set from the variables in the macro code.

![ds002](https://raw.githubusercontent.com/dprojects/getDimensions/master/Docs/Screenshots/ds002.png)

**Note:** Most of all `toPrint` reports screenshots are made with `sLTF` variable set to `n`, for better readability.

# Furniture parts

Furniture parts are base objects for building furniture, base construction element. Each object needs to have three dimensions (`Width`, `Height`, `Length`) to be considered as furniture part. Also it needs to have rectangular shape (four edges), to calculate area and edge size. You can consider furniture part as wood board, or even better, the rectangular chipboard. 

## Cube - quickstart

Cube is the easiest way to create furniture. You can create it just by single button click. To do that, just follow steps:

* Go to `FreeCAD > Part > Create a cube solid > Cube data (tab)`
* Set `Length` to e.g. 300
* Set `Width` to e.g. 600
* Set `Height` to e.g. 18

	![FPartCube001](https://raw.githubusercontent.com/dprojects/getDimensions/master/Docs/Screenshots/FPartCube001.png)

	**Note**: Now You should have furniture part `300 mm x 600 mm x 18 mm`. You can create any furniture You like using such furniture part, even group them in folders.

* Now, just run the macro, to get report `toPrint`:
	
	![FPartCube002](https://raw.githubusercontent.com/dprojects/getDimensions/master/Docs/Screenshots/FPartCube002.png)

## Pad - quickstart

Pad is not base object. In fact, it is a transformation on the `Sketch` object. However, for the macro purposes it is considered as base element for furniture building, furniture part. Mostly because the `Sketch` is not real-life object, because it has only two dimensions. To start with Pad furniture part, You have to create `Sketch` object first.

* To create `Sketch` compliant with the macro You should use only the drawing object marked with the red border and zoommed below:
	
	![FPartPad001](https://raw.githubusercontent.com/dprojects/getDimensions/master/Docs/Screenshots/FPartPad001.png)

	**Note:** `Sketch` object do not recognize what shape it is and do not keep such information, so if this will be something different than rectangle or square the macro will not be able to get dimensions for the final Pad object. 
	
* You should have `Sketch` like this:

	![FPartPad002](https://raw.githubusercontent.com/dprojects/getDimensions/master/Docs/Screenshots/FPartPad002.png)

	**Note:** This `Sketch` is fully constrained because the right bottom corner is connected with the center of `XY`.

* If You have the `Sketch` created already, just click the `Sketch` object and then the icon bordered in red at the screenshot below. The icon is also zoomed at the image:

	![FPartPad003](https://raw.githubusercontent.com/dprojects/getDimensions/master/Docs/Screenshots/FPartPad003.png)

	**Note**: Now You should have furniture part `300 mm x 600 mm x 18 mm`. You can create any furniture You like using such furniture part, even group them in folders.
	
* Now, just run the macro, to get report `toPrint`:

	![FPartPad004](https://raw.githubusercontent.com/dprojects/getDimensions/master/Docs/Screenshots/FPartPad004.png)

	**Note:** Normally, when You are creating Pad object, the related Sketch object should be in the "Pad folder" (object content). If You do not have such tree structure, please make sure each Pad object has the correct reference in the `Profile` structure. Sketch dimensions are getting from Pad, exactly from `.Profile[0].Shape.OrderedEdges[0].Length` and `.Profile[0].Shape.OrderedEdges[1].Length`. The last dimension is getting from Pad as well, but this time, exactly from `.Length.Value`. So, the key point it that, the values need to be accessible and correct to get it to work.

## Design furniture not the furniture parts

Personally, I used to design everything with `Cube` furniture part. With calculator and `Placement` option I was able to design any furniture I needed, even some tools like doweling jig. Designing simple furniture with `Cube` takes about 5 minutes and You can just use `CTRL-C` and `CTRL-V` keys to multiply quickly the `Cube` furniture part, move it and change some dimensions, if needed.

However, I see the power of `Pad`. The `Pad` furniture part is better supported by FreeCAD. I would say, this is how it should be designed under the FreeCAD. First You should create `Sketch` object, make it fully constrained and use `Pad` option on the fully constrained `Sketch`. It takes more time and effort but You can use more transformations then and such furniture is more compliant with FreeCAD point of view.

However, if You are new FreeCAD user and You want design single furniture, I would **strongly recommend to start with `Cube`**. Your `workbench` to start should be `Part` not `Part Design`. You should not try to design furniture part to design furniture. It is not needed, the best furniture part for furniture designing is already there at `Part` workbench and is named `Cube`. Designing furniture parts should be left for FreeCAD developers or for really advanced projects and designers familiar with FreeCAD. The `Cube` furniture part is more macro friendly, the object shape is known and the dimensions are easy to get, this is the way it should be for furniture design. 

The main problem with `Pad` is that the `Sketch` does not know what shape You drew, so You have to know what You are doing, to use the macro later. If You draw strange shape and `Pad` it later, You will not be able to get the correct dimensions from the final `Pad` object. However, You can always extend Your knowledge, to use transformations supported by FreeCAD for `Pad` only.

## Basic furniture example

* Create `Cube` furniture part using the `Cube` dimensions bordered at the image:

    ![exB001](https://raw.githubusercontent.com/dprojects/getDimensions/master/Docs/Screenshots/exB001.png)
 
* Click the created `Cube` and press `CTRL-C` and `CTRL-V`, to make a copy of the `Cube` furniture part. You should have new `Cube1` created:

    ![exB002](https://raw.githubusercontent.com/dprojects/getDimensions/master/Docs/Screenshots/exB002.png)
    
*  The `Cube1` is at the same place as `Cube`, this is why it is not visible at the 3D model. To move the `Cube1` to the right place, click the `Cube1` at the `Tree` view and change its `Placement` values:
    
    ![exB003](https://raw.githubusercontent.com/dprojects/getDimensions/master/Docs/Screenshots/exB003.png)
    
* You can create any furniture using this method very quickly, rename the folders and objects names:
    
    ![exB004](https://raw.githubusercontent.com/dprojects/getDimensions/master/Docs/Screenshots/exB004.png)

* Now, just run the macro, to get report `toPrint`:
    
    ![exB005](https://raw.githubusercontent.com/dprojects/getDimensions/master/Docs/Screenshots/exB005.png)

# Transformations

For the macro purposes the transformation of a furniture part will be considered as any FreeCAD operation that creates a new object and simplifies the process of furniture design. To use the macro You should use the transformation only for furniture parts, `Cube` and `Pad`. 

Do not use any transformation at `Sketch`, even if the FreeCAD allows for that. It might be good for FreeCAD purposes and the FreeCAD point of view but it is not supported by the macro. The main reason for that is that `Sketch` object do not recognize what shape You drew and do not keep such information. If You draw something different than rectangle or square the macro will not be able to recognize the shape and get the correct dimensions for the final `Pad` object.

**Note:** FreeCAD allows for many objects transformations but some combinations are not supported by FreeCAD e.g.: `PartDesign :: Mirrored :: Cube` or `PartDesign :: MultiTransform :: Cube`. However, this macro support any furniture part for each transformation. 

## Part :: Mirroring :: Cube

* To start with `Part :: Mirroring :: Cube` transformation, You have to create the furniture part for transformation first. In this case this will be `Cube` furniture part:

	![TPartMirroring001](https://raw.githubusercontent.com/dprojects/getDimensions/master/Docs/Screenshots/TPartMirroring001.png)

* Click the `Cube` furniture part and create `Part :: Mirroring :: Cube` transformation as it is demonstrated below:

	![TPartMirroring002](https://raw.githubusercontent.com/dprojects/getDimensions/master/Docs/Screenshots/TPartMirroring002.png)

* You should have `Part :: Mirroring :: Cube` transformation created :

	![TPartMirroring003](https://raw.githubusercontent.com/dprojects/getDimensions/master/Docs/Screenshots/TPartMirroring003.png)

* Now, just run the macro, to get report `toPrint`:
	
	![TPartMirroring004](https://raw.githubusercontent.com/dprojects/getDimensions/master/Docs/Screenshots/TPartMirroring004.png)

## Part :: Mirroring :: Pad

To start with `Part :: Mirroring :: Pad` transformation, You have to create the furniture part for transformation first. In this case this will be `Pad` furniture part. If You already have the `Pad` created, just follow steps: 

* Click the `Pad` furniture part and create `Part :: Mirroring :: Pad` as it is demonstrated below:

	![TPartMirroring005](https://raw.githubusercontent.com/dprojects/getDimensions/master/Docs/Screenshots/TPartMirroring005.png)

* Now, just run the macro, to get report `toPrint`:
	
	![TPartMirroring006](https://raw.githubusercontent.com/dprojects/getDimensions/master/Docs/Screenshots/TPartMirroring006.png)

## Draft :: Array :: Cube

To start with `Draft :: Array :: Cube` transformation, You have to create the furniture part for transformation first. In this case this will be `Cube` furniture part. If You already have the `Cube` created, just follow steps: 

* Click the `Cube` furniture part and create `Draft :: Array :: Cube` as it is demonstrated below:

	![TDraftArray001](https://raw.githubusercontent.com/dprojects/getDimensions/master/Docs/Screenshots/TDraftArray001.png)

* Now, just run the macro, to get report `toPrint`:
	
	![TDraftArray002](https://raw.githubusercontent.com/dprojects/getDimensions/master/Docs/Screenshots/TDraftArray002.png)

## Draft :: Array :: Pad

To start with `Draft :: Array :: Pad` transformation, You have to create the furniture part for transformation first. In this case this will be `Pad` furniture part. If You already have the `Pad` created, just follow steps: 

* Click the `Pad` furniture part and create `Draft :: Array :: Pad` as it is demonstrated below:

	![TDraftArray003](https://raw.githubusercontent.com/dprojects/getDimensions/master/Docs/Screenshots/TDraftArray003.png)

* Now, just run the macro, to get report `toPrint`:
	
	![TDraftArray004](https://raw.githubusercontent.com/dprojects/getDimensions/master/Docs/Screenshots/TDraftArray004.png)
	
* FreeCAD transformations have hidden base elements. Only the final transformed object is visible. Hovewer, it is not the issue, to have the `edge size` calculated as well just e.g. press the `Spacebar` key while on the `Pad` to make it visible and run the macro again:
	
	![TDraftArray005](https://raw.githubusercontent.com/dprojects/getDimensions/master/Docs/Screenshots/TDraftArray005.png)
	
	**Note:** Now You should see the `edge size` is calculated correctly.

## Draft :: Array Polar :: Cube

To start with `Draft :: Array Polar :: Cube` transformation, You have to create the furniture part for transformation first. In this case this will be `Cube` furniture part. If You already have the `Cube` created, just follow steps: 

* Click the `Cube` furniture part and create `Draft :: Array Polar :: Cube` as it is demonstrated below:

	![TDraftArrayPolar001](https://raw.githubusercontent.com/dprojects/getDimensions/master/Docs/Screenshots/TDraftArrayPolar001.png)

* Now, just run the macro, to get report `toPrint`:
	
	![TDraftArrayPolar002](https://raw.githubusercontent.com/dprojects/getDimensions/master/Docs/Screenshots/TDraftArrayPolar002.png)

## Draft :: Array Polar :: Pad

To start with `Draft :: Array Polar :: Pad` transformation, You have to create the furniture part for transformation first. In this case this will be `Pad` furniture part. If You already have the `Pad` created, just follow steps: 

* Click the `Pad` furniture part and create `Draft :: Array Polar :: Pad` as it is demonstrated below:

	![TDraftArrayPolar003](https://raw.githubusercontent.com/dprojects/getDimensions/master/Docs/Screenshots/TDraftArrayPolar003.png)

* Now, just run the macro, to get report `toPrint`:
	
	![TDraftArrayPolar004](https://raw.githubusercontent.com/dprojects/getDimensions/master/Docs/Screenshots/TDraftArrayPolar004.png)

## PartDesign :: Mirrored :: Pad

To start with `PartDesign :: Mirrored :: Pad` transformation, You have to create the furniture part for transformation first. In this case this will be `Pad` furniture part. If You already have the `Pad` created, just follow steps: 

* Click the `Pad` furniture part and create `PartDesign :: Mirrored :: Pad` as it is demonstrated below:

	![TPartDesignMirrored001](https://raw.githubusercontent.com/dprojects/getDimensions/master/Docs/Screenshots/TPartDesignMirrored001.png)

* Now, just run the macro, to get report `toPrint`:
	
	![TPartDesignMirrored002](https://raw.githubusercontent.com/dprojects/getDimensions/master/Docs/Screenshots/TPartDesignMirrored002.png)

## PartDesign :: MultiTransform :: Pad

The `PartDesign :: MultiTransform :: Pad` allows for many transformations at the single step. To start with `PartDesign :: MultiTransform :: Pad` transformation, You have to create the furniture part for transformation first. In this case this will be `Pad` furniture part. If You already have the `Pad` created, just follow steps: 

* Click the `Pad` furniture part and create `PartDesign :: MultiTransform :: Pad` as it is demonstrated below:

	![TPartDesignMultiTransform001](https://raw.githubusercontent.com/dprojects/getDimensions/master/Docs/Screenshots/TPartDesignMultiTransform001.png)

* Now, just run the macro, to get report `toPrint`:
	
	![TPartDesignMultiTransform002](https://raw.githubusercontent.com/dprojects/getDimensions/master/Docs/Screenshots/TPartDesignMultiTransform002.png)

## Advanced furniture example

To use any mirror type of feature part with Your furniture project just follow the steps:

* Create any furniture using Pads and Sketches. You can use `PartDesign :: Mirrored :: Pad` and `PartDesign :: MultiTransform :: Pad` at the same project. For example legs are four, so You can use `PartDesign :: MultiTransform :: Pad` from the single leg and `PartDesign :: Mirrored :: Pad` for each pair of supporters between them:

	![exA001](https://raw.githubusercontent.com/dprojects/getDimensions/master/Docs/Screenshots/exA001.png)
	
* You can also create global furniture dimensions in a separate spreadsheet that gives You the ability to change the global furniture size later:
    
	![exA002](https://raw.githubusercontent.com/dprojects/getDimensions/master/Docs/Screenshots/exA002.png)
        
* Now, just run the macro, to get report `toPrint`:

	![exA003](https://raw.githubusercontent.com/dprojects/getDimensions/master/Docs/Screenshots/exA003.png)
	
	**Note:** If You want to calculate the `edge size` correctly, You have to use the visibility to show e.g. top and hide legs and other parts.

# Report customization

## Visibility

* Search `Toggle Visibility Feature` part in the `Default Settings` section in the macro code.
* Set `sTVF` variable to `on`.
* Now You can create any report You want just by toggle visibility items or group of items.

    ![RVisibility001](https://raw.githubusercontent.com/dprojects/getDimensions/master/Docs/Screenshots/RVisibility001.png)

    ![RVisibility002](https://raw.githubusercontent.com/dprojects/getDimensions/master/Docs/Screenshots/RVisibility002.png)

    **Note:** You can generate different reports at the same furniture project. Just rename the TechDraw page `toPrint` to store it and prevent it from an overwrite or save it as `pdf` file.

## Group furniture parts

* Search `Label Type Feature` part in the `Default Settings` section in the macro code.
* Set `sLTF` variable to the exact value You want.

### Name report

* To create list of names just set `sLTF` variable to `n` and run macro:

    ![RGroup001](https://raw.githubusercontent.com/dprojects/getDimensions/master/Docs/Screenshots/RGroup001.png)

### Quantity report

* To create quantity report just set `sLTF` variable to `q` and run macro:

    ![RGroup002](https://raw.githubusercontent.com/dprojects/getDimensions/master/Docs/Screenshots/RGroup002.png)
    
### Group report

* To create quantity report just set `sLTF` variable to `g` and run macro. However, for group mode, You need to have exact folder tree structure in Your furniture project. The idea behind this is that each element needs to have parent folder and also grandparent folder. For example, an element named `Foot L` needs to be in the parent folder (e.g. named `Foot`). Also the `Foot` folder needs to be in the grandparent folder (e.g. named `White color`). For the `Pad` furniture part, the `Body` object is considered as parent folder. See the screenshot tree:

    ![RGroup003](https://raw.githubusercontent.com/dprojects/getDimensions/master/Docs/Screenshots/RGroup003.png)
    
* Now, just run the macro, to get report `toPrint`:

    ![RGroup004](https://raw.githubusercontent.com/dprojects/getDimensions/master/Docs/Screenshots/RGroup004.png)
    
## Edge size

* Search `Toggle Visibility Feature` part in the `Default Settings` section in the macro code.
* By default the feature `Toggle Visibility Feature` is set to `edge` because in the real world the `edge size` that needs to be covered is very often much smaller. For example You can skip any parts to calculate costs better. To do this, just organize Your project tree with exact visibility, because this feature works for any folder and transformation like `Array`:

    ![REdge001](https://raw.githubusercontent.com/dprojects/getDimensions/master/Docs/Screenshots/REdge001.png)
    
    ![REdge002](https://raw.githubusercontent.com/dprojects/getDimensions/master/Docs/Screenshots/REdge002.png)
    
* Hide parts You do not wish to calculate (e.g. press the `Spacebar` key while on the `Array`) as it is demonstrated below:

    ![REdge003](https://raw.githubusercontent.com/dprojects/getDimensions/master/Docs/Screenshots/REdge003.png)
    
* Now, just run the macro, to get report `toPrint`:
    
    ![REdge004](https://raw.githubusercontent.com/dprojects/getDimensions/master/Docs/Screenshots/REdge004.png)

    **Note:** The `edge size` should be different now.

* If You want to calculate the `edge size` for all furniture parts just set `sTVF` to `off`:
	
	![REdge005](https://raw.githubusercontent.com/dprojects/getDimensions/master/Docs/Screenshots/REdge005.png)

## Constraints - totally custom report

This macro expects from each furniture part to have three dimensions: `Width`,` Height` and `Length`. `Pad` furniture part has only` Length` dimension, this is the `Pad` option value, so macro can be sure for that. Other two dimensions are hidden at `Sketch` object. Unfortunately, if the `Sketch` has something different than rectangle or square, there is no way to determine which one `constraint` is the correct `Width` or ` Height` or maybe it is offset or something else.

If everyone was disciplined enough and they would be naming the `constraints` correctly or FreeCAD would add extra option for that, this would be possible for automatic handlig such thing and calculate area as well. This is why this kind of report is not supported by the macro right now ;-)

However, You can create pretty usefull report with all important `constraints` and the macro will calculate the quantity for You automatically, becuse macro supports all the transformations for custom report of `constraints`, as well.

* To create custom report of `constraints` You have to add `Name` for the `constraint` You want to have listed at report. This is how the macro know which one `constraint` is important to You. All other `constraints` with empty names will be skipped at report:

	![RConstraints001](https://raw.githubusercontent.com/dprojects/getDimensions/master/Docs/Screenshots/RConstraints001.png)
	
* For this type of report You can use any drawing at `Sketch`:

	![RConstraints002](https://raw.githubusercontent.com/dprojects/getDimensions/master/Docs/Screenshots/RConstraints002.png)

* To create `constraints` report just set `sLTF` variable to `c` and run macro:

    ![RConstraints003](https://raw.githubusercontent.com/dprojects/getDimensions/master/Docs/Screenshots/RConstraints003.png)

# Known issues

* **Issue**: Special characters (e.g. Polish) for chipboards (objects names) are not supported. 
	* **Workaround**: You can change the names later manually in the spreadsheet `toCut` and the TechDraw report named `toPrint` will be automatically updated with new names.

* **Issue**: Units at TechDraw page `toPrint` disappear after open project again.
	* **Workaround**: FreeCAD has problem with units generally. The units are still available in the spreadsheet `toCut`. To bring them back to the TechDraw report named `toPrint` You have to run the macro again. To keep them forever just save the TechDraw report named `toPrint` to `pdf` file.

* **Issue**: Long report not fits to the TechDraw page `toPrint`.
	* **Workaround**: FreeCAD not support multipage `pdf` export. Long report can be generated especially for `Constraints` (`sLTF` variable set to `c`) or for objects names listing (`sLTF` variable set to `n`). 
		1. You can change the `sLTF` variable to `q` to sum up all the same dimensions and get the shortest possible report. 
		2. You can use my project created for this purpose here: [sheet2export](https://github.com/dprojects/sheet2export).
		3. Another way is to copy manually data from spreadsheet `toCut`. For example You can export spreadsheet `toCut` to `.csv` file and open `.csv` file under `LibreOffice Writer` and covert it to the table.

# Special thanks

* `Array` feature has been suggested to me at the [FreeCAD forum thread by jaisejames](https://forum.freecadweb.org/viewtopic.php?p=164072#p164072), Thanks.

* `Inches` feature has been suggested to me at the [FreeCAD forum thread by acousticguy](https://forum.freecadweb.org/viewtopic.php?p=286030#p286030), Thanks.

* `Pads` feature has been suggested to me at the [FreeCAD forum thread by Petert](https://forum.freecadweb.org/viewtopic.php?p=547453#p547453), Thanks.

# Feature requests

Best way to ask for new feature is [FreeCAD forum thread](https://forum.freecadweb.org/viewtopic.php?f=22&t=21127). However, You need to be convincing and provide an argument and concrete examples of the use of this functionality in the furniture design process. You have to keep in mind that FreeCAD has a lot of possibilities and not everything has to be implemented. 

___
**Note:** For more details see the [Demo folder](https://github.com/dprojects/getDimensions/tree/master/Demo).
