# -*- coding: utf-8 -*-


from safrs import jsonapi_rpc # rpc decorator
from sqlalchemy import func, case, or_ #, inspect

from isp.safrs import ispSAFRSModel, db, isoDateType, isoDateTimeType

from safrs import log
from flask import Response 

class dbskeleton( ispSAFRSModel ):
    """.. restdoc::
        
        description:  Tests - Test von ispSAFRSModel
        
        ----
        In der Datenbank wird immer komplett abgelegt.
        
        Numeric auch DECIMAL
        
        precision=None,
        scale=None,
        decimal_return_scale=None, 
        asdecimal=True, - es wird ein formatierter string zurückgegeben (gerundet)
        
        db.Float( precision=5, asdecimal=True, decimal_return_scale=4 )
    """
    
    __bind_key__ = 'skeleton'
    
    __table_args__ = {'extend_existing': True}
    
    __tablename__ = "dbskeleton"
    
    id = db.Column('id', db.Integer, primary_key=True, unique=True, autoincrement=True)
    string = db.Column('string', db.String, nullable=False) # 
    date = db.Column('date', isoDateType ) # YYYY-MM-DD
    datetime = db.Column('datetime', isoDateTimeType ) # YYYY-MM-DD HH:mm:SS
    integer = db.Column('integer', db.Integer, nullable=True)
    data = db.Column('data', db.JSON ) 
    tags = db.Column('tags',  db.String, nullable=True)
    gruppe = db.Column('gruppe',  db.String, nullable=True)
    aktiv = db.Column('aktiv', db.Integer, nullable=False, default=True)
    float = db.Column('float', db.Float( asdecimal=True ), nullable=False, default=0) # (5,True,4) gibt 0.3333 als str
    
    decimal = db.Column('decimal', db.DECIMAL( 5, 2, 1, True ), nullable=False, default=0)
    numeric = db.Column('numeric', db.Numeric( 5, 2, 3, False ), nullable=False, default=0 )
        
    @classmethod
    @jsonapi_rpc( http_methods=['GET'] )
    def table( cls, **kwargs ):
        """.. restdoc::
        summary : Testdaten ausgabe
        parameters:
            - name : _ispcp
              default : {}
              description : zusätzliche parameter
              type: object
            - name: art
              description : bestimmt die art
              default : 
            - name: filter
              description : rql Filterbedingung                  
        ----
            
        Parameters
        ----------
        **kwargs : dict
            named arguments allows you to pass keyworded variable length of arguments to a function.
            
        """
        import pandas as pd
         
        query = cls.query
        
        data_frame = pd.read_sql_query(sql=query.statement, con=cls.getConnection() )
        #print(data_frame)
        # pandas dataframe als Tabelle
        table_html = (
            data_frame.round(2).style
            .set_uuid( "test_pandas_" )
            .set_table_attributes('class="dbtests sysinfo layout-fill-width"') \
            #.format( { 'Gantry':'{0:.1f}', 'Kollimator':'{0:.1f}', 'delta':'{0:.3f}'} )
            .hide_index()
            #.highlight_max(subset=["delta"], color='yellow', axis=0)
            .render()
        )
            
        style = '''
            table.dbtests{
                margin-bottom: 5px;
                border-collapse: collapse;
            }
            table.dbtests, table.dbtests th, table.dbtests td{
                border: 1px solid silver;
            }
            table.dbtests tr:nth-child(even) {
        		background-color: #f2f2f2;
        	}
            table.dbtests th.level0 {
            	min-width: 50px;
        	}

        '''
        html = '''
        <style>{}</style>
        <div class="_sysinfo">
        {} 
        </div>
        '''.format(
            style,
            table_html
        )
        
        return Response( html , mimetype='text/html')  

    @classmethod
    @jsonapi_rpc( http_methods=['GET'] )
    def hello( cls, **kwargs ):
        """.. restdoc::
        summary : Hello world test
        description : Eine neue jsonapi_rpc Methode
        parameters:
            - name : format
              in : query
              required : false
              default : json
              description : Format der Ausgabe [ json, html ]         
        ----

        Diese Funktion wird über /api/dbtests/hello aufgerufen
        
        Wird der Parameter ?format=html angegeben erfolgt die Rückgabe als HTML
        """
        if kwargs["format"] == "json":
            return cls._int_json_response({"data":{"Hello": "world"}})
        else:
            return Response( "Hello world" , mimetype='text/html') 
        
