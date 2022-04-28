import mechanize

def download_spate_bibliography():
    # Get URL of Centaur advanced search
    url = "https://centaur.reading.ac.uk/cgi/search/advanced"

    # Setup a browser
    br = mechanize.Browser()
    br.set_handle_robots(False)
    br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

    # Open Centaur
    br.open(url)

    # Search form is the 0th form. Select and fill in the author list and select Dpt of Meteorology.
    br.select_form(nr=0)
    br['nas_multiname_merge'] = ['ANY']
    br['nas_multiname'] = "Lockwood, M. Owens, M. Scott, C. Harrison, R. Nicoll, K. Airey, M. Barnard, L."
    br['nas_school']=["5_c6358d36",]
    # Submit the search
    br.submit(nr=0) 

    # On the response, now select the form for selecting download format, select HTML and download.
    br.select_form(nr=1)
    br['output'] = ["HTML",]
    resp = br.submit()

    # Write the HTML to file.
    with open("spate_bibliography.html", 'w', encoding="utf-8") as file:
        file.write(resp.read().decode("utf-8"))
        
    return

if __name__ == "__main__":
    download_spate_bibliography()