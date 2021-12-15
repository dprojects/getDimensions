# -*- coding: utf-8 -*-

# FreeCAD macro for woodworking
# Author: Darek L (aka dprojects)
# Version: 2021.12.15
# Latest version: https://github.com/dprojects/getDimensions

import FreeCAD, Draft, Spreadsheet


# ###################################################################################################################
# SETTINGS ( SET HERE )
# ###################################################################################################################


# set language:
# "pl" - Polish
# "en" - English
sLang = "en"

# set metric system for all elements:
# "mm" - millimeter
# "m" - meter
# "in" - inch
sUnitsMetric = "mm"

# set square area units:
# "m"  - meter
# "mm" - millimeter
# "in" - inch
sUnitsArea = "m"

# Toggle Visibility Feature:
# "on" - all hidden items with visibility = false will be skipped
# "edge" - hidden elements will not be added to edge size only
# "off" - all items will be listed and calculated
sTVF = "edge"

# Label Type Feature:
# "n" - show name of the element first for each group
# "q" - show quantity first for each group
# "g" - show group name first for each group (grandparent or parent folder)
sLTF = "n"


# ###################################################################################################################
# Autoconfig - define globals ( NOT CHANGE HERE )
# ###################################################################################################################

# set reference point to Active Document
gAD = FreeCAD.activeDocument()

# get all objects from 3D model
gOBs = gAD.Objects

# fake Cube database for objects and dimensions
gFakeCubeO = []
gFakeCubeW = dict()
gFakeCubeH = dict()
gFakeCubeL = dict()

# init database for sizes (quantity) report
if sLTF == "q":
	gSizesQ = dict() # quantity
	gSizesA = dict() # area

# init database for name report
if sLTF == "n":
	gNameQ = dict() # quantity
	gNameA = dict() # area

# init database for group report
if sLTF == "g":
	gGroupQ = dict() # quantity
	gGroupA = dict() # area

# init database for thickness report
gThickQ = dict() # quantity
gThickA = dict() # area

# init database for edge report
gEdgeSize = 0 # edge size

# unit for calculation purposes
gUnitC = "mm"


# ###################################################################################################################
# Support for dimensions calculations
# ###################################################################################################################


# ###################################################################################################################
def getParentGroup(iLabel):
	for iGroup in gAD.Objects:
		if iGroup.isDerivedFrom("App::DocumentObjectGroup"):
			for iChild in iGroup.Group:
				if iChild.Label == iLabel:
					return iGroup
	return ""


# ###################################################################################################################
def getKey(iObj, iW, iH, iL, iType):

	# set array with values
	vKeyArr = [ iW, iH, iL ]

	# sort as values to have thickness first
	vKeyArr.sort()

	# create key string with thickness first
	vKey = ""
	vKey += str(vKeyArr[0])
	vKey += ":"
	vKey += str(vKeyArr[1])
	vKey += ":"
	vKey += str(vKeyArr[2])

	# key for sizes database
	if iType == "size":
		return str(vKey)

	# key for name database
	elif iType == "name":
		vKey = str(vKey) + ":" + str(iObj.Label)
		return str(vKey)

	# key for thickness database (this is value, not string)
	elif iType == "thick":
		return vKeyArr[0]

	# key for group database
	elif iType == "group":	
		
		# get parent folder (group name)
		vParent = getParentGroup(iObj.Label)
		
		if vParent != "":
			vPL = vParent.Label
			
			# get grandparent folder
			vGrand = getParentGroup(vPL)

			if vGrand != "":
				vKey = str(vKey) + ":" + str(vGrand.Label)
			else:
				vKey = str(vKey) + ":" + str(vPL)
		else:
			vKey = str(vKey) + ":[...]"

	return str(vKey)


