# -*- coding: utf-8 -*-

# FreeCAD macro for woodworking
# Author: Darek L (aka dprojects)
# Version: 4.0
# Latest version: https://github.com/dprojects/getDimensions

import FreeCAD,Draft,Spreadsheet

# language translation (change this if there is no your language version available)
sLang1 = 'Name'
sLang2 = 'Dimensions (mm)'
sLang3 = 'Qty'
sLang4 = 'Surface (m²)'
sLang5 = 'Summary'
sLang6 = 'Length (mm)'

# create spreadsheet and prepere it for data
if FreeCAD.ActiveDocument.getObject("toCut"):
    FreeCAD.ActiveDocument.removeObject("toCut")

result = FreeCAD.ActiveDocument.addObject("Spreadsheet::Sheet","toCut")

result.mergeCells('B1:F1')

result.set( 'A1', sLang1 )
result.set( 'B1', sLang2 )
result.set( 'G1', sLang3 )
result.set( 'H1', sLang4 )

result.setForeground( 'A1:H1', (0,0,0) )
result.setBackground( 'A1:H1', (1,1,1) )
result.setStyle( 'A1:H1', 'bold', 'add')
result.setAlignment( 'A1:H1', 'top', 'keep' )
result.setAlignment( 'A1:H1', 'center', 'keep' )

# scan all objects and count chipboards (cubes)
objs = FreeCAD.ActiveDocument.Objects

quantity = dict()
sqmSum = dict()
lenSum = dict()

for obj in objs:

    # support for cube objects
    if obj.isDerivedFrom("Part::Box"):

        keyArr = [ str(obj.Length),
                   str(obj.Width),
                   str(obj.Height) ]
        keyArr.sort()
                # Second array to be sorted numericaly
        keyArr2 = [ int(str(obj.Length).replace(' mm', '')),
                    int(str(obj.Width).replace(' mm', '')),
                    int(str(obj.Height).replace(' mm', '')) ]
        keyArr2.sort()

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

        keyArr = [ str(obj.Base.Length),
                   str(obj.Base.Width),
                   str(obj.Base.Height) ]
        keyArr.sort()
        keyArr2 = [ int(str(obj.Base.Length).replace(' mm', '')),
                    int(str(obj.Base.Width).replace(' mm', '')),
                    int(str(obj.Base.Height).replace(' mm', '')) ]
        keyArr2.sort()

        key = "x".join(keyArr)
        if key in quantity:
            quantity[key] = quantity[key] + arrayQuantity
        else:
            quantity[key] = arrayQuantity

# check what we have...
sqm = 0
length = 0
i = 1

for obj in objs:

    if obj.isDerivedFrom("Part::Box"):

        keyArr = [ str(obj.Length),
                   str(obj.Width),
                   str(obj.Height) ]
        keyArr.sort()
        keyArr2 = [ int(str(obj.Length).replace(' mm', '')),
                    int(str(obj.Width).replace(' mm', '')),
                    int(str(obj.Height).replace(' mm', '')) ]
        keyArr2.sort()
        sizes = keyArr2

        key = "x".join(keyArr)
        if not key in quantity:
            continue

        i = i + 1

        # Surface (in m²) is defined by both higher dimensions (in mm)
        sqm = (quantity[key] * sizes[1]/1000 * sizes[2]/1000)
        # Length is the last dimension
        length = (quantity[key] * sizes[2])

        # ...and add to spreadsheet
        result.set( 'A'+str(i), str(obj.Label) )
        result.set( 'B'+str(i), str(sizes[0]) )
        result.set( 'C'+str(i), 'x' )
        result.set( 'D'+str(i), str(sizes[1]) )
        result.set( 'E'+str(i), 'x' )
        result.set( 'F'+str(i), str(sizes[2]) )
        result.set( 'G'+str(i), str(quantity[key]) )
        result.set( 'H'+str(i), str(sqm) )

        del quantity[key]

        # recalculate and add partial square meters
        key = str(sizes[0])
        if key in sqmSum:
            sqmSum[key] = sqmSum[key] + sqm
        else:
            sqmSum[key] = sqm

        # Lengths
        key = str(sizes[0])+'.'+str(sizes[1])
        if key in lenSum:
            lenSum[key] = lenSum[key] + length
        else:
            lenSum[key] = length

sqmSumIdx = sorted(sqmSum, key=float)
lenSumIdx = sorted(lenSum, key=float)

# Summary Surfaces
i = i + 1
i1 = i + 1
for idx in sqmSumIdx:
    i = i + 1
    result.set( 'B'+str(i), str(idx) )
    result.set( 'H'+str(i), str(sqmSum[idx]) )
    i2 = i

result.mergeCells('A'+str(i1)+':A'+str(i2))
result.set( 'A'+str(i1), sLang5 + '\n' + sLang4 )

# Summary Lengths
i = i + 1
i1 = i + 1
for idx in lenSumIdx:
    i = i + 1
    result.set( 'B'+str(i), str(idx.replace('.', ' x ')) )
    result.set( 'F'+str(i), str(lenSum[idx]) )
    i2 = i

result.mergeCells('A'+str(i1)+':A'+str(i2))
result.set( 'A'+str(i1), sLang5 + '\n' + sLang6 )

# final decoration
result.setForeground( 'A2:H'+str(i), (0,0,0) )
result.setBackground( 'A2:H'+str(i), (1,1,1) )

result.setStyle( 'A2:A'+str(i), 'bold', 'add')

result.setColumnWidth( 'A', 160 )
result.setColumnWidth( 'B', 80 )
result.setColumnWidth( 'C', 20 )
result.setColumnWidth( 'D', 80 )
result.setColumnWidth( 'E', 20 )
result.setColumnWidth( 'F', 80 )
result.setColumnWidth( 'G', 60 )
result.setColumnWidth( 'H', 120 )

result.setAlignment( 'B2:B'+str(i), 'right', 'keep' )
result.setAlignment( 'C2:C'+str(i), 'center', 'keep' )
result.setAlignment( 'D2:D'+str(i), 'right', 'keep' )
result.setAlignment( 'E2:E'+str(i), 'center', 'keep' )
result.setAlignment( 'F2:F'+str(i), 'right', 'keep' )
result.setAlignment( 'G2:G'+str(i), 'right', 'keep' )
result.setAlignment( 'H2:H'+str(i), 'right', 'keep' )

# refresh document
App.ActiveDocument.recompute()
