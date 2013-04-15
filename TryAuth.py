try:
  from xml.etree import ElementTree
except ImportError:
  from elementtree import ElementTree
import gdata.calendar.data
import gdata.calendar.client
import gdata.acl.data
import atom.data
import time


client = gdata.calendar.client.CalendarClient(source='softdesproject')
client.ClientLogin('lsilverwolf7@gmail.com', "Let'sgogr33n", client.source)
