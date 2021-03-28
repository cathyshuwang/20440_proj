# Overview

20440_proj contains data and code files that (will) compare inflammation and cancer data using 
PCA and clustering techniques to understand trends in protein expression levels among disease. 
Functionally, there is a script to load in gastric disease data and plot protein expression of 
20 proteins in one replicate of each condition. 

## Data
Data was generated from experimental data of three papers and found publicly online or 
through contacting the first-author (Haudek-Prinz et al, 2012; Fernandez-Coto et al, 2018; 
McCaffrey et al, 2020 preprint).

## Structure
- code_EDA/
	- Python and Jupyter Notebook file for loading and plotting preliminary figure of
	gastric data 
- data/
	- raw/
		- raw dataset, entire spreadsheet files
	- processed/ 
		- (will) contain cleaned/relevant lines of data from original datasets
- figures
	- results from plotting (currently, one preliminary figure of protein expression of 
	one set of gastric data) 

## Installation/Usage 
Packages used include pandas (1.1.2), numpy (1.19.2), and matplotlib (3.3.2). You can run Python files in any text 
editor/IDE and generate associated figures. Jupyter Notebook or Conda may be needed to run 
.ipynb files.
