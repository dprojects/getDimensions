# -*- coding: utf-8 -*-

# FreeCAD macro for woodworking
# Author: Darek L (aka dprojects)
# Version: 7.1
# Latest version: https://github.com/dprojects/getDimensions

import FreeCAD,Draft,Spreadsheet


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
sUnitsMetric = "in"

# set square area units:
# "m"  - meter
# "mm" - millimeter
# "in" - inch
sUnitsArea = "in"

# Toggle Visibility Feature:
# "on" - all hidden items with visibility = false will be skipped
# "edge" - hidden elements will not be added to edge size only
# "off" - all items will be listed and calculated
sTVF = "edge"

# Label Type Feature:
# "n" - show name of the element first for each group
# "q" - show quantity first for each group
# "g" - show group name first for each group (grandparent or parent folder)
sLTF = "q"


# ###################################################################################################################
# Autoconfig ( NOT CHANGE HERE )
# ###################################################################################################################

# Maximum thickness size - do not set this value too high, beacuse the thickness 
# will not be recognized correctly and you may see incorrect calculation 
# for small elements e.g. 3 mm x 30 mm x 30 mm. Thickness should always be 
# as low as possible. In Poland usually we use chipboards 18 mm of thickness.
# There are MDF 40 mm but they are not so common. So the thickess should be 
# 20 mm max in this case. If you use much bigger chipboards or wood just set this 
# value higher as you need but make sure the small elements are listed correctly.
vThickMax = 20

if sUnitsMetric == "in":
	vThickMax = float(vThickMax) * float(0.0393700787)

if sUnitsMetric == "m":
	vThickMax = float(vThickMax) * float(0.001)

# get all objects from 3D model
objs = FreeCAD.ActiveDocument.Objects

# init database for sizes (quantity) report
if sLTF == "q":
	vSizesQ = dict() # quantity
	vSizesA = dict() # area

# init database for name report
if sLTF == "n":
	vNameQ = dict() # quantity
	vNameA = dict() # area

# init database for group report
if sLTF == "g":
	vGroupQ = dict() # quantity
	vGroupA = dict() # area

# init database for thickness report
vThickQ = dict() # quantity
vThickA = dict() # area

# init database for edge report
vEdgeSize = 0 # edge size


# ###################################################################################################################
# Functions
# ###################################################################################################################

# ###################################################################################################################
def getParentGroup(iLabel):
	for iGroup in FreeCAD.ActiveDocument.Objects:
		if iGroup.isDerivedFrom("App::DocumentObjectGroup"):
			for iChild in iGroup.Group:
				if iChild.Label == iLabel:
					return iGroup
	return ""

# ###################################################################################################################
def getKey(iObj, iType):

	# create key string with thickness first

	if iObj.Length.getValueAs(sUnitsMetric).Value < vThickMax:
		key = str(iObj.Length.getValueAs(sUnitsMetric)) + " " + sUnitsMetric
		key += ":"
		key += str(iObj.Width.getValueAs(sUnitsMetric)) + " " + sUnitsMetric
		key += ":"
		key += str(iObj.Height.getValueAs(sUnitsMetric)) + " " + sUnitsMetric

	elif iObj.Width.getValueAs(sUnitsMetric).Value < vThickMax:
		key = str(iObj.Width.getValueAs(sUnitsMetric)) + " " + sUnitsMetric
		key += ":"
		key += str(iObj.Length.getValueAs(sUnitsMetric)) + " " + sUnitsMetric
		key += ":"
		key += str(iObj.Height.getValueAs(sUnitsMetric)) + " " + sUnitsMetric

	else:
		key = str(iObj.Height.getValueAs(sUnitsMetric)) + " " + sUnitsMetric
		key += ":"
		key += str(iObj.Width.getValueAs(sUnitsMetric)) + " " + sUnitsMetric
		key += ":"
		key += str(iObj.Length.getValueAs(sUnitsMetric)) + " " + sUnitsMetric

	# key for sizes database
	if iType == "size":
		return str(key)

	# key for name database
	elif iType == "name":
		key = str(key) + ":" + str(iObj.Label)
		return str(key)

	# key for thickness database
	elif iType == "thick":
        
		if iObj.Length.getValueAs(sUnitsMetric).Value < vThickMax:
			key = str(iObj.Length.getValueAs(sUnitsMetric)) + " " + sUnitsMetric
		
		elif iObj.Width.getValueAs(sUnitsMetric).Value < vThickMax:
			key = str(iObj.Width.getValueAs(sUnitsMetric)) + " " + sUnitsMetric
		
		else:
			key = str(iObj.Height.getValueAs(sUnitsMetric)) + " " + sUnitsMetric

	# key for group database
	elif iType == "group":	
		
		# get parent folder (group name)
		vParent = getParentGroup(iObj.Label)
		
		if vParent != "":
			vPL = vParent.Label
			
			# get grandparent folder
			vGrand = getParentGroup(vPL)

			if vGrand != "":
				key = str(key) + ":" + str(vGrand.Label)
			else:
				key = str(key) + ":" + str(vPL)
		else:
			key = str(key) + ":[...]"

	return str(key)


