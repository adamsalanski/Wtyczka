# -*- coding: utf-8 -*-
"""
/***************************************************************************
 WtyczkaASDialog
                                 A QGIS plugin
 Projekt nr 2 Informatyka
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2023-06-09
        git sha              : $Format:%H$
        copyright            : (C) 2023 by Adam Sałański, Łukasz Floryszczyk, Sebastian Królik
        email                : adam.salanski1234@gmail.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

import os

from qgis.PyQt import uic
from qgis.PyQt import QtWidgets
from qgis.utils import iface
import numpy as np

# This loads your .ui file so that PyQt can populate your plugin with the elements from Qt Designer
FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'Wtyczka_AS_dialog_base.ui'))


class WtyczkaASDialog(QtWidgets.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        """Constructor."""
        super(WtyczkaASDialog, self).__init__(parent)
        # Set up the user interface from Designer through FORM_CLASS.
        # After self.setupUi() you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        self.setupUi(self)
        self.Policz_roznice_wysokosci.clicked.connect(self.roznica_wysokosci)
        self.Policz_pole.clicked.connect(self.pole)
        
    def roznica_wysokosci(self):
        aktywna_warstwa = iface.activeLayer()
        zaznaczone_punkty = aktywna_warstwa.selectedFeatures()
        if len(zaznaczone_punkty) != 2:
            iface.messageBar().pushMessage('Aby przeprowadzić tę operację trzeba\nzaznaczyć dokładnie 2 punkty')
            self.Wyniki.setText('Aby przeprowadzić tę operację trzeba\nzaznaczyć dokładnie 2 punkty')
        else:
            out_str = f"""Wybrane punkty:
            Punkt numer {zaznaczone_punkty[0][0]}, wysokość: {zaznaczone_punkty[0][1]}m
            Punkt numer {zaznaczone_punkty[1][0]}, wysokość: {zaznaczone_punkty[1][1]}m
            Różnica wysokości wynosi {round(abs(float(zaznaczone_punkty[0][1]) - float(zaznaczone_punkty[1][1])), 2)}m
            """
            self.Wyniki.setText(out_str)
    
        
    
        
                
    def pole(self):
        aktywna_warstwa = iface.activeLayer()
        zaznaczone_punkty = aktywna_warstwa.selectedFeatures()
        liczba_zaznaczonych_elementów = len(zaznaczone_punkty)
        X = []
        Y =[]
        
        if liczba_zaznaczonych_elementów > 2:
            for feature in zaznaczone_punkty:
                geom = feature.geometry()
                y = geom.asPoint().y()
                x=geom.asPoint().x()
                X.append(x)
                Y.append(y)
            pole = 0.5*np.abs(np.dot(X,np.roll(Y,1))-np.dot(Y,np.roll(X,1)))
            self.Wyniki.setText(f"Pole jest równe {'''%7.0f''' % abs(pole)} m^2")
        else:
            self.Wyniki.setText(f"Podales zbyt malo punktow, podaj\nminimum 3 punkty")
        
    
    
                
    
       
            

    
            
    
    
      
    
    
        
        
        
        
        
        
        
        
        
        
        
        
        
