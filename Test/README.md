# Test platform 

FreeCAD 0.19.3 AppImage under Ubuntu 20.04.2 LTS 64-bit.

# Test procedure

Run from terminal: `bash Test/bin/autotest.bash`

# Test cases

1. **Test001_features:** 
	* Test all the stable features supported by the macro.
	* **Settings:** `Result type` to `n`.
	* Create Markdown file via [sheet2export](https://github.com/dprojects/sheet2export) in the main directory.
2. **Test002_edgeband:** 
    * Test edgeband and extended edge report type view.
    * **Settings:** 
        * `Result type` to `e`, 
        * `Furniture color` to `white`, 
        * `Edge color` to `black`.
    * Create Markdown file via [sheet2export](https://github.com/dprojects/sheet2export) in the main directory.
