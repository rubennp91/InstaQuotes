import wikiquotes
import os
from time import sleep
from sys import argv
from sys import exit
from getpass import getpass
from random import randint
from PIL import Image, ImageDraw, ImageFont, ImageStat
wd = os.getcwd() # Get the working directory
    
    
def getInstagramFile(username):
    """
    This function handles the call to the instagram-scraper
    and the actual download of instagram images.
    It does so by calling a command line with os.system()
    
    Arguments taken:
        username: the instagram account name
    Returns:
        the result of keepRandomFile()
    
    Internal calls:
        getLogin()
        keepRandomFile()
    """
    
    usr, pswd = getLogin() # Get a username and password
    
    current = os.listdir(wd) # Get the current files in the working directory
    
    os.system("instagram-scraper "+username+" -u "+usr+" -p "+pswd+" -d "+wd+" -m 20 -t image")
    
    new = os.listdir(wd) # Once downloaded, get the new list of files in the working directory
    
    return keepRandomFile(current, new) # Return a random file
    
def keepRandomFile(current, new):
    """
    This function selects a random file from the previously
    downloaded with instagram-scraper and deletes the rest.
    
    Arguments taken:
        current: the list of current files in the wd
        new: the list of new files in the wd, with the instagram pictures
    Returns:
        toKeep: the name of the randomly selected file
    """
    
    for item in current: # Iterate the two lists of files to find the original ones
        if item in new:
            new.remove(item) # Remove the original from the list of new ones
            
    flag = True # Flag used to separate .jpg from other formats
    while flag:
        toKeep = new[randint(0,len(new)-1)] # Pick a random file
        if toKeep.endswith('.jpg') or toKeep.endswith('.png'):
            flag = False # Exit the loop if it is a .jpg or .png file
    
    for item in new: # Delete the files you don't want to keep
        if toKeep in item:
            pass
        else:
            os.remove(os.path.join(wd,item))

    return toKeep
    
    
def getLogin():
    """
    Deactivated by default
    
    This function handles the login session for the instagram-scraper
    using the getpass library through console input.
    If no user or password are written the function
    will return "a" as password and username. This is ok for 
    instagram-scraper and will get the public pictures from
    the selected profile.
    
    Arguments taken:
        None
    Returns:
        usr: instagram username
        pswd: instagram password
    """
    
    return "a", "a" # Comment this line for login options
    
    # Uncomment the next lines for login options
    """
    usr = raw_input("IG Username (yours, optional): ")
    pswd = str(getpass())
    if pswd == "" or usr == "":
        return "a", "a"
    else:
        return usr,pswd
    """
    
def getQuote(author, language = False):
    """
    This function retrieves a random quote from the selected
    wikiquote page.
    
    Arguments taken:
        author: the page to retrieve the quote from
    Returns:
        quote: the quote itself in a string
        count: the lenght of the quote in words
        language: the languages used to retrieve the quote (english or spanish)
    """
    count = float('inf')
    languages = ["en","es","de","fr","it"] # Languages to search the author
    
    while count > 15: # Keep it short, no quotes longer than 15 words
        
        if language == False:
            for lang in languages: # Iterate trough the languages until it finds a result
                try:
                    quote = wikiquotes.random_quote(author,lang)
                    break
                except:
                    exit("Couldn't get the quote for some reason.")
        else:
            try:
                quote = wikiquotes.random_quote(author,language)
            except:
                exit("Couuldn't get the quote for some reason.")
    
        count = quote.split(" ")
        count = len(count) # Count the words in the sentence
        
    if '"' in quote:
        quote = quote[1:-1]
    
    return quote, count
    
    