# ###################################################################################################################
def getArea(iObj):

	# make sure to not calculate thickness
	if iObj.Length.getValueAs(sUnitsMetric).Value < vThickMax:
		size1 = iObj.Width
		size2 = iObj.Height
	
	elif iObj.Width.getValueAs(sUnitsMetric).Value < vThickMax:
		size1 = iObj.Length
		size2 = iObj.Height
	
	else:
		size1 = iObj.Length
		size2 = iObj.Width

	# calculate area without thickness
	area = size1.getValueAs(sUnitsArea) * size2.getValueAs(sUnitsArea)

	return area


# ###################################################################################################################
def setDB(iObj, iDB):

	# support for arrays
	if iObj.isDerivedFrom("Part::FeaturePython") and iObj.Base.isDerivedFrom("Part::Box"):

		if iObj.ArrayType == "polar":
			value = iObj.NumberPolar - 1 # without the base element
		else:
			value = (iObj.NumberX * iObj.NumberY * iObj.NumberZ) - 1 # without the base element

		iObj = iObj.Base # change obejct reference
		area = getArea(iObj) * value # get area for object
	
	else:
		value = 1 # single object
		area = getArea(iObj) # get area for object
	
	# set DB for name of element database
	if iDB == "name":

		key = getKey(iObj, "name")

		if key in vNameQ:
			vNameQ[key] = vNameQ[key] + value
			vNameA[key] = vNameA[key] + area
		else:
			vNameQ[key] = value
			vNameA[key] = area

	# set DB for sizes (quantity) database
	elif iDB == "size":

		key = getKey(iObj, "size")

		if key in vSizesQ:
			vSizesQ[key] = vSizesQ[key] + value
			vSizesA[key] = vSizesA[key] + area
		else:
			vSizesQ[key] = value
			vSizesA[key] = area

	# set DB for group database
	elif iDB == "group":

		key = getKey(iObj, "group")

		if key in vGroupQ:
			vGroupQ[key] = vGroupQ[key] + value
			vGroupA[key] = vGroupA[key] + area
		else:
			vGroupQ[key] = value
			vGroupA[key] = area
	
	# set DB for thickness database
	elif iDB == "thick":

		key = getKey(iObj, "thick")

		if key in vThickQ:
			vThickQ[key] = vThickQ[key] + value
			vThickA[key] = vThickA[key] + area
		else:
			vThickQ[key] = value
			vThickA[key] = area


# ###################################################################################################################
def getEdge(iObj):

	# support for arrays
	if iObj.isDerivedFrom("Part::FeaturePython") and iObj.Base.isDerivedFrom("Part::Box"):

		if iObj.ArrayType == "polar":
			value = iObj.NumberPolar - 1 # without the base element
		else:
			value = (iObj.NumberX * iObj.NumberY * iObj.NumberZ) - 1 # without the base element

		iObj = iObj.Base # change object reference
	else:
		value = 1 # single object

	# skip the thickness dimension
	if iObj.Length.getValueAs(sUnitsMetric).Value < vThickMax:
		size1 = iObj.Width
		size2 = iObj.Height

	elif iObj.Width.getValueAs(sUnitsMetric).Value < vThickMax:
		size1 = iObj.Length
		size2 = iObj.Height

	else:
		size1 = iObj.Length
		size2 = iObj.Width

	# calculate the edge size
	edge = ((2 * size1.getValueAs(sUnitsMetric).Value) + (2 * size2.getValueAs(sUnitsMetric).Value)) * value

	return edge


# ###################################################################################################################
# Build objects database
# ###################################################################################################################

