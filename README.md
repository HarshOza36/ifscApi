# ifsc_api

![Python package](https://github.com/HarshOza36/ifsc_api/workflows/Python%20package/badge.svg)
![Python application](https://github.com/HarshOza36/ifsc_api/workflows/Python%20application/badge.svg)

# Documentation

IFSC API was build to get details of ```BANK``` and the ```ADDRESS OF THE BANK``` from the IFSC CODE quickly.

This library was build specially for Arihant Capital Pvt. Ltd.

# Installation:
```pip install git+https://github.com/HarshOza36/ifsc_api.git```

OR

```pip install ifscApi```

# USAGE:

IFSC_API
--------

- To use the package in User Interface @ ```localhost``` (with caution), simply do::

        You can also just use the api without User Interface @ ```localhost/ifsc```  which is a RestFul Api.

    ```python
        >>> from ifscApi import app
        >>> app.runServer()
    ```

- To just use it normally(with caution), simply do::
    ```python
        >>> from ifscApi.getDetails import FetchData
        >>> parser = FetchData() # Create a parser
        >>> ifsc = 'ANY_CODE_HERE'
        >>> result = parser.getdata(ifsc)
        >>> print(result)
    ```
Note : The getdata function has parameter dbFilePath which can be overwritten with your own IFSC code Db which should have Table name ```data``` and three columns ```ifsc,bank,address```

- To just use it As AWS LAMBDA compatible Function(with caution), simply do::
    ```python
        >>> from ifscApi.getDetailsLambda import FetchData
        >>> parser = FetchData() # Create a parser
        >>> ifsc = 'ANY_CODE_HERE'
        >>> result = parser.getdata(ifsc)
        >>> print(result)
    ```
Note : The getdata function has parameter dbFilePath which can be overwritten with your own IFSC code Db which should have Table name ```data``` and three columns ```ifsc,bank,address```
