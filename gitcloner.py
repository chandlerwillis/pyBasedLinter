import os
from git.repo.base import Repo
import pylint.lint


#get git link
gitLink = "https://github.com/chandlerwillis/pylinttest.git"

#download git files
directory = os.getcwd()
Repo.clone_from(gitLink,"New")

#current directory

#cycle thru files for .py
#then lint them
os.chdir("New")
def findPyFiles():
    pyExt = ('.py')
    for pyFiles in os.listdir():
        if pyFiles.endswith(pyExt):
            print("------------------------------------------------------------------------------------------------------------------")
            print("The following file is a py file: " + pyFiles)
            print("------------------------------------------------------------------------------------------------------------------")
            lintPythonFiles = pyFiles
            pylint_opts = ['--disable=line-too-long', pyFiles]
            gunga = pylint.lint.Run(pylint_opts)
            print(gunga)
            #os.system("pylint " + pyFiles)
            #os.system("bandit -r " + pyFiles)
            print("------------------------------------------------------------------------------------------------------------------")
        else:
            continue
findPyFiles()

#cycle thru files for .yaml (cloudformation)
#then lint them
def findCloudFormationFiles():
    cfExt = ('.yaml')
    for cfFiles in os.listdir():
        if cfFiles.endswith(cfExt):
            print("The following file is a CFN file: " + cfFiles)
            lintCloudFormationFiles = cfFiles
            os.system("cfn-lint " + cfFiles)
        else:
            continue
findCloudFormationFiles()

#cycle thru files for .js (node js)
#then lint them
def findNodeJSFiles():
    jsExt = ('.js')
    for jsFiles in os.listdir():
        if jsFiles.endswith(jsExt):
            print("The following file is a JS file: " + jsFiles)
            lintJSFiles = jsFiles
            os.system("eslint " + jsFiles)
        else:
            continue
findNodeJSFiles()










