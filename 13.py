#!/usr/bin/env python
#title: call him
#hint1: phone that evil
#hint2: link to phonebook.php
#fact1: level 12's 4th fact said that "Bert is evil"
#fact2: phonebook.php returns an XMLRPC error
import xmlrpclib
server = xmlrpclib.Server('http://www.pythonchallenge.com/pc/phonebook.php')
# we'll need to discover Server API
print server.system.listMethods()
print server.phone('Bert')
# Solution: italy

# Added for Level 17
print server.phone('Leopold')
# Solution: violin
