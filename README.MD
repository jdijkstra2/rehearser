# Project description

This project implements a rehearser for language-learning purposes and more generally for any things that can be rehearsed by repetition.

The rehearser can take as inputs .xlsx files consisting of two columns of arbitrary length.

Example .xlsx file:

    A       B
1   ENGLISH DUTCH
2   one     een
3   two     twee
4   ...     ...

# How to use
The rehearser can be used by cloning the project and runnning the main.py file.
-> 'python main.py -f hiragana.xlsx' runs the rehearser with the file "hiragana.xlsx" that should be present in the \excel_files directory.
-> 'python main.py' prompts the user for the filename and starts the rehearser with the file provided


# Japanese Kanji

The project has additional functionality focused on rehearsing the Japanese Kanji.
This functionality allows the rehearsal of tables found on: https://en.wikipedia.org/wiki/Ky%C5%8Diku_kanji
They can be used for rehearsal by simply copying the contents of the table into a .txt file and placing them in the '\txt_files' directory.
Example: 

216 	売 	7 	sell 	bai 	u-ru
217 	午 	4 	noon 	go 	uma
218 	汽 	7 	steam 	ki 	
219 	弓 	3 	bow  	kyū 	yumi
220 	回 	6 	times 	kai 	
221 	会 	6 	meet 	kai, e 	a-u
222 	組 	11 	team 	so 	kumi
223 	船 	11 	ship 	sen 	fune
224 	明 	8 	bright 	mei 	aka-rui
225 	社 	7 	company 	sha 	yashiro

The rehearser focuses on learning the relation between the symbol and the meaning of the word, which is the 2nd and 4th column respectively.