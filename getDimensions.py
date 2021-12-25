# -*- coding: utf-8 -*-

# FreeCAD macro for woodworking
# Author: Darek L (aka dprojects)
# Version: 2021.12.25
# Latest version: https://github.com/dprojects/getDimensions

import FreeCAD, Draft, Spreadsheet


# ###################################################################################################################
# Default Settings ( CHANGE HERE IF NEEDED )
# ###################################################################################################################


# Languages:
# "pl" - Polish
# "en" - English
sLang = "en"

# Units for dimensions:
# "mm" - millimeter
# "m" - meter
# "in" - inch
sUnitsMetric = "mm"

# Units for edge size:
# "mm" - millimeter
# "m" - meter
# "in" - inch
sUnitsEdge = "m"

# Units for area:
# "m" - square meter (m2)
# "mm" - square millimeter (mm2)
# "in" - square inch (inch2)
sUnitsArea = "m"

# Visibility (Toggle Visibility Feature):
# "on" - skip all hidden objects and groups
# "edge" - show all hidden objects and groups but not add to the edge size
# "off" - show and calculate all objects and groups
sTVF = "edge"

# Report customization (Label Type Feature):
# "n" - automatic by objects names (listing)
# "g" - automatic by groups (folder names)
# "q" - automatic by quantity (dimensions)
# "c" - custom by constraints names (totally custom report)
sLTF = "q"

# Report print quality:
# "eco" - low ink mode (good for printing)
# "hq" - high quality mode (good for pdf)
sRPQ = "hq"


# ###################################################################################################################
# Autoconfig - define globals ( NOT CHANGE HERE )
# ###################################################################################################################


# set reference point to Active Document
gAD = FreeCAD.activeDocument()

# get all objects from 3D model
gOBs = gAD.Objects

# unit for calculation purposes (not change)
gUnitC = "mm"

# header color
gHeadCS = (0.862745,0.862745,0.862745,1.000000) # strong
gHeadCW = (0.941176,0.941176,0.941176,1.000000) # weak

# remove existing Fake Cube object if exists (auto clean after error)
if gAD.getObject("gFakeCube"):
	gAD.removeObject("gFakeCube")

# create Fake Cube but not call recompute
gFakeCube = gAD.addObject("Part::Box", "gFakeCube")


# ###################################################################################################################
# Init databases
# ###################################################################################################################


# init database for Fake Cube
dbFCO = [] # objects
dbFCW = dict() # width
dbFCH = dict() # height
dbFCL = dict() # length

# init database for dimensions
dbDQ = dict() # quantity
dbDA = dict() # area

# init database for thickness
dbTQ = dict() # quantity
dbTA = dict() # area

# init database for edge
dbE = dict()
dbE["size"] = 0 # edge size

# init database for Constraints Named
dbCNO = [] # objects
dbCNL = dict() # length
dbCNQ = dict() # quantity
dbCNN = dict() # names
dbCNV = dict() # values


# ###################################################################################################################
# Support for errors
# ###################################################################################################################


# ###################################################################################################################
def showError(iObj, iPlace, iError):

	FreeCAD.Console.PrintMessage("\n ====================================================== \n")
	
	try:
		FreeCAD.Console.PrintMessage("ERROR: ")
		FreeCAD.Console.PrintMessage(" | ")
		FreeCAD.Console.PrintMessage(str(iObj.Label))
		FreeCAD.Console.PrintMessage(" | ")
		FreeCAD.Console.PrintMessage(str(iPlace))
		FreeCAD.Console.PrintMessage(" | ")
		FreeCAD.Console.PrintMessage(str(iError))
		
	except:
		FreeCAD.Console.PrintMessage("FATAL ERROR, or even worse :-)")
		
	FreeCAD.Console.PrintMessage("\n ====================================================== \n")
	
	return 0


# ###################################################################################################################
# Support for calculations
# ###################################################################################################################


