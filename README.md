# Git-Cache-Remover
Python script for removing unwanted files that may (or not) be staged before.
## Have you staged A LOT of files that you didn't want to?
Just run this scipt inside your git repository and it will automatically detect the files that you previusly selected.
## Set up
Open the file with any text editor and add the extensions or names of files that you want to remove.
As an example:
```
if ('__pycache__' in line) or ('.pyc' in line) or ('your-extension-exampe' in line):
```
## Oops...bugs? Suggestions?
Just Fork Request it! Or contact me at: agmachiavello@gmail.com

