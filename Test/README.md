# Table of Contents

1. [Test001_features](#test001_features)

## Test001_features

This demo shows all the stable features supported by the macro. Also, I use this demo for testing macro purposes.

![Test001](https://raw.githubusercontent.com/dprojects/getDimensions/master/Test/Screenshots/Test001/001.png)

**Tests passed:** If the final report looks like below, it is highly possible that all features are working fine and there is no broken functionality. Make sure You have the latest version of FreeCAD (it was tested at FreeCAD 0.19.3 AppImage under Ubuntu).

* `sLTF` variable set to `c`:

	![Test001](https://raw.githubusercontent.com/dprojects/getDimensions/master/Test/Screenshots/Test001/002.png)

* `sLTF` variable set to `q`:

	![Test001](https://raw.githubusercontent.com/dprojects/getDimensions/master/Test/Screenshots/Test001/003.png)

* `sLTF` variable set to `g`:

	![Test001](https://raw.githubusercontent.com/dprojects/getDimensions/master/Test/Screenshots/Test001/003.png)

* `sLTF` variable set to `n`:

	|   |   |   |   |   |   |   |
	|:--|--:|:-:|--:|--:|--:|--:|
	|   Name|   Dimensions|   |   |   Thickness|   Quantity|   Square meters   |
	|   Back HDF|   200 mm|   x|   300 mm|   3 mm|   1|   0.06   |
	|   Black Front|   200 mm|   x|   300 mm|   18 mm|   1|   0.06   |
	|   Side 1|   200 mm|   x|   300 mm|   18 mm|   1|   0.06   |
	|   Side 2|   200 mm|   x|   300 mm|   18 mm|   1|   0.06   |
	|   Top 1|   200 mm|   x|   300 mm|   18 mm|   1|   0.06   |
	|   Foot 1|   80 mm|   x|   700 mm|   80 mm|   1|   0.056   |
	|   Foot 2|   80 mm|   x|   700 mm|   80 mm|   1|   0.056   |
	|   NoParent 200|   200 mm|   x|   300 mm|   18 mm|   1|   0.06   |
	|   NoGrand 100|   100 mm|   x|   300 mm|   18 mm|   1|   0.03   |
	|   Small Cube 2|   100 mm|   x|   100 mm|   18 mm|   1|   0.01   |
	|   Small Cube 1|   100 mm|   x|   100 mm|   18 mm|   1|   0.01   |
	|   Array Cube|   200 mm|   x|   300 mm|   18 mm|   6|   0.36   |
	|   Hidden Cube|   200 mm|   x|   300 mm|   18 mm|   1|   0.06   |
	|   Sort Order|   50 mm|   x|   120 mm|   18 mm|   1|   0.006   |
	|   PDMirror Pad|   200 mm|   x|   300 mm|   18 mm|   2|   0.12   |
	|   Pad Single|   200 mm|   x|   300 mm|   18 mm|   1|   0.06   |
	|   PDMulti 4 Pad|   200 mm|   x|   300 mm|   18 mm|   4|   0.24   |
	|   PDMulti 8 Pad|   200 mm|   x|   300 mm|   18 mm|   8|   0.48   |
	|   Array Pad|   80 mm|   x|   700 mm|   80 mm|   4|   0.224   |
	|   Array Polar Pad|   80 mm|   x|   700 mm|   80 mm|   4|   0.224   |
	|   Array Polar Cube|   80 mm|   x|   700 mm|   80 mm|   4|   0.224   |
	|   PMirror 2 Cube|   200 mm|   x|   300 mm|   18 mm|   2|   0.12   |
	|   Summary by thickness|   |   |   |   |   |      |
	|   |   |   |   |   3 mm|   1|   0.06   |
	|   |   |   |   |   18 mm|   33|   1.796   |
	|   |   |   |   |   80 mm|   14|   0.784   |
	|   |   |   |   |   |   |      |
	|   Edge size|   |   14.06 m|   |   |   |      |
	|   |   |   |   |   |   |      |
	|   |   |   |   |   |   |      |
	|   |   |   |   |   |   |      |


**Note:** This long report has been created using [sheet2export](https://github.com/dprojects/sheet2export).
