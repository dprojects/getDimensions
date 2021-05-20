# -*- coding: utf-8 -*-

# FreeCAD macro for woodworking
# Author: Darek L (aka dprojects)
# Version: 5.0
# Latest version: https://github.com/dprojects/getDimensions

import FreeCAD,Draft,Spreadsheet

# #######################################################
# SETTINGS ( SET HERE )
# #######################################################

# set language:
# "pl" - Polish
# "en" - English
sLang = "pl"

# set metric system:
# "mm" - millimeter
# "m" - meter
# "in" - inch
sUnits = 'mm'

# set square area units:
# "m"  - meter
# "mm" - millimeter
# "in" - inch
sSquareArea = 'm'

# toggle visibility:
# "on" - the feature is on and hidden items (visibility = false) will be skipped
# "off" - all items are calculated, like it was before
sVisible = 'on'

# #######################################################
# MAIN CODE ( NOT CHANGE HERE )
# #######################################################

# setting variables - autoconfig
if sLang  == "pl":
    vLang1 = 'Element'
    vLang2 = 'Wymiary'
    vLang3 = 'Grubość'
    vLang4 = 'Sztuki'
    
    if sSquareArea == "mm":
        vLang5 = 'Milimetry kwadratowe'
    if sSquareArea == "m":
        vLang5 = 'Metry kwadratowe'
    if sSquareArea == "in":
        vLang5 = 'Cale kwadratowe'        

    vLang6 = 'Suma'
else:
    vLang1 = 'Name'
    vLang2 = 'Dimensions'
    vLang3 = 'Thickness'
    vLang4 = 'Quantity'

    if sSquareArea == "mm":
        vLang5 = 'Square millimeters'
    if sSquareArea == "m":
        vLang5 = 'Square meters'
    if sSquareArea == "in":
        vLang5 = 'Square inches'        

    vLang6 = 'Summary'

# create spreadsheet and prepere it for data
if FreeCAD.ActiveDocument.getObject("toCut"):
	FreeCAD.ActiveDocument.removeObject("toCut")

result = FreeCAD.ActiveDocument.addObject("Spreadsheet::Sheet","toCut")

result.mergeCells('B1:D1')

result.set( 'A1', vLang1 )
result.set( 'B1', vLang2 )
result.set( 'E1', vLang3 )
result.set( 'F1', vLang4 )
result.set( 'G1', vLang5 )

result.setForeground( 'A1:G1', (0,0,0) )
result.setBackground( 'A1:G1', (1,1,1) )
result.setStyle( 'A1:G1', 'bold', 'add')
result.setAlignment( 'A1:G1', 'top', 'keep' )
result.setAlignment( 'A1:G1', 'center', 'keep' )

# scan all objects and count chipboards (cubes)
objs = FreeCAD.ActiveDocument.Objects

quantity = dict()
sqmSum = dict()
 
for obj in objs:

	if sVisible == "on":
		if FreeCADGui.ActiveDocument.getObject( obj.Name ).Visibility == False:
			continue

	# support for cube objects		
	if obj.isDerivedFrom("Part::Box"):
	
		keyArr = [ str(obj.Length), str(obj.Width), str(obj.Height) ]
		keyArr.sort()
		key = "x".join(keyArr)
		if key in quantity:
			quantity[key] = quantity[key] + 1
		else:
			quantity[key] = 1

	# support for array objects with cube as base
	elif obj.isDerivedFrom("Part::FeaturePython") and obj.Base.isDerivedFrom("Part::Box"):

		# the main box cube will be added in next loop
		if obj.ArrayType == "polar":
			arrayQuantity = obj.NumberPolar - 1
		else:
			arrayQuantity = obj.NumberX * obj.NumberY * obj.NumberZ - 1

		keyArr = [ str(obj.Base.Length), str(obj.Base.Width), str(obj.Base.Height) ]
		keyArr.sort()
		key = "x".join(keyArr)
		if key in quantity:
			quantity[key] = quantity[key] + arrayQuantity
		else:
			quantity[key] = arrayQuantity


# check what we have...
sqm = 0
i = 1
# calculate rows for later TechDraw print, first row for header
vRows = 1

