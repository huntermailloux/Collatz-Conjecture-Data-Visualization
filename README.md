/**************************************************** INSTALLATION ***************************************************\

For installing and getting the program to work, you'll need these 4 things:
	Updated version of Python3 (I used 3.10)
	Latest version of pip
	Latest version of plotly library (I used v5.13.0)
		To install plotly library, open up the terminal and type "pip install plotly"
	Latest version of pandas library (I used v1.5.3)
		To install pandas library, open up the terminal and type "pip install pandas"

Once you have all of that, you should be able to run the Python problem with no problem!


/**************************************************** MONOLOGUE *******************************************************\


I've been wanting to do a data visualization of the Collatz Conjecture for quite some time now, so this is my first go at it!

For those who don't know what the Collatz Conjecture is, it's an algorithm that states the following:
	The number must be an integer
	If you have an even number, divide it by 2
	If you have an odd number, multiply by 3 and add 1
	Keep doing the previous 2 steps until you reach 1

I first got introduced to the algorithm in one of my first year courses (COMP-1410 Intro to Algorithms and Programming II) and was immediately fascinated by it!
Such a simple formula, yet it can produce millions of numbers! If you look closely to tests of it too, you can see that there are common patterns that all lead back 
to 1 like when hitting the number 10 or 64. There's a pretty cool visualization of the numbers here: 
https://d2r55xnwy6nx47.cloudfront.net/uploads/2019/12/CollatzGraph_1300Lede.jpg

For my algorithm, I coded it in Python and used a couple of libraries to help chart out the data. I found the Plotly library to be the most useful in this case, 
and I had to also download the pandas library to get it to work. 

It's my first attempt at it, and I'm hoping later on I can port over a similar program to a website and have the whole interaction between the user entering a
number and seeing the data on the graph all in the same page (which is why this is V1).
