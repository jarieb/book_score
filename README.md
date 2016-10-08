A python script to give statics on a manuscript so a writer can track their
progress along the lines of word count, readability, and happiness.

Written by Jarie Bolander

The code is licensed under MIT license.

Overview
-------------------------------------------------------------------------------
book_score.py is a script to score a series of chapters on word count, 
readability, and happiness.

The word count and readability is based on the textstat library while the happiness 
score is based on labMTsimple, a library from the University of Vermont 
[hedonometer.org](http://hedonometer.org) project.

The script needs the following external libraries (versions in requirements.txt):
	labMTsimple
	textstat
	natsort
	argparse

Usage
-------------------------------------------------------------------------------

The script expects a directory filled with .txt files that contain the text you 
want to grade. Each file is a chapter and will be graded individually. The text file 
should be utf8. Paragraphs are determined by a double return (e.g. \n\n).

Chapter files should have the chapter number first and then the title since the script
sorts the chapters by number. This is important so you can see the overall linear 
trend of the manuscript.

	example/
		1-Introduction.txt
		2-Missed It By That Much.txt
		3-Finding the Crazy Ones.txt

To run the script, simply type the following command where book_score.py resides

	$ python book_score.py -d <name_of_directory>

See the example directory to see a snapshot of my book and the format of .txt files.

The script will produce two .csv files. One is book_stats_<name_of_directory>.csv and 
the other is page_sparklines_<name_of_directory>.csv.

book_stats_<name_of_directory>.csv contains the Word Count (WC), Reading Level (RL), 
and Happiness Score (HS) for each chapter in the directory.

page_sparklines_<name_of_directory>.csv contains the HS scores for each page in 
the chapter. It's called sparklines because I use this page data to graph sparklines
in excel. The default words per page is 250. This can be changed via an optional 
command line arg as follows:

	$ python book_score.py -d <name_of_directory> -w 200

The example directory also contains the two .csv files with the stats from the
example directory.

Inspiration
-------------------------------------------------------------------------------

This script was inspired by Shawn Coyne's and Tim Grahl's the [Story Grid Podcast](http://www.storygrid.com/) 
and the researchers at the [hedonometer.org](http://hedonometer.org) project to
track the book I'm working on about Entrepreneurship.

You can see the results of the script and my progress by going to
[The Entrepreneur Ethos]() page on my blog.

The idea is that there are 6 basic story types that follow a certain pattern. This
pattern is the highs and lows of the story. The Happiness Score (HS) attempts to
figure out if the text is positive (high score) or negative (low score). By
graphing these highs and lows, I can figure out the mood of a chapter
and the overall mood of the book.

The 6 different story types are: rages to riches (rise), riches to rages (fall), 
man in a hole (fall then rise), Icraus (rise then fall), 
Cinderella (rise then fall then rise), and Oedipus (fall then rise then fall).

These story types are based on [Kurt Vonnegut’s story mapping in Palm Sunday](http://www.theatlantic.com/technology/archive/2016/07/the-six-main-arcs-in-storytelling-identified-by-a-computer/490733/).

The Word Count (WC) and Reading Level (RL) were added so I can track my progress
and make the overall book have a reading level of around 8th grade. 8th grade
was choosen by reading an excellent post by [Shane Snow](https://www.linkedin.com/pulse/how-much-does-reading-level-matter-shane-snow) on
the reading levels of non-fiction best sellers.

I'm also using [Hemingway](http://www.hemingwayapp.com/) to see where I can 
improve my prose. The online version is free to try out. The readability score
from Hemingway is a little different than my readability level. I might change
the code to make it closer but for now, I'll just deal with it.

Future Work
-------------------------------------------------------------------------------

I'm going to look into some more AI type sentiment analysis. It would be fun to
do some Natural Language Processing (NLP) as well to get a more indepth look sentence
by sentence. 

Have fun and shoot me an email if you find this useful: jarie.bolander@gmail.com

