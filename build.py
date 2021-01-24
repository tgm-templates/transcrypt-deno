#!/usr/bin/env python3

import os

main_py = "main.py"
# check stubs import
stubs_code = "from stubs import *"
main_py_dode = open(main_py, 'r').read()
stubs_included = False
if main_py_dode.find(stubs_code) >= 0:
    print("Begin to replace code")
    stubs_included = True
    plainCode = main_py_dode.replace(stubs_code, "")
    main_py_file = open(main_py, "w")
    main_py_file.write(plainCode)
    main_py_file.close()

# execute transcrypt build
print("Execute transcrypt compile\n")
os.system('transcrypt --build ' + main_py)

if os.path.isfile("global.js"):
    print("Merge with global.js\n")
    # merge global.js with
    global_js_code = open('global.js', 'r').read()
    main_js_code = open('__target__/main.js', 'r').read()
    # write new content
    main_js_file = open("__target__/main.js", "w")
    main_js_file.write(global_js_code + main_js_code)
    main_js_file.close()

# write back to main.py
if stubs_included:
    main_py_file = open(main_py, "w")
    main_py_file.write(main_py_dode)
    main_py_file.close()

print("Build done!")
