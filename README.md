# tkmenu
generate tkinter menu code using an Excel spreadsheet
-----------------------------------------------------

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

