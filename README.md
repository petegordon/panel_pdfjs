Started to demonstrate how PDF.js can be used with Python Panel through a HTML Widget.

Most important change is [here](https://github.com/petegordon/panel_pdfjs/blob/38444ef0104be517571be780026cffa513986fbd/pdfjs-3.8.162-dist/web/viewer.html#L37) in viewer.html.


Made changes to the viewer.html in the PDF.js environment for this to work with coordinates (page 65 and 300px on the y position) passed on the query string to the viewer.html but coded into panel as a variable.

```python
coordinates_string = """{"65":[0,800,0,0]}""" 
```

Behaves a little funky for refresh. But, gives the basic point.
