# -*- coding: utf-8 -*-
import FreeCAD,Draft,Spreadsheet

if FreeCAD.ActiveDocument.getObject("toCut"):
	FreeCAD.ActiveDocument.removeObject("toCut")

result = FreeCAD.ActiveDocument.addObject("Spreadsheet::Sheet","toCut")

result.mergeCells('B1:D1')

result.set( 'A1', 'Name' )
result.set( 'B1', 'Dimensions' )
result.set( 'E1', 'Thickness' )
result.set( 'F1', 'Quantity' )
result.set( 'G1', 'Square meters' )

result.setForeground( 'A1:G1', (0,0,0) )
result.setBackground( 'A1:G1', (1,1,1) )
result.setStyle( 'A1:G1', 'bold', 'add')
result.setAlignment( 'A1:G1', 'top', 'keep' )
result.setAlignment( 'A1:G1', 'center', 'keep' )

objs = FreeCAD.ActiveDocument.Objects

quantity = dict()
sqmSum = dict()

for obj in objs:
	if obj.isDerivedFrom("Part::Box"):
		
		keyArr = [ str(obj.Length), str(obj.Width), str(obj.Height) ]
		keyArr.sort()
		key = "x".join(keyArr)
		if key in quantity:
			quantity[key] = quantity[key] + 1
		else:
			quantity[key] = 1

sqm = 0
i = 1

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
		
		sqm = (quantity[key] * size1 * size2 / 1000000).Value

		result.set( 'A'+str(i), str(obj.Label) )
		result.set( 'B'+str(i), str(size1) )
		result.set( 'C'+str(i), 'x' )
		result.set( 'D'+str(i), str(size2) )
		result.set( 'E'+str(i), str(thick) )
		result.set( 'F'+str(i), str(quantity[key]) )
		result.set( 'G'+str(i), str(sqm) )

		del quantity[key]
		key = str(thick)

		if key in sqmSum:
			sqmSum[key] = sqmSum[key] + sqm
		else:
			sqmSum[key] = sqm

i = i + 1

for key in sqmSum.keys():
	i = i + 1	
	result.set( 'A'+str(i), 'Summary' )
	result.set( 'E'+str(i), str(key) )
	result.set( 'G'+str(i), str(sqmSum[key]) )

result.setForeground( 'A2:G'+str(i), (0,0,0) )
result.setBackground( 'A2:G'+str(i), (1,1,1) )
		
result.setStyle( 'A2:A'+str(i), 'bold', 'add')

result.setColumnWidth( 'A', 135 )
result.setColumnWidth( 'B', 80 )
result.setColumnWidth( 'C', 40 )
result.setColumnWidth( 'D', 80 )
result.setColumnWidth( 'E', 100 )
result.setColumnWidth( 'F', 100 )
result.setColumnWidth( 'G', 160 )

result.setAlignment( 'B2:B'+str(i), 'right', 'keep' )
result.setAlignment( 'C2:C'+str(i), 'right', 'keep' )
result.setAlignment( 'D2:D'+str(i), 'right', 'keep' )
result.setAlignment( 'F2:F'+str(i), 'center', 'keep' )
result.setAlignment( 'G2:G'+str(i), 'right', 'keep' )

App.ActiveDocument.recompute()
