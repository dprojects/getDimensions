# Test platform 

FreeCAD 0.19.3 AppImage under Ubuntu 20.04.2 LTS 64-bit.

# Test procedure

1. `cd ./getDimensions`
2. Create Markdown files for all needed test cases via [sheet2export](https://github.com/dprojects/sheet2export) in the main directory.
3. Run from terminal: `bash ./Test/bin/autotest.bash`

# Test cases

1. **Test001_features:** 
	* Test all the basic features supported by the macro.
	* **Settings:** `Report type` to `n`.
2. **Test002_edgeband:** 
    * Test edgeband and extended edge report.
    * **Settings:** 
        * `Report type` to `e`, 
        * `Furniture color` to `white`, 
        * `Edgeband code` to `black`.
2. **Test003_holes:** 
    * Test detailed report with edgeband, holes and countersinks and advanced features like Mirrored on Body, Clone, multi object MultiTransform.
    * **Settings:** 
        * `Report type` to `d`, 
        * `Edgeband code` to `bronze`.
