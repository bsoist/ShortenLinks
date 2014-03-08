# Link Shortener 
This is a link shortening tool I use, and it works for me.

It might seem obtuse to some, but you can read more about my reasoning at
http://bsoi.st

## How it works
I've written a blog post about why I set this up the way I did and I go into more detail there about how this works. The best way to understand with all of the backstory is to read below about how I use it.

## How I use it
I have a symbolic link in my PATH to the linkit.py script which I call linkit. When I want to create a link, I do this ...

    linkit http://sub.domain.tld/path/to/page.html

This does the following 

1. opens a CSV file containing all short strings and links I've created before
2. if it finds the URL in the CSV file, it prints out the short string followed by my short domain
3. if it doesn't, it finds a short string I've not used yet ( example XX )
4. creates a folder in my cloud cannon site using that short string
5. saves the URL and the short string to the CSV file
6. builds some xhtml that will redirect to the URL I passed in
7. saves that xhtml string to a file called index.html in the folder just created ( example XX/index.html )
8. creates an apache2 redirect rule to send http://XX.bsoi.st to http://links.cloudvent.net/XX 
9. saves that redirect string to a config file in my cloud cannon folder

Another process ( grab_config.sh ) runs as a cron job on my server to keep looking for modifications to that config_file.txt and pull it down and restart apache.

## How YOU can use it
This was written for use under very specific circumstances, but if you are interested in a similiar setup, this is what you need.

1. root access a server that runs apache2
2. some other website that serves content from a folder on the same machine on which you plan to create links


I've created the settings.py file and added a variable to the top of grab_config.sh specifically so you could see what variables you would need to change to make this work for you, but this all assumes you use Apache2 and Cloud Cannon and Google Analytics. If you know enough about Apache and DNS, you should have enough to adjust other things if your situation is a little different. 