# ###################################################################################################################
def getUnit(iValue, iType):

	iValue = float(iValue)

	# for dimensions
	if iType == "d":
		
		if sUnitsMetric == "mm":
			return "'" + str( int(round(iValue, 0)) ) + " " + sUnitsMetric
		
		if sUnitsMetric == "m":
			return "'" + str( round(iValue * float(0.001), 3) ) + " " + sUnitsMetric
		
		if sUnitsMetric == "in":
			return "'" + str( round(iValue * float(0.0393700787), 3) ) + " " + sUnitsMetric
	
	# for edge
	if iType == "edge":
		
		if sUnitsEdge == "mm":
			return "'" + str( int(round(iValue, 0)) ) + " " + sUnitsEdge
		
		if sUnitsEdge == "m":
			return "'" + str( round(iValue * float(0.001), 3) ) + " " + sUnitsEdge
		
		if sUnitsEdge == "in":
			return "'" + str( round(iValue * float(0.0393700787), 3) ) + " " + sUnitsEdge
	
	# for area
	if iType == "area":
		
		if sUnitsArea == "mm":
			return "'" + str( int(round(iValue, 0)) )
		
		if sUnitsArea == "m":
			return "'" + str( round(iValue * float(0.000001), 6) )
		
		if sUnitsArea == "in":
			return "'" + str( round(iValue * float(0.0015500031), 6) )
		
	return -1


# ###################################################################################################################
def getGroup(iObj):

	# init variable
	vGroup = ""

	# support for Cube furniture part
	if iObj.isDerivedFrom("Part::Box"):
		
		# get grandparent
		try:
			vGroup = iObj.getParentGroup().getParentGroup().Label
		except:
			vGroup = ""
		
		# get parent
		if vGroup == "":
			try:
				vGroup = iObj.getParentGroup().Label
			except:
				vGroup = ""
			
	# support for Pad furniture part
	elif iObj.isDerivedFrom("PartDesign::Pad"):
		
		# get grandparent
		try:
			vGroup = iObj.Profile[0].Parents[0][0].getParentGroup().Label
		except:
			vGroup = ""
		
		# get parent
		if vGroup == "":
			try:
				vGroup = iObj.Profile[0].Parents[0][0].Label
			except:
				vGroup = ""

	return vGroup


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

	# key for quantity report
	if iType == "d" and sLTF == "q":
		return str(vKey)

	# key for name report
	elif iType == "d" and sLTF == "n":
		vKey = str(vKey) + ":" + str(iObj.Label)
		return str(vKey)

	# key for group report
	elif iType == "d" and sLTF == "g":
		
		# get grandparent or parent group name
		vGroup = getGroup(iObj)
		
		if vGroup != "":
			vKey = str(vKey) + ":" + str(vGroup)
		else:
			vKey = str(vKey) + ":[...]"

	# return thickness (this is value, not string)
	elif iType == "thick":
		return vKeyArr[0]

	return str(vKey)


# ###################################################################################################################
def getArea(iObj, iW, iH, iL):

	# make sure to not calculate thickness
	vT = getKey(iObj, iW, iH, iL, "thick")

	if iL == vT:
		vD1 = iW
		vD2 = iH
	
	elif iW == vT:
		vD1 = iL
		vD2 = iH
	
	else:
		vD1 = iL
		vD2 = iW

	# calculate area without thickness
	vArea = vD1 * vD2

	return vArea


# ###################################################################################################################
def getEdge(iObj, iW, iH, iL):

	# skip the thickness dimension
	vT = getKey(iObj, iW, iH, iL, "thick")

	if iL == vT:
		vD1 = iW
		vD2 = iH

	elif iW == vT:
		vD1 = iL
		vD2 = iH

	else:
		vD1 = iL
		vD2 = iW

	# calculate the edge size
	vEdge = (2 * vD1) + (2 * vD2)

	return vEdge


# ###################################################################################################################
# Database controllers - set db only via this controllers
# ###################################################################################################################


