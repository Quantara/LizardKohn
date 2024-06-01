# pass
python .\ScaleCounterCLI.py -s .135182Dorsal-NoFlash-2.png
python .\ScaleCounterCLI.py -s .135182Dorsal-NoFlash-2.png -o test_here
python .\ScaleCounterCLI.py -s .135182Dorsal-NoFlash-2.png -o test_here -scs

# fail
python .\ScaleCounterCLI.py -s .\test\
python .\ScaleCounterCLI.py -s .\test\ -o test_here
python .\ScaleCounterCLI.py -s .\test\ -o test_here -scs

# pass
python .\ScaleCounterCLI.py -s .\test\135182Dorsal-NoFlash-2.png
python .\ScaleCounterCLI.py -s .\test\135182Dorsal-NoFlash-2.png -o test_here
python .\ScaleCounterCLI.py -s .\test\135182Dorsal-NoFlash-2.png -o test_here -scs

# pass
python .\ScaleCounterCLI.py -s '.\test\test copy\'
python .\ScaleCounterCLI.py -s '.\test\test copy' -o test_here
python .\ScaleCounterCLI.py -s '.\test\test copy/' -o test_here

# get warning
python .\ScaleCounterCLI.py -s '.\test\test copy' -o test_here -scs 


# fail
python .\ScaleCounterCLI.py -s '.\test\test copy\' -o test_here
python .\ScaleCounterCLI.py -s '.\test\test copy\' -o test_here -scs 

# pass
python .\ScaleCounterCLI.py -s '.\test\test copy\135182Dorsal-NoFlash-2.png'
python .\ScaleCounterCLI.py -s '.\test\test copy\135182Dorsal-NoFlash-2.png' -o test_here
python .\ScaleCounterCLI.py -s '.\test\test copy\135182Dorsal-NoFlash-2.png' -o test_here -scs

