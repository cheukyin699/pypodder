import urllib.request as ur
import xml.etree.ElementTree as ET

def getXML(url):
    '''
    Using the url, gets the XML file
    @param url The url string
    @return The XML parsed file
    '''
    h = ur.urlopen(url)
    return ET.fromstring(h.read())

def fileList(root):
    '''
    Extracts the URL of MP3 file, along with the title, into a list of tuples
    @param root The root XML node
    @return A list of tuples
    '''
    ret = []
    for i in root[0].findall('item'):
        title = i.findall('title')[-1].text
        mp3 = i.findall('enclosure')[-1].attrib['url']
        ret.append((title, mp3))

    return ret

def downloadFile(url, fn):
    '''
    Using the url, gets and downloads the (MP3) file.
    @param url The url string
    @param fn The target filename
    '''
    ur.urlretrieve(url, fn)
