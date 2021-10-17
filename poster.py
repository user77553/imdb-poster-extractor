import requests
import re
import urllib.request

link = input("Enter IMDb link: ")
if link:
    f = requests.get(link)

    # get mediaviewer link
    output = re.search('<a class="ipc-lockup-overlay ipc-focusable" href="(.*?)"', f.text, flags=re.IGNORECASE)
    if output is not None:
        output = output.group(0)

    output = re.search('\/.+\/', output, flags=re.IGNORECASE)
    if output is not None:
        output = output.group(0)
    link = "https://www.imdb.com/" + output
    f = requests.get(link)

    # get image url
    output = re.search('<img(.*?)src=(.*?)"\/>', f.text, flags=re.IGNORECASE)
    if output is not None:
        output = filename = output.group(0)

    output = re.findall('src="(.*?)"', output, flags=re.IGNORECASE)
    link = output[-1]

    output = re.findall('alt="(.*?)"', filename, flags=re.IGNORECASE)
    filename = output[-1]
    filename = filename.replace(" ", ".")
    filename = filename.replace("(", "")
    filename = filename.replace(")", "") + ".jpg"

    urllib.request.urlretrieve(link, filename)
    print(filename + " downloaded successfully.")
