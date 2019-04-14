# Betamaze
Betamaze is a python script that generates betamaze maps from text.

# Usage
Clone this repo and then navigate into it from the cli. Generate a new map with the following command:
```bash
python3 betamaze.py 10 "This is a test."
```

This will generate a map like this:
![Example betamaze](https://i.imgur.com/HJxWIxk.png "Example betamaze")

# Parameters
In the above command the 10 represents the max number of glyphs in a line before it wraps to the next line. For example, if you have a piece of text that is 25 characters long, specifying a max line length of 5 would result in a 5 x 5 map.

The text to be mapped should be enclosed in brackets otherwise the script will only map the first word.

If you have any questions, feel free to reach out to me on [Twitter](https://twitter.com/user_r00).
