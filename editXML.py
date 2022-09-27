import xml.etree.ElementTree as ET
import lxml.etree as le
from lxml import etree


### Working through https://lxml.de/tutorial.html to better grasp editing xml with python for updating scripting for metadata

root = etree.Element("root")
root.append(etree.Element("child1"))
print(root.tag)
child2=etree.SubElement(root, "child2")
child3=etree.SubElement(root, "child3")
print(etree.tostring(root, pretty_print=True))
child=root[0]
print(child.tag)
root.index(root[1])
children=list(root)
print(children)
for child in root:
    print(child.tag)
root.insert(0, etree.Element("child0"))
start = root[:1]
end = root[-1:]
print(start[0].tag)
print(end[0].tag)

print(etree.iselement(root))#tests if it is some kind of Element

if len(root):
    print("The root element has children")
print(root[0])  
root[0]=root[-1]
for child in root:
    print(child.tag)
root is root[0].getparent()
"""
element=etree.Element("neu")
element.append(deepcopy(root[1]))
print (element[0].tag)
print([c.tag for c in root])
"""
root[0] is root[1].getprevious()
root[1] is root[0].getnext()

root=etree.Element("root", interesting="totally")#This section is interesting I want to see if I can use this then count the number of dates aka children for the mdattim element
etree.tostring(root)
print(root.get("interesting"))

print(root.get("hello"))
root.set("hello","huhu")
print(root.get("hello"))

etree.tostring(root)
sorted(root.keys())
for name, value in sorted(root.items()):
    print('%s=%r'%(name, value))

attributes = root.attrib
print(attributes["interesting"])
print(attributes.get("no-such-attribute"))
attributes["hello"]= "gluten tag" # lol typo
print(attributes["hello"])
print(root.get("hello"))
d=dict(root.attrib)
print(sorted(d.items()))

root = etree.Element("root")
root.text="TEXT"
print(root.text)
print(etree.tostring(root))

html=etree.Element("html")
print(etree.tostring(html))
body = etree.SubElement(html,"body")
print(etree.tostring(html))
body.text="TEXT"
print(etree.tostring(html))
br=etree.SubElement(body, "br")
print(etree.tostring(html))
br.tail="TAIL"
print(etree.tostring(html))

print(etree.tostring(br))
print(etree.tostring(br, with_tail=False))
print(etree.tostring(html, method="text"))

#Using XPath to find text
print(html.xpath("string()"))
print(html.xpath("//text()"))
build_text_list=etree.XPath("//text()")#put it into a function
print(build_text_list(html))



for i in range(1,100):
    if i % 15 == 0:
        print ("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)



a=[0,0,0,0,1,1,1,1,2,2,2,3,3,3,4,4,4,5]#length -1 because we start by looking at second in list
for i in range(len(a)-1,0,-1):#start at length of A-1, stop at 0, move back 1 each time
    if a[i] == a[i-1]:
        del a[i]
        print (a)
print (a)

n = 100
fib=[0, 1]
print(fib)
for i in range(1,20):
    sum=(fib[i-1]+fib[i])
    fib.append(sum)
print (fib)


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
"""
tree = ET.parse('time.xml')
root = tree.getroot()
print(root)

rank=root.find('mdattim')
print (rank)
type(root.findall('mdattim'))
print(root.findall('mdattim'))
for date in root.findall('mdattim'):
    print("dkjalsdf;jkl;")
    if date == 1:
        print("delete me ")
    else:
        print("all good")

print("hello?")

"""
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








