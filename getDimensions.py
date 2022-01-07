# -*- coding: utf-8 -*-

# FreeCAD macro for woodworking
# Author: Darek L (aka dprojects)
# Version: 2022.01.07
# Latest version: https://github.com/dprojects/getDimensions

import FreeCAD, Draft, Spreadsheet
from PySide import QtGui, QtCore

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

# Qt GUI
# "yes" - to show
# "no" - to hide
sQT = "yes"


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

# language support
gLang1 = ""
gLang2 = ""
gLang3 = ""
gLang4 = ""
gLang5 = ""
gLang6 = ""
gLang7 = ""
gLang8 = ""
gLang9 = ""

# spreadsheet result
gSheet = gAD

# spreadsheet result
gSheetRow = 1

# for cancel buttons assign "no"
gExecute = "yes"


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
# Support for Qt GUI
# ###################################################################################################################


# ###################################################################################################################
def showQtGUI():

	global gExecute

	# ############################################################################
	# Qt Main Class
	# ############################################################################
	
	class QtMainClass(QtGui.QDialog):

		def __init__(self):
			super(QtMainClass, self).__init__()
			self.initUI()

		def initUI(self):

			# window
			self.result = userCancelled
			self.setGeometry(250, 200, 500, 500)
			self.setWindowTitle("getDimensions - settings")
			self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)

			# set line start point
			vLine = 10
			vLineNextRow = 20
			vLineOffset = 60

			# ############################################################################
			# languages
			# ############################################################################

			# label
			self.LangL = QtGui.QLabel("Report language:", self)
			self.LangL.move(10, vLine + 3)
			
			# options
			self.LangList = ("pl", "en")
			self.LangO = QtGui.QComboBox(self)
			self.LangO.addItems(self.LangList)
			self.LangO.setCurrentIndex(self.LangList.index("en"))
			self.LangO.activated[str].connect(self.setLang)
			self.LangO.move(10, vLine + vLineNextRow)

			# info screen
			self.LangIS = QtGui.QLabel("English language", self)
			self.LangIS.move(70, vLine + vLineNextRow + 3)

			# ############################################################################
			# report print quality
			# ############################################################################

			# set line separator
			vLine = vLine + vLineOffset

			# label
			self.rpqL = QtGui.QLabel("Report quality:", self)
			self.rpqL.move(10, vLine + 3)
			
			# options
			self.rpqList = ("eco", "hq")
			self.rpqO = QtGui.QComboBox(self)
			self.rpqO.addItems(self.rpqList)
			self.rpqO.setCurrentIndex(self.rpqList.index("hq"))
			self.rpqO.activated[str].connect(self.setQuality)
			self.rpqO.move(10, vLine + vLineNextRow)

			# info screen
			self.rpqIS = QtGui.QLabel("high quality mode (good for pdf)", self)
			self.rpqIS.move(70, vLine + vLineNextRow + 3)

			# ############################################################################
			# visibility (Toggle Visibility Feature)
			# ############################################################################

			# set line separator
			vLine = vLine + vLineOffset

			# label
			self.visibilityL = QtGui.QLabel("Visibility (Toggle Visibility Feature):", self)
			self.visibilityL.move(10, vLine + 3)
			
			# options
			self.visibilityList = ("on", "edge", "off")
			self.visibilityO = QtGui.QComboBox(self)
			self.visibilityO.addItems(self.visibilityList)
			self.visibilityO.setCurrentIndex(self.visibilityList.index("edge"))
			self.visibilityO.activated[str].connect(self.setVisibility)
			self.visibilityO.move(10, vLine + vLineNextRow)

			# info screen
			self.visibilityIS = QtGui.QLabel("show all hidden objects and groups but not add to the edge size", self)
			self.visibilityIS.move(80, vLine + vLineNextRow + 3)
			
			# ############################################################################
			# units for dimensions
			# ############################################################################

			# set line separator
			vLine = vLine + vLineOffset

			# label
			self.ufdL = QtGui.QLabel("Units for dimensions:", self)
			self.ufdL.move(10, vLine + 3)
			
			# options
			self.ufdList = ("mm", "m", "in")
			self.ufdO = QtGui.QComboBox(self)
			self.ufdO.addItems(self.ufdList)
			self.ufdO.setCurrentIndex(self.ufdList.index("mm"))
			self.ufdO.activated[str].connect(self.setDFO)
			self.ufdO.move(10, vLine + vLineNextRow)

			# info screen
			self.ufdIS = QtGui.QLabel("millimeter", self)
			self.ufdIS.move(70, vLine + vLineNextRow + 3)

			# ############################################################################
			# report customization (Label Type Feature)
			# ############################################################################

			# set line separator
			vLine = vLine + vLineOffset

			# label
			self.rcL = QtGui.QLabel("Report customization (sLTF):", self)
			self.rcL.move(10, vLine + 3)
			
			# options
			self.rcList = ("n", "g", "q", "c")
			self.rcO = QtGui.QComboBox(self)
			self.rcO.addItems(self.rcList)
			self.rcO.setCurrentIndex(self.rcList.index("q"))
			self.rcO.activated[str].connect(self.setRC)
			self.rcO.move(10, vLine + vLineNextRow)

			# info screen
			self.rcIS = QtGui.QLabel("automatic by quantity (dimensions)                                     ", self)
			self.rcIS.move(70, vLine + vLineNextRow + 3)

			# ############################################################################
			# units for area
			# ############################################################################

			# set line separator
			vLine = vLine + vLineOffset

			# label
			self.ufaL = QtGui.QLabel("Units for area:", self)
			self.ufaL.move(10, vLine + 3)
			
			# options
			self.ufaList = ("mm", "m", "in")
			self.ufaO = QtGui.QComboBox(self)
			self.ufaO.addItems(self.ufaList)
			self.ufaO.setCurrentIndex(self.ufaList.index("m"))
			self.ufaO.activated[str].connect(self.setUFA)
			self.ufaO.move(10, vLine + vLineNextRow)

			# info screen
			self.ufaIS = QtGui.QLabel("square meter (m2)                                     ", self)
			self.ufaIS.move(70, vLine + vLineNextRow + 3)

			# ############################################################################
			# units for edge size
			# ############################################################################

			# set line separator
			vLine = vLine + vLineOffset

			# label
			self.ufsL = QtGui.QLabel("Units for edge size:", self)
			self.ufsL.move(10, vLine + 3)
			
			# options
			self.ufsList = ("mm", "m", "in")
			self.ufsO = QtGui.QComboBox(self)
			self.ufsO.addItems(self.ufsList)
			self.ufsO.setCurrentIndex(self.ufsList.index("m"))
			self.ufsO.activated[str].connect(self.setUFS)
			self.ufsO.move(10, vLine + vLineNextRow)

			# info screen
			self.ufsIS = QtGui.QLabel("meter                        ", self)
			self.ufsIS.move(70, vLine + vLineNextRow + 3)

			# ############################################################################
			# buttons
			# ############################################################################

			# button - cancel
			cancelButton = QtGui.QPushButton('Cancel', self)
			cancelButton.clicked.connect(self.onCancel)
			cancelButton.setAutoDefault(True)
			cancelButton.move(120, 450)
			
			# button - ok
			okButton = QtGui.QPushButton('OK', self)
			okButton.clicked.connect(self.onOk)
			okButton.move(300, 450)

			# ############################################################################
			# show
			# ############################################################################

			self.show()

		# ############################################################################
		# actions
		# ############################################################################

		def setLang(self, selectedText):
			global sLang

			if selectedText == "pl":
				sLang = "pl"
				self.LangIS.setText("Polish language")
			if selectedText == "en":
				sLang = "en"
				self.LangIS.setText("English language")

		def setQuality(self, selectedText):
			global sRPQ

			if selectedText == "hq":
				sRPQ = "hq"
				self.rpqIS.setText("high quality mode (good for pdf)")
			if selectedText == "eco":
				sRPQ = "eco"
				self.rpqIS.setText("low ink mode (good for printing)")

		def setVisibility(self, selectedText):
			global sTVF

			if selectedText == "on":
				sTVF = "on"
				self.visibilityIS.setText("skip all hidden objects and groups")
			if selectedText == "edge":
				sTVF = "edge"
				self.visibilityIS.setText("show all hidden objects and groups but not add to the edge size")
			if selectedText == "off":
				sTVF = "off"
				self.visibilityIS.setText("show and calculate all objects and groups")

		def setDFO(self, selectedText):
			global sUnitsMetric

			if selectedText == "mm":
				sUnitsMetric = "mm"
				self.ufdIS.setText("millimeter")
			if selectedText == "m":
				sUnitsMetric = "m"
				self.ufdIS.setText("meter")
			if selectedText == "in":
				sUnitsMetric = "in"
				self.ufdIS.setText("inch")

		def setRC(self, selectedText):
			global sLTF

			if selectedText == "n":
				sLTF = "n"
				self.rcIS.setText("automatic by objects names (listing)")
			if selectedText == "g":
				sLTF = "g"
				self.rcIS.setText("automatic by groups (folder names)")
			if selectedText == "q":
				sLTF = "q"
				self.rcIS.setText("automatic by quantity (dimensions)")
			if selectedText == "c":
				sLTF = "c"
				self.rcIS.setText("custom by constraints names (totally custom report)")
				
		def setUFA(self, selectedText):
			global sUnitsArea

			if selectedText == "mm":
				sUnitsArea = "mm"
				self.ufaIS.setText("square millimeter (mm2)")
			if selectedText == "m":
				sUnitsArea = "m"
				self.ufaIS.setText("square meter (m2)")
			if selectedText == "in":
				sUnitsArea = "in"
				self.ufaIS.setText("square inch (inch2)")

		def setUFS(self, selectedText):
			global sUnitsEdge

			if selectedText == "mm":
				sUnitsEdge = "mm"
				self.ufsIS.setText("millimeter")
			if selectedText == "m":
				sUnitsEdge = "m"
				self.ufsIS.setText("meter")
			if selectedText == "in":
				sUnitsEdge = "in"
				self.ufsIS.setText("inch")

		def onCancel(self):
			self.result = userCancelled
			self.close()
		def onOk(self):
			self.result = userOK
			self.close()
	
	# ############################################################################
	# final settings
	# ############################################################################

	userCancelled = "Cancelled"
	userOK = "OK"
	
	form = QtMainClass()
	form.exec_()
	
	if form.result == userCancelled:
		gExecute = "no"
		pass
	
	if form.result == userOK:
		gExecute = "yes"


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
# Scan objects (MAIN CALCULATIONS LOOP)
# ###################################################################################################################


