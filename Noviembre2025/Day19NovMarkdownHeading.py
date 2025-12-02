"""
Markdown Heading Converter

Given a string representing a Markdown heading, return the equivalent HTML heading.

A valid Markdown heading must:

    Start with zero or more spaces, followed by
    1 to 6 hash characters (#) in a row, then
    At least one space. And finally,
    The heading text.

The number of hash symbols determines the heading level. For example, one hash symbol corresponds to an h1 tag, and six hash symbols correspond to an h6 tag.

If the given string doesn't have the exact format above, return "Invalid format".

For example, given "# My level 1 heading", return "<h1>My level 1 heading</h1>".

Note: The console may not display HTML tags in strings when logging messages. Check the browser console to see logs with tags included.

"""

def convert(heading):

    words = heading.split(' ')
    words = [x for x in words if x]
    character = words[0]
    
    if "#" in character and len(character) <= 5:
        for i in character:
            if i.isalpha():
                print("Invalid format")
        print(f'<h{len(character)}>{' '.join(words[1:])}</h{len(character)}>')
    else:
        print("Invalid format")
        

convert("  ###  My level 3 heading")