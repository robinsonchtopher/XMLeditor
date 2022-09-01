import xml.etree.ElementTree as ET
import lxml.etree as le

#The goal for this program is to search through a folder of XMLs
#look at each XML and identify if it has the mdattim Element
#If it does  check the number of sngdate elements
#if the number is exactly one, delete the mdattim element from the file

#End goal, give this code a path to the folder of XMLs, make a report of things changed.

#for i in tile_index
#open filename (i)
 # for j in <sngdate> #value in xml we want to update

#    if <sngdate> in dictionary.i
      #no change
#    else
      #delete sngdate, caldate, /sngdate


#sf = shapefile.Reader("shapefiles/blockgroups.shp")

tree = ET.parse('time.xml')
root = tree.getroot()
print(root)

rank=root.find('mdattim')
print (rank)
for date in root.findall('mdattim'):
    print("dkjalsdf;jkl;")
    if date == 1:
        print("delete me ")
    else:
        print("all good")

print("hello?")


"""
print("hell")
tree = ET.parse('time.xml')
root= tree.getroot()
#print(root.findall('caldate'))
group = root.find('timeinfo')
print(group)

print(group.findall('sngdate'))
print(root.findall(".//sngdate"))
"""
"""
with open('time.xml','r') as f:
    doc=le.parse(f)
    for elem in doc.xpath('//*[caldate]'):
        print("look here")
        print(elem)
        for subelement in elem:
            if
            print("good!")
        else:
            print("this bad")
"""





        #for i in group
        #root.remove
#    print("text")
#    print(caldate)
  #if date not in #list of dates
    #root.remove(i)
#print("hellno")
"""
root.findall(".//sngdate")


tree.write('output.xml')
"""