# ###################################################################################################################
def scanObjects():

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


# ###################################################################################################################
# View types (regiester each view at view selector)
# ###################################################################################################################


# ###################################################################################################################
def initView():

	global gLang1
	global gLang2
	global gLang3
	global gLang4
	global gLang5
	global gLang6
	global gLang7
	global gLang8
	global gLang9
	
	global gSheet
	
	# Polish language
	if sLang  == "pl":

		gLang1 = "Element"
		gLang2 = "Wymiary"
		gLang3 = "Grubość"
		gLang4 = "Sztuki"
		
		if sUnitsArea == "mm":
			gLang5 = "Milimetry kwadratowe"
		if sUnitsArea == "m":
			gLang5 = "Metry kwadratowe"
		if sUnitsArea == "in":
			gLang5 = "Cale kwadratowe"        

		gLang6 = "Podsumowanie dla koloru elementu"
		gLang7 = "Podsumowanie dla grubości elementu"
		gLang8 = "Długość obrzeża"
		gLang9 = "Długość"

	# English language
	else:

		gLang1 = "Name"
		gLang2 = "Dimensions"
		gLang3 = "Thickness"
		gLang4 = "Quantity"

		if sUnitsArea == "mm":
			gLang5 = "Square millimeters"
		if sUnitsArea == "m":
			gLang5 = "Square meters"
		if sUnitsArea == "in":
			gLang5 = "Square inches"        

		gLang6 = "Summary by colors"
		gLang7 = "Summary by thickness"
		gLang8 = "Edge size"
		gLang9 = "Length"
		

	# remove spreadsheet if exists
	if gAD.getObject("toCut"):
		gAD.removeObject("toCut")

	# create empty spreadsheet
	gSheet = gAD.addObject("Spreadsheet::Sheet","toCut")


