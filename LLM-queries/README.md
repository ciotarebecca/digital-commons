# llm-queries-for-elsevier-digital-commons
These are queries I use to generate metadata for batch ingest via Excel spreadsheet into Digital Commons.

# Copyright Notice
These queries are under exclusive copyright by their author. No unauthorized copying, distribution, or modifications are allowed without the written permission of the author.

# LLM Data Extraction for Law Journals
The William A. Wise Law Library at the University of Colorado Law School utilizes Digital Commons (Elsevier) as their institutional repository. Digital Commons allows batch ingest via Excel spreadsheets (.xls).

The Wise Law Library began a project of ingesting the backfiles of its three student-led law journals - the <a href='https://scholar.law.colorado.edu/lawreview/'>Colorado Law Review</a>, the <a href='https://scholar.law.colorado.edu/celj/'>Colorado Environmental Law Journal</a>, and the <a href='https://scholar.law.colorado.edu/ctlj/'>Colorado Technology Law Journal</a>. They had 60, 30, and 20 year backfiles, respectively; and had published multiple issues each of those years. The backfiles came as individual PDFs, and our original process was to manually enter each one into the system. I implemented the batch upload, but I still had to manually type the metadata into the spreadsheet. I attempted Python (PyMuPDF) but it couldn't quite parse the PDFs' formatting. So then I turned to LLMs to extract data from a PDF table of contents and populate a Digital Commons batch ingest spreadsheet.

# Which LLMs to use.
I developed these for <a href='https://copilot.microsoft.com/chats/xfhAYakuv258sauAA6X7p'>Microsoft Copilot Personal</a>, though I have seen success using <a href='https://aistudio.google.com/prompts/new_chat'>Google AI Studio</a> as well. I believe the paid versions of Gemini and ChatGPT can also perform these, though I have not tested.
