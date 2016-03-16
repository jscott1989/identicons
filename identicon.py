
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

def get_image(filename, search_string, digest, transparent=True):
    # if transparent:
        # search_string += " transparent"
    if transparent:
        return image_search(search_string, 0, transparent)
    else:
        return image_search(search_string, ord(digest[1]) % 14, transparent)

def generate_identicon(str):

    h = hashlib.md5(str)
    digest = h.digest()
    background_digest = digest[:8]
    foreground_digest = digest[:8]
    img = get_image("background.png", background_strings[ord(background_digest[0]) % 14], background_digest, False)
    img_w, img_h = img.size
    background = Image.new('RGBA', (1000, 1000), (255, 255, 255, 255))

    bg_w, bg_h = background.size
    offset = ((bg_w - img_w) / 2, (bg_h - img_h) / 2)
    background.paste(img, offset)

    try:
        img = get_image("foreground.png", str, foreground_digest)
    except:
        img = get_image("foreground.png", foreground_strings[ord(foreground_digest[0]) % 14], foreground_digest)
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

    # background.thumbnail((200, 200))

    background.save('%s.png' % str)
generate_identicon("jscott1989")

for n in [
    "admin",
    "mydaemon",
    "hectorhamilton",
    "rwejuli",
    "nawar",
    "panos",
    "lanzures",
    "iliketosneeze",
    "plavixo",
    "charlie",
    "john",
    "priyankasingh",
    "DevasenaInupakutika",
    "AlanPonce",
    "Mikec",
    "victor",
    "krongboon",
    "plutorial",
    "olorogun_gatsby",
    "ashahmali",
    "lloyd",
    "divya",
    "leesavage09",
    "aprilush",
    "andrew",
    "luke",
    "shahreeza_safiruz",
    "amber",
    "andrew2",
    "tunde",
    "NeoSilky",
    "Jetroid",
    "ian",
    "mikejewell",
    "tsg1g13",
    "sarahbeharry",
    "xc9e14",
    "nathan",
    "ketan",
    "elomatt",
    "maimuna",
    "Matt",
    "NickT",
    "zhelyazko",
    "rikkiprince",
    "Landric",
    "david",
    "Eoin",
    "karen",
    "Shirlyn",
    "toby",
    "Adimote",
    "XXX",
    "metin",
    "steppers",
    "ravigoyal",
    "ben",
    "ElliotJH",
    "tom",
    "nikola",
    "Jeremy",
    "sy3298444",
    "ahmed",
    "marcus",
    "kay",
    "Chetan",
    "pablo",
    "carlos",
    "yiannis",
    "Mr_Foulkes",
    "imran",
    "abcKelvin",
    "asim",
    "alan",
    "alan2",
    "ads04r",
    "annabel",
    "emmanuel",
    "henry",
    "fatma2",
    "blake",
    "jimmy",
    "henco",
    "prasoc",
    "elham",
    "sean1985zc",
    "jmpe2g11",
    "el",
    "norbert",
    "george",
    "tetiana",
    "msp301",
    "nPlus",
    "stanislav2",
    "Rebroser",
    "fatma",
    "harpolea",
    "stanislav",
    "bryan",
    "holyone2",
    "aAndzans",
    "sparkyair",
    "tedigc",
    "gcjensen",
    "saroj",
    "mahdi",
    "xiyun",
    "ivaylo",
    "petar",
    "globalkeith",
    "fractalysefiend",
    "richardtomsett",
    "umang",
    "fernalizael",
    "richard",
    "henry2",
    "alper",
    "jem1g13",
    "martin",
    "lu",
    "sihong",
    "fchandra",
    "nahser",
    "afridi",
    "james",
    "q",
    "awezan",
    "cnlizeyu",
    "medo007",
    "joseph_w.",
    "loko",
    "saber",
    "prince",
    "roy",
    "lee",
    "andrew3",
    "AdrianRoe",
    "dcurrie",
    "adam",
    "mrj",
    "sebastian",
    "PaulT",
    "yuan",
    "Skybound1",
    "ldibanyez",
    "peter",
    "drewwestcott",
    "Tetiana12345678",
    "noureldien",
    "anly2",
    "brodders61",
    "sminny",
    "josh",
    "pra",
    "mark",
    "jenny",
    "qing",
    "Hardeep_Chahal",
    "ben2",
    "Serban",
    "iain",
    "sasan-m",
    "sadegh",
    "rp10g13",
    "fyakeel",
    "hc1u14",
    "MonsterCode8000",
    "charles",
    "jemeson007",
    "rkh2n14",
    "sam",
    "vimal",
    "lb18g12",
    "ym3y14",
    "Patient0",
    "szymon",
    "alex",
    "karunakar",
    "me_gone_mad1",
    "KacperW",
    "JPML",
    "kierdavis",
    "rk13g15",
    "bloosk84fun",
    "maciej",
    "Berry-95",
    "Gkjt",
    "cjthorne",
    "abhishekgaloda",
    "Teza",
    "badmus",
    "Shuayb2001",
    "AndyBS",
    "MartinReid",
    "saw1g15",
    "gb4g15",
    "toby2",
    "keith",
    "Faranak",
    "mateusz",
    "darcy",
    "Lakshays",
    "dawei",
    "jw14g15",
    "joel44321",
    "alitwin",
    "Lnicky",
    "Xplicit",
    "bothersMcBitey",
    "AnonymHax",
    "asfnemo",
    "BogdanL",
    "ccheung",
    "mikeyredtiger22",
    "antonnikitin97",
    "me_gone_mad12",
    "Felix_christ",
    "Keletso",
    "andreadoli",
    "bc5g15",
    "fredtargaryen",
    "jeffrey",
    "superwool",
    "willmac",
    "MattGreyDesign",
    "redoc",
    "nabeelkabour",
    "Jamie-",
    "ventsislaf",
    "asher",
    "ola",
    "PrestonAWH",
    "oew1v07",
    "aaronsear",
    "zxuan",
    "rat1g15",
    "tn1g15",
    "Lewis_xiao",
    "mjhunter",
    "ZFundamental",
    "luna",
    "mspraggs",
    "synes",
    "jscott1989",
    "Tmzhao",
    "harrybeadle",
    "njr2g15",
    "houhaichao830",
    "alex89",
    "Nora",
    "holyjoly",
    "jgpg1g14",
    "huwcbjones",
    "hannah",
    "bigboateng",
    "tjd1g15",
    "blueteeth",
    "bm6g14",
    "hhc553169030",
    "brian",
    "shamuric",
    "channerduan",
    "zuladli",
    "sp16g14",
    "adam2",
    "XeroreX",
    "ljayb118",
    "emm1g12",
    "moumou",
    "yzj3232185",
    "Kanter666",
    "ai1v14",
    "sb2g14",
    "ng1v14",
    "eipin14",
    "simontudge",
    "TheCommieDuck",
    "sim",
    "apd1g14",
    "Genericblackkid"]:
        generate_identicon(n)