# search all objects and set database for each one
for obj in objs:

	# if feature is on, just skip all hidden elements
	if sTVF == "on":
		if FreeCADGui.ActiveDocument.getObject(obj.Name).Visibility == False:
			continue

	# support for cube objects
	if obj.isDerivedFrom("Part::Box"):
		keepGoing = 1 # just do nothing
	
	# support for array objects with cube as base
	elif obj.isDerivedFrom("Part::FeaturePython") and obj.Base.isDerivedFrom("Part::Box"):
		keepGoing = 1 # just do nothing
	
	# skip if object is not reconized
	else: 
		continue

	# set db for main report
	if sLTF == "n":
		setDB(obj, "name")

	if sLTF == "q":
		setDB(obj, "size")

	if sLTF == "g":
		setDB(obj, "group")

	# set db for thickness report
	setDB(obj, "thick")

	# set db for edge report
	edge = getEdge(obj)
	
	if sTVF == "edge":
		if FreeCADGui.ActiveDocument.getObject(obj.Name).Visibility == False:
			edge = 0 # skip if object is not visible			
 
	vEdgeSize = vEdgeSize + edge


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
if FreeCAD.ActiveDocument.getObject("toCut"):
	FreeCAD.ActiveDocument.removeObject("toCut")

result = FreeCAD.ActiveDocument.addObject("Spreadsheet::Sheet","toCut")

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
	for key in vNameA.keys():
		i = i + 1
		a = key.split(":")
		result.set("A" + str(i), "'" + str(a[3]))
		result.set("B" + str(i), "'" + str(a[1]))
		result.set("C" + str(i), "'" + "x")
		result.set("D" + str(i), "'" + str(a[2]))
		result.set("E" + str(i), "'" + str(a[0]))
		result.set("F" + str(i), "'" + str(vNameQ[key]))
		result.set("G" + str(i), "'" + str(vNameA[key]))

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
	for key in vSizesQ.keys():
		i = i + 1
		a = key.split(":")
		result.set("A" + str(i), "'" + str(vSizesQ[key])+" x")
		result.set("B" + str(i), "'" + str(a[1]))
		result.set("C" + str(i), "x")
		result.set("D" + str(i), "'" + str(a[2]))
		result.set("E" + str(i), "'" + str(a[0]))
		result.set("F" + str(i), "'" + str(vSizesA[key]))

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
	for key in vGroupA.keys():
		i = i + 1
		a = key.split(":")
		result.set("A" + str(i), "'" + str(a[3]))
		result.set("B" + str(i), "'" + str(a[1]))
		result.set("C" + str(i), "'" + "x")
		result.set("D" + str(i), "'" + str(a[2]))
		result.set("E" + str(i), "'" + str(a[0]))
		result.set("F" + str(i), "'" + str(vGroupQ[key]))
		result.set("G" + str(i), "'" + str(vGroupA[key]))

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
	for key in vThickQ.keys():
		result.set("A" + str(i), "'" + str(vThickQ[key])+" x")
		result.set("E" + str(i), "'" + str(key))
		result.set("F" + str(i), "'" + str(vThickA[key]))
		result.setAlignment("A" + str(i), "right", "keep")
		result.setAlignment("E" + str(i), "right", "keep")
		result.setAlignment("F" + str(i), "right", "keep")
		i = i + 1

# for thickness	(group & name)
if sLTF == "g" or sLTF == "n":
	for key in vThickQ.keys():
		result.set("E" + str(i), "'" + str(key))
		result.set("F" + str(i), "'" + str(vThickQ[key]))
		result.set("G" + str(i), "'" + str(vThickA[key]))
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
result.set(vCell, "'" + str(vEdgeSize) + " " + sUnitsMetric)
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

Tree = App.ActiveDocument.Name

# remove existing toPrint page
if FreeCAD.ActiveDocument.getObject("toPrint"):
	App.getDocument(Tree).removeObject("toPrint")

# create TechDraw page for print
App.activeDocument().addObject("TechDraw::DrawPage","toPrint")
App.activeDocument().addObject("TechDraw::DrawSVGTemplate","Template")
App.activeDocument().Template.Template = App.getResourceDir() + "Mod/TechDraw/Templates/A4_Portrait_blank.svg"
App.activeDocument().toPrint.Template = App.activeDocument().Template

# add spreadsheet to TechDraw page
App.activeDocument().addObject("TechDraw::DrawViewSpreadsheet","Sheet")
App.activeDocument().Sheet.Source = App.activeDocument().toCut
App.activeDocument().toPrint.addView(App.activeDocument().Sheet)

# add decoration to the table
FreeCAD.getDocument(Tree).getObject("Sheet").X = 105.00
FreeCAD.getDocument(Tree).getObject("Sheet").Y = 200.00
FreeCAD.getDocument(Tree).getObject("Sheet").CellEnd = "G" + str(i)


# ###################################################################################################################
# Reload to see changes
# ###################################################################################################################

App.ActiveDocument.recompute()
