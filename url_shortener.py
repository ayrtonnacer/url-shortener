import pyshorteners

def shorten_url():
    """
    Prompts the user for a URL, shortens it using TinyURL, and displays the result.
    """
    # Ask the user to input a link
    link = input("Enter a link to shorten:\nThe link is as follows: ")

    # Shorten the link
    shortener = pyshorteners.Shortener()  
    short_link = shortener.tinyurl.short(link)  

    # Display the result
    print("\nResult:")
    print(f"Original URL: {link}")
    print(f"Shortened URL: {short_link}")


if __name__ == '__main__':
    shorten_url()