# ###################################################################################################################
def setViewN():

	global gSheet
	global gSheetRow

	# add headers
	gSheet.set("A1", gLang1)
	gSheet.set("B1", gLang2)
	gSheet.set("E1", gLang3)
	gSheet.set("F1", gLang4)
	gSheet.set("G1", gLang5)
	gSheet.mergeCells("B1:D1")

	vCell = "A" + str(gSheetRow) + ":G" + str(gSheetRow)
	gSheet.setBackground(vCell, gHeadCS)

	# go to next spreadsheet row
	gSheetRow = gSheetRow + 1

	# add values
	for key in dbDA.keys():

		a = key.split(":")

		gSheet.set("A" + str(gSheetRow), "'" + str(a[3]))
		gSheet.set("B" + str(gSheetRow), getUnit(a[1], "d"))
		gSheet.set("C" + str(gSheetRow), "'" + "x")
		gSheet.set("D" + str(gSheetRow), getUnit(a[2], "d"))
		gSheet.set("E" + str(gSheetRow), getUnit(a[0], "d"))
		gSheet.set("F" + str(gSheetRow), "'" + str(dbDQ[key]))
		gSheet.set("G" + str(gSheetRow), getUnit(dbDA[key], "area"))

		# go to next spreadsheet row
		gSheetRow = gSheetRow + 1

	# cell sizes
	gSheet.setColumnWidth("A", 135)
	gSheet.setColumnWidth("B", 80)
	gSheet.setColumnWidth("C", 40)
	gSheet.setColumnWidth("D", 80)
	gSheet.setColumnWidth("E", 100)
	gSheet.setColumnWidth("F", 100)
	gSheet.setColumnWidth("G", 180)

	# alignment
	gSheet.setAlignment("A1:A" + str(gSheetRow), "left", "keep")
	gSheet.setAlignment("B1:B" + str(gSheetRow), "right", "keep")
	gSheet.setAlignment("C1:C" + str(gSheetRow), "center", "keep")
	gSheet.setAlignment("D1:D" + str(gSheetRow), "right", "keep")
	gSheet.setAlignment("E1:E" + str(gSheetRow), "right", "keep")
	gSheet.setAlignment("F1:F" + str(gSheetRow), "right", "keep")
	gSheet.setAlignment("G1:G" + str(gSheetRow), "right", "keep")