# ###################################################################################################################
def setDB(iObj, iW, iH, iL):

	try:
		
		# set db for Fake Cube Object 
		dbFCO.append(iObj)

		# set db for Fake Cube dimensions
		dbFCW[iObj.Label] = iW
		dbFCH[iObj.Label] = iH
		dbFCL[iObj.Label] = iL

		# get area for object
		vArea = getArea(iObj, iW, iH, iL) 
	
		# get key  for object
		vKey = getKey(iObj, iW, iH, iL, "d")
	
		# set dimensions db for quantity & area
		if vKey in dbDQ:
	
			dbDQ[vKey] = dbDQ[vKey] + 1
			dbDA[vKey] = dbDA[vKey] + vArea
		else:
	
			dbDQ[vKey] = 1
			dbDA[vKey] = vArea

		# get key  for object (convert value to dimension string)
		vKey = str(getKey(iObj, iW, iH, iL, "thick"))
	
		# set thickness db for quantity & area
		if vKey in dbTQ:
	
			dbTQ[vKey] = dbTQ[vKey] + 1
			dbTA[vKey] = dbTA[vKey] + vArea
		else:
	
			dbTQ[vKey] = 1
			dbTA[vKey] = vArea

		# set edge db for edge size
		vEdge = getEdge(iObj, iW, iH, iL)

		if sTVF == "edge":
			if FreeCADGui.ActiveDocument.getObject(iObj.Name).Visibility == False:
				vEdge = 0 # skip if object is not visible			

		dbE["size"] = dbE["size"] + vEdge

	except:

		# set db error
		showError(iObj, "setDB", "set db error")
		return -1

	return 0


# ###################################################################################################################
def setDBConstraints(iObj, iL, iN, iV):

	try:

		# set key
		vKey = iObj.Label
				
		# set quantity
		if vKey in dbCNQ:

			# increase quantity only
			dbCNQ[vKey] = dbCNQ[vKey] + 1

			# show only one object at report
			return 0
			
		# init quantity
		dbCNQ[vKey] = 1

		# add object with no empty constraints names
		dbCNO.append(iObj)

		# set length, names, values
		dbCNL[vKey] = iL
		dbCNN[vKey] = iN
		dbCNV[vKey] = iV

	except:

		# set db error
		showError(iObj, "setDBConstraints", "set db error")
		return -1

	return 0


# ###################################################################################################################
# Support for base furniture parts
# ###################################################################################################################


# ###################################################################################################################
def setCube(iObj):

	try:

		# get correct dimensions as values
		vW = iObj.Width.getValueAs(gUnitC).Value
		vH = iObj.Height.getValueAs(gUnitC).Value
		vL = iObj.Length.getValueAs(gUnitC).Value

		# set db for quantity & area & edge size
		setDB(iObj, vW, vH, vL)

	except:

		# if no access to the values
		showError(iObj, "setCube", "no access to the values")
		return -1

	return 0


# ###################################################################################################################
def setPad(iObj):

	try:
		
		# assign values to the Fake Cube dimensions
		gFakeCube.Width = iObj.Profile[0].Shape.OrderedEdges[0].Length
		gFakeCube.Height = iObj.Profile[0].Shape.OrderedEdges[1].Length
		gFakeCube.Length = iObj.Length.Value
		
		# get values as the correct dimensions
		vW = gFakeCube.Width.getValueAs(gUnitC).Value
		vH = gFakeCube.Height.getValueAs(gUnitC).Value
		vL = gFakeCube.Length.getValueAs(gUnitC).Value

		# set db for quantity & area & edge size
		setDB(iObj, vW, vH, vL)

	except:

		# if no access to the values (wrong design of Sketch and Pad)
		showError(iObj, "setPad", "no access to the values")
		return -1

	return 0


