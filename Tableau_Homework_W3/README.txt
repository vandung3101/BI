Ex.1
	- Connect google sheet to tableau via the given link
	- Authenticate with google account
Ex. 2
	- Open Sheet1
	- Drag State to Columns
	- Drag Profit to Rows
	- Click maps on Show Me
	- Adjust Opacity and show mark labels
Ex. 3
	- Open Sheet2
	- Drap State to Columns
	- Drap Profit to Rows
	- Click maps on Show Me
	- Adjust Opacity
	- Select 'Show mark labels' and 
	- Choose 'Min/Max' in 'Mark to labels'
Ex. 4
	- Open Sheet3
	- Drag Customer ID to detail on Marks panel
	- Drag Sales to Columns
	- Drag Profit to Rows
	- Choose scatter plots on Show Me
	- Drag Profit to Color
Ex. 5
	- Drag Sales to Columns
	- Drag Customer Name to Rows
	- Drag Customer Name to color on Marks panel
	- Choose color
	- Click sort button on toolbar
Ex. 6
	- Let's say everyone is equal no matter what ship mode was
	- We calculate the days which they take to ship the shipment
	
		IF [Ship Date] - [Order Date] < 4 THEN 'Early'
		ELSEIF [Ship Date] - [Order Date] < 6 THEN 'On time'
		ELSE 'Late'
		END
	
	- Drag Order Date to Columns, choose week presentation
	- Drag new measure to Rows, choose Count
	- Drag to color on Marks
	- Edit some stuff