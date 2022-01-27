# Table of Contents

1. [Default Settings](#default-settings)
2. [Furniture parts](#furniture-parts)
	1. [Cube - quickstart](#cube---quickstart)
	2. [Pad - quickstart](#pad---quickstart)
	3. [Design furniture not the furniture parts](#design-furniture-not-the-furniture-parts)
	4. [Basic furniture example](#basic-furniture-example)
3. [Report customization](#report-customization)
	1. [Report types](#report-types)
		* [q - report type](#q---report-type)
		* [n - report type](#n---report-type)
		* [g - report type](#g---report-type)
		* [e - report type](#e---report-type)
		* [c - report type](#c---report-type)
	2. [Visibility](#visibility)
	3. [Edge size](#edge-size)
	4. [Report - export](#report---export)
4. [Transformations](#transformations)
	1. [Part :: Mirroring](#part--mirroring)
	2. [Draft :: Array :: Cube](#draft--array--cube)
	3. [Draft :: Array :: Pad](#draft--array--pad)
	4. [Draft :: Array Polar :: Cube](#draft--array-polar--cube)
	5. [Draft :: Array Polar :: Pad](#draft--array-polar--pad)
	6. [Draft :: Clone](#draft--clone)
	7. [PartDesign :: Mirrored :: Pad](#partdesign--mirrored--pad)
	8. [PartDesign :: MultiTransform :: Pad](#partdesign--multitransform--pad)
	9. [Advanced furniture example](#advanced-furniture-example)
5. [Woodworking - usage examples](#woodworking---usage-examples)
	1. [Constraints - totally custom report](#constraints---totally-custom-report)
	2. [Wood Properties - grain, type, color, etc.](#wood-properties---grain-type-color-etc)
	3. [Edgeband](#edgeband)
		* [Edgeband - quick way](#edgeband---quick-way)
		* [Edgeband - described](#edgeband---described)
		* [Edgeband - detailed by selection](#edgeband---detailed-by-selection)
	4. [Dowels, pilot holes, countersinks](#dowels-pilot-holes-countersinks)
	5. [Custom furniture part](#custom-furniture-part)
6. [Known issues](#known-issues)
7. [Special thanks](#special-thanks)
8. [Feature requests](#feature-requests)

# Default Settings

This macro supports `Qt Graphical User Interface (GUI)`, so You can quickly change the settings by scrolling the mouse wheel. This screenshot below represents the `Default Settings`:

![ds001](https://raw.githubusercontent.com/dprojects/getDimensions/master/Docs/Screenshots/ds001.png)

If for some reasons would You like to turn off the `Qt Graphical User Interface (GUI)`, just edit the macro code and set the variable `sQT` to `"no"`. All the `Default Settings` will be set from the variables in the macro code.

**Note:** Some reports screenshots are presented with `Report type` variable set to `n` and `Report quality` set to `eco`, for better readability.

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

# Report customization

## Report types

### q - report type

This type of report is `default` type of report. It is the shortest one. It can be used for huge projects to make simple short report. Also if You do not need to take care of something like `grain direction`, `detailed edgeband`, `wood type`, `wood color`, this type of report is just for You. Personally, I prefer this type of report the most. Also this type of report has space at the left side, so You can add extra notes later after print.

* To create the quantity report just set `Report type` variable to `q` and run the macro:

    ![ReportTypeQ001](https://raw.githubusercontent.com/dprojects/getDimensions/master/Docs/Screenshots/ReportTypeQ001.png)

### n - report type

This type of report is mostly used by me for documentation purposes. It is simple objects listing. However, it can be very useful for project veryfication. You can list all objects and see if the dimensions are set correctly.

* To create the name report just set `Report type` variable to `n` and run the macro:

    ![ReportTypeN001](https://raw.githubusercontent.com/dprojects/getDimensions/master/Docs/Screenshots/ReportTypeN001.png)

### g - report type

This type of report is very useful to divide furniture parts into categories. It can be used for `grain direction`, `detailed edgeband`, `wood type`, `wood color` or for any other category. Also, the `Thickness` column is just after the `Name` column. This is because if You go to cutting chipboards service, first You give `wood color`, second the `thickness`, next `dimensions` and `quantity` at the end. This aproach simplifies the more detailed ordering process.

* To create the group report just set `Report type` variable to `g` and run the macro:

    ![ReportTypeG001](https://raw.githubusercontent.com/dprojects/getDimensions/master/Docs/Screenshots/ReportTypeG001.png)

**Note:** For this report type, You need to have exact folder tree structure in Your furniture project. The idea behind this is that each element needs to have parent folder or also grandparent folder. First the grandparent folder is getting and if there is no grandparent folder there will be parent folder name at the report. For the `Pad` furniture part, the `Body` object is considered as parent folder. To add grandparent folder for `Pad` it needs to be in the parent folder (e.g. named `Furniture_pad`) together with its `Body`. 
	
For more details see: [Wood Properties - grain, type, color, etc.](#wood-properties---grain-type-color-etc) section.

### e - report type

This type of report is designed for more advanced edge report. It is mostly used for edgeband. Also You can verify if Your 3D model have correctly applied veneer. This type of report recognize automatically if the covered `face` is `surface` or `edge` type. Also shows the dimension for `edge` type of face and given veneer description.

* To create the extended edge report just set `Report type` variable to `e` and run the macro:

    ![ReportTypeE001](https://raw.githubusercontent.com/dprojects/getDimensions/master/Docs/Screenshots/ReportTypeE001.png)

**Note:** 

* Each column represents `face` object number at 3D model.
* If Your furniture part `Height` is `Thickness` the `1`, `2`, `3`, `4` will be `edges`, and `5`, `6` will be `surfaces`. If Your 3D model is designed differently the columns `5`, `6` may be covered with veneer but this will be recognized as `edge` type. 
* Some transformations can have more than 6 faces. To apply veneer correctly for transformation make sure You add `face color` at base object only. You have to change the base object visibility first.
* This type of report can exceed a single TechDraw page. To export this type of report just see the [Report - export](#report---export) section.

### c - report type

This type of report is totally custom and it is supported only for `Pad` furniture parts. It can be used as additional report for any other type of report. This type of report can provide such information as: offset, radius, doweling, holes, bar codes, reference numbers, detailed edge banding or any other description You add for dimension (`constraints name`).

* To create the constraints report just set `Report type` variable to `c` and run the macro:

    ![ReportTypeC001](https://raw.githubusercontent.com/dprojects/getDimensions/master/Docs/Screenshots/ReportTypeC001.png)

**Note:**

* Eeach row represents `constraints name` description. 
* The `Length` dimension is the `Length` dimension for `Sketch > Pad` option.
* This type of report can exceed a single TechDraw page. To export this type of report just see the [Report - export](#report---export) section.

For more details see: [Constraints - totally custom report](#constraints---totally-custom-report) section.

## Visibility

* Search `Visibility` part in the `Default Settings` and set to `on`.
* Now You can create any report You want just by toggle visibility items or group of items.

    ![RVisibility001](https://raw.githubusercontent.com/dprojects/getDimensions/master/Docs/Screenshots/RVisibility001.png)

    ![RVisibility002](https://raw.githubusercontent.com/dprojects/getDimensions/master/Docs/Screenshots/RVisibility002.png)

## Edge size

* Search `Visibility` part in the `Default Settings`.
* By default the feature `Visibility` is set to `edge` because in the real world the `edge size` that needs to be covered is very often much smaller. For example You can skip any parts to calculate costs better. To do this, just organize Your project tree with exact visibility:

    ![REdge001](https://raw.githubusercontent.com/dprojects/getDimensions/master/Docs/Screenshots/REdge001.png)
    
* Hide parts You do not wish to calculate:

    ![REdge002](https://raw.githubusercontent.com/dprojects/getDimensions/master/Docs/Screenshots/REdge002.png)
    
**Note:** The `Cube` furniture part is hidden, so the `edge size` is different now. Also, the edge of the `Pad` furniture part has no veneer applied, so the extended edgeband info is automatically hidden.
    
## Report - export

* You can generate different reports at the same furniture project. Just copy (`CTRL-C` and `CTRL-V`) and rename the spreadsheet `toCut` to store it and prevent it from an overwrite or export the TechDraw page `toPrint` to `pdf` file.

* To export multi-page report or export many spreadsheets at once You can use my project created for this purpose here [sheet2export](https://github.com/dprojects/sheet2export).

# Transformations

For the macro purposes the transformation of a furniture part will be considered as any FreeCAD operation that creates a new object and simplifies the process of furniture design. To use the macro You should use the transformation only for furniture parts, `Cube` and `Pad`. 

Do not use any transformation at `Sketch`, even if the FreeCAD allows for that. It might be good for FreeCAD purposes and the FreeCAD point of view but it is not supported by the macro. The main reason for that is that `Sketch` object do not recognize what shape You drew and do not keep such information. If You draw something different than rectangle or square the macro will not be able to recognize the shape and get the correct dimensions for the final `Pad` object.

**Note:** FreeCAD allows for many objects transformations but some combinations are not supported by FreeCAD e.g.: `PartDesign :: Mirrored :: Cube` or `PartDesign :: MultiTransform :: Cube`. However, this macro support any furniture part for each transformation. 

## Part :: Mirroring

* To start with `Part :: Mirroring` transformation, You have to create the furniture part for transformation first. In this case this will be `Cube` furniture part:

	![TPartMirroring001](https://raw.githubusercontent.com/dprojects/getDimensions/master/Docs/Screenshots/TPartMirroring001.png)

* Click the `Cube` furniture part and create `Part :: Mirroring` transformation as it is demonstrated below:

	![TPartMirroring002](https://raw.githubusercontent.com/dprojects/getDimensions/master/Docs/Screenshots/TPartMirroring002.png)

* You should have `Part :: Mirroring` transformation created :

	![TPartMirroring003](https://raw.githubusercontent.com/dprojects/getDimensions/master/Docs/Screenshots/TPartMirroring003.png)

* Now, just run the macro, to get report `toPrint`:
	
	![TPartMirroring004](https://raw.githubusercontent.com/dprojects/getDimensions/master/Docs/Screenshots/TPartMirroring004.png)
	
	**Note:** You can do the same for `Cube`, `Body` or any other object supported by the macro.

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

## Draft :: Clone

To start with `Draft :: Clone` transformation, You have to create the furniture part for transformation first. In this case this will be `Pad` furniture part. If You already have the `Pad` created, just follow steps: 

* Click the `Pad` furniture part and create `Draft :: Clone` with the cute dolly sheep icon:

	![TDraftClone001](https://raw.githubusercontent.com/dprojects/getDimensions/master/Docs/Screenshots/TDraftClone001.png)

* You can also change the `Position` of the cloned `Pad`:

	![TDraftClone002](https://raw.githubusercontent.com/dprojects/getDimensions/master/Docs/Screenshots/TDraftClone002.png)

* Now, just run the macro, to get report `toPrint`:

    ![TDraftClone003](https://raw.githubusercontent.com/dprojects/getDimensions/master/Docs/Screenshots/TDraftClone003.png)

	**Note:** You can do the same for `Cube`, `Body` or any other object supported by the macro.

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

# Woodworking - usage examples

## Constraints - totally custom report

This macro expects from each furniture part to have three dimensions: `Width`,` Height` and `Length`. `Pad` furniture part has only` Length` dimension, this is the ` Length` of `Sketch > Pad` option. For this dimension macro can be sure. Other two dimensions are hidden at `Sketch` object. Unfortunately, if the `Sketch` has something different than rectangle or square, there is no way to determine which one `constraint` is the correct `Width` or ` Height` or maybe it is offset or something else.

However, You can create pretty useful report with all important `constraints` and the macro will calculate the quantity for You automatically, becuse macro supports all the transformations for custom report of `constraints`, as well.

* To create custom report of `constraints` You have to add `Name` for the `constraint` You want to have listed at report. This is how the macro know which one `constraint` is important for You. All other `constraints` with empty names will be skipped at report:

	![RConstraints001](https://raw.githubusercontent.com/dprojects/getDimensions/master/Docs/Screenshots/RConstraints001.png)
	
* For this type of report You can use any drawing at `Sketch`:

	![RConstraints002](https://raw.githubusercontent.com/dprojects/getDimensions/master/Docs/Screenshots/RConstraints002.png)

* To create `constraints` report just set `Report type` variable to `c` and run macro:

    ![RConstraints003](https://raw.githubusercontent.com/dprojects/getDimensions/master/Docs/Screenshots/RConstraints003.png)

## Wood Properties - grain, type, color, etc.

FreeCAD not support description for objects. This is not possible to add any note or custom text to the object during furniture design process. You can use `constraints name` at `Sketch` but this is not supported for `Cube` furniture part. Best way to do it is to use currently supported group report (`Report type` variable set to `g`). You can just organize You tree structure and create any report You want.

* For example for `grain direction`:

	![WoodProperties001](https://raw.githubusercontent.com/dprojects/getDimensions/master/Docs/Screenshots/WoodProperties001.png)

* For example for `type of wood`:
	
	![WoodProperties002](https://raw.githubusercontent.com/dprojects/getDimensions/master/Docs/Screenshots/WoodProperties002.png)

* For example for `wood color`:
	
	![WoodProperties003](https://raw.githubusercontent.com/dprojects/getDimensions/master/Docs/Screenshots/WoodProperties003.png)

## Edgeband

The edgeband is a very problematic matter. Mainly because the edge You want to cover is up to human's choice. The macro cannot guess the edge to cover. For example, You may want to cover the front part of the shelf, or the back part too, or all the edges. The same for the other furniture parts. To solve this problem, a person has to select and mark the edge (or rather the `face`) to be covered. 

From the other side, during the furniture production process, there are always some leftover veneers for edge banding. But it is always better to have more than less veneer. If You buy a veneer for the entire edge, You can be sure that this veneer is enough for edge banding.

### Edgeband - quick way

The quickest way to add edgeband is to use the `Visibility` and `g - report type` (`Report type` variable set to `g`) feature together. You can organize furniture parts in groups and hide the furniture parts without edgeband. All You have to do is to create groups and name them appropriately. This is very quick way and in some cases may be very precised.

* See the screenshot example below:

	![Edgeband001](https://raw.githubusercontent.com/dprojects/getDimensions/master/Docs/Screenshots/Edgeband001.png)

	**Note:** As You see the `Edge size` is `20.4 m` which is very close to the correct value `18.8 m`.

### Edgeband - described

If You want more detailed report about the edgeband You should consider [Constraints - totally custom report](#constraints---totally-custom-report). This type of report not support the `Edge size` but it can be a good addition to any other type of report.

* For example for this top of the table You may want to cover all edges except this one from the side of the wall:
	
	![Edgeband002](https://raw.githubusercontent.com/dprojects/getDimensions/master/Docs/Screenshots/Edgeband002.png)

* To do this, this must be `Pad` furniture part and You have to edit the `Sketch` to have constraints for each edge, to be able to describe each edgeband precisely:
	
	![Edgeband003](https://raw.githubusercontent.com/dprojects/getDimensions/master/Docs/Screenshots/Edgeband003.png)

* To avoid the error reported by FreeCAD, check the `Reference` option:

	![Edgeband004](https://raw.githubusercontent.com/dprojects/getDimensions/master/Docs/Screenshots/Edgeband004.png)
	
* To create `constraints` report just set `Report type` variable to `c` and run macro:
	
	![Edgeband005](https://raw.githubusercontent.com/dprojects/getDimensions/master/Docs/Screenshots/Edgeband005.png)

### Edgeband - detailed by selection

* This way use `e - report type`. For this type of report You need to have the veneer applied correctly for each `face` at 3D model that needs to be covered. Also You have to provide Your furniture color for edgeband color comparision. To apply veneer for `face` use: 
	* `Mouse Right Button` click for object.
	* Choose from submenu `Set colors...`.
	* Select all needed `faces` using pressed `CTRL` keyboard key with `Mouse Left Button` click.

	![Edgeband006](https://raw.githubusercontent.com/dprojects/getDimensions/master/Docs/Screenshots/Edgeband006.png)

* To create the extended edge report just set `Report type` variable to `e` and run the macro:

    ![Edgeband007](https://raw.githubusercontent.com/dprojects/getDimensions/master/Docs/Screenshots/Edgeband007.png)

	**Note:** This feature not working for multi-color furniture. To determine the edgeband color the macro compare the `face` color with given `furniture color`. If You want to generate report for multi-color furniture just organize You furniture parts in folders and use `Visibility` to generate report for each color. 

## Dowels, pilot holes, countersinks

* To create dowel You have to create `Pad` so first start with `Sketch` at the furniture part:

	![PDHole001](https://raw.githubusercontent.com/dprojects/getDimensions/master/Docs/Screenshots/PDHole001.png)
	
	**Note:** Make sure You added desired `constraints name`. Only constraints with no empty `constraints name` 
	will be visisble at the final report. Not add `constraints name` for those that should be hidden.

* You can use `PartDesign :: MultiTransform` at this dowel using `DatumPlane` to make more copies:

	![PDHole002](https://raw.githubusercontent.com/dprojects/getDimensions/master/Docs/Screenshots/PDHole002.png)

* Also You can add new dowel and do the same:

	![PDHole003](https://raw.githubusercontent.com/dprojects/getDimensions/master/Docs/Screenshots/PDHole003.png)
	![PDHole004](https://raw.githubusercontent.com/dprojects/getDimensions/master/Docs/Screenshots/PDHole004.png)

* To create pilot hole You have to create `Hole` transformation but first start with `Sketch` at the furniture part:

	![PDHole005](https://raw.githubusercontent.com/dprojects/getDimensions/master/Docs/Screenshots/PDHole005.png)
	
	**Note:** Make sure You added desired `constraints name`. Only constraints with no empty `constraints name` 
	will be visisble at the final report. Not add `constraints name` for those that should be hidden.

* The same for countersink:

	![PDHole006](https://raw.githubusercontent.com/dprojects/getDimensions/master/Docs/Screenshots/PDHole006.png)

* You can use `PartDesign :: MultiTransform` at the pilot hole and countersink using `DatumPlane` to make more copies:

	![PDHole007](https://raw.githubusercontent.com/dprojects/getDimensions/master/Docs/Screenshots/PDHole007.png)

* The final 3D model should look like this:

	![PDHole008](https://raw.githubusercontent.com/dprojects/getDimensions/master/Docs/Screenshots/PDHole008.png)

* To create `constraints` report just set `Report type` variable to `c` and run macro:

    ![PDHole009](https://raw.githubusercontent.com/dprojects/getDimensions/master/Docs/Screenshots/PDHole009.png)

## Custom furniture part

You can use [Draft :: Clone](#draft--clone) and [Part :: Mirroring](#part--mirroring) features to create custom furniture part. To do this You can use the whole `Body` content as custom furniture part. 

* To make more copis of the `Body` object use the `Draft :: Clone`:

	![CustomPart001](https://raw.githubusercontent.com/dprojects/getDimensions/master/Docs/Screenshots/CustomPart001.png)

* To make mirror of all the elements use the `Part :: Mirroring` on all cloned `Body` objects:

	![CustomPart002](https://raw.githubusercontent.com/dprojects/getDimensions/master/Docs/Screenshots/CustomPart002.png)

* As You see the countersinks are at the correct side now:

	![CustomPart003](https://raw.githubusercontent.com/dprojects/getDimensions/master/Docs/Screenshots/CustomPart003.png)
	![CustomPart004](https://raw.githubusercontent.com/dprojects/getDimensions/master/Docs/Screenshots/CustomPart004.png)

* To create `constraints` report just set `Report type` variable to `c` and run macro:

    ![CustomPart005](https://raw.githubusercontent.com/dprojects/getDimensions/master/Docs/Screenshots/CustomPart005.png)

# Known issues

* **Issue**: Special characters (e.g. Polish) for chipboards (objects names) are not supported. 
	* **Workaround**: You can change the names later manually in the spreadsheet `toCut` and the TechDraw report named `toPrint` will be automatically updated with new names.

* **Issue**: Units at TechDraw page `toPrint` disappear after open project again.
	* **Workaround**: FreeCAD has problem with units generally. The units are still available in the spreadsheet `toCut`. To bring them back to the TechDraw report named `toPrint` You have to run the macro again. To keep them forever just save the TechDraw report named `toPrint` to `pdf` file.

* **Issue**: Long report not fits to the TechDraw page `toPrint`.
	* **Workaround**: FreeCAD not support multipage `pdf` export. Long report can be generated especially for `Constraints` (`Report type` variable set to `c`) or for objects names listing (`Report type` variable set to `n`). 
		1. You can change the `Report type` variable to `q` to sum up all the same dimensions and get the shortest possible report. 
		2. You can use my project created for this purpose here: [sheet2export](https://github.com/dprojects/sheet2export).
		3. Another way is to copy manually data from spreadsheet `toCut`. For example You can export spreadsheet `toCut` to `.csv` file and open `.csv` file under `LibreOffice Writer` and covert it to the table.

# Special thanks

* Very important thing like `Grain Direction` has been reminded to me at the [FreeCAD forum thread by zohozer](https://forum.freecadweb.org/viewtopic.php?p=560407#p560407), This was already supported but `Grain Direction` had to be more clearly decribed at the documentation, Thanks.

* `Array` feature has been suggested to me at the [FreeCAD forum thread by jaisejames](https://forum.freecadweb.org/viewtopic.php?p=164072#p164072), Thanks.

* `Inches` feature has been suggested to me at the [FreeCAD forum thread by acousticguy](https://forum.freecadweb.org/viewtopic.php?p=286030#p286030), Thanks.

* `Pads` feature has been suggested to me at the [FreeCAD forum thread by Petert](https://forum.freecadweb.org/viewtopic.php?p=547453#p547453), Thanks.

# Feature requests

Best way to ask for new feature is [FreeCAD forum thread](https://forum.freecadweb.org/viewtopic.php?f=22&t=21127). However, You need to be convincing and provide an argument and concrete examples of the use of this functionality in the furniture design process. You have to keep in mind that FreeCAD has a lot of possibilities and not everything has to be implemented. 

___
**Note:** For more details see the [Demo folder](https://github.com/dprojects/getDimensions/tree/master/Demo).