# ###################################################################################################################
def setViewQ():

	global gSheet
	global gSheetRow

	# add headers
	gSheet.set("A1", gLang4)
	gSheet.set("B1", gLang2)
	gSheet.set("E1", gLang3)
	gSheet.set("F1", gLang5)
	gSheet.mergeCells("B1:D1")

	vCell = "A" + str(gSheetRow) + ":G" + str(gSheetRow)
	gSheet.setBackground(vCell, gHeadCS)

	# go to next spreadsheet row
	gSheetRow = gSheetRow + 1
		
	# add values
	for key in dbDQ.keys():

		a = key.split(":")

		gSheet.set("A" + str(gSheetRow), "'" + str(dbDQ[key])+" x")
		gSheet.set("B" + str(gSheetRow), getUnit(a[1], "d"))
		gSheet.set("C" + str(gSheetRow), "x")
		gSheet.set("D" + str(gSheetRow), getUnit(a[2], "d"))
		gSheet.set("E" + str(gSheetRow), getUnit(a[0], "d"))
		gSheet.set("F" + str(gSheetRow), getUnit(dbDA[key], "area"))

		# go to next spreadsheet row
		gSheetRow = gSheetRow + 1

	# cell sizes
	gSheet.setColumnWidth("A", 80)
	gSheet.setColumnWidth("B", 80)
	gSheet.setColumnWidth("C", 20)
	gSheet.setColumnWidth("D", 80)
	gSheet.setColumnWidth("E", 100)
	gSheet.setColumnWidth("F", 180)

	# alignment
	gSheet.setAlignment("A1:A" + str(gSheetRow), "right", "keep")
	gSheet.setAlignment("B1:B" + str(gSheetRow), "right", "keep")
	gSheet.setAlignment("C1:C" + str(gSheetRow), "center", "keep")
	gSheet.setAlignment("D1:D" + str(gSheetRow), "right", "keep")
	gSheet.setAlignment("E1:E" + str(gSheetRow), "right", "keep")
	gSheet.setAlignment("F1:F" + str(gSheetRow), "right", "keep")


