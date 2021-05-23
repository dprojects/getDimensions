# -*- coding: utf-8 -*-

# FreeCAD macro for woodworking
# Author: Darek L (aka dprojects)
# Version: 6.0
# Latest version: https://github.com/dprojects/getDimensions

import FreeCAD,Draft,Spreadsheet


# #######################################################
# SETTINGS ( SET HERE )
# #######################################################

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
# "off" - all items will be listed and calculated
sTVF = "on"

# Summary By Colors Feature:
# "on" - shows parent folder names and summary by grandparent folder
# "off" - feature is off, so only labels of elements are listed
sSBCF = "off"


# #######################################################
# MAIN CODE ( NOT CHANGE HERE )
# #######################################################

# define function
def getParentGroup(iLabel):
	for iGroup in FreeCAD.ActiveDocument.Objects:
		if iGroup.isDerivedFrom("App::DocumentObjectGroup"):
			for iChild in iGroup.Group:
				if iChild.Label == iLabel:
					return iGroup

# setting variables - autoconfig
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

# create spreadsheet and prepere it for data
if FreeCAD.ActiveDocument.getObject("toCut"):
	FreeCAD.ActiveDocument.removeObject("toCut")

result = FreeCAD.ActiveDocument.addObject("Spreadsheet::Sheet","toCut")

# set headers
result.set("A1", vLang1)
result.set("B1", vLang2)
result.set("E1", vLang3)
result.set("F1", vLang4)
result.set("G1", vLang5)
result.mergeCells("B1:D1")


# #######################################################
# Calculation loop
# #######################################################

# scan all objects and count chipboards (cubes)
objs = FreeCAD.ActiveDocument.Objects

# init data storage
vQuantity = dict()
vArea = dict()
vThick = dict()

if sSBCF == "on":
	vGroupSqm = dict()
	vGroupQua = dict()

# build data for later calculation
for obj in objs:

    	# if feature is on, just skip all hidden elements
	if sTVF == "on":
		if FreeCADGui.ActiveDocument.getObject(obj.Name).Visibility == False:
			continue

	# support for cube objects
	if obj.isDerivedFrom("Part::Box"):
        
		# create unique key
		keyArr = [ str(obj.Length), str(obj.Width), str(obj.Height) ]
		keyArr.sort()
		key = "x".join(keyArr)

		# calculate
		if key in vQuantity:
			vQuantity[key] = vQuantity[key] + 1
		else:
			vQuantity[key] = 1

	# support for array objects with cube as base
	elif obj.isDerivedFrom("Part::FeaturePython") and obj.Base.isDerivedFrom("Part::Box"):

		# the main box cube will be added in next loop
		if obj.ArrayType == "polar":
			arrayQuantity = obj.NumberPolar - 1
		else:
			arrayQuantity = obj.NumberX * obj.NumberY * obj.NumberZ - 1

		# create unique key
		keyArr = [ str(obj.Base.Length), str(obj.Base.Width), str(obj.Base.Height) ]
		keyArr.sort()
		key = "x".join(keyArr)

		# calculate
		if key in vQuantity:
			vQuantity[key] = vQuantity[key] + arrayQuantity
		else:
			vQuantity[key] = arrayQuantity


# reset local variables
sqm = 0
i = 1

# check what we have...
for obj in objs:

	if obj.isDerivedFrom("Part::Box"):
		
		# set unique key for search
		keyArr = [ str(obj.Length), str(obj.Width), str(obj.Height) ]
		keyArr.sort()
		key = "x".join(keyArr)

		# search the key in stored data
		if not key in vQuantity:
			continue

		i = i + 1

		if obj.Length.Value < 30:
			size1 = obj.Width
			size2 = obj.Height
			thick = obj.Length
		elif obj.Width.Value < 30:
			size1 = obj.Length
			size2 = obj.Height
			thick = obj.Width
		else:
			size1 = obj.Length
			size2 = obj.Width
			thick = obj.Height
		
		# calculate square area
		sqm = vQuantity[key] * size1.getValueAs(sUnitsArea) * size2.getValueAs(sUnitsArea)
		
		# ...and add to spreadsheet
		if sSBCF == "on":
			
			# get parent folder (group name)
			vParent = getParentGroup(obj.Label)
			vPL = vParent.Label

			# add group name to spreadsheet
			result.set("A"+str(i), "'" + str(vPL))
			
			# get grandparent folder
			vGrand = getParentGroup(vPL)
			vGL = vGrand.Label

			# store number of items
			if vGL in vGroupQua:
				vGroupQua[vGL] = vGroupQua[vGL] + len(vParent.Group)
			else:
				vGroupQua[vGL] = len(vParent.Group)

			# store square area
			if vGL in vGroupSqm:
				vGroupSqm[vGL] = vGroupSqm[vGL] + sqm
			else:
				vGroupSqm[vGL] = sqm
			
		else:
			# add element name to spreadsheet if the feature is off
			result.set("A"+str(i), "'" + str(obj.Label))

		# add other values to spreadsheet
		result.set("B"+str(i), "'" + str(size1.getValueAs(sUnitsMetric))+" "+sUnitsMetric)
		result.set("C"+str(i), "x")
		result.set("D"+str(i), "'" + str(size2.getValueAs(sUnitsMetric))+" "+sUnitsMetric)
		result.set("E"+str(i), "'" + str(thick.getValueAs(sUnitsMetric))+" "+sUnitsMetric)
		result.set("F"+str(i), "'" + str(vQuantity[key]))
		result.set("G"+str(i), "'" + str(sqm))

		vQ = vQuantity[key]

		# recalculate and add partial square meters
		del vQuantity[key]
		key = str(thick.getValueAs(sUnitsMetric))+" "+sUnitsMetric

		if key in vArea:
			vArea[key] = vArea[key] + sqm
		else:
			vArea[key] = sqm

		if key in vThick:
			vThick[key] = vThick[key] + vQ
		else:
			vThick[key] = vQ


