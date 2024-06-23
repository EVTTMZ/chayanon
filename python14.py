"""
#
# Part: Python PIP
#
"""

#pip list
#python .exe -m pip install  --upfrade pip 
#pip insatll camelcase

import camelcase
camel = camelcase.Camelcase()
txt = "hello wolrd"
print(camel.hump(txt))

