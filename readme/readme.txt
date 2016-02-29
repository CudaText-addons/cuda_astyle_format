Plugin "AStyle Format" for CudaText.
It allows to format (beautify) source code for these lexers: C++, C, C#, Java, using good AStyle library.

If selection is made (only normal selection supported) then only selection is formatted, otherwise entire file is formatted. But note: selection formatting is incorrect in many cases, e.g. if you format only nested { } block, it will have incorrect indent regarding parent { } block. Sublime's plugin AStyleFormatter does special work for this case, and it's too complex, so it's not "repeated" here.

Plugin has commands in menu "Plugins".
Plugin has configuration file. It's single-line text file with AStyle command-line options, see list of those at: 
http://astyle.sourceforge.net/astyle.html

You can edit config file using two "Configure" commands:

    "Configure" opens config-file from "settings" folder, which is used when local file doesn't exist.
    "Configure (local)" opens config-file from the folder of current editor file. If local file doesn't exist, command suggests to copy global file into local name, and then opens it. 


Author: Alexey T.
