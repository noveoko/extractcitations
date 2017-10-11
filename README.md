# extractcitations
Use this handy script to extract citations from your PDF files

In order to run the test:
Do these only the FIRST time:
1. Make sure you have Python 2x installed
2. Make sure you have the "refextract" library installed (install by opening terminal and typing: "pip install pyextract" NO QUOTES)

Do these every time you need to extract citations from a PDF document:
1. Add a selection of PDFs to the folder "PDFS_to_PROCESS" located in the root of this project
2. Open your TERMINAL from the ROOT/MAIN folder of this project
3. In the TERMINAL write: python parse.py
4. Wait for the results
5. Copy the contents of "drop_these_into_anystyledotio.txt"
6. In your browser visit "https://anystyle.io/"
7. Paste what you copied in step 6 into the box labelled, "Paste your references here"
8. Click parse
9. Once your job is completed scroll down and select from: BibText, CiteProc/JSON, XML
DONE!
