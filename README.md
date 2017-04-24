# CNN-Query-Searching-

I have often felt that the search function in news sites aren’t adequate. Especially to a journalist who is looking for data/information about a certain topic.  For this project I decided to create a search function for the CNN website that will produce the following results apart from showing the links to a query: 

1.	List the total number of results of the query 
2.	List the top authors who wrote about that query
3.	List the top five most common words that appear in articles about the query

*The program will take the following input from the user:*

1.	Query [ limited to one word as of now]
2.	Sections of the website in which the user wants to search for the query. E.g. Search for articles about Trump in the entertainment section only. 
3.	The year of the query
4.	The month of the query 

*The algorithm of the program:*

1.	Takes in the inputs from the user
2.	Looks at CNN’s sitemap for the articles in the date range provided by the user
3.	Takes the query from the user and converts it into a regular expression
4.	Looks for all the articles within the section provided by the user and matches the regular expression to find all the articles about the query – All articles with the query word in the link-
5.	Puts all the articles into a list ‘finalist’
6.	If ‘finalist’ is empty, asks the user to change their query
7.	Writes final list into a CSV ( as per requirements of the project | The Programm could directly read the article links from the ‘finalist’ but since the project description specifies the need to write it into a CSV or excel file)
8.	Takes each link and extracts the text, and authors from the article 
9.	Tokenizes the article text 
10.	Puts the authors in a list 
11.	Performs a Frequency distribution of the tokens from all the articles 
12.	Performs a Frequency distribution on the author's list to get the top authors
13.	Prints the results 





