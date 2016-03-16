
import urllib
import urllib2
import json

from PIL import Image
import urllib2 as urllib
import io
import hashlib

# Bing API key
API_KEY = "iMCYf9GiK+QFcfGDspHWbRUuyePrL3c+N4XIoo8Nh4Q"

def bing_search(query, search_type):
    #search_type: Web, Image, News, Video
    key= "iMCYf9GiK+QFcfGDspHWbRUuyePrL3c+N4XIoo8Nh4Q"
    query = urllib.quote(query)
    # create credential for authentication
    user_agent = 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; FDM; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 1.1.4322)'
    credentials = (':%s' % key).encode('base64')[:-1]
    auth = 'Basic %s' % credentials
    url = 'https://api.datamarket.azure.com/Data.ashx/Bing/Search/'+search_type+'?Query=%27'+query+'%27&$top=15&$format=json'
    request = urllib2.Request(url)
    request.add_header('Authorization', auth)
    request.add_header('User-Agent', user_agent)
    request_opener = urllib2.build_opener()
    response = request_opener.open(request)
    response_data = response.read()
    json_result = json.loads(response_data)
    result_list = json_result['d']['results']
    return result_list

def image_search(searchterm,n,transp=True):
    pictures = bing_search(searchterm,'Image')
    image = pictures[n]
    url = image["MediaUrl"]

    try:
        fd = urllib.urlopen(url)
    except:
        return image_search(searchterm,n+1,transp=True)

    image_file = io.BytesIO(fd.read())
    try:
        im = Image.open(image_file)
        return im
    except:
        return image_search(searchterm,n+1,transp=True)

    return image_file

background_strings = [
    "space",
    "beach",
    "park",
    "desert",
    "forest",
    "ice",
    "factory",
    "road",
    "building",
    "office",
    "city",
    "japan",
    "america",
    "castle",
    "monument"
]

foreground_strings = [
    "person",
    "clown",
    "family",
    "dancer",
    "sportsperson",
    "programmer",
    "dolphin",
    "dinosaur",
    "computer",
    "bus",
    "car",
    "monster",
    "alien",
    "food",
    "mime"
]

def get_image(filename, strings_list, digest, transparent=True):
    search_string = strings_list[ord(digest[0]) % 14]
    if transparent:
        search_string += " transparent"
    return image_search(search_string, ord(digest[1]) % 14, transparent)

def generate_identicon(str):

    h = hashlib.md5(str)
    digest = h.digest()
    background_digest = digest[:8]
    foreground_digest = digest[:8]

    img = get_image("background.png", background_strings, background_digest, False)
    img_w, img_h = img.size
    background = Image.new('RGBA', (1000, 1000), (255, 255, 255, 255))

    bg_w, bg_h = background.size
    offset = ((bg_w - img_w) / 2, (bg_h - img_h) / 2)
    background.paste(img, offset)

    img = get_image("foreground.png", foreground_strings, foreground_digest)
    x_size = (sum(ord(f) for f in foreground_digest[1:4]) % 400) + 400
    y_size = x_size
    img.thumbnail((x_size, y_size))

    x_offset = sum(ord(f) for f in foreground_digest[1:4]) % (1000 - x_size)
    y_offset = sum(ord(f) for f in foreground_digest[5:]) % (1000 - y_size)

    offset = (x_offset, y_offset)
    try:
        background.paste(img, offset, img)
    except:
        background.paste(img, offset)

    background.thumbnail((200, 200))

    background.save('%s.png' % str)


generate_identicon("Jonathan Scott")
generate_identicon("Rikki Prince")
generate_identicon("3")
generate_identicon("4")
generate_identicon("5")