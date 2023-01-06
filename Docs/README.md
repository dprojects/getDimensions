# Table of Contents

* [Default Settings](#default-settings)
* [Furniture parts](#furniture-parts)
	* [Cube - quickstart](#cube---quickstart)
	* [Pad - quickstart](#pad---quickstart)
	* [Design furniture not the furniture parts](#design-furniture-not-the-furniture-parts)
	* [Basic furniture example](#basic-furniture-example)
* [Report customization](#report-customization)
	* [Report types](#report-types)
		* [q - report type](#q---report-type)
		* [n - report type](#n---report-type)
		* [g - report type](#g---report-type)
		* [e - report type](#e---report-type)
		* [d - report type](#d---report-type)
		* [c - report type](#c---report-type)
		* [p - report type](#p---report-type)
		* [a - report type](#a---report-type)
	* [Additional reports](#additional-reports)
		* [Custom measurements](#custom-measurements)
		* [Dowels and Screws](#dowels-and-screws)
		* [Construction profiles](#construction-profiles)
		* [Decoration](#decoration)
	* [Visibility](#visibility)
		* [Visibility: off](#visibility-off)
		* [Visibility: on](#visibility-on)
		* [Visibility: edge](#visibility-edge)
		* [Visibility: parent](#visibility-parent)
		* [Visibility: inherit](#visibility-inherit)
		* [special BOM attribute](#special-bom-attribute)
	* [Part :: Cut content visibility](#part--cut-content-visibility)
		* [Part :: Cut content visibility: all](#part--cut-content-visibility-all)
		* [Part :: Cut content visibility: base](#part--cut-content-visibility-base)
		* [Part :: Cut content visibility: tool](#part--cut-content-visibility-tool)
	* [Edge size](#edge-size)
	* [Report - export](#report---export)
* [Transformations](#transformations)
	* [Part :: Mirroring](#part--mirroring)
	* [Draft :: Array](#draft--array)
	* [Draft :: Array Polar](#draft--array-polar)
	* [Draft :: Clone](#draft--clone)
	* [PartDesign :: Hole](#partdesign--hole)
	* [PartDesign :: Pocket](#partdesign--pocket)
	* [PartDesign :: LinearPattern](#partdesign--linearpattern)
	* [PartDesign :: Mirrored](#partdesign--mirrored)
	* [PartDesign :: MultiTransform](#partdesign--multitransform)
	* [App :: LinkGroup and App :: Link](#app--linkgroup-and-app--link)
	* [Advanced furniture example](#advanced-furniture-example)
* [Woodworking - usage examples](#woodworking---usage-examples)
	* [Constraints - totally custom report](#constraints---totally-custom-report)
	* [Wood Properties - grain, type, color, etc.](#wood-properties---grain-type-color-etc)
	* [Edgeband](#edgeband)
		* [Edgeband - quick way](#edgeband---quick-way)
		* [Edgeband - described](#edgeband---described)
		* [Edgeband - detailed by selection](#edgeband---detailed-by-selection)
	* [Dowels, pilot holes, countersinks](#dowels-pilot-holes-countersinks)
	* [Custom furniture part](#custom-furniture-part)
	* [32 mm cabinetmaking system](#32-mm-cabinetmaking-system)
* [Known issues](#known-issues)
* [Special thanks](#special-thanks)
* [Feature requests](#feature-requests)

___
# Default Settings

This macro supports `Qt Graphical User Interface (GUI)`, so You can quickly change the settings by scrolling the mouse wheel. This screenshot below represents the `Default Settings`:

![ds001](https://raw.githubusercontent.com/dprojects/getDimensions/master/Docs/Screenshots/ds001.png)

If for some reasons would You like to turn off the `Qt Graphical User Interface (GUI)`, just edit the macro code and set the variable `sQT` to `"no"`. All the `Default Settings` will be set from the variables in the macro code.

**Note:** Some reports screenshots are presented with `Report type` variable set to `n` and `Report quality` set to `eco`, for better readability.

___
# Furniture parts

Furniture parts are base objects for building furniture, base construction element. Each object needs to have three dimensions (`Width`, `Height`, `Length`) to be considered as the furniture part. Also it needs to have rectangular shape (four edges), to calculate area and edge size. You can consider furniture part as wood board, or even better, the rectangular chipboard. 

___
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

___
## Pad - quickstart

Pad is not base object. In fact, it is a transformation on the `Sketch` object. However, for the macro purposes it is considered as base element for furniture building, furniture part. Mostly because the `Sketch` is not real-life object, because it has only two dimensions. To start with Pad furniture part, You have to create `Sketch` object first.

* To create `Sketch` compliant with the macro You should use only the drawing object marked with the red border:
	
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

___
## Design furniture not the furniture parts

Personally, I used to design everything with `Cube` furniture part. With calculator and `Placement` option I was able to design any furniture I needed, even some tools like doweling jig. Designing simple furniture with `Cube` takes about 5 minutes and You can just use `CTRL-C` and `CTRL-V` keys to multiply quickly the `Cube` furniture part, move it and change some dimensions, if needed.

However, I see the power of `Pad`. The `Pad` furniture part is better supported by FreeCAD. I would say, this is how it should be designed under the FreeCAD. First You should create `Sketch` object, make it fully constrained and use `Pad` option on the fully constrained `Sketch`. It takes more time and effort but You can use more transformations then and such furniture is more compliant with FreeCAD point of view.

However, if You are new FreeCAD user and You want design single furniture, I would **strongly recommend to start with `Cube`**. Your `workbench` to start should be `Part` not `Part Design`. You should not try to design furniture part to design furniture. It is not needed, the best furniture part for furniture designing is already there at `Part` workbench and is named `Cube`. Designing furniture parts should be left for FreeCAD developers or for really advanced projects and designers familiar with FreeCAD. The `Cube` furniture part is more macro friendly, the object shape is known and the dimensions are easy to get, this is the way it should be for furniture design. 

The main problem with `Pad` is that the `Sketch` does not know what shape You drew, so You have to know what You are doing, to use the macro later. If You draw strange shape and `Pad` it later, You will not be able to get the correct dimensions from the final `Pad` object. However, You can always extend Your knowledge, to use transformations supported by FreeCAD for `Pad` only.

___
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

___
# Report customization

## Report types

This macro allows You to select the type of report to be displayed. Some types of reports are very complex and can be many pages long for the real-life project. Some types of reports also require special settings in the project. The type of report should be selected according to Your needs and the design of the project. It is best to start with the simplest type of report.

___
### q - report type

This type of report is `default` type of report. It is the shortest one. It can be used for huge projects to make simple short report. Also if You do not need to take care of something like `grain direction`, `detailed edgeband`, `wood type`, `wood color`, this type of report is just for You. Personally, I prefer this type of report the most. Also this type of report has space at the left side, so You can add extra notes later after print.

* To create the quantity report just set `Report type` variable to `q` and run the macro:

    ![ReportTypeQ001](https://raw.githubusercontent.com/dprojects/getDimensions/master/Docs/Screenshots/ReportTypeQ001.png)

___
### n - report type

This type of report is mostly used by me for documentation purposes. It is simple objects listing. However, it can be very useful for project verification. You can list all objects and see if the dimensions are set correctly.

* To create the name report just set `Report type` variable to `n` and run the macro:

    ![ReportTypeN001](https://raw.githubusercontent.com/dprojects/getDimensions/master/Docs/Screenshots/ReportTypeN001.png)

___
### g - report type

This type of report is very useful to divide furniture parts into categories. It can be used for `grain direction`, `detailed edgeband`, `wood type`, `wood color` or for any other category. Also, the `Thickness` column is just after the `Name` column. This is because if You go to cutting chipboards service, first You give `wood color`, second the `thickness`, next `dimensions` and `quantity` at the end. This approach simplifies the more detailed ordering process.

* To create the group report just set `Report type` variable to `g` and run the macro:

    ![ReportTypeG001](https://raw.githubusercontent.com/dprojects/getDimensions/master/Docs/Screenshots/ReportTypeG001.png)

**Note:** For this report type, You need to have exact folder tree structure in Your furniture project. The idea behind this is that each element needs to have parent folder or also grandparent folder. First the grandparent folder is getting and if there is no grandparent folder there will be parent folder name at the report. For the `Pad` furniture part, the `Body` object is considered as parent folder. To add grandparent folder for `Pad` it needs to be in the parent folder (e.g. named `Furniture_pad`) together with its `Body`. 
	
For more details see: [Wood Properties - grain, type, color, etc.](#wood-properties---grain-type-color-etc) section.

___
### e - report type

This type of report is designed for edgeband. Also You can verify if Your 3D model have correctly applied veneer. This type of report recognize automatically if the covered `face` is `surface` or `edge`. Also shows the dimension for `edge` type of face and given `edgeband code`.

* To create the extended edge report just set `Report type` variable to `e` and run the macro:

    ![ReportTypeE001](https://raw.githubusercontent.com/dprojects/getDimensions/master/Docs/Screenshots/ReportTypeE001.png)

**Note:** 

* Each column represents `face` object number at 3D model.
* If Your furniture part `Height` is `Thickness` the `1`, `2`, `3`, `4` will be recognized as `edge`, and `5`, `6` will be `surface`. If Your 3D model is designed differently the columns `5`, `6` may be covered with veneer but this will be recognized as `edge`. 
* Some transformations can have more than 6 faces. To apply veneer correctly for transformation make sure You add `face color` at base object. You have to change the base object visibility first.
* All faces with other color than `object color` will be considered as edgeband. If You want to use the edgeband feature, the best way is to leave the furniture without color and apply only color for faces that need to be covered with veneer. 
* Report for multi-color furniture can be achieved by making two reports for each color (use [Visibility](#visibility) feature to hide each color).
* The edgeband color at 3D model does not matter. `Edgeband code` is only text that will be displayed at report. It can represent any veneer tape color at shop, even reference code. The spreadsheet column width is limited, however at HTML export this can be extended.
* This type of report can exceed a single TechDraw page. To export this type of report, see the [Report - export](#report---export) section.

___
### d - report type

This type of report might be useful for raw wood projects, CNC or very detailed furniture design, because it is designed for very detailed view of edgeband, holes and countersinks. Also it allows for long description based on group name. Regarding edgeband it works like [e - report type](#e---report-type) but has also additional part for holes and countersinks.

* To create the extended edge report just set `Report type` variable to `d` and run the macro:

    ![ReportTypeD001](https://raw.githubusercontent.com/dprojects/getDimensions/master/Docs/Screenshots/ReportTypeD001.png)

**Note:** 

* Each column represents `face` object number at 3D model.
* If Your furniture part `Height` is `Thickness` the `1`, `2`, `3`, `4` will be recognized as `edge`, and `5`, `6` will be `surface`. If Your 3D model is designed differently the columns `5`, `6` may be covered with veneer but this will be recognized as `edge`. 
* Some transformations can have more than 6 faces. To apply veneer correctly for transformation make sure You add `face color` at base object. You have to change the base object visibility first.
* All faces with other color than `object color` will be considered as edgeband. If You want to use the edgeband feature, the best way is to leave the furniture without color and apply only color for faces that need to be covered with veneer.
* Report for multi-color furniture can be achieved by making two reports for each color (use [Visibility](#visibility) feature to hide each color).
* The edgeband color at 3D model does not matter. `Edgeband code` is only text that will be displayed at report. It can represent any veneer tape color at shop, even reference code. The spreadsheet column width is limited, however at HTML export this can be extended.
* The holes and countersinks are taken from `constraints names` of the base object of the group. For example if You make `MultiTransform` You have to set the `constraints names` at the base object.
* If the hole is "through all" there is no `Depth`.
* This type of report can exceed a single TechDraw page. To export this type of report, see the [Report - export](#report---export) section.

___
### c - report type

This type of report is totally custom and it is supported only for `Pad` furniture parts. It can be used as additional report for any other type of report. This type of report can provide such information as: offset, radius, doweling, holes, bar codes, reference numbers, detailed edge banding or any other description You add for dimension (`constraints name`).

* To set `constraint` dimension at the desired object place, You can move the `Sketch XY` by changing the `Position` of `Sketch`:

    ![ReportTypeC001](https://raw.githubusercontent.com/dprojects/getDimensions/master/Docs/Screenshots/ReportTypeC001.png)

* To create the constraints report just set `Report type` variable to `c` and run the macro:

    ![ReportTypeC002](https://raw.githubusercontent.com/dprojects/getDimensions/master/Docs/Screenshots/ReportTypeC002.png)

**Note:**

* Each row represents `constraints name` description and dimension.
* The `Length` dimension is the `Length` dimension for `Sketch > Pad` option.
* This type of report can exceed a single TechDraw page. To export this type of report just see the [Report - export](#report---export) section.

For more details see: [Constraints - totally custom report](#constraints---totally-custom-report) section.

___
### p - report type

This type of report is designed for projects based only on `Pads`. Especially, if You created project with `Pads`, very detailed, but do not have `constraints names`. If You want to get all the non-zero constraints, even those without names, this report is for You. It can be used as additional report for any other type of report, for example if You have also `Cubes` You can generate other report designed for `Cubes`. 

* To create the pads report just set `Report type` variable to `p` and run the macro:

    ![ReportTypeP001](https://raw.githubusercontent.com/dprojects/getDimensions/master/Docs/Screenshots/ReportTypeP001.png)

**Note:**

* Each row represents `constraints name` description and dimension.
* The `Length` dimension is the `Length` dimension for `Sketch > Pad` option.
* This type of report can exceed a single TechDraw page. To export this type of report just see the [Report - export](#report---export) section.
* Zero constraints should be generally avoided, so they are skipped to not overload the report.

___
### a - report type

This report is some kind of approximation of needed material. It uses different approach to dimensions, because the dimensions are not get here from objects, they are calculated from raw vertices. 

You have to be careful because the dimensions are rounded and given in raw form. In fact the dimensions here are not real objects dimensions, they are some kind of occupied space in 3D by the object. You can see the difference for all rotated elements. For rotated elements the occupied space in 3D will not be the same as dimensions. 

However, this approach might be very useful at furniture designing process if You know how it works. Normally, all the `Pad` or `Cube` elements, should be created according to the `XYZ` plane, so You will not see the difference in this case between real dimensions and occupied space in 3D.

It has been inspired by [Dimensions of not-rectangle #8](https://github.com/dprojects/getDimensions/issues/8) issue and can be very useful for irregular shapes, to caclulate needed material. Also, You can use it if You cut wood on Your own and You do not have waste material. This type of report can be directly imported at [cutlistoptimizer.com](https://www.cutlistoptimizer.com/) website tool.

* For sample objects:

	![ReportTypeA001](https://raw.githubusercontent.com/dprojects/getDimensions/master/Docs/Screenshots/ReportTypeA001.png)

* The calculated report looks like this below:

	![ReportTypeA002](https://raw.githubusercontent.com/dprojects/getDimensions/master/Docs/Screenshots/ReportTypeA002.png)

	**Note:** This is because all the objects take the same space in 3D. Also the `Circle` object is not supported because it does not have exact vertices information for calculation `(0, 0, 18)`.

* However, this report can be exported to CSV and directly imported at [cutlistoptimizer.com](https://www.cutlistoptimizer.com/):
	
	![ReportTypeA003](https://raw.githubusercontent.com/dprojects/getDimensions/master/Docs/Screenshots/ReportTypeA003.png)
	
* For normal `Cube` furniture, works without missing parts and with accurate dimensions:

	![ReportTypeA004](https://raw.githubusercontent.com/dprojects/getDimensions/master/Docs/Screenshots/ReportTypeA004.png)

* Directly imported at [cutlistoptimizer.com](https://www.cutlistoptimizer.com/):

	![ReportTypeA005](https://raw.githubusercontent.com/dprojects/getDimensions/master/Docs/Screenshots/ReportTypeA005.png)

* To have added automatically "grain direction" and "custom label" You have to create exact folder structure. Folder label structure should be: `label, grain`. The comma and space is important and it is separator to split label from grain information. For more details see: [Demo009_approximation](https://github.com/dprojects/getDimensions/tree/master/Demo#demo009_approximation).
	
	![ReportTypeA006](https://raw.githubusercontent.com/dprojects/getDimensions/master/Docs/Screenshots/ReportTypeA006.png)
	
## Additional reports

There are also additional reports that can be generated. By default if any of those objects exists at Your project the additional report will be shown with the content. However, You can turn off any additional report type and choose the content You want to see there.

### Custom measurements
**Supported:** `App::MeasureDistance`.
___


* With the `Custom measurements` report You can generate report for measurements objects. The custom measurements can be easily added via [magicMeasure](https://github.com/dprojects/Woodworking/tree/master/Docs#magicmeasure) tool from [Woodworking workbench](https://github.com/dprojects/Woodworking):

	![ARMeasurements001](https://raw.githubusercontent.com/dprojects/getDimensions/master/Docs/Screenshots/ARMeasurements001.png)
	![ARMeasurements002](https://raw.githubusercontent.com/dprojects/getDimensions/master/Docs/Screenshots/ARMeasurements002.png)

___
### Dowels and Screws
**Supported:** `Part::Cylinder`.
___


* With the `Dowels and Screws` report You can generate report for screws, dowels and any other mounting points. It is recommended to use [magicDowels](https://github.com/dprojects/Woodworking/tree/master/Docs#magicdowels) tool from [Woodworking workbench](https://github.com/dprojects/Woodworking), because it takes only a while to add all the visible mounting points:

	![ARMounting001](https://raw.githubusercontent.com/dprojects/getDimensions/master/Docs/Screenshots/ARMounting001.png)
	
* The report for mounting points will be generated below normal report type:
	
	![ARMounting002](https://raw.githubusercontent.com/dprojects/getDimensions/master/Docs/Screenshots/ARMounting002.png)
	
* The header for mounting points is automatically generated by the `magicDowels` tool and the report get first word from object's label:
	
	![ARMounting003](https://raw.githubusercontent.com/dprojects/getDimensions/master/Docs/Screenshots/ARMounting003.png)

___
### Construction profiles
**Supported:** `PartDesign::Thickness`, `Dodo workbench profiles`.
___


* With the `Construction profiles` report You can generate report for construction profiles. Using `PartDesign::Thickness` at 2 faces You can create profile and get information about the elements:

	![ARProfiles001](https://raw.githubusercontent.com/dprojects/getDimensions/master/Docs/Screenshots/ARProfiles001.png)
	![ARProfiles002](https://raw.githubusercontent.com/dprojects/getDimensions/master/Docs/Screenshots/ARProfiles002.png)

* Also You can generate report for `Dodo workbench profiles`:
	
	![ARProfiles003](https://raw.githubusercontent.com/dprojects/getDimensions/master/Docs/Screenshots/ARProfiles003.png)
	![ARProfiles004](https://raw.githubusercontent.com/dprojects/getDimensions/master/Docs/Screenshots/ARProfiles004.png)

___
### Decoration
**Supported:** `PartDesign::Fillet`, `PartDesign::Chamfer`, `Part::Sphere`, `Part::Cone`, `Part::Torus`.
___


* With the `Decoration` report You can generate report for some decoration parts like e.g. drawer handle:

	![ARDecoration001](https://raw.githubusercontent.com/dprojects/getDimensions/master/Docs/Screenshots/ARDecoration001.png)
	![ARDecoration002](https://raw.githubusercontent.com/dprojects/getDimensions/master/Docs/Screenshots/ARDecoration002.png)

___
## Visibility

The `Visibility` option is related to visibility feature functionality. This feature have several options:

### Visibility: off

* By default this feature is set to `off` allowing hidden content to be calculated and listed at the report. This option has been set to default because FreeCAD has many complicated objects with hidden content. For PartDesign objects usually, only the objects of last operation is visible but the first Pad with dimensions is hidden. Similar thing is for Cut objects where the content with dimensions is hidden but the Cut object has no information about dimensions of its parts.

	![RVisibility001](https://raw.githubusercontent.com/dprojects/getDimensions/master/Docs/Screenshots/RVisibility001.png)

### Visibility: on

* This option is mostly dedicated to simple `Cube` objects not `Part :: Cut` hidden behind deeply nested containers. This option turn on the feature basic functionality and You can create report by toggle visibility items or group of items. It can be useful especially for simple costs calculation. You can quickly calculate different types of wood by grouping them inside `Group`, or `LinkGroup` and toggle visibility of `Group` or `LinkGroup`:

	![RVisibility002](https://raw.githubusercontent.com/dprojects/getDimensions/master/Docs/Screenshots/RVisibility002.png)
	![RVisibility003](https://raw.githubusercontent.com/dprojects/getDimensions/master/Docs/Screenshots/RVisibility003.png)

### Visibility: edge

* This option allows to show all hidden objects and groups but not add hidden objects to the edge size. This is useful if You want to calculate edgeband for different types of wood or colors. As You see below, all the objects are listed at the report but the edge size is calculated only for visible HDF element.

	![RVisibility004](https://raw.githubusercontent.com/dprojects/getDimensions/master/Docs/Screenshots/RVisibility004.png)

	**Note:** See the [Edge size](#edge-size) section for more details.

### Visibility: parent

* This option allows to inherit visibility from nearest container. You can hide only part of the sctructure. Even if the content is hidden by the higher container, the content from lower level will be listed if the nearest container is visible. This approach is more closer to those what FreeCAD user see at 3D view, but You need to know that FreeCAD 3D view, Grey object at Tree, and Visibility option not match with each other. 

	![RVisibility005](https://raw.githubusercontent.com/dprojects/getDimensions/master/Docs/Screenshots/RVisibility005.png)
	![RVisibility006](https://raw.githubusercontent.com/dprojects/getDimensions/master/Docs/Screenshots/RVisibility006.png)

* This option can be used for Cut direct elements linking where Link is inside the Cut structure but the Base parametric element is outside the Cut structure. Also all Cubes the Base outside the Cut and Link are invisible. Only the Cut container is visible. In this case you can show all elements, Base or Tool.

	![RVisibility006a](https://raw.githubusercontent.com/dprojects/getDimensions/master/Docs/Screenshots/RVisibility006a.png)
	![RVisibility006b](https://raw.githubusercontent.com/dprojects/getDimensions/master/Docs/Screenshots/RVisibility006b.png)
	![RVisibility006c](https://raw.githubusercontent.com/dprojects/getDimensions/master/Docs/Screenshots/RVisibility006c.png)

### Visibility: inherit

* This is the most advanced option and in my opinion the most powerful and useful for parametric modeling in practice. In this mode the feature inherits the visibility from the highest containers in the structure. If the highest container is hidden the content will not be listed, even if the nearest container and content is visible.
	
	![RVisibility007](https://raw.githubusercontent.com/dprojects/getDimensions/master/Docs/Screenshots/RVisibility007.png)
	
* If the highest container is visible but the lower container is not visible the content will inherit the visibility from the highest container and the content will be listed.

	![RVisibility008](https://raw.githubusercontent.com/dprojects/getDimensions/master/Docs/Screenshots/RVisibility008.png)

* This might be strange but this apparoach allows for visible content linking inside hidden container. So the base objects will be hidden and not calculated and only links will be visible and calculated.

	![RVisibility009](https://raw.githubusercontent.com/dprojects/getDimensions/master/Docs/Screenshots/RVisibility009.png)

* This option should be used with `LinkGroup` as a container not `Group`. This feature not inherit visibility from `Group` container to allow group more complicated parametric structures to be grouped in folder and have clear Tree structure. For example you can put all merged realistic screws in `Group` and link the base middle container. If you hide the highest container from the base screw the base screw will not be calculted and visible but the mounting points will be calculated correctly only using visible links. All structure will be well organized, clean, parametric and correctly calculated at the report.
	
	![RVisibility010](https://raw.githubusercontent.com/dprojects/getDimensions/master/Docs/Screenshots/RVisibility010.png)
	![RVisibility011](https://raw.githubusercontent.com/dprojects/getDimensions/master/Docs/Screenshots/RVisibility011.png)

### special BOM attribute

* If object has `BOM` attribute set to `False` (`App::PropertyBool`) it will be skipped during parsing and not listed at the report. This special attribute is used by [magicCut](https://github.com/dprojects/Woodworking/tree/master/Docs#magiccut) and [magicKnife](https://github.com/dprojects/Woodworking/tree/master/Docs#magicknife) tools to skip copies at the report.

For more details see video tutorial: [Skip copies in cut-list](https://www.youtube.com/watch?v=rFEDLaD8lxM)

___
## Part :: Cut content visibility

This option is related to `Part :: Cut` structures. It allows to choose parsing method for the content of `Part :: Cut`.

### Part :: Cut content visibility: all

* This option allows to show all the `Part :: Cut` structure.

	![RPartCut001](https://raw.githubusercontent.com/dprojects/getDimensions/master/Docs/Screenshots/RPartCut001.png)

* For example this is useful if You use [magicCut](https://github.com/dprojects/Woodworking/tree/master/Docs#magiccut) to create quick Dado joints. This tool creates copies of the objects, so the structure can be listed even if it is hidden. Only the common part is removed so the elements not change places.

	![RPartCut002](https://raw.githubusercontent.com/dprojects/getDimensions/master/Docs/Screenshots/RPartCut002.png)
	![RPartCut003](https://raw.githubusercontent.com/dprojects/getDimensions/master/Docs/Screenshots/RPartCut003.png)

### Part :: Cut content visibility: base

* This option allows to show only `Base` elements from the `Part :: Cut` structure. This is FreeCAD Part Boolean Cut default apparoach, where the `Base` is the object after `Tool` operation.

	![RPartCut004](https://raw.githubusercontent.com/dprojects/getDimensions/master/Docs/Screenshots/RPartCut004.png)

### Part :: Cut content visibility: tool

* This option allows to show only `Tool` elements from the `Part :: Cut` structure.

	![RPartCut005](https://raw.githubusercontent.com/dprojects/getDimensions/master/Docs/Screenshots/RPartCut005.png)

___
## Edge size

The `edge size` depends on `Visibility` option at the [Default Settings](#default-settings):
* If the `Visibility` is set to `off` option then all objects are visible at the report and all edges are calculated.
* If the `Visibility` is set to `edge` option then all objects are visible at the report but only edges of hidden objects are not calculated.
* If the `Visibility` is set to `on` option then all hidden objects are skipped at report and at the `edge size` calculation.

	![REdge001](https://raw.githubusercontent.com/dprojects/getDimensions/master/Docs/Screenshots/REdge001.png)

**Note:** This `edge` option has been implemented at a time when there was no support for Transformations and even Pads. The Transformations hide base object. For example if You create MultiTransform, the base Pad object is hidden by default. If `Visibility` is set to `edge`, You have to make the base Pad object visible to calculate the `edge size` correctly. So, this `edge` option is no longer default. However, this option still can be very useful for quick edgeband approximation.

* In the real world the `edge size` that needs to be covered with veneer is very often much smaller. However, selecting each edge (face of the object) might be too annoying and sometimes pointless if You have elements that will not be covered with veneer entirely. In that case, You can move them all into one directory, hide the entire directory, and set `Visibility` to `edge`:

    ![REdge002](https://raw.githubusercontent.com/dprojects/getDimensions/master/Docs/Screenshots/REdge002.png)
    
	**Note:** The `Cube` furniture part is hidden, so the `edge size` is different now. Also, the edge of the `Pad` furniture part has no veneer applied, so the extended edgeband info is automatically hidden.

___
## Report - export

* You can generate different reports at the same furniture project. Just copy (`CTRL-C` and `CTRL-V`) and rename the spreadsheet `toCut` to store it and prevent it from an overwrite or export the TechDraw page `toPrint` to `pdf` file.

* To export multi-page report or export many spreadsheets at once You can use my project created for this purpose here [sheet2export](https://github.com/dprojects/sheet2export).

___
# Transformations

For the macro purposes the transformation of a furniture part will be considered as any FreeCAD operation that creates a new object and simplifies the process of furniture design. To use the macro You should use the transformation only for supported furniture parts. Each transformation has information about supported objects (tested combinations).

Do not use any transformation at `Sketch`, even if the FreeCAD allows for that. It might be good for FreeCAD purposes and the FreeCAD point of view but it is not supported by the macro for now.

___
## Part :: Mirroring
**Supported:** `Cube`, `Pad`, `Body`, `Clone`.
___

* To start with `Part :: Mirroring` transformation, You have to create the furniture part for transformation first. In this case this will be `Cube` furniture part:

	![TPartMirroring001](https://raw.githubusercontent.com/dprojects/getDimensions/master/Docs/Screenshots/TPartMirroring001.png)

* Click the `Cube` furniture part and create `Part :: Mirroring` transformation as it is demonstrated below:

	![TPartMirroring002](https://raw.githubusercontent.com/dprojects/getDimensions/master/Docs/Screenshots/TPartMirroring002.png)

* You should have `Part :: Mirroring` transformation created :

	![TPartMirroring003](https://raw.githubusercontent.com/dprojects/getDimensions/master/Docs/Screenshots/TPartMirroring003.png)

* Now, just run the macro, to get report `toPrint`:
	
	![TPartMirroring004](https://raw.githubusercontent.com/dprojects/getDimensions/master/Docs/Screenshots/TPartMirroring004.png)

___
## Draft :: Array
**Supported:** `Cube`, `Pad`, `Array on Array`, `Part :: Compound`.
___

To start with `Draft :: Array` transformation, You have to create the furniture part for transformation first. In this case this will be `Pad` furniture part. If You already have the `Pad` created, just follow steps: 

* Click the `Pad` furniture part and create `Draft :: Array` as it is demonstrated below:

	![TDraftArray001](https://raw.githubusercontent.com/dprojects/getDimensions/master/Docs/Screenshots/TDraftArray001.png)

* Now, just run the macro, to get report `toPrint`:
	
	![TDraftArray002](https://raw.githubusercontent.com/dprojects/getDimensions/master/Docs/Screenshots/TDraftArray002.png)
	
* FreeCAD transformations have hidden base elements. Only the final transformed object is visible. However, it is not the issue, to have the `edge size` calculated as well just e.g. press the `spacebar key` while on the `Pad` to make it visible and run the macro again:
	
	![TDraftArray003](https://raw.githubusercontent.com/dprojects/getDimensions/master/Docs/Screenshots/TDraftArray003.png)
	
	**Note:** Now You should see the `edge size` is calculated correctly.

___
## Draft :: Array Polar
**Supported:** `Cube`, `Pad`.
___

To start with `Draft :: Array Polar` transformation, You have to create the furniture part for transformation first. In this case this will be `Pad` furniture part. If You already have the `Pad` created, just follow steps: 

* Click the `Pad` furniture part and create `Draft :: Array Polar` as it is demonstrated below:

	![TDraftArrayPolar001](https://raw.githubusercontent.com/dprojects/getDimensions/master/Docs/Screenshots/TDraftArrayPolar001.png)

* Now, just run the macro, to get report `toPrint`:
	
	![TDraftArrayPolar002](https://raw.githubusercontent.com/dprojects/getDimensions/master/Docs/Screenshots/TDraftArrayPolar002.png)

___
## Draft :: Clone
**Supported:** `Cube`, `Pad`, `Body`.
___

To start with `Draft :: Clone` transformation, You have to create the furniture part for transformation first. In this case this will be `Pad` furniture part. If You already have the `Pad` created, just follow steps: 

* Click the `Pad` furniture part and create `Draft :: Clone` with the cute Dolly sheep icon:

	![TDraftClone001](https://raw.githubusercontent.com/dprojects/getDimensions/master/Docs/Screenshots/TDraftClone001.png)

* You can also change the `Position` of the cloned `Pad`:

	![TDraftClone002](https://raw.githubusercontent.com/dprojects/getDimensions/master/Docs/Screenshots/TDraftClone002.png)

* Now, just run the macro, to get report `toPrint`:

    ![TDraftClone003](https://raw.githubusercontent.com/dprojects/getDimensions/master/Docs/Screenshots/TDraftClone003.png)

___
## PartDesign :: Hole
**Supported:** `Cube`, `Pad`.
___

To start with `PartDesign :: Hole` transformation, You have to create the furniture part for transformation first. In this case this will be `Pad` furniture part. If You already have the `Pad` created, just follow steps: 

* Create `Sketch` at the `Pad` furniture part as it is demonstrated below:

    ![TPDHole001](https://raw.githubusercontent.com/dprojects/getDimensions/master/Docs/Screenshots/TPDHole001.png)

	**Note:** To set correct dimensions from the edge You can change `Sketch` position values to move `XY` to correct place at the `Pad` object, see [c - report type](#c---report-type).

* Click the `Sketch` object and create `PartDesign :: Hole` as it is demonstrated below:

    ![TPDHole002](https://raw.githubusercontent.com/dprojects/getDimensions/master/Docs/Screenshots/TPDHole002.png)

* Click the `Reversed` option if You do not see the hole at the `Pad`:

    ![TPDHole003](https://raw.githubusercontent.com/dprojects/getDimensions/master/Docs/Screenshots/TPDHole003.png)

* Now, just run the macro, to get report `toPrint`:

    ![TPDHole004](https://raw.githubusercontent.com/dprojects/getDimensions/master/Docs/Screenshots/TPDHole004.png)

	**Note:** The `PartDesign :: Hole` is supported only by the [c - report type](#c---report-type).

___
## PartDesign :: Pocket
**Supported:** `Pad`.
___

To start with `PartDesign :: Pocket` transformation, You have to create the furniture part for transformation first. In this case this will be `Pad` furniture part. If You already have the `Pad` created, just follow steps: 

* Create `Sketch` at the `Pad` furniture part as it is demonstrated below and click `Pocket` icon:

    ![TPartDesignPocket001](https://raw.githubusercontent.com/dprojects/getDimensions/master/Docs/Screenshots/TPartDesignPocket001.png)

	**Note:** You can describe constraints to get better [p - report type](#p---report-type) later. However, for [c - report type](#c---report-type) it is needed.

* Now, just run the macro, to get report `toPrint`:

    ![TPartDesignPocket002](https://raw.githubusercontent.com/dprojects/getDimensions/master/Docs/Screenshots/TPartDesignPocket002.png)

	**Note:** The `PartDesign :: Pocket` is supported only by the [c - report type](#c---report-type) and [p - report type](#p---report-type).

___
## PartDesign :: LinearPattern
**Supported:** `Cube`, `Pad`, `Hole`.
___

To start with `PartDesign :: LinearPattern` transformation, You have to create the furniture part for transformation first. In this case this will be `Pad` furniture part. If You already have the `Pad` created, just follow steps: 

* Click the `Pad` furniture part and create `PartDesign :: LinearPattern` as it is demonstrated below:

    ![TPDLinearPattern001](https://raw.githubusercontent.com/dprojects/getDimensions/master/Docs/Screenshots/TPDLinearPattern001.png)

* Now, just run the macro, to get report `toPrint`:

    ![TPDLinearPattern002](https://raw.githubusercontent.com/dprojects/getDimensions/master/Docs/Screenshots/TPDLinearPattern002.png)

* To show the edge size correctly just make the base element `Pad` visible or turn off the [Visibility](#visibility) feature at [Default Settings](#default-settings) GUI:

    ![TPDLinearPattern003](https://raw.githubusercontent.com/dprojects/getDimensions/master/Docs/Screenshots/TPDLinearPattern003.png)

___
## PartDesign :: Mirrored
**Supported:** `Pad`. Not supported by FreeCAD: `Cube`.
___

To start with `PartDesign :: Mirrored` transformation, You have to create the furniture part for transformation first. In this case this will be `Pad` furniture part. If You already have the `Pad` created, just follow steps: 

* Click the `Pad` furniture part and create `PartDesign :: Mirrored` as it is demonstrated below:

	![TPartDesignMirrored001](https://raw.githubusercontent.com/dprojects/getDimensions/master/Docs/Screenshots/TPartDesignMirrored001.png)

* Now, just run the macro, to get report `toPrint`:
	
	![TPartDesignMirrored002](https://raw.githubusercontent.com/dprojects/getDimensions/master/Docs/Screenshots/TPartDesignMirrored002.png)

___
## PartDesign :: MultiTransform
* **Supported objects:** `Pad`, `Hole`. Not supported by FreeCAD: `Cube`, `Body`.
* **Supported transformations:** `Mirror`, `LinearPattern`.
___

The `PartDesign :: MultiTransform` allows for many transformations at the single step. To start with `PartDesign :: MultiTransform` transformation, You have to create the furniture part for transformation first. In this case this will be `Pad` furniture part. If You already have the `Pad` created, just follow steps: 

* Click the `Pad` furniture part and create `PartDesign :: MultiTransform` as it is demonstrated below:

	![TPartDesignMultiTransform001](https://raw.githubusercontent.com/dprojects/getDimensions/master/Docs/Screenshots/TPartDesignMultiTransform001.png)

* Now, just run the macro, to get report `toPrint`:
	
	![TPartDesignMultiTransform002](https://raw.githubusercontent.com/dprojects/getDimensions/master/Docs/Screenshots/TPartDesignMultiTransform002.png)

___
## App :: LinkGroup and App :: Link
* **Supported objects:** `Cube`, `Pad`.
___

This feature has been designed for [fully parametric furniture examples](https://github.com/dprojects/Woodworking/tree/master/Examples), to make more copies of furniture. 

To make more copies You can use [Draft :: Clone](#draft--clone) on the whole `Body` but the problem with that is that [Draft :: Clone](#draft--clone) not keep face color settings. The new cloned furniture will be all blue color. So, You have to set each face color again manually.

To use the `App :: LinkGroup` and `App :: Link` correctly You have to keep such rules:
1. Use `App :: LinkGroup` as folder for base elements only. Do not make more copies with it.
2. If You want more copies use `App :: Link` at `App :: LinkGroup` folder.
3. If You want to move whole new furniture copy, just change position of `App :: Link` or `App :: LinkGroup`.
4. If You want to change color of the furniture or add new element, change the base content, I mean `App :: LinkGroup` content and all linked copies will be updated.

**Note:** The `App :: LinkGroup` is supported only if this is called from `App :: Link`. This is because if You select several `Cubes` and make `App :: LinkGroup` it looks like FreeCAD move them into `App :: LinkGroup` content but in fact, in XML file the unlinked elements still exists additionally. So, if the `App :: LinkGroup` would be calculated from main, all the elements would be calculated twice.

* See the example drawers set how the `Tree` structure is organized. The first bottom element is `App :: LinkGroup` and next two above are just links made with `App :: Link`. If You resize or change the base `App :: LinkGroup` all others will be changed as well. Also the linked copies preserve the face colors:

	![TALink001](https://raw.githubusercontent.com/dprojects/getDimensions/master/Docs/Screenshots/TALink001.png)
	![TALink002](https://raw.githubusercontent.com/dprojects/getDimensions/master/Docs/Screenshots/TALink002.png)

___
## Advanced furniture example

To use any mirror type of feature part with Your furniture project just follow the steps:
	
* Create any furniture using Pads and Sketches. You can use [PartDesign :: Mirrored](#partdesign--mirrored) and [PartDesign :: MultiTransform](#partdesign--multitransform) at the same project. For example legs are four, so You can use [PartDesign :: MultiTransform](#partdesign--multitransform) from the single leg and [PartDesign :: Mirrored](#partdesign--mirrored) for each pair of supporters between them:

	![exA001](https://raw.githubusercontent.com/dprojects/getDimensions/master/Docs/Screenshots/exA001.png)
	
* You can also create global furniture dimensions in a separate spreadsheet that gives You the ability to change the global furniture size later:
    
	![exA002](https://raw.githubusercontent.com/dprojects/getDimensions/master/Docs/Screenshots/exA002.png)
        
* Now, just run the macro, to get report `toPrint`:

	![exA003](https://raw.githubusercontent.com/dprojects/getDimensions/master/Docs/Screenshots/exA003.png)
	
	**Note:** If You want to calculate the `edge size` correctly, You have to use the visibility to show e.g. top and hide legs and other parts.

___
# Woodworking - usage examples

___
## Constraints - totally custom report

This macro expects from each furniture part to have three dimensions: `Width`,` Height` and `Length`. `Pad` furniture part has only` Length` dimension, this is the ` Length` of `Sketch > Pad` option. For this dimension macro can be sure. Other two dimensions are hidden at `Sketch` object. Unfortunately, if the `Sketch` has something different than rectangle or square, there is no way to determine which one `constraint` is the correct `Width` or ` Height` or maybe it is offset or something else.

However, You can create pretty useful report with all important `constraints` and the macro will calculate the quantity for You automatically, because macro supports all the transformations for custom report of `constraints`, as well.

* To create custom report of `constraints` You have to add `Name` for the `constraint` You want to have listed at report. This is how the macro know which one `constraint` is important for You. All other `constraints` with empty names will be skipped at report:

	![RConstraints001](https://raw.githubusercontent.com/dprojects/getDimensions/master/Docs/Screenshots/RConstraints001.png)
	
* For this type of report You can use any drawing at `Sketch`:

	![RConstraints002](https://raw.githubusercontent.com/dprojects/getDimensions/master/Docs/Screenshots/RConstraints002.png)

* To create `constraints` report just set `Report type` variable to `c` and run macro:

    ![RConstraints003](https://raw.githubusercontent.com/dprojects/getDimensions/master/Docs/Screenshots/RConstraints003.png)

___
## Wood Properties - grain, type, color, etc.

FreeCAD not support description for objects. This is not possible to add any note or custom text to the object during furniture design process. You can use `constraints name` at `Sketch` but this is not supported for `Cube` furniture part. Best way to do it is to use currently supported group report (`Report type` variable set to `g`). You can just organize You tree structure and create any report You want.

* For example for `grain direction`:

	![WoodProperties001](https://raw.githubusercontent.com/dprojects/getDimensions/master/Docs/Screenshots/WoodProperties001.png)

* For example for `type of wood`:
	
	![WoodProperties002](https://raw.githubusercontent.com/dprojects/getDimensions/master/Docs/Screenshots/WoodProperties002.png)

* For example for `wood color`:
	
	![WoodProperties003](https://raw.githubusercontent.com/dprojects/getDimensions/master/Docs/Screenshots/WoodProperties003.png)

___
## Edgeband

The edgeband is a very problematic matter. Mainly because the edge You want to cover is up to human's choice. The macro cannot guess the edge to cover. For example, You may want to cover the front part of the shelf, or the back part too, or all the edges. The same for the other furniture parts. To solve this problem, a person has to select and mark the edge (or rather the `face`) to be covered. 

From the other side, during the furniture production process, there are always some leftover veneers for edge banding. But it is always better to have more than less veneer. If You buy a veneer for the entire edge, You can be sure that this veneer is enough for edge banding.

___
### Edgeband - quick way

The quickest way to add edgeband is to use the `Visibility` and `g - report type` (`Report type` variable set to `g`) feature together. You can organize furniture parts in groups and hide the furniture parts without edgeband. All You have to do is to create groups and name them appropriately. This is very quick way and in some cases may be very precised.

* See the screenshot example below:

	![Edgeband001](https://raw.githubusercontent.com/dprojects/getDimensions/master/Docs/Screenshots/Edgeband001.png)

	**Note:** As You see the `Edge size` is `20.4 m` which is very close to the correct value `18.8 m`.

___
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

___
### Edgeband - detailed by selection

* This way use `e - report type`. For this type of report You need to have the veneer applied correctly for each `face` at 3D model that needs to be covered. To apply veneer for `face` use: 
	* `Mouse Right Button` click for object.
	* Choose from submenu `Set colors...`.
	* Select all needed `faces` using pressed `CTRL` keyboard key with `Mouse Left Button` click.

	![Edgeband006](https://raw.githubusercontent.com/dprojects/getDimensions/master/Docs/Screenshots/Edgeband006.png)

* To create the extended edge report just set `Report type` variable to `e` and run the macro:

    ![Edgeband007](https://raw.githubusercontent.com/dprojects/getDimensions/master/Docs/Screenshots/Edgeband007.png)

	**Note:** This feature not working for multi-color furniture. To determine the edgeband color the macro compare the `face` color with `object color`. If You want to generate report for multi-color furniture just organize You furniture parts in folders and use `Visibility` to generate report for each color. 

___
## Dowels, pilot holes, countersinks

* To create dowel You have to create `Pad` so first start with `Sketch` at the furniture part:

	![PDHole001](https://raw.githubusercontent.com/dprojects/getDimensions/master/Docs/Screenshots/PDHole001.png)
	
	**Note:** Make sure You added desired `constraints name`. Only constraints with no empty `constraints name` 
	will be visible at the final report. Not add `constraints name` for those that should be hidden.

* You can use `PartDesign :: MultiTransform` at this dowel using `DatumPlane` to make more copies:

	![PDHole002](https://raw.githubusercontent.com/dprojects/getDimensions/master/Docs/Screenshots/PDHole002.png)

* Also You can add new dowel and do the same:

	![PDHole003](https://raw.githubusercontent.com/dprojects/getDimensions/master/Docs/Screenshots/PDHole003.png)
	![PDHole004](https://raw.githubusercontent.com/dprojects/getDimensions/master/Docs/Screenshots/PDHole004.png)

* To create pilot hole You have to create `Hole` transformation but first start with `Sketch` at the furniture part:

	![PDHole005](https://raw.githubusercontent.com/dprojects/getDimensions/master/Docs/Screenshots/PDHole005.png)
	
	**Note:** Make sure You added desired `constraints name`. Only constraints with no empty `constraints name` 
	will be visible at the final report. Not add `constraints name` for those that should be hidden.

* The same for countersink:

	![PDHole006](https://raw.githubusercontent.com/dprojects/getDimensions/master/Docs/Screenshots/PDHole006.png)

* You can use `PartDesign :: MultiTransform` at the pilot hole and countersink using `DatumPlane` to make more copies:

	![PDHole007](https://raw.githubusercontent.com/dprojects/getDimensions/master/Docs/Screenshots/PDHole007.png)

* The final 3D model should look like this:

	![PDHole008](https://raw.githubusercontent.com/dprojects/getDimensions/master/Docs/Screenshots/PDHole008.png)

* To create `constraints` report just set `Report type` variable to `c` and run macro:

    ![PDHole009](https://raw.githubusercontent.com/dprojects/getDimensions/master/Docs/Screenshots/PDHole009.png)

___
## Custom furniture part

You can use [Draft :: Clone](#draft--clone) and [Part :: Mirroring](#part--mirroring) features to create custom furniture part. To do this You can use the whole `Body` content as custom furniture part. 

* To make more copies of the `Body` object use the `Draft :: Clone`:

	![CustomPart001](https://raw.githubusercontent.com/dprojects/getDimensions/master/Docs/Screenshots/CustomPart001.png)

* To make mirror of all the elements use the `Part :: Mirroring` on all cloned `Body` objects:

	![CustomPart002](https://raw.githubusercontent.com/dprojects/getDimensions/master/Docs/Screenshots/CustomPart002.png)

* As You see the countersinks are at the correct side now:

	![CustomPart003](https://raw.githubusercontent.com/dprojects/getDimensions/master/Docs/Screenshots/CustomPart003.png)
	![CustomPart004](https://raw.githubusercontent.com/dprojects/getDimensions/master/Docs/Screenshots/CustomPart004.png)

* To create `constraints` report just set `Report type` variable to `c` and run macro:

    ![CustomPart005](https://raw.githubusercontent.com/dprojects/getDimensions/master/Docs/Screenshots/CustomPart005.png)

___
## 32 mm cabinetmaking system

To make very quickly many holes for shelf support You can use [PartDesign :: MultiTransform](#partdesign--multitransform) with [PartDesign :: Hole](#partdesign--hole).

* First create `Sketch` for single hole at the `Pad`:
	
	![32System001](https://raw.githubusercontent.com/dprojects/getDimensions/master/Docs/Screenshots/32System001.png)

* Create single hole at the `Pad`:
	
	![32System002](https://raw.githubusercontent.com/dprojects/getDimensions/master/Docs/Screenshots/32System002.png)

* Create `DatumPlane` for `Mirrored`:
	
	![32System003](https://raw.githubusercontent.com/dprojects/getDimensions/master/Docs/Screenshots/32System003.png)

* Now You can use [PartDesign :: MultiTransform](#partdesign--multitransform). First create `Mirrored`:
	
	![32System004](https://raw.githubusercontent.com/dprojects/getDimensions/master/Docs/Screenshots/32System004.png)

* Next create `LinearPattern`:
	
	![32System005](https://raw.githubusercontent.com/dprojects/getDimensions/master/Docs/Screenshots/32System005.png)

* Now, You should have all the holes:
	
	![32System006](https://raw.githubusercontent.com/dprojects/getDimensions/master/Docs/Screenshots/32System006.png)

* To create `constraints` report just set `Report type` variable to `c` and run macro:

	![32System007](https://raw.githubusercontent.com/dprojects/getDimensions/master/Docs/Screenshots/32System007.png)

___
# Known issues

* **Issue**: Special characters (e.g. Polish) for chipboards (objects names) are not supported. 
	* **Workaround**: You can change the names later manually in the spreadsheet `toCut` and the TechDraw report named `toPrint` will be automatically updated with new names.

* **Issue**: Units at TechDraw page `toPrint` disappear after open project again.
	* **Workaround**: FreeCAD has problem with units generally. The units are still available in the spreadsheet `toCut`. To bring them back to the TechDraw report named `toPrint` You have to run the macro again. To keep them forever just save the TechDraw report named `toPrint` to `pdf` file.

* **Issue**: Long report not fits to the TechDraw page `toPrint`.
	* **Workaround**: FreeCAD not support multi-page `pdf` export. Long report can be generated especially for `Constraints` (`Report type` variable set to `c`) or for objects names listing (`Report type` variable set to `n`). 
		1. You can change the `Report type` variable to `q` to sum up all the same dimensions and get the shortest possible report. 
		2. You can use my project created for this purpose here: [sheet2export](https://github.com/dprojects/sheet2export).
		3. Another way is to copy manually data from spreadsheet `toCut`. For example You can export spreadsheet `toCut` to `.csv` file and open `.csv` file under `LibreOffice Writer` and convert it to the table.

* **Issue**: Special characters (comma and whitespace) for `constraints name` are not supported generally. At Ubuntu the validation not works so You can use `constraints name` as `description` (label from FreeCAD point of view) but if You use expressions the expressions will be removed after file reopen ([FreeCAD bug described here](https://forum.freecadweb.org/viewtopic.php?f=10&t=67042)).
	* **Workaround**: There is [workaround](https://github.com/dprojects/getDimensions/commit/6a50fef4a8bbb4729ad8960a79f21b91b5712990), that allow to encode and decode comma and whitespace. To encode `", "` (comma and whitespace) in `constraints name` use `00` (zero twice). To encode `" "` (single whitespace) in `constraints name` use `0` (zero once). So, the encoded `constraints name` e.g. `Bottom00Joint0Size01` will be decoded at report as `Bottom, Joint Size 1`. Underscores way of encoding may not be supported for Windows users at FreeCAD. If You want to use underscores way, You have to test it first on Your own.

___
# Special thanks

* [jaisejames](https://forum.freecadweb.org/viewtopic.php?p=164072#p164072): for the `Array` suggestion.
* [acousticguy](https://forum.freecadweb.org/viewtopic.php?p=286030#p286030): for the `Inches` suggestion.
* [Petert](https://forum.freecadweb.org/viewtopic.php?p=547453#p547453): for the `Pads` suggestion.
* [zohozer](https://forum.freecadweb.org/viewtopic.php?p=560407#p560407): for the `edgeband` suggestion.
* [kisolre](https://forum.freecadweb.org/viewtopic.php?p=565403#p565403): for the `Body Clone` suggestion.

___
# Feature requests

Best way to ask for new feature is [FreeCAD forum thread](https://forum.freecadweb.org/viewtopic.php?f=22&t=21127). 

**Note:** However, You need to be convincing and provide an argument and concrete examples of the use of this functionality in the furniture design process. You have to keep in mind that FreeCAD has a lot of possibilities and not everything has to be implemented. 
___
**Note:** For more details see the [Demo folder](https://github.com/dprojects/getDimensions/tree/master/Demo).
