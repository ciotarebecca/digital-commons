# Digital Commons
The information analytics company <a href="https://www.elsevier.com/">Elsevier</a> offers a platform called <a href="https://www.elsevier.com/products/digital-commons">Digital Commons</a> (formerly bepress) to institutions (primarily libraries, in my experience) to serve as an <a href="https://en.wikipedia.org/wiki/Institutional_repository>institutional repository</a>.

My first experience using Digital Commons was at the University of Colorado Law School, when the law library determined that it would shut down its Islandora project and migrate its digital primary law collections to Digital Commons. As I had been managing Islandora nad the digitized primary law collections, I inherited Digital Commons. Finding Digital Commons less intuitive and more labor-intensive to use than my previous open source system, I decided to 

# Copyright Notice
These queries are under exclusive copyright by their author. No unauthorized copying, distribution, or modifications are allowed without the written permission of the author.

# What's included in this github repo?
I am including various scripts, pages, and queries that I have created to improve my usage of Digital Commons.

So far that includes:
<ul>
  <li>a Python script that makes an API call to CU Law's Session Laws Collection, to assist the Colorado General Assembly and Legislative Council in searching the collection</li>
  <li>an LLM query that uses a PDF table of contents to create a .csv compatible (it must be converted to .xls) with Digital Commons' bulk upload functionality, specifically for the Colorado Environmental Law Journal</li>
  <li>an in-progress search page that will (hopefully) use the aforementioned Python API script to allow patrons to search the Colorado Session Laws Collection.</li>
</ul>
