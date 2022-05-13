# -*- coding: utf-8 -*-

"""

* https://cdnjs.com/libraries
* https://unpkg.com/#/
"""

import os
from os import path as osp
import shutil
import requests
from pygments.formatters import get_formatter_by_name

ABSPATH = os.path.dirname( os.path.abspath( __file__) )
resources_path =  osp.join( ABSPATH , "resources")
vendor_path = osp.join( resources_path, "vendor")
tests_vendor_path = osp.join( ABSPATH, "tests", "resources" ,"vendor")

vendors = [
	"d3",
	"fonts",
	"material",
	"paho-mqtt",
	"pygment",
	"ace",
    "st",
    "vuejs"
]

resources = [
	
    { "from":"https://cdnjs.cloudflare.com/ajax/libs/d3/5.7.0/d3.min.js", "to":"d3/d3-5.7.0.min.js", "typ":"text" },
    
    { "from":"https://cdnjs.cloudflare.com/ajax/libs/paho-mqtt/1.1.0/paho-mqtt.min.js", "to":"paho-mqtt/paho-mqtt-1.1.0.min.js", "typ":"text" },
    
    # MaterialDesign-Webfont
    { "from":"https://cdnjs.cloudflare.com/ajax/libs/MaterialDesign-Webfont/5.8.55/css/materialdesignicons.min.css", "to":"material/materialdesignicons.min.css", "typ":"text" },
    
    { "from":"https://cdnjs.cloudflare.com/ajax/libs/MaterialDesign-Webfont/5.8.55/fonts/materialdesignicons-webfont.eot", "to":"fonts/materialdesignicons-webfont.eot", "typ":"bin" },
    { "from":"https://cdnjs.cloudflare.com/ajax/libs/MaterialDesign-Webfont/5.8.55/fonts/materialdesignicons-webfont.ttf", "to":"fonts/materialdesignicons-webfont.ttf", "typ":"bin" },
    { "from":"https://cdnjs.cloudflare.com/ajax/libs/MaterialDesign-Webfont/5.8.55/fonts/materialdesignicons-webfont.woff", "to":"fonts/materialdesignicons-webfont.woff", "typ":"bin" },
    { "from":"https://cdnjs.cloudflare.com/ajax/libs/MaterialDesign-Webfont/5.8.55/fonts/materialdesignicons-webfont.woff2", "to":"fonts/materialdesignicons-webfont.woff2", "typ":"bin" },
    
    # materialicons
    { "from":"https://fonts.gstatic.com/s/materialicons/v102/flUhRq6tzZclQEJ-Vdg-IuiaDsNc.woff2", "to":"fonts/materialicons-webfont.woff2", "typ":"bin" },
    { "from":"https://github.com/google/material-design-icons/blob/master/font/MaterialIcons-Regular.ttf?raw=true", "to":"fonts/materialicons-webfont.ttf", "typ":"bin" },
    
    # ace
    { "from":"https://cdnjs.cloudflare.com/ajax/libs/ace/1.4.12/ace.min.js", "to":"ace/ace-1.4.12.min.js", "typ":"text" },
    { "from":"https://cdnjs.cloudflare.com/ajax/libs/ace/1.4.12/mode-text.min.js", "to":"ace/mode-text.js", "typ":"text" },
   	{ "from":"https://cdnjs.cloudflare.com/ajax/libs/ace/1.4.12/mode-json.min.js", "to":"ace/mode-json.js", "typ":"text" },
   	{ "from":"https://cdnjs.cloudflare.com/ajax/libs/ace/1.4.12/worker-json.min.js", "to":"ace/worker-json.js", "typ":"text" },
   	{ "from":"https://cdnjs.cloudflare.com/ajax/libs/ace/1.4.12/mode-markdown.min.js", "to":"ace/mode-markdown.js", "typ":"text" },
   	{ "from":"https://cdnjs.cloudflare.com/ajax/libs/ace/1.4.12/theme-twilight.min.js", "to":"ace/theme-twilight.js", "typ":"text" },
   	{ "from":"https://cdnjs.cloudflare.com/ajax/libs/ace/1.4.12/ext-beautify.min.js", "to":"ace/ext-beautify.min.js", "typ":"text" },

    # vue 3
    { "from":"https://cdn.jsdelivr.net/npm/vue@3/dist/vue.global.js", "to":"vuejs/vue-3.x.js", "typ":"text" },
    { "from":"https://cdn.jsdelivr.net/npm/vue@3/dist/vue.global.prod.js", "to":"vuejs/vue-3.x.min.js", "typ":"text" },
  
    # .vue sfc loader
    { "from":"https://cdn.jsdelivr.net/npm/vue3-sfc-loader@0.8.4/dist/vue3-sfc-loader.js", "to":"vuejs/vue3-sfc-loader.js", "typ":"text" },
  
    # 
    # quasar
    { "from":"https://cdn.jsdelivr.net/npm/quasar@2.6.2/dist/quasar.umd.prod.js", "to":"vuejs/quasar-2.x.umd.prod.js", "typ":"text" },
    { "from":"https://cdn.jsdelivr.net/npm/quasar@2.6.2/dist/lang/de.umd.prod.js", "to":"vuejs/quasar-de-2.x.umd.prod.js", "typ":"text" },
    { "from":"https://cdn.jsdelivr.net/npm/quasar@2.6.2/dist/quasar.prod.css", "to":"vuejs/quasar-2.x.prod.css", "typ":"text" },

    # pinia
    { "from":" https://unpkg.com/pinia@2.0.12/dist/pinia.iife.prod.js", "to":"vuejs/pinia-2.x.prod.js", "typ":"text" },
    { "from":" https://unpkg.com/pinia@2.0.12/dist/pinia.iife.js", "to":"vuejs/pinia-2.x.js", "typ":"text" },


    # router
    { "from":"https://unpkg.com/vue-router@4.0.14/dist/vue-router.global.js", "to":"vuejs/vue-router.global-4.x.js", "typ":"text" },

    # vuelidate
    { "from":"https://cdn.jsdelivr.net/npm/vue-demi", "to":"vuejs/vue-demi-0.12.x.min.js", "typ":"text" },
    { "from":"https://cdn.jsdelivr.net/npm/@vuelidate/core", "to":"vuejs/vuelidate-0.7.x.min.js", "typ":"text" },
    { "from":"https://cdn.jsdelivr.net/npm/@vuelidate/validators", "to":"vuejs/validators-0.7.x.min.js", "typ":"text" },
   

]

