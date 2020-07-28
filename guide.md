Guide to the menu xlsx templates
--------------------------------

In this system (`tkmenu.py`)  
a toplevel or parent --> first level (parent) (--> second level items)   
Nothing beyond second level menu items.  

Each row is one menu item.  
The parent menu item comes after all the children items  
and its label name starts with an "_" underscrore.  
The parent of a "submenu" item works the same way.  

In the templates "second level" items all use the  
variable name "`submenu`"  

For clarity prefix each command with its variable name.  
e.g. "`mn_file`" and "`mn_file_save`"  


## To Use ##
- modify the template spreadsheet and save under different name.
- generate the code:  

`python3 tkmenu.py my_menus.xlsx`  

_OUTPUT IS TO CONSOLE_

copy the output from the console into the  
`tkauto_tpl.py` template.  

- save `tkauto_tpl.py` as something else
- test it
- if you're using with `tkauto.py` generated program  
    first finish generating with `tkauto.py`, then use  
    `tkmenu.py` if you also want menus.

    



