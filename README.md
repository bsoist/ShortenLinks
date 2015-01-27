# Link Shortener 
This is a link shortening tool I use, and it works for me.

It might seem obtuse to some. If you want to know more about why I do things this way, [start here][newdoc].

## How it works
I've written a couple of blog posts ( [here][newdoc] and [here][olddoc] ) about why I set this up the way I did and I go into more detail there about how this works. The best way to understand with all of the backstory is to read below about how I use it.

## How I use it
I have a symbolic link in my PATH to the linkit.py script which I call linkit. When I want to create a link, I do this ...

    linkit http://sub.domain.tld/path/to/page.html

This does the following 

1. opens a CSV file containing all short strings and links I've created before
2. if it finds the URL in the CSV file, it prints out the short string followed by my short domain
3. if it doesn't, it finds a short string I've not used yet ( example 07 )
4. creates a folder in my cloud cannon site using that short string
5. saves the URL and the short string to the CSV file
6. builds some xhtml that will redirect to the URL I passed in
7. saves that xhtml string to a file called index.html in the folder just created ( example 07/index.html )

## How YOU can use it
This was written for use under very specific circumstances, but if you are interested in a similiar setup, this is what you need.

1. root access to a server that runs apache2
2. a wildcard rule that servers whatever.yourdomain.tld to /whatever/ on your cloudcannon site 

I've created the settings.py file specifically so you could see what variables you would need to change to make this work for you, but this all assumes you use Cloud Cannon and Google Analytics. If you know enough about this stuff, you should have enough to adjust other things if your situation is a little different. 

[newdoc]: http://www.bsoi.st/2015/01/26/shortening-links/
[olddoc]: http://www.bsoi.st/oped/2014/03/08/howIShortenLinks.html 