for obj in objs:

	if obj.isDerivedFrom("Part::Box"):
		
		keyArr = [ str(obj.Length), str(obj.Width), str(obj.Height) ]
		keyArr.sort()
		key = "x".join(keyArr)
		if not key in quantity:
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
		sqm = quantity[key] * size1.getValueAs(sSquareArea) * size2.getValueAs(sSquareArea)
		
		# ...and add to spreadsheet
		result.set( 'A'+str(i), "'"+str(obj.Label) )
		result.set( 'B'+str(i), "'"+str(size1) )
		result.set( 'C'+str(i), 'x' )
		result.set( 'D'+str(i), "'"+str(size2) )
		result.set( 'E'+str(i), "'"+str(thick) )
		result.set( 'F'+str(i), "'"+str(quantity[key]) )
		result.set( 'G'+str(i), "'"+str(sqm) )
		vRows = vRows + 1

		# set metric system
		result.setDisplayUnit('B'+str(i), sUnits)		
		result.setDisplayUnit('D'+str(i), sUnits)
		result.setDisplayUnit('E'+str(i), sUnits)
		
		# recalculate and add partial square meters
		del quantity[key]
		key = str(thick)

		if key in sqmSum:
			sqmSum[key] = sqmSum[key] + sqm
		else:
			sqmSum[key] = sqm

# add to spreadsheet summary for square meters
i = i + 1
# add empty line separator
vRows = vRows + 1

for key in sqmSum.keys():
	i = i + 1	
	result.set( 'A'+str(i), vLang6 )
	result.set( 'E'+str(i), "'"+str(key) )
	result.set( 'G'+str(i), "'"+str(sqmSum[key]) )
	result.setDisplayUnit('E'+str(i), sUnits)	
	vRows = vRows + 1

# final decoration
result.setForeground( 'A2:G'+str(i), (0,0,0) )
result.setBackground( 'A2:G'+str(i), (1,1,1) )
		
#result.setStyle( 'A2:A'+str(i), 'bold', 'add')

result.setColumnWidth( 'A', 135 )
result.setColumnWidth( 'B', 80 )
result.setColumnWidth( 'C', 40 )
result.setColumnWidth( 'D', 80 )
result.setColumnWidth( 'E', 100 )
result.setColumnWidth( 'F', 100 )
result.setColumnWidth( 'G', 180 )

result.setAlignment( 'A1:A'+str(i), 'left', 'keep' )
result.setAlignment( 'B2:B'+str(i), 'right', 'keep' )
result.setAlignment( 'C1:C'+str(i), 'center', 'keep' )
result.setAlignment( 'D1:D'+str(i), 'right', 'keep' )
result.setAlignment( 'E1:E'+str(i), 'right', 'keep' )
result.setAlignment( 'F1:F'+str(i), 'right', 'keep' )
result.setAlignment( 'G1:G'+str(i), 'right', 'keep' )

result.setAlignment( 'B1:B1', 'center', 'keep' )
result.setAlignment( 'C1:C1', 'center', 'keep' )
result.setAlignment( 'D1:D1', 'center', 'keep' )

# refresh document
App.ActiveDocument.recompute()

# remove existing toPrint page
if FreeCAD.ActiveDocument.getObject("toPrint"):
	App.getDocument("Index").removeObject("toPrint")

# create TechDraw page for print
App.activeDocument().addObject('TechDraw::DrawPage','toPrint')
App.activeDocument().addObject('TechDraw::DrawSVGTemplate','Template')
App.activeDocument().Template.Template = App.getResourceDir()+'Mod/TechDraw/Templates/A4_Portrait_blank.svg'
App.activeDocument().toPrint.Template = App.activeDocument().Template

# add spreadsheet to TechDraw page
App.activeDocument().addObject('TechDraw::DrawViewSpreadsheet','Sheet')
App.activeDocument().Sheet.Source = App.activeDocument().toCut
App.activeDocument().toPrint.addView(App.activeDocument().Sheet)

# add decoration to the table
FreeCAD.getDocument("Index").getObject("Sheet").X = 105.00
FreeCAD.getDocument("Index").getObject("Sheet").Y = 260.00
FreeCAD.getDocument("Index").getObject("Sheet").CellEnd = "G"+str(vRows)

# reload to see changes
App.ActiveDocument.recompute()