pygments = {"class": "codehilite", "to":"pygment/codehilite.css"}
materialize = {"from":"https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/css/materialize.css", "to":"material/materialize-colors.css", "typ":"text", "before":"/*! normalize.css" }

#
# start copy resources
#

print("create vendor path", vendor_path)

errors = 0
if not os.path.exists( vendor_path ):
    try:
        os.makedirs( vendor_path )
    except IOError as e:
        errors += 1
        print("Unable to create dir.", e)

# create all vendor paths
for vendor in vendors:
	if not os.path.exists( osp.join(vendor_path, vendor) ):
		try:
			os.makedirs( osp.join(vendor_path, vendor) )
		except IOError as e:
			print("Unable to create dir.", e)

for resource in resources:
    print("loading:", resource["from"])
    resource_to =  osp.join( vendor_path, resource["to"] )
    response = requests.get( resource["from"] )
    if resource["typ"] == "text":
        try:
            with open(resource_to, "w") as f:
                f.write(response.text)
        except IOError as e:
            print("Unable to create file.", e)
    elif resource["typ"] == "bin":
        try:
            with open(resource_to, "wb") as f:
                f.write(response.content)
        except IOError as e:
            print("Unable to create file.", e)

#
# get colors from materialize
#
print("get named-colors from materialize:", materialize["from"])
response = requests.get( materialize["from"] )
#
pos = response.text.find( materialize["before"] )
# print( response.text[ : pos ] )
try:
    pos = response.text.find( materialize["before"] )
    with open(osp.join(vendor_path, materialize["to"]), "w") as f:
        f.write(response.text[ : pos ] )
except IOError as e:
    print("Unable to create file.", e)

'''
..TODO:: material-color to vendor/material/

    https://github.com/mrmlnc/material-color
'''

#
# create pygments css rules for codehilite
#
print("create pygments/codehilite.css with pygments")
fmter = get_formatter_by_name("html", style="default")
css_content = fmter.get_style_defs( ".{}".format(pygments["class"]) )
try:
    with open( osp.join(vendor_path, pygments["to"]), "w") as f:
        f.write(css_content)
except IOError as e:
    print("Unable to create file.", e)


#
# create vendor in tests/recources
# 
print("create tests/resources/vendor and copy needed dirs")
if not os.path.exists( tests_vendor_path ):
    try:
        os.makedirs( tests_vendor_path )
    except IOError as e:
        errors += 1
        print("Unable to create dir.", e)

#
# copy needed vendor dirs to tests/recources/vendor
#

sub_dirs = [
    "fonts",
    "material",
    "pygment"
]

for sub_dir in sub_dirs:
    src = osp.join(vendor_path, sub_dir)
    dst = osp.join(tests_vendor_path, sub_dir)
   
    if os.path.exists( dst ):
        shutil.rmtree( dst )
        
    try:
        shutil.copytree(src, dst)
    except IOError as e:
        errors += 1
        print("Unable to copy dir {}.".format( dst ), e)

#
# print result
#
if errors > 0:
    print( "Installation error." )

else:
    print('''
    Run as sudo to copy materialdesignicons_webfont to your system fonts:

> sudo cp ./resources/vendor/fonts/materialdesignicons-webfont.ttf /usr/share/fonts/truetype/materialdesignicons_webfont.ttf
> sudo chmod 644 /usr/share/fonts/truetype/materialdesignicons_webfont.ttf
''')

