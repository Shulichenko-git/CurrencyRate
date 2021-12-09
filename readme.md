###About Currency Rate Project
___


This project consists of one application: currencies_app
<br>
Implemented with Django 3.2.9
___
The application receives data on the hryvnia to dollar exchange rate
from the database and displays a graph.
___
The user can go to the page for updating or creating a currency rate for any date at the present moment or earlier.

To do this, you can use the button on the right on the navbar and the "Add Rate" item.
___
There are two fields in the form for adding a currency rate: rate and date.
___
__Data format__
1. The value of the 'rate' field is a positive decimal number with two decimal places (minimum value 0.01)
2. The 'date' has the input format "YYYY-MM-DD".
___
If the user enters a date that is **already in the database** and, accordingly, on the chart,the rate value for that date is **updated**. 
If the value is **new**, then it is **created**.

_Thanks for reading!_