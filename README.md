# ifsc_api

![Python package](https://github.com/HarshOza36/ifsc_api/workflows/Python%20package/badge.svg)
![Python application](https://github.com/HarshOza36/ifsc_api/workflows/Python%20application/badge.svg)

# Documentation

IFSC API was build to get details of ```BANK``` and the ```ADDRESS OF THE BANK``` from the IFSC CODE quickly.

This library was build specially for Arihant Capital Pvt. Ltd.

# Installation:
```pip install git+https://github.com/HarshOza36/ifsc_api.git```


# USAGE:

IFSC_API
--------

To use the server in ```localhost@localhost/ifsc```(with caution), simply do::

```python
    >>> from ifscApi import app
    >>> app.runServer()
```

To just use it normally(with caution), simply do::
```python
    >>> from ifscApi.getDetails import FetchData
    >>> parser = FetchData() # Create a parser
    >>> ifsc = 'ANY_CODE_HERE'
    >>> result = parser.getdata(ifsc)
    >>> print(result)
```
