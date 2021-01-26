#!/usr/bin/env python3

import os
import re

main_py = "main.py"
main_js = "main.js"
compile_command = "transcrypt --build " + main_py

# check stubs import
stubs_import_regex = "from stubs import .*"
main_py_dode = open(main_py, 'r').read()
stubs_included = False
if main_py_dode.find("from stubs import") >= 0:
    print("Begin to replace code")
    stubs_included = True
    cleaned_code = re.sub(stubs_import_regex, "", main_py_dode)
    with open(main_py, "w") as main_py_file:
        main_py_file.write(cleaned_code)

# execute transcrypt build
print("Execute transcrypt compile\n")
os.system(compile_command)

if os.path.isfile("deps.js"):
    print("Merge with deps.js\n")
    # merge deps.js with
    global_js_code = open('deps.js', 'r').read()
    main_js_code = open('__target__/' + main_js, 'r').read()
    # write new content
    with open("__target__/" + main_js, "w") as main_js_file:
        main_js_file.write(global_js_code + main_js_code)

# write back to main.py
if stubs_included:
    with open(main_py, "w") as main_py_file:
        main_py_file.write(main_py_dode)

print("Build done!")