# ###################################################################################################################
def setViewG():

	global gSheet
	global gSheetRow

	# add headers
	gSheet.set("A1", gLang1)
	gSheet.set("B1", gLang2)
	gSheet.set("E1", gLang3)
	gSheet.set("F1", gLang4)
	gSheet.set("G1", gLang5)
	gSheet.mergeCells("B1:D1")

	vCell = "A" + str(gSheetRow) + ":G" + str(gSheetRow)
	gSheet.setBackground(vCell, gHeadCS)

	# go to next spreadsheet row
	gSheetRow = gSheetRow + 1

	# add values
	for key in dbDA.keys():

		a = key.split(":")

		gSheet.set("A" + str(gSheetRow), "'" + str(a[3]))
		gSheet.set("B" + str(gSheetRow), getUnit(a[1], "d"))
		gSheet.set("C" + str(gSheetRow), "'" + "x")
		gSheet.set("D" + str(gSheetRow), getUnit(a[2], "d"))
		gSheet.set("E" + str(gSheetRow), getUnit(a[0], "d"))
		gSheet.set("F" + str(gSheetRow), "'" + str(dbDQ[key]))
		gSheet.set("G" + str(gSheetRow), getUnit(dbDA[key], "area"))

		# go to next spreadsheet row
		gSheetRow = gSheetRow + 1

	# cell sizes
	gSheet.setColumnWidth("A", 135)
	gSheet.setColumnWidth("B", 80)
	gSheet.setColumnWidth("C", 40)
	gSheet.setColumnWidth("D", 80)
	gSheet.setColumnWidth("E", 100)
	gSheet.setColumnWidth("F", 100)
	gSheet.setColumnWidth("G", 180)

	# alignment
	gSheet.setAlignment("A1:A" + str(gSheetRow), "left", "keep")
	gSheet.setAlignment("B1:B" + str(gSheetRow), "right", "keep")
	gSheet.setAlignment("C1:C" + str(gSheetRow), "center", "keep")
	gSheet.setAlignment("D1:D" + str(gSheetRow), "right", "keep")
	gSheet.setAlignment("E1:E" + str(gSheetRow), "right", "keep")
	gSheet.setAlignment("F1:F" + str(gSheetRow), "right", "keep")
	gSheet.setAlignment("G1:G" + str(gSheetRow), "right", "keep")