# ###################################################################################################################
def getArea(iObj, iW, iH, iL):

	# make sure to not calculate thickness
	vT = getKey(iObj, iW, iH, iL, "thick")

	if iL == vT:
		vSize1 = iW
		vSize2 = iH
	
	elif iW == vT:
		vSize1 = iL
		vSize2 = iH
	
	else:
		vSize1 = iL
		vSize2 = iW

	# calculate area without thickness
	vArea = vSize1 * vSize2

	return vArea


# ###################################################################################################################
def setDB(iObj, iW, iH, iL, iDB):

	# get area for object
	vArea = getArea(iObj, iW, iH, iL) 
	
	# set DB for name of element database
	if iDB == "name":

		vKey = getKey(iObj, iW, iH, iL, "name")

		if vKey in gNameQ:
			gNameQ[vKey] = gNameQ[vKey] + 1
			gNameA[vKey] = gNameA[vKey] + vArea
		else:
			gNameQ[vKey] = 1
			gNameA[vKey] = vArea

	# set DB for sizes (quantity) database
	elif iDB == "size":

		vKey = getKey(iObj, iW, iH, iL, "size")

		if vKey in gSizesQ:
			gSizesQ[vKey] = gSizesQ[vKey] + 1
			gSizesA[vKey] = gSizesA[vKey] + vArea
		else:
			gSizesQ[vKey] = 1
			gSizesA[vKey] = vArea

	# set DB for group database
	elif iDB == "group":

		vKey = getKey(iObj, iW, iH, iL, "group")

		if vKey in gGroupQ:
			gGroupQ[vKey] = gGroupQ[vKey] + 1
			gGroupA[vKey] = gGroupA[vKey] + vArea
		else:
			gGroupQ[vKey] = 1
			gGroupA[vKey] = vArea
	
	# set DB for thickness database
	elif iDB == "thick":

		# convert value to dimension string
		vKey = str(getKey(iObj, iW, iH, iL, "thick"))
	
		if vKey in gThickQ:
			gThickQ[vKey] = gThickQ[vKey] + 1
			gThickA[vKey] = gThickA[vKey] + vArea
		else:
			gThickQ[vKey] = 1
			gThickA[vKey] = vArea


# ###################################################################################################################
def getEdge(iObj, iW, iH, iL):

	# skip the thickness dimension
	vT = getKey(iObj, iW, iH, iL, "thick")

	if iL == vT:
		vSize1 = iW
		vSize2 = iH

	elif iW == vT:
		vSize1 = iL
		vSize2 = iH

	else:
		vSize1 = iL
		vSize2 = iW

	# calculate the edge size
	vEdge = (2 * vSize1) + (2 * vSize2)

	return vEdge


# ###################################################################################################################
def getUnit(iValue, iType):

	iValue = float(iValue)

	if iType == "size":
		
		if sUnitsMetric == "mm":
			return "'" + str( int(round(iValue, 0)) ) + " " + sUnitsMetric
		
		if sUnitsMetric == "m":
			return "'" + str( round(iValue * float(0.001), 3) ) + " " + sUnitsMetric
		
		if sUnitsMetric == "in":
			return "'" + str( round(iValue * float(0.0393700787), 3) ) + " " + sUnitsMetric
		
	if iType == "area":
		
		if sUnitsArea == "mm":
			return "'" + str( int(round(iValue, 0)) )
		
		if sUnitsArea == "m":
			return "'" + str( round(iValue * float(0.000001), 6) )
		
		if sUnitsArea == "in":
			return "'" + str( round(iValue * float(0.0015500031), 6) )
		
	return -1


# ###################################################################################################################
# Support for base objects types
# ###################################################################################################################


# ###################################################################################################################
def setCube(iObj):

	# support for Cube objects
	if iObj.isDerivedFrom("Part::Box"):
        
		gFakeCubeO.append(iObj)
		gFakeCubeW[iObj.Label] = iObj.Width.getValueAs(gUnitC).Value
		gFakeCubeH[iObj.Label] = iObj.Height.getValueAs(gUnitC).Value
		gFakeCubeL[iObj.Label] = iObj.Length.getValueAs(gUnitC).Value
	
	return 0