# ###################################################################################################################
def setConstraints(iObj):

	try:

		# init variables
		isSet = 0
		vNames = ""
		vValues = ""
	
		# set reference point
		vCons = iObj.Profile[0].Constraints
	
		for c in vCons:
			if c.Name != "":
				
				# set Constraint Name
				vNames += str(c.Name) + ":"
	
				# assign values to the Fake Cube dimensions
				gFakeCube.Width = c.Value
				
				# get values as the correct dimensions
				vValues += str(gFakeCube.Width.getValueAs(gUnitC).Value) + ":"
	
				# non empty names, so object can be set
				isSet = 1
	
		if isSet == 1:
	
			# assign values to the Fake Cube dimensions
			gFakeCube.Length = iObj.Length.Value
				
			# get values as the correct dimensions
			vLength = str(gFakeCube.Length.getValueAs(gUnitC).Value)
	
			# set db for Constraints
			setDBConstraints(iObj, vLength, vNames, vValues)

	except:
		
		# if there is wrong structure
		showError(iObj, "setConstraints", "wrong structure")
		return -1

	return 0


# ###################################################################################################################
# Furniture parts selector - add objects to db only via this selector
# ###################################################################################################################


# ###################################################################################################################
def selectFurniturePart(iObj):

	# normal report
	if sLTF != "c":

		# support for Cube furniture part
		if iObj.isDerivedFrom("Part::Box"):
			setCube(iObj)
    
		# support for Pad furniture part
		if iObj.isDerivedFrom("PartDesign::Pad"):
			setPad(iObj)

	# custom report
	else:

		# support for Pad furniture part with constraints
		if iObj.isDerivedFrom("PartDesign::Pad"):
			setConstraints(iObj)
		
	# skip not supported furniture parts with no error
	# Sheet, Transformations will be handling later
	return 0	


# ###################################################################################################################
# Support for transformations of base furniture parts
# ###################################################################################################################


# ###################################################################################################################
def setPartMirroring(iObj):

	# support for Part :: Mirroring FreeCAD feature
	if iObj.isDerivedFrom("Part::Mirroring"):

		try:

			# set reference point to the furniture part
			key = iObj.Source

			# select and add furniture part
			selectFurniturePart(key)

		except:

			# if there is wrong structure
			showError(iObj, "setPartMirroring", "wrong structure")
			return -1
	
	return 0


# ###################################################################################################################
def setDraftArray(iObj):

	# support for Array FreeCAD feature
	if iObj.isDerivedFrom("Part::FeaturePython"):

		try:

			# set reference point to the furniture part
			key = iObj.Base

			if iObj.ArrayType == "polar":
				
				# without the base furniture part
				vArray = iObj.NumberPolar - 1
			else:
				
				# without the base furniture part
				vArray = (iObj.NumberX * iObj.NumberY * iObj.NumberZ) - 1

			# calculate the base furniture part
			k = 0
			
			while k < vArray:

				# select and add furniture part
				selectFurniturePart(key)
				k = k + 1
		
		except:
			
			# if there is wrong structure
			showError(iObj, "setDraftArray", "wrong structure")
			return -1
	
	return 0


# ###################################################################################################################
def setPartDesignMirrored(iObj):

	# support for Single Mirror FreeCAD feature
	if iObj.isDerivedFrom("PartDesign::Mirrored"):

		try:

			# skip single mirrors from MultiTransform with no error
			if len(iObj.Originals) != 0:

				# set reference point to the base furniture part
				key = iObj.Originals[0]

				# if object is Mirror this create new furniture part
				selectFurniturePart(key)
		
		except:
			
			# if there is wrong structure
			showError(iObj, "setPartDesignMirrored", "wrong structure")
			return -1
	
	return 0