# #######################################################
# Spreadsheet data decoration
# #######################################################

# colors
result.setForeground("A1:G"+str(i), (0,0,0))
result.setBackground("A1:G"+str(i), (1,1,1))

# cell sizes
result.setColumnWidth("A", 135)
result.setColumnWidth("B", 80)
result.setColumnWidth("C", 40)
result.setColumnWidth("D", 80)
result.setColumnWidth("E", 100)
result.setColumnWidth("F", 100)
result.setColumnWidth("G", 180)

# alignment
result.setAlignment("A1:A"+str(i), "left", "keep")
result.setAlignment("B1:B"+str(i), "right", "keep")
result.setAlignment("C1:C"+str(i), "center", "keep")
result.setAlignment("D1:D"+str(i), "right", "keep")
result.setAlignment("E1:E"+str(i), "right", "keep")
result.setAlignment("F1:F"+str(i), "right", "keep")
result.setAlignment("G1:G"+str(i), "right", "keep")

# fix for center header text in merged cells
result.setAlignment("B1:B1", "center", "keep")
result.setAlignment("C1:C1", "center", "keep")
result.setAlignment("D1:D1", "center", "keep")

# text header decoration
result.setStyle("A1:G1", "bold", "add")


# #######################################################
# Spreadsheet summary 
# #######################################################

# add empty line separator
i = i + 1

# show summary for groups
if sSBCF == "on":

	# add empty line separator
	i = i + 1
	
	# add summary title
	vCell = "A"+str(i)+":D"+str(i)
	result.set(vCell, vLang6)
	result.setStyle(vCell, "bold", "add")
	result.mergeCells(vCell)
	result.setAlignment(vCell, "left", "keep")
		
	# add empty line separator
	i = i + 1

	# add values
	for key in vGroupSqm.keys():
		result.set("A"+str(i), "'" + str(key))
		result.set("F"+str(i), "'" + str(vGroupQua[key]))
		result.set("G"+str(i), "'" + str(vGroupSqm[key]))
		result.setDisplayUnit("E"+str(i), sUnitsMetric)	
		result.setAlignment("A"+str(i), "left", "keep")
		result.setAlignment("F"+str(i), "right", "keep")
		result.setAlignment("G"+str(i), "right", "keep")
		i = i + 1

# add empty line separator
i = i + 1

# add summary title for thickness
vCell = "A"+str(i)+":D"+str(i)
result.set(vCell, vLang7)
result.setStyle(vCell, "bold", "add")
result.mergeCells(vCell)
result.setAlignment(vCell, "left", "keep")

# add empty line separator
i = i + 1

# add summary values for thickness	
for key in vArea.keys():
	result.set("E"+str(i), "'" + str(key))
	result.set("F"+str(i), "'" + str(vThick[key]))
	result.set("G"+str(i), "'" + str(vArea[key]))
	result.setAlignment("E"+str(i), "right", "keep")
	result.setAlignment("F"+str(i), "right", "keep")
	result.setAlignment("G"+str(i), "right", "keep")
	i = i + 1


# #######################################################
# TechDraw part
# #######################################################

# remove existing toPrint page
if FreeCAD.ActiveDocument.getObject("toPrint"):
	App.getDocument("Index").removeObject("toPrint")

# create TechDraw page for print
App.activeDocument().addObject("TechDraw::DrawPage","toPrint")
App.activeDocument().addObject("TechDraw::DrawSVGTemplate","Template")
App.activeDocument().Template.Template = App.getResourceDir()+"Mod/TechDraw/Templates/A4_Portrait_blank.svg"
App.activeDocument().toPrint.Template = App.activeDocument().Template

# add spreadsheet to TechDraw page
App.activeDocument().addObject("TechDraw::DrawViewSpreadsheet","Sheet")
App.activeDocument().Sheet.Source = App.activeDocument().toCut
App.activeDocument().toPrint.addView(App.activeDocument().Sheet)

# add decoration to the table
FreeCAD.getDocument("Index").getObject("Sheet").X = 105.00
FreeCAD.getDocument("Index").getObject("Sheet").Y = 200.00
FreeCAD.getDocument("Index").getObject("Sheet").CellEnd = "G"+str(i)


# #######################################################
# Reload to see changes
# #######################################################

App.ActiveDocument.recompute()
