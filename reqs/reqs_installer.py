'''
installs packages depending on if inside a virtual environment or not
by following a file hierarchy thingy
'''

from os import system

folderName = 'files/'

print("updating pip..")
system('pip install update')

print("Installing pre-reqs..")
system('pip install -r' + folderName + 'pre-reqs.txt')

print('Installing dev-reqs')
system('pip install -r' + folderName + 'dev-reqs.txt')

print('Installing reqs')
system('pip install -r' + folderName + 'reqs.txt')