# ###################################################################################################################
def setPartDesignMultiTransform(iObj):
	
	# support for MultiTransform FreeCAD feature
	if iObj.isDerivedFrom("PartDesign::MultiTransform"):

		try:
			
			# set number of transformations available    
			lenT = len(iObj.Transformations)
			k = 0

			# if this is MultiTransform, not single mirror
			if lenT > 0:
				
				# mirror makes 2 elements but each mirror in MultiTransform makes next mirror but using 
				# current transformed object, so this will raise the number of mirrors to the power, 
				# also you have to remove the base furniture part already added
				while k < (2 ** lenT) - 1:

					# set reference point to the base furniture part
					key = iObj.Originals[0]

					# if object is mirror this create new furniture part
					# Note: you cannot call setPartDesignMirrored here on this because 
					# it is transformation with empty array, there is no access
					# to the base furniture part
					selectFurniturePart(key)
					k = k + 1

		except:

			# if there is wrong structure
			showError(iObj, "setPartDesignMultiTransform", "wrong structure")
			return -1
	
	return 0


# ###################################################################################################################
# MAIN LOOP - calculate and set databases for supported objects
# ###################################################################################################################


# search all objects in document and set database for correct ones
for obj in gOBs:

	# if feature is on, just skip all hidden elements
	if sTVF == "on":
		if FreeCADGui.ActiveDocument.getObject(obj.Name).Visibility == False:
			continue

	# select and set furniture part
	selectFurniturePart(obj)

	# set transformations
	setPartMirroring(obj)
	setDraftArray(obj)
	setPartDesignMirrored(obj)
	setPartDesignMultiTransform(obj)

# remove existing fake Cube object before recompute
if gAD.getObject("gFakeCube"):
	gAD.removeObject("gFakeCube")


# ###################################################################################################################
# Spreadsheet - data init
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
	vLang9 = "Długość"

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
	vLang9 = "Length"
    

# create spreadsheet and prepere it for data
if gAD.getObject("toCut"):
	gAD.removeObject("toCut")

result = gAD.addObject("Spreadsheet::Sheet","toCut")

# init spreadsheet row access point
i = 1


# ###################################################################################################################
# Spreadsheet - main report - name
# ###################################################################################################################


if sLTF == "n":

	# add headers
	result.set("A1", vLang1)
	result.set("B1", vLang2)
	result.set("E1", vLang3)
	result.set("F1", vLang4)
	result.set("G1", vLang5)
	result.mergeCells("B1:D1")

	vCell = "A" + str(i) + ":G" + str(i)
	result.setBackground(vCell, gHeadCS)

	# go to next spreadsheet row
	i = i + 1

	# add values
	for key in dbDA.keys():

		a = key.split(":")

		result.set("A" + str(i), "'" + str(a[3]))
		result.set("B" + str(i), getUnit(a[1], "d"))
		result.set("C" + str(i), "'" + "x")
		result.set("D" + str(i), getUnit(a[2], "d"))
		result.set("E" + str(i), getUnit(a[0], "d"))
		result.set("F" + str(i), "'" + str(dbDQ[key]))
		result.set("G" + str(i), getUnit(dbDA[key], "area"))

		# go to next spreadsheet row
		i = i + 1

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
# Spreadsheet - main report - quantity
# ###################################################################################################################


if sLTF == "q":

	# add headers
	result.set("A1", vLang4)
	result.set("B1", vLang2)
	result.set("E1", vLang3)
	result.set("F1", vLang5)
	result.mergeCells("B1:D1")

	vCell = "A" + str(i) + ":G" + str(i)
	result.setBackground(vCell, gHeadCS)

	# go to next spreadsheet row
	i = i + 1
		
	# add values
	for key in dbDQ.keys():

		a = key.split(":")

		result.set("A" + str(i), "'" + str(dbDQ[key])+" x")
		result.set("B" + str(i), getUnit(a[1], "d"))
		result.set("C" + str(i), "x")
		result.set("D" + str(i), getUnit(a[2], "d"))
		result.set("E" + str(i), getUnit(a[0], "d"))
		result.set("F" + str(i), getUnit(dbDA[key], "area"))

		# go to next spreadsheet row
		i = i + 1

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
# Spreadsheet - main report - group
# ###################################################################################################################


