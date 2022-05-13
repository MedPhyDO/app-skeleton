# -*- coding: utf-8 -*-

import os
from os import path as osp
import json
from shutil import copyfile
from skimage import io as img_io
from skimage.util import compare_images
import numpy as np

ABSPATH = osp.dirname( osp.abspath( __file__) )

import unittest


class testCaseBase(unittest.TestCase):
    def check_pdf_data( self, data, contents=-1, pages=-1, intern_check:bool=False ):
        ''' Prüft pdf data mit vorher gespeicherten data

        Erzeugt in unittest dir auf dem Server ein dir 'check', um dort die Vergleichsdaten zu speichern

        Parameters
        ----------
        data : dict
            - content: dict
                page_names : dict
            - overlays: dict
            - pages: int
            - pdf_filename: string
            - pdf_filepath: string
            - png_filename: string
            - png_filepath: string
        contents : int
            Anzahl der Seiten im Content
        pages : int
            Anzahl der Seiten im PDF
        intern_check:
            Wenn True wird in tests und nicht im normalem pdf Ablegeort geprüft. Default is False

        Returns
        -------
        None.

        '''
        #print( data["content"].keys() )

        self.assertIn("pdf_filepath", data,
             "PDF data fehlerhaft filename fehlt"
        )
        self.assertIn("png_filepath", data,
             "PNG data fehlerhaft filepath fehlt"
        )

        check = {}

        #
        # Vorbereitungen
        #

        if intern_check == True:
            test_dir = osp.join( ABSPATH, "files", "pdf" )
            check_dir = osp.join( ABSPATH, "resources", "check" )
        else:
            test_dir = os.path.dirname( data["pdf_filepath"] )
            check_dir = osp.join( test_dir, "check" )
        

        # create the folders if not already exists
        if not osp.exists( check_dir ):
            try:
                os.makedirs( check_dir )
            except IOError as e:
                 print("Unable to create dir.", e)

        # Dateiname für den Inhalt festlegen
        json_test_name = osp.join( test_dir, data["pdf_filename"] ) + ".json"
        json_check_name = osp.join( check_dir, data["pdf_filename"] ) + ".json"

        pdf_check_name = osp.join( check_dir, data["pdf_filename"] )

        png_check_name = osp.join( check_dir, data["png_filename"] )

        png_new_name  = data["png_filepath"]

        # changeback resources path in content
        if "_variables" in data:
            json_data = json.dumps( data["content"])
           
            json_data = json_data.replace( data["_variables"]["resources"], "{{resources}}")
            json_data = json_data.replace( data["_variables"]["templates"], "{{templates}}")
            data["content"] = json.loads(json_data)
        
        # immer den content in unittest ablegen
        with open(json_test_name, "w" ) as json_file:
            json.dump( data["content"] , json_file, indent=2 )

        # beim erstenmal content nach check kopieren
        if not os.path.exists( json_check_name ):
            try:
                copyfile(json_test_name, json_check_name)
            except IOError as e:
                print("Unable to copy file.", e)

        # beim erstenmal pdf nach check kopieren
        if not os.path.exists( pdf_check_name ):
            try:
                copyfile(data["pdf_filepath"], pdf_check_name)
            except IOError as e:
                print("Unable to copy file.", e)

        # beim erstenmal png nach check kopieren
        if not os.path.exists( png_check_name ):
            try:
                copyfile(png_new_name, png_check_name)
            except IOError as e:
                print("Unable to copy file.", e)
                
        #
        # Überprüfungen
        #

        # passende check daten (json_check_name) laden
        with open( json_check_name ) as json_file:
            check = json.load( json_file )

        page_names = data["content"].keys()
        # Anzahl der Bereiche prüfen
        if contents > -1:
            self.assertEqual(
                len( page_names ),
                contents,
                "Anzahl der content Bereiche in '{}' stimmt nicht.".format( data["pdf_filepath"] )
            )
        # Namen der Bereiche
        self.assertEqual(
            page_names,
            check.keys(),
            "Namen der Bereiche '{}' stimmt nicht.".format( data["pdf_filepath"] )
        )

        # Anzahl der Seiten prüfen
        if pages > -1:
            self.assertEqual(
                data["pages"],
                pages,
                "Anzahl der Seiten in '{}' stimmt nicht.".format( data["pdf_filepath"] )
            )

        # einige content Inhalte prüfen

        from bs4 import BeautifulSoup
        for page_name, content in data["content"].items():
            bs_data = BeautifulSoup( content, 'html.parser')
            bs_check = BeautifulSoup( check[ page_name ], 'html.parser')

            # die text Bereiche
            data_text_list = bs_data.find_all('div', {"class": "text"} )
            check_text_list = bs_check.find_all('div', {"class": "text"} )

            self.assertEqual(
                data_text_list,
                check_text_list,
                "PDF content .text in '{}' ist fehlerhaft".format( data["pdf_filepath"] )
            )

        #return
        # erzeugte png vergleichen und diff speichern
        png_check = img_io.imread( png_check_name )
        png_new = img_io.imread( png_new_name )
        
        # python 3.7 - cairo 1.16.0 (https://cairographics.org) - %PDF-1.5
        #   (1120, 790, 3) tests/files/pdf/test-1.pdf
        # python 3.8 - WeasyPrint 54.0 - %PDF-1.7
        #   (1123, 794, 3) tests/files/pdf/test-1.pdf
        #   (1123, 794, 4) 
        
        # check only size not depth
        self.assertEqual(
            list(png_check.shape)[:2], 
            list(png_new.shape)[:2], 
            "Die Bildgrößen in '{}' stimmen nicht.PDF files:\n{}\n{}".format( 
                data["pdf_filepath"],
                data["pdf_filepath"],
                pdf_check_name
            )
        )

        # Bild verleich erstellen und speichern
        compare = compare_images(png_check, png_new, method='diff')
        img_io.imsave( png_new_name + ".diff.png",  compare )

        # gesamt check der Bilder
        def check_mse(imageA, imageB):
        	# the 'Mean Squared Error' between the two images is the
        	# sum of the squared difference between the two images;
        	# NOTE: the two images must have the same dimension
        	err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
        	err /= float(imageA.shape[0] * imageA.shape[1])

        	# return the MSE, the lower the error, the more "similar"
        	# the two images are
        	return err

        # MeanCheck durchführen
        try:
            mse = check_mse( png_check, png_new )
        except:
            mse = -1

        # small changes depends on diffrent font rendering
        le = 350.0
        le = 100
        self.assertLessEqual( mse, le,
            "Der PNG Vergleichsbild MSE stimmt nicht. Diff image '{}' prüfen. PDF files:\n{}\n{}".format( 
                data["png_filepath"] + ".diff.png",
                data["pdf_filepath"],
                pdf_check_name
            )
        )