# -*- coding: utf-8 -*-

'''
Das eigentliche starten der app wird über run erledigt

'''

import logging

from isp.config import ispConfig

from app.db import dbtests

from isp.webapp import ispBaseWebApp
from isp.safrs import system, db
class system( system ):
    
    @classmethod
    def _extendedSystemCheck(self):
        """filled Stub Function for api_list (Systeminformationen)
        
        Returns
        -------
        dict, string
        
        """
        import os
        import json
        config = ispConfig()
        html = "<h4>System Check</h4>"
        
        # --------------- MQTT
        mqtt_config = config.get( "server.mqtt" )
        mqtt_config_copy = mqtt_config.copy()
        mqtt_config_copy.password = "********"
        if mqtt_config_copy.get("host", "") == "":
            html += '<div class="alert alert-info" >MQTT deaktiviert'
        else:
            html += '<div class="alert alert-dark" >Prüfe <span class="badge badge-info">server.mqtt</span> - Konfiguration:'
            html += '<pre>{}</pre>'.format( json.dumps( mqtt_config_copy.toDict(), indent=2 ) )
            
            mqtt = config.mqttGetHandler()
            if not mqtt:
                info_class = "danger"   
                info_text = "MQTT Zugriff ist nicht möglich."
            else:    
                info_class = "info"   
                info_text = 'MQTT Zugriff ist eingerichtet. <button type="button" class="btn btn-primary" onClick="mqttTest( this )">Prüfen</button>'
                 
            html += '<div id="MQTT-checkline" class="alert alert-{} ">{}<div id="MQTT-results" class"alert"></div></div>'.format( info_class, info_text ) 
            
        html += "</div>"
        html += '''
            <script>
            var box = document.querySelector("#MQTT-checkline");
            var result_box = document.querySelector("#MQTT-results");
            if ( typeof app.clientMqtt === "object" ) {
                app.clientMqtt.subscribe( "MQTT/test", function( msg ) {
                    box.className = "alert alert-success";
                    result_box.className = "alert alert-success";
                    result_box.innerHTML = "MQTT Test erfolgreich";
                } );      
            }
            function mqttTest( btn ){
                box.className = "alert alert-info";
                result_box.className = "";
                   
                if ( typeof app.clientMqtt === "object" ) {
                    result_box.className = "alert alert-danger";
                    result_box.innerHTML = "MQTT Test nicht erfolgreich.";
                    app.clientMqtt.publish( "MQTT/test", { "test":"MQTT" } );
                } else {
                    result_box.className = "alert alert-warning";
                    result_box.innerHTML = "kein clientMqtt vorhanden";
                } 
            }
            </script>
        '''
        return {}, html

# -----------------------------------------------------------------------------      
def run( overlay:dict={} ):
    ''' Startet ispBaseWebApp mit zusätzlichen config Angaben
    
    Parameters
    ----------
    overlay : dict, optional
        Overlay Angaben für config. The default is {}.

    Returns
    -------
    webApp : ispBaseWebApp
        Die gestartete WebApplication

    '''
   
    # Konfiguration öffnen
    _config = ispConfig( mqttlevel=logging.WARNING )
    
    _apiConfig = {
        "models": [ dbtests, system ],
    }
    
    # Webserver starten
    webApp = ispBaseWebApp( _config, db, apiconfig=_apiConfig, overlay=overlay )
    
    #  mqtt in config schließen
    _config.mqttCleanup( )
    return webApp