# ###################################################################################################################
def setViewC():

	global gSheet
	global gSheetRow

	# search objects for constraints (custom report)
	for o in dbCNO:

		# set key for db
		vKey = o.Label
		
		# set object header
		vCell = "A" + str(gSheetRow)
		vStr = str(dbCNQ[vKey]) + " x "
		gSheet.set(vCell, vStr)
		gSheet.setAlignment(vCell, "right", "keep")
		gSheet.setStyle(vCell, "bold", "add")
		gSheet.setBackground(vCell, gHeadCS)

		vCell = "B" + str(gSheetRow) + ":G" + str(gSheetRow)
		vStr = str(vKey)
		gSheet.set(vCell, vStr)
		gSheet.mergeCells(vCell)	
		gSheet.setAlignment(vCell, "left", "keep")
		gSheet.setStyle(vCell, "bold", "add")
		gSheet.setBackground(vCell, gHeadCS)

		# go to next spreadsheet row
		gSheetRow = gSheetRow + 1

		# set object length
		vCell = "A" + str(gSheetRow)
		gSheet.setBackground(vCell, (1,1,1))

		vCell = "B" + str(gSheetRow) + ":F" + str(gSheetRow)
		gSheet.set(vCell, gLang9)
		gSheet.mergeCells(vCell)	
		gSheet.setAlignment(vCell, "left", "keep")
		gSheet.setStyle(vCell, "bold", "add")
		gSheet.setBackground(vCell, gHeadCW)

		vCell = "G" + str(gSheetRow)
		vStr = getUnit(dbCNL[vKey], "d")
		gSheet.set(vCell, vStr)
		gSheet.setAlignment(vCell, "right", "keep")
		gSheet.setStyle(vCell, "bold", "add")
		gSheet.setBackground(vCell, gHeadCW)

		# create constraints lists
		keyN = dbCNN[vKey].split(":")
		keyV = dbCNV[vKey].split(":")

		# go to next spreadsheet row
		gSheetRow = gSheetRow + 1

		# set all constraints
		k = 0
		while k < len(keyN)-1: 
	
			# the first A column is empty for better look
			vCell = "A" + str(gSheetRow)
			gSheet.setBackground(vCell, (1,1,1))

			# set constraint name
			vCell = "B" + str(gSheetRow) + ":F" + str(gSheetRow)
			gSheet.set(vCell, "'" + str(keyN[k]))
			gSheet.mergeCells(vCell)
			gSheet.setAlignment(vCell, "left", "keep")

			# set dimension
			vCell = "G" + str(gSheetRow)
			gSheet.set(vCell, getUnit(keyV[k], "d"))
			gSheet.setAlignment(vCell, "right", "keep")

			# go to next spreadsheet row
			gSheetRow = gSheetRow + 1

			# go to next constraint
			k = k + 1
			
	# set cell width
	gSheet.setColumnWidth("A", 60)
	gSheet.setColumnWidth("B", 155)
	gSheet.setColumnWidth("C", 120)
	gSheet.setColumnWidth("D", 80)
	gSheet.setColumnWidth("E", 100)
	gSheet.setColumnWidth("F", 100)
	gSheet.setColumnWidth("G", 100)


# ###################################################################################################################
def setViewThickness():

	global gSheet
	global gSheetRow

	# add summary title for thickness
	vCell = "A" + str(gSheetRow) + ":G" + str(gSheetRow)
	gSheet.mergeCells(vCell)
	gSheet.set(vCell, gLang7)
	gSheet.setStyle(vCell, "bold", "add")
	gSheet.setAlignment(vCell, "left", "keep")
	gSheet.setBackground(vCell, gHeadCS)

	# go to next spreadsheet row
	gSheetRow = gSheetRow + 1
	
	# for thickness	 (quantity)
	if sLTF == "q":
		for key in dbTQ.keys():

			gSheet.set("A" + str(gSheetRow), "'" + str(dbTQ[key])+" x")
			gSheet.set("E" + str(gSheetRow), getUnit(key, "d"))
			gSheet.set("F" + str(gSheetRow), getUnit(dbTA[key], "area"))
			gSheet.setAlignment("A" + str(gSheetRow), "right", "keep")
			gSheet.setAlignment("E" + str(gSheetRow), "right", "keep")
			gSheet.setAlignment("F" + str(gSheetRow), "right", "keep")

			# go to next spreadsheet row
			gSheetRow = gSheetRow + 1
	
	# for thickness	 (group & name)
	if sLTF == "g" or sLTF == "n":
		for key in dbTQ.keys():

			gSheet.set("E" + str(gSheetRow), getUnit(key, "d"))
			gSheet.set("F" + str(gSheetRow), "'" + str(dbTQ[key]))
			gSheet.set("G" + str(gSheetRow), getUnit(dbTA[key], "area"))
			gSheet.setAlignment("E" + str(gSheetRow), "right", "keep")
			gSheet.setAlignment("F" + str(gSheetRow), "right", "keep")
			gSheet.setAlignment("G" + str(gSheetRow), "right", "keep")

			# go to next spreadsheet row
			gSheetRow = gSheetRow + 1