# ###################################################################################################################
def setPad(iObj):

	# support for Pads and Sketches
	if iObj.isDerivedFrom("PartDesign::Pad"):

		try:

			# remove existing fakeCube object
			if gAD.getObject("fakeCube"):
				gAD.removeObject("fakeCube")

			# create fake Cube 
			fakeCube = gAD.addObject("Part::Box", "fakeCube")

			# assign values to the fake Cube dimensions
			fakeCube.Width = iObj.Profile[0].Shape.OrderedEdges[0].Length
			fakeCube.Height = iObj.Profile[0].Shape.OrderedEdges[1].Length
			fakeCube.Length = iObj.Length.Value
			
			# get values as the correct dimensions and set database
			gFakeCubeO.append(iObj)
			gFakeCubeW[iObj.Label] = fakeCube.Width.getValueAs(gUnitC).Value
			gFakeCubeH[iObj.Label] = fakeCube.Height.getValueAs(gUnitC).Value
			gFakeCubeL[iObj.Label] = fakeCube.Length.getValueAs(gUnitC).Value

			if gAD.getObject("fakeCube"):
				gAD.removeObject("fakeCube")

		except:

			# remove existing fakeCube object
			if gAD.getObject("fakeCube"):
				gAD.removeObject("fakeCube")

			# skip if no access to the values (wrong design of Sketch and Pad)
			return 1

	return 0


# ###################################################################################################################
# Support for base objects transformations
# ###################################################################################################################


# ###################################################################################################################
def setArray(iObj):

	# support for Array FreeCAD feature
	if iObj.isDerivedFrom("Part::FeaturePython"):

		try:

			# set reference point to the base Pad object
			key = iObj.Base

			if iObj.ArrayType == "polar":
				
				# without the base element
				vArray = iObj.NumberPolar - 1
			else:
				
				# without the base element
				vArray = (iObj.NumberX * iObj.NumberY * iObj.NumberZ) - 1

			# calculate the Base Cube object
			k = 0
			
			while k < vArray:

				# add the Base Cube object
				setCube(key)
				
				# go to the next object
				k = k + 1
		
		except:
			
			# skip if there is no Base object
			return 1
	
	return 0


# ###################################################################################################################
def setSingleMirror(iObj):

	# support for Pads single mirror FreeCAD feature
	if iObj.isDerivedFrom("PartDesign::Mirrored"):

		try:

			# set reference point to the base Pad object
			key = iObj.Originals[0]

			# if object is Mirror this can be calculated as new Pad
			setPad(key)
		
		except:
			
			# skip if there is no base Pad object
			return 1
	
	return 0


# ###################################################################################################################
def setMultiTransform(iObj):
	
	# support for Pads MultiTransform FreeCAD feature
	if iObj.isDerivedFrom("PartDesign::MultiTransform"):

		try:
			
			# set number of mirror transformations available    
			lenT = len(iObj.Transformations)
			k = 0

			# if this is MultiTransform, not single mirror
			if lenT > 0:
				
				# Mirror makes 2 elements but each Mirror in MultiTransform makes next Mirror but using 
				# current transformed object, so this will raise the number of Mirrors to the power, 
				# also you have to remove the base Pad object already added
				while k < (2 ** lenT) - 1:

					# set reference point to the base Pad object
					key = iObj.Originals[0]

					# if object is Mirror this can be calculated as new Pad
					setPad(key)
					
					# go to the next Mirror object and do the same
					k = k + 1

		except:

			# skip if there is no exact structure
			return 1
	
	return 0


# ###################################################################################################################
# MAIN LOOP - set database for objects
# ###################################################################################################################


# search all objects in document and set database for correct ones
for obj in gOBs:

	# if feature is on, just skip all hidden elements
	if sTVF == "on":
		if FreeCADGui.ActiveDocument.getObject(obj.Name).Visibility == False:
			continue

	# set base objects
	setCube(obj)
	setPad(obj)
	
	# set transformations
	setArray(obj)
	setSingleMirror(obj)
	setMultiTransform(obj)


