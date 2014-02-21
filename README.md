split-layer
===========
Iterates through an ArcMap layer and creates new layers based on distinct values in a given field.

#####Details

Developed in Arc 10.2

This tool takes a layer from the TOC or a .lyr file.  User must specify a field in the given layer on which to set up definition queries. Tool finds all distinct values in field and creates a new layer with a definition query specific to distinct value. The tool can be run a second time on a resulting layer to split on a different field.

The associated xml files contain in-program  documentation for the tool and toolbox.

#####Set-up

#####Quirks
* During testing the topmost layer does not get labeled appropriately in the TOC. Checking the 'General' tab shows the correct label and upon clicking OK the TOC updates.
* The .pyt file is just a simple text file...Notepad++ did not recognize the Python so I had to change the language manually for coloring and syntax recognition.