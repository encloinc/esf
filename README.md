#Esf

Esf is the easiest way to load and save arrays onto files, made for beginners!

Esf makes a great alternative to other file formatting engines, such as JSON or PyYaml. Its functions are really simple,
made so even the newest of programmers can understand it without digging deep in stackoverflow :P

Esf makes it as simple as providing a file path for your file to be stored, and naming the file (remember to end it with a .esf format)
also remember to use forward slashes when typing in your directory (Backward slashes wont work, so copying and pasting the directory of your choice wont work unless you change all the backward slashes to forward slashes)

also dont put your file in the filepath, add your file name on the second arguent of the functions class
###Getting started with ESF###
```python
import esf
f = functions('C:/Users/your/file/path', 'test.esf')
```
###Now you can get started with ESF!###

Esf aims at keeping things as simple as possible, infact its so simple you can treat your file as an array!
Yup there is no need to worry about saving and loading files, esf does it for you ;)

####Add something to your file####
```Python
f.append('Thing')
```

####Remove something from your file####
```Python
f.pop(item)
```

####Replace an item on your file####
```Python
f.replace(item, 'Thing')
```

###If you feel like having more control of your .esf files, esf has functions for you too###

####Get an index from your file (Works just like list.index)####
```Python
f.index(payload)
```

####Return your file as a list for you to edit as you wish####
```Python
list = f.get_list()
```

####Save a list of your choice into your file (Overwrites what was previously there)####
```Python
f.upload_list(list)
```

####Delete you file (Create a new function session after doing this)####
```Python
f.delete()
```

Esf can also create directories, if the directory you type in isnt found, ESF does it for you (;
We believe everyone should be able to save their data, even beginners (;