# ###################################################################################################################
# MAIN LOOP - set database for dimensions
# ###################################################################################################################


# search all correct objects and set database for dimensions
for obj in gFakeCubeO:

	# assign values
	vW = gFakeCubeW[obj.Label]
	vH = gFakeCubeH[obj.Label]
	vL = gFakeCubeL[obj.Label]

	# set db for main report
	if sLTF == "n":
		setDB(obj, vW, vH, vL, "name")

	if sLTF == "q":
		setDB(obj, vW, vH, vL, "size")

	if sLTF == "g":
		setDB(obj, vW, vH, vL, "group")

	# set db for thickness report
	setDB(obj, vW, vH, vL, "thick")

	# set db for edge report
	edge = getEdge(obj, vW, vH, vL)
	
	if sTVF == "edge":
		if FreeCADGui.ActiveDocument.getObject(obj.Name).Visibility == False:
			edge = 0 # skip if object is not visible			
 
	gEdgeSize = gEdgeSize + edge


# ###################################################################################################################
# Spreadsheet data init
# ###################################################################################################################


# Polish language
if sLang  == "pl":
    vLang1 = "Element"
    vLang2 = "Wymiary"
    vLang3 = "Grubość"
    vLang4 = "Sztuki"
    
    if sUnitsArea == "mm":
        vLang5 = "Milimetry kwadratowe"
    if sUnitsArea == "m":
        vLang5 = "Metry kwadratowe"
    if sUnitsArea == "in":
        vLang5 = "Cale kwadratowe"        

    vLang6 = "Podsumowanie dla koloru elementu"
    vLang7 = "Podsumowanie dla grubości elementu"
    vLang8 = "Długość obrzeża"

# English language
else:
    vLang1 = "Name"
    vLang2 = "Dimensions"
    vLang3 = "Thickness"
    vLang4 = "Quantity"

    if sUnitsArea == "mm":
        vLang5 = "Square millimeters"
    if sUnitsArea == "m":
        vLang5 = "Square meters"
    if sUnitsArea == "in":
        vLang5 = "Square inches"        

    vLang6 = "Summary by colors"
    vLang7 = "Summary by thickness"
    vLang8 = "Edge size"

# create spreadsheet and prepere it for data
if gAD.getObject("toCut"):
	gAD.removeObject("toCut")

result = gAD.addObject("Spreadsheet::Sheet","toCut")

# init spreadsheet row access point
i = 1


# ###################################################################################################################
# Spreadsheet main report - name
# ###################################################################################################################


if sLTF == "n":

	# add headers
	result.set("A1", vLang1)
	result.set("B1", vLang2)
	result.set("E1", vLang3)
	result.set("F1", vLang4)
	result.set("G1", vLang5)
	result.mergeCells("B1:D1")

	# add values
	for key in gNameA.keys():
		i = i + 1
		a = key.split(":")
		result.set("A" + str(i), "'" + str(a[3]))
		result.set("B" + str(i), getUnit(a[1], "size"))
		result.set("C" + str(i), "'" + "x")
		result.set("D" + str(i), getUnit(a[2], "size"))
		result.set("E" + str(i), getUnit(a[0], "size"))
		result.set("F" + str(i), "'" + str(gNameQ[key]))
		result.set("G" + str(i), getUnit(gNameA[key], "area"))

	# cell sizes
	result.setColumnWidth("A", 135)
	result.setColumnWidth("B", 80)
	result.setColumnWidth("C", 40)
	result.setColumnWidth("D", 80)
	result.setColumnWidth("E", 100)
	result.setColumnWidth("F", 100)
	result.setColumnWidth("G", 180)

	# alignment
	result.setAlignment("A1:A" + str(i), "left", "keep")
	result.setAlignment("B1:B" + str(i), "right", "keep")
	result.setAlignment("C1:C" + str(i), "center", "keep")
	result.setAlignment("D1:D" + str(i), "right", "keep")
	result.setAlignment("E1:E" + str(i), "right", "keep")
	result.setAlignment("F1:F" + str(i), "right", "keep")
	result.setAlignment("G1:G" + str(i), "right", "keep")