# ###################################################################################################################
def setViewEdge():

	global gSheet
	global gSheetRow

	# go to next spreadsheet row
	gSheetRow = gSheetRow + 1

	# add summary for edge size
	vCell = "A" + str(gSheetRow) + ":B" + str(gSheetRow)
	gSheet.mergeCells(vCell)
	gSheet.set(vCell, gLang8)
	gSheet.setStyle(vCell, "bold", "add")
	gSheet.setAlignment(vCell, "left", "keep")

	vCell = "C" + str(gSheetRow) + ":E" + str(gSheetRow)
	gSheet.mergeCells(vCell)
	gSheet.set(vCell, getUnit(dbE["size"], "edge"))
	gSheet.setAlignment(vCell, "right", "keep")

	vCell = "A" + str(gSheetRow) + ":E" + str(gSheetRow)
	gSheet.setBackground(vCell, gHeadCS)


# ###################################################################################################################
def finalViewSettings():

	global gSheet
	global gSheetRow
	
	# colors
	gSheet.setForeground("A1:G" + str(gSheetRow), (0,0,0))
	
	# fix for center header text in merged cells
	gSheet.setAlignment("B1:B1", "center", "keep")
	gSheet.setAlignment("C1:C1", "center", "keep")
	gSheet.setAlignment("D1:D1", "center", "keep")
	
	# text header decoration
	gSheet.setStyle("A1:G1", "bold", "add")


# ###################################################################################################################
def codeLink():

	global gSheet
	global gSheetRow

	# add empty line separator
	gSheetRow = gSheetRow + 3

	# add link 
	vCell = "A" + str(gSheetRow) + ":G" + str(gSheetRow)
	gSheet.mergeCells(vCell)
	gSheet.set(vCell, "Generated by FreeCAD macro: github.com/dprojects/getDimensions")
	gSheet.setAlignment(vCell, "left", "keep")
	gSheet.setBackground(vCell, gHeadCW)


# ###################################################################################################################
# View selector
# ###################################################################################################################


# ###################################################################################################################
def selectView():

	global gSheet
	global gSheetRow

	initView()

	# main report - name
	if sLTF == "n":
		setViewN()
		setViewThickness()
		setViewEdge()
		finalViewSettings()
		
	# main report - quantity
	if sLTF == "q":
		setViewQ()
		setViewThickness()
		setViewEdge()
		finalViewSettings()
		
	# main report - group
	if sLTF == "g":
		setViewG()
		setViewThickness()
		setViewEdge()
		finalViewSettings()
		
	# main report - constraints (custom report)
	if sLTF == "c":
		setViewC()
		
	codeLink()

		# reset settings for eco mode
	if sRPQ == "eco":
		vCell = "A1" + ":G" + str(gSheetRow)
		gSheet.setBackground(vCell, (1,1,1))


# ###################################################################################################################
# TechDraw part
# ###################################################################################################################


# ###################################################################################################################
def setTechDraw():

	global gAD
	global gSheet
	global gSheetRow

	# add empty line at the end of spreadsheet to fix merged cells at TechDraw page
	gSheetRow = gSheetRow + 1

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
	gAD.getObject("Sheet").CellEnd = "G" + str(gSheetRow)


# ###################################################################################################################
# MAIN
# ###################################################################################################################


# show Qt GUI
if sQT == "yes":
	showQtGUI()

# if Qt GUI ok button
if gExecute == "yes":
	
	# remove existing Fake Cube object if exists (auto clean after error)
	if gAD.getObject("gFakeCube"):
		gAD.removeObject("gFakeCube")

	# create Fake Cube but not call recompute
	gFakeCube = gAD.addObject("Part::Box", "gFakeCube")

	# main loop for calculations
	scanObjects()

	# remove existing fake Cube object before recompute
	if gAD.getObject("gFakeCube"):
		gAD.removeObject("gFakeCube")

	# select and set view
	selectView()

	# set TechDraw page
	setTechDraw()

	# reload to see changes
	gAD.recompute()


# ###################################################################################################################

