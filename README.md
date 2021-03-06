## Table of contents
* [General info](#general-info)
* [Functions](#functions)


## General info
I made this to assist in solving the 'eye mystery' in the game Noita. The general purpose of it was to visualize the message boards in a more customizable way.
I have added functions after they felt needed, and i will gladly take suggestions on new features to implement.
I would also like to add that all nine messages are pre-defined in the script as numpy arrays to make it easier to use.
All tables are imported as in a dictionary called tbl. So if you want east1, simply call tbl['east1'] to retrieve it.

	
## Functions

A quick overview of the current functions intended for user use and how to use them.

### plotEyeTable(table, center, up, right, down, left, alpha=0.3, pause=0)
This is intended to plot tables as they are in-game, for you who are familiar with python this is the easiest function to use.
for example:
* Plot tables individually
* Plot all tables overlapping
* Plot chosen tables overlapping
* Change colour and/or symbol of each eye 
* Enable/Disable eye directions for plotting, for example only plot eyes looking to the left.
* Change the alpha of each eye


some notes:
- if you want each eye direction to have unique alpha, you have to do that in the function itself.
- Available markers can be found [here](https://matplotlib.org/stable/api/markers_api.html)
- If you dont use the spyder IDE or plots wont show up, write plt.show() below the desired plot.


The example below shows how to plot all eyes from table east1, west1 and east2 overlapping with the alpha set to 0.2

```
plotEyeTable(tbl['east1'], True, True, True, True, True, 0.2)
plotEyeTable(tbl['west1'], True, True, True, True, True, 0.2)
plotEyeTable(tbl['east2'], True, True, True, True, True, 0.2)

```

### plotTables()
This is intended to plot tables as they are in-game, but for you who are not so familiar with python syntax. 
simply call the function like this:
```
plotTables()
```
And answer the promts that show up in Console. 
Correct tables would be one of these: east1, west1, east2, west2, east3, west3, east4, west4 or east5
You can print as many as you'd like, just go through the promts then type exit when promted for it and you are ready for plotting.

for example; you can print all eyes in east1 as red squares with alpha 0.1, and all up eyes in east3 as blue circles with alpha 0.7



### genTri(msg, base)
generates triagrams from the pre-defined arrays of messages.

msg: pre-defined array, east1, east2, eg.
base: what kind base you want the values to have.  'b5', 'b10' is returned as list of strings. Leave empty for base5 returned as two-dim array with int.

example use for base10:
```
e1t10 = genTri(east1, 'b10')

```
example use for base5:
```
e1t10 = genTri(east1, 'b5')

```
example use for base5 with integer arrays:
```
e1t10 = genTri(east1)

```