# ###################################################################################################################
# Spreadsheet main report - sizes (quantity)
# ###################################################################################################################


if sLTF == "q":

	# add headers
	result.set("A1", vLang4)
	result.set("B1", vLang2)
	result.set("E1", vLang3)
	result.set("F1", vLang5)
	result.mergeCells("B1:D1")
		
	# add values
	for key in gSizesQ.keys():
		i = i + 1
		a = key.split(":")
		result.set("A" + str(i), "'" + str(gSizesQ[key])+" x")
		result.set("B" + str(i), getUnit(a[1], "size"))
		result.set("C" + str(i), "x")
		result.set("D" + str(i), getUnit(a[2], "size"))
		result.set("E" + str(i), getUnit(a[0], "size"))
		result.set("F" + str(i), getUnit(gSizesA[key], "area"))

	# cell sizes
	result.setColumnWidth("A", 80)
	result.setColumnWidth("B", 80)
	result.setColumnWidth("C", 20)
	result.setColumnWidth("D", 80)
	result.setColumnWidth("E", 100)
	result.setColumnWidth("F", 180)

	# alignment
	result.setAlignment("A1:A" + str(i), "right", "keep")
	result.setAlignment("B1:B" + str(i), "right", "keep")
	result.setAlignment("C1:C" + str(i), "center", "keep")
	result.setAlignment("D1:D" + str(i), "right", "keep")
	result.setAlignment("E1:E" + str(i), "right", "keep")
	result.setAlignment("F1:F" + str(i), "right", "keep")


# ###################################################################################################################
# Spreadsheet main report - group
# ###################################################################################################################


if sLTF == "g":

	# add headers
	result.set("A1", vLang1)
	result.set("B1", vLang2)
	result.set("E1", vLang3)
	result.set("F1", vLang4)
	result.set("G1", vLang5)
	result.mergeCells("B1:D1")

	# add values
	for key in gGroupA.keys():
		i = i + 1
		a = key.split(":")
		result.set("A" + str(i), "'" + str(a[3]))
		result.set("B" + str(i), getUnit(a[1], "size"))
		result.set("C" + str(i), "'" + "x")
		result.set("D" + str(i), getUnit(a[2], "size"))
		result.set("E" + str(i), getUnit(a[0], "size"))
		result.set("F" + str(i), "'" + str(gGroupQ[key]))
		result.set("G" + str(i), getUnit(gGroupA[key], "area"))

	# cell sizes
	result.setColumnWidth("A", 135)
	result.setColumnWidth("B", 80)
	result.setColumnWidth("C", 40)
	result.setColumnWidth("D", 80)
	result.setColumnWidth("E", 100)
	result.setColumnWidth("F", 100)
	result.setColumnWidth("G", 180)

	# alignment
	result.setAlignment("A1:A" + str(i), "left", "keep")
	result.setAlignment("B1:B" + str(i), "right", "keep")
	result.setAlignment("C1:C" + str(i), "center", "keep")
	result.setAlignment("D1:D" + str(i), "right", "keep")
	result.setAlignment("E1:E" + str(i), "right", "keep")
	result.setAlignment("F1:F" + str(i), "right", "keep")
	result.setAlignment("G1:G" + str(i), "right", "keep")


# ###################################################################################################################
# Spreadsheet main report - final decoration
# ###################################################################################################################


# colors
result.setForeground("A1:G" + str(i), (0,0,0))
result.setBackground("A1:G" + str(i), (1,1,1))

# fix for center header text in merged cells
result.setAlignment("B1:B1", "center", "keep")
result.setAlignment("C1:C1", "center", "keep")
result.setAlignment("D1:D1", "center", "keep")

