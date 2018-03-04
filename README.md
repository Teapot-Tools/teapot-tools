# Teapot-Tools

Teapot-Tools is a very simple python 3 module that lets you play with Google's 418 teapot, by rotating it or making it pour tea whenever you want.
It currently only works with Firefox, but adapting it to Chrome would be pretty easy. Universal version coming soon:tm:

This module assumes you have the selenium package installed, and the path to its firefox driver.

## Usage
An example of how it works:
```python
from teapottools import TeapotTools as teapot
import time

tt = teapot('C:/geckodriver.exe') #this will fire up a new browser session.

tt.rotate(150) #rotate the teapot to 150 degrees
tt.pour() #make the teapot pour tea (beware, it's never heard of gravity before)
time.sleep(5)
tt.unpour() #stop the teapot from spilling tea on the floor
```

## Parameters
You can pass 2 parameters into `TeapotTools`:
* `gecko_exec` - The path to your firefox driver (probably called `geckodriver.exe` if you're on Windows)
* `delay` - The time in s to wait before trying to fetch the data from the website. This is especially useful for people with slow internet connections, as it allows them to wait longer until the page has fully finshed loading. Defaults to `2`.