def writeOnImage(picture,quoteL):
    """
    This function opens the image for the PIL library to work with.
    It also handles the size of the text and the position it should
    go inside the picture. It writes to the pictures and saves it
    in the current working directory.
    
    Arguments taken:
        picture: the name of the file to edit
        quoteL: the quote, divided in two
    Returns:
        "1.png": the name of the file to save
        
    Internal calls:
        complementaryColor()
    """
    
    txtPos = []
    
    try:
        img = Image.open(picture) # Open the image with the PIL library
    except:
        exit("Something went wrong opening the picture")
    
    width, height = img.size # Get the size of the image

    hFourth = height/4 # Get the fourth of the height of the image
    wThird = width/3 # Get the third of the width of the image     
    
    fontsPath = os.path.join(wd,"fonts")
    fonts = os.listdir(fontsPath)
    scale = 0.08
    
    def calculateFontSize(scale, width, height, quoteL, fontsPath):
        """
        Calculates the size of the font depending on the
        width of the given image.
        
        Arguments taken:
            scale: the scale of the font against the image
            width: width of the image
            height: height of the image
            quoteL: the quote to write
            fontsPath: folder where the fonts exist
        Returns:
            tSize: text size in pixels
            fontSize: the size of the calculated font
            fnt: the font in ImageFont format
        """
        fontSize = int(height*scale)
        
        # Iterate through the fonts folder
        if fonts:
            fnt = ImageFont.truetype(os.path.join(fontsPath,fonts[randint(0,len(fonts)-1)]),fontSize)
        else:
            fnt = ImageFont.truetype(wd+'\\fonts\\IndieFlower.ttf',fontSize) # Selected font
            
        tSize = [d.textsize(quoteL[0],font = fnt),d.textsize(quoteL[1],font = fnt)]
        
        # Check if the text fits the image
        if tSize[0][0] > width or tSize[1][0] > width:
            scale = scale - 0.005
            return calculateFontSize(scale, width, height, quoteL, fontsPath)
        else:
            return tSize, int(fontSize), fnt
        
    d = ImageDraw.Draw(img) # Open the image to write on it
    
    # Get the size that will have the text in the picture as a list 
    # where position [0] is the first half of the sentence 
    # and position [1] the second, to be able to fit it in the picture.
    tSize, fontSize, fnt = calculateFontSize(scale, width, height, quoteL, fontsPath)
    
    # tSize = [d.textsize(quoteL[0],font = fnt),d.textsize(quoteL[1],font = fnt)]
    
    r, g, b = complementaryColor(img) # Get the complementary color for the text
    
    # Determinate the position of the first line of text, by substracting
    # the lenght of the text from the width of the image and the one fourth
    # of the height of the picture multiplied by 3. tSize[0][0] = lenght
    # This is a tuple
    txtPos.append((((width/2)-(int(tSize[0][0])/2)),hFourth*3))
    
    # Determinate the poisition of the second ilne of text as before, but
    # adding the size of the font to fit it just below the first line
    txtPos.append((((width/2)-(int(tSize[1][0])/2)),hFourth*3+fontSize))
    
    # Write the first half of the text using the parameters calculated above
    d.text(txtPos[0], quoteL[0], font=fnt, fill = (r, g, b))
    # d.text((((width/2)-(int(tSize[0][0])/2)),hFourth*3), quoteL[0], font=fnt, fill = (r, g, b))
    
    # Write the second half of the text using the parameters calculated above
    d.text(txtPos[1], quoteL[1], font=fnt, fill = (r, g, b))
    # d.text((((width/2)-(int(tSize[1][0])/2)),hFourth*3+fontSize), quoteL[1], font=fnt, fill = (r, g, b))
    
    img.save('1.png') # Save the image as 1.png
    os.remove(os.path.join(wd,picture)) # Remove the original picture
    
    return "1.png"
    

def complementaryColor(img):
    """
    Get the text used for the color by using the
    median color of the image and calculating
    the complementary. This is not ideal does not work
    quite properly.
    
    Arguments taken:
        img: the image in PIL format
    Returns:
        r: red color
        g: green color
        b: blue color
    """
    a = ImageStat.Stat(img) # Open the image with ImageStat
    a = a.median # Calculate the median of each color band
    
    r = 255 - a[0] # Calculate
    g = 255 - a[1] # the
    b = 255 - a[2] # complementary
    
    return int(r), int(g), int(b)
    

def main():
    """
    The main function handles the call to all
    the other functions that make the script work.
    It also takes care of some other things, like getting
    the arguments from the console line. And for some
    reason also to divide the quote in two and sort
    it by language.
    
    Arguments taken:
        None
    Returns:
        None
    """
    
    # Get the arguments from the console
    # Otherwise assign two default ones
    try:
        account = argv[1] if len(argv) > 1 else "natgeo"
        quote_author = argv[2] if len(argv) > 1 else "Snoop Dogg"
        language = argv[3] if len(argv) > 1 else "en"
    except:
        language = "en"
        
    # Get the picture to work with
    picture = getInstagramFile(str(account))
    
    # Get the quote
    quoteL = []
    quote, lenght = getQuote(str(quote_author), language)

    
    # Split the quote in two equal parts, by words
    quoteL.append(" ".join(quote.rsplit(" ")[:int(lenght/2)]))
    quoteL.append(" ".join(quote.rsplit(" ")[int(lenght/2):]))
    
    # Write the text on the image
    image = writeOnImage(picture,quoteL)
    
    # When finished, open the image to see
    os.system(os.path.join(wd,image))
    exit("All done, goodbye!")


if __name__ == '__main__':
    """
    This is the main call
    """
    main()