# text header decoration
result.setStyle("A1:G1", "bold", "add")


# ###################################################################################################################
# Spreadsheet report for thickness
# ###################################################################################################################


# add empty line separator
i = i + 1

# add summary title for thickness
vCell = "A" + str(i) + ":D" + str(i)
result.mergeCells(vCell)
result.set(vCell, vLang7)
result.setStyle(vCell, "bold", "add")
result.setAlignment(vCell, "left", "keep")

# add empty line separator
i = i + 1

# for thickness	(quantity)
if sLTF == "q":
	for key in gThickQ.keys():
		result.set("A" + str(i), "'" + str(gThickQ[key])+" x")
		result.set("E" + str(i), getUnit(key, "size"))
		result.set("F" + str(i), getUnit(gThickA[key], "area"))
		result.setAlignment("A" + str(i), "right", "keep")
		result.setAlignment("E" + str(i), "right", "keep")
		result.setAlignment("F" + str(i), "right", "keep")
		i = i + 1

# for thickness	(group & name)
if sLTF == "g" or sLTF == "n":
	for key in gThickQ.keys():
		result.set("E" + str(i), getUnit(key, "size"))
		result.set("F" + str(i), "'" + str(gThickQ[key]))
		result.set("G" + str(i), getUnit(gThickA[key], "area"))
		result.setAlignment("E" + str(i), "right", "keep")
		result.setAlignment("F" + str(i), "right", "keep")
		result.setAlignment("G" + str(i), "right", "keep")
		i = i + 1


# ###################################################################################################################
# Spreadsheet report for edge
# ###################################################################################################################


# add empty line separator
i = i + 1

# add summary for edge size
vCell = "A" + str(i) + ":B" + str(i)
result.mergeCells(vCell)
result.set(vCell, vLang8)
result.setStyle(vCell, "bold", "add")
result.setAlignment(vCell, "left", "keep")

vCell = "C" + str(i) + ":E" + str(i)
result.mergeCells(vCell)
result.set(vCell, getUnit(gEdgeSize, "size"))
result.setAlignment(vCell, "right", "keep")


# ###################################################################################################################
# Code link
# ###################################################################################################################


# add empty line separator
i = i + 3

# add link 
vCell = "A" + str(i) + ":G" + str(i)
result.mergeCells(vCell)
result.set(vCell, "Generated by FreeCAD macro: github.com/dprojects/getDimensions")
result.setAlignment(vCell, "left", "keep")


# ###################################################################################################################
# TechDraw part
# ###################################################################################################################


# add empty line at the end of spreadsheet to fix merged cells at TechDraw page
i = i + 1

# remove existing toPrint page
if gAD.getObject("toPrint"):
	gAD.removeObject("toPrint")

# create TechDraw page for print
gAD.addObject("TechDraw::DrawPage","toPrint")
gAD.addObject("TechDraw::DrawSVGTemplate","Template")
gAD.Template.Template = FreeCAD.getResourceDir() + "Mod/TechDraw/Templates/A4_Portrait_blank.svg"
gAD.toPrint.Template = gAD.Template

# add spreadsheet to TechDraw page
gAD.addObject("TechDraw::DrawViewSpreadsheet","Sheet")
gAD.Sheet.Source = gAD.toCut
gAD.toPrint.addView(gAD.Sheet)

# set in the center of the template
gAD.getObject("Sheet").X = gAD.getObject("Template").Width / 2
gAD.getObject("Sheet").Y = gAD.getObject("Template").Height / 2

# try to set fonts
try:
	gAD.getObject("Sheet").Font = "DejaVu Sans"
except:
	gAD.getObject("Sheet").Font = "Arial"

gAD.getObject("Sheet").TextSize = 13

# fix FreeCAD bug
gAD.getObject("Sheet").CellEnd = "G" + str(i)


# ###################################################################################################################
# Reload to see changes
# ###################################################################################################################


gAD.recompute()