if sLTF == "g":

	# add headers
	result.set("A1", vLang1)
	result.set("B1", vLang2)
	result.set("E1", vLang3)
	result.set("F1", vLang4)
	result.set("G1", vLang5)
	result.mergeCells("B1:D1")

	vCell = "A" + str(i) + ":G" + str(i)
	result.setBackground(vCell, gHeadCS)

	# go to next spreadsheet row
	i = i + 1

	# add values
	for key in dbDA.keys():

		a = key.split(":")

		result.set("A" + str(i), "'" + str(a[3]))
		result.set("B" + str(i), getUnit(a[1], "d"))
		result.set("C" + str(i), "'" + "x")
		result.set("D" + str(i), getUnit(a[2], "d"))
		result.set("E" + str(i), getUnit(a[0], "d"))
		result.set("F" + str(i), "'" + str(dbDQ[key]))
		result.set("G" + str(i), getUnit(dbDA[key], "area"))

		# go to next spreadsheet row
		i = i + 1

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
# Spreadsheet - thickness
# ###################################################################################################################


# skip if report for constraints (custom report)
if sLTF != "c":

	# add summary title for thickness
	vCell = "A" + str(i) + ":G" + str(i)
	result.mergeCells(vCell)
	result.set(vCell, vLang7)
	result.setStyle(vCell, "bold", "add")
	result.setAlignment(vCell, "left", "keep")
	result.setBackground(vCell, gHeadCS)

	# go to next spreadsheet row
	i = i + 1
	
	# for thickness	 (quantity)
	if sLTF == "q":
		for key in dbTQ.keys():

			result.set("A" + str(i), "'" + str(dbTQ[key])+" x")
			result.set("E" + str(i), getUnit(key, "d"))
			result.set("F" + str(i), getUnit(dbTA[key], "area"))
			result.setAlignment("A" + str(i), "right", "keep")
			result.setAlignment("E" + str(i), "right", "keep")
			result.setAlignment("F" + str(i), "right", "keep")

			# go to next spreadsheet row
			i = i + 1
	
	# for thickness	 (group & name)
	if sLTF == "g" or sLTF == "n":
		for key in dbTQ.keys():

			result.set("E" + str(i), getUnit(key, "d"))
			result.set("F" + str(i), "'" + str(dbTQ[key]))
			result.set("G" + str(i), getUnit(dbTA[key], "area"))
			result.setAlignment("E" + str(i), "right", "keep")
			result.setAlignment("F" + str(i), "right", "keep")
			result.setAlignment("G" + str(i), "right", "keep")

			# go to next spreadsheet row
			i = i + 1


# ###################################################################################################################
# Spreadsheet - edge
# ###################################################################################################################


# skip if report for constraints (custom report)
if sLTF != "c":

	# go to next spreadsheet row
	i = i + 1

	# add summary for edge size
	vCell = "A" + str(i) + ":B" + str(i)
	result.mergeCells(vCell)
	result.set(vCell, vLang8)
	result.setStyle(vCell, "bold", "add")
	result.setAlignment(vCell, "left", "keep")

	vCell = "C" + str(i) + ":E" + str(i)
	result.mergeCells(vCell)
	result.set(vCell, getUnit(dbE["size"], "edge"))
	result.setAlignment(vCell, "right", "keep")

	vCell = "A" + str(i) + ":E" + str(i)
	result.setBackground(vCell, gHeadCS)


# ###################################################################################################################
# Spreadsheet - main report - constraints (custom report)
# ###################################################################################################################


