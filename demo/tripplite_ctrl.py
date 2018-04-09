#!/usr/bin/env python
#
# Last Change: Mon Apr 09, 2018 at 12:10 AM -0400

import sys
from os.path import dirname, abspath, join

from pysnmp.hlapi import *
from pysnmp.smi import builder, view, compiler

# The absolute path of the mib files
mib_path = 'file://' + join(
    dirname(dirname(abspath(__file__))), 'labSNMP', 'MIB', 'Tripp_Lite')

# Compile mib
mibBuilder = builder.MibBuilder()
mibViewController = view.MibViewController(mibBuilder)
compiler.addMibCompiler(mibBuilder, sources=[
    mib_path,
    'http://mibs.snmplabs.com/asn1/@mib@'])

# Load mib
mibBuilder.loadModules('TRIPPLITE-PRODUCTS')

# Get the name of the SMTP command that will be executed
cmd = ObjectIdentity('TRIPPLITE-PRODUCTS', sys.argv[1], 0)

# Perform lookup
g = getCmd(SnmpEngine(),
           CommunityData('tripplite'),
           UdpTransportTarget((sys.argv[2], 161)),
           ContextData(),
           ObjectType(cmd))
print(next(g))

# Printout the result
print(str(cmd))