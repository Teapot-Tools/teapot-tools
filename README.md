# Teapot-Tools

Teapot-Tools is a very simple python 3 module that lets you play with Google's 418 teapot, by rotating it or making it pour tea whenever you want.
~~It currently only works with Firefox, but adapting it to Chrome would be pretty easy. Universal version coming soon:tm:~~ Universal version is out! See `Parameters` below. Untested on other browsers than Firefox, but it _should_ work on them as well.

This module assumes you have the selenium package installed, and the path to its driver (depends on the browser you're using).

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
tt.reset() #reset the teapot to its original state
tt.close() #close the browser session
```

## Parameters
You can pass 3 parameters into `TeapotTools`:
* `browser` - The browser you're using. Valid options are 'Firefox', 'Chrome', 'Ie' and 'Opera'.
* `driver_exec` - The path to your browser's selenium driver
* `delay` - The time in s to wait before trying to fetch the data from the website. This is especially useful for people with slow internet connections, as it allows them to wait longer until the page has fully finshed loading. Defaults to `2`.