if sLTF == "c":
	
	# search objects for constraints (custom report)
	for o in dbCNO:

		# set key for db
		vKey = o.Label
		
		# set object header
		vCell = "A" + str(i)
		vStr = str(dbCNQ[vKey]) + " x "
		result.set(vCell, vStr)
		result.setAlignment(vCell, "right", "keep")
		result.setStyle(vCell, "bold", "add")
		result.setBackground(vCell, gHeadCS)

		vCell = "B" + str(i) + ":G" + str(i)
		vStr = str(vKey)
		result.set(vCell, vStr)
		result.mergeCells(vCell)	
		result.setAlignment(vCell, "left", "keep")
		result.setStyle(vCell, "bold", "add")
		result.setBackground(vCell, gHeadCS)

		# go to next spreadsheet row
		i = i + 1

		# set object length
		vCell = "A" + str(i)
		result.setBackground(vCell, (1,1,1))

		vCell = "B" + str(i) + ":F" + str(i)
		result.set(vCell, vLang9)
		result.mergeCells(vCell)	
		result.setAlignment(vCell, "left", "keep")
		result.setStyle(vCell, "bold", "add")
		result.setBackground(vCell, gHeadCW)

		vCell = "G" + str(i)
		vStr = getUnit(dbCNL[vKey], "d")
		result.set(vCell, vStr)
		result.setAlignment(vCell, "right", "keep")
		result.setStyle(vCell, "bold", "add")
		result.setBackground(vCell, gHeadCW)

		# create constraints lists
		keyN = dbCNN[vKey].split(":")
		keyV = dbCNV[vKey].split(":")

		# go to next spreadsheet row
		i = i + 1

		# set all constraints
		k = 0
		while k < len(keyN)-1: 
	
			# the first A column is empty for better look
			vCell = "A" + str(i)
			result.setBackground(vCell, (1,1,1))

			# set constraint name
			vCell = "B" + str(i) + ":F" + str(i)
			result.set(vCell, "'" + str(keyN[k]))
			result.mergeCells(vCell)
			result.setAlignment(vCell, "left", "keep")

			# set dimension
			vCell = "G" + str(i)
			result.set(vCell, getUnit(keyV[k], "d"))
			result.setAlignment(vCell, "right", "keep")

			# go to next spreadsheet row
			i = i + 1

			# go to next constraint
			k = k + 1
			
	# set cell width
	result.setColumnWidth("A", 60)
	result.setColumnWidth("B", 155)
	result.setColumnWidth("C", 120)
	result.setColumnWidth("D", 80)
	result.setColumnWidth("E", 100)
	result.setColumnWidth("F", 100)
	result.setColumnWidth("G", 100)


# ###################################################################################################################
# Spreadsheet main report - code link
# ###################################################################################################################


# add empty line separator
i = i + 3

# add link 
vCell = "A" + str(i) + ":G" + str(i)
result.mergeCells(vCell)
result.set(vCell, "Generated by FreeCAD macro: github.com/dprojects/getDimensions")
result.setAlignment(vCell, "left", "keep")
result.setBackground(vCell, gHeadCW)


# ###################################################################################################################
# Spreadsheet - final decoration
# ###################################################################################################################


# skip if report for constraints (custom report)
if sLTF != "c":

	# colors
	result.setForeground("A1:G" + str(i), (0,0,0))
	
	# fix for center header text in merged cells
	result.setAlignment("B1:B1", "center", "keep")
	result.setAlignment("C1:C1", "center", "keep")
	result.setAlignment("D1:D1", "center", "keep")
	
	# text header decoration
	result.setStyle("A1:G1", "bold", "add")

# reset settings for eco mode
if sRPQ == "eco":
	vCell = "A1" + ":G" + str(i)
	result.setBackground(vCell, (1,1,1))


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
gAD.getObject("Sheet").X = int(float(gAD.getObject("Template").Width) / 2)
gAD.getObject("Sheet").Y = int(float(gAD.getObject("Template").Height) / 2)

# try to set fonts
try:
	gAD.getObject("Sheet").Font = "DejaVu Sans"
except:
	gAD.getObject("Sheet").Font = "Arial"

gAD.getObject("Sheet").TextSize = 13

# set border line width
gAD.getObject("Sheet").LineWidth = 0.10

# fix FreeCAD bug
gAD.getObject("Sheet").CellEnd = "G" + str(i)


# ###################################################################################################################
# Reload to see changes
# ###################################################################################################################


gAD.recompute()

