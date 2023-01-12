class tools_do(): 

    #-------------------------------------------------------------------------------#

    def html_tab_extractor(URL_https : str):
    
        import pandas as pd
    
    # with pandas we go to read the html page where the data of our interest are located
        tab_team : list = pd.read_html(URL_https)

        # enumerate() provides a convenient way to iterate through a list and have access to both the index of the current 
        # element and the element itself
        for idx,table in enumerate(tab_team): 
            # idx represents the current index of the element in the tab_team list
            # table represents the element itself in the tab_team list at the current index
            idx
            table

        # of all the tables present we are going to extract only the one in position 1 
        dataframe = tab_team[1] # pandas.core.frame.DataFrame

        return(dataframe)

    #-------------------------------------------------------------------------------#

    def sql_savior(dictionary : dict):
        
        import pandas as pd
        import time
        import psycopg2

        # loop to iterate through the key-value pairs in dictionary 
        for key, value in dictionary.items():
            team : str = key # name of the team
            url_tabs : str = value # team url page
            
            # dataframe extraction and creation 
            dataframe = tools_do.html_tab_extractor(value)

            # perform operations on the dataframe
            dataframe = dataframe.drop(dataframe.columns[18], axis=1) # drop Note column 
            dataframe= dataframe.dropna() # only take sitance sove are not prensent na
            dataframe.insert(1,'SQUADRA',team) # add the column of the squad

            capitano_ = dataframe.Capitano
            capitano_ = capitano_.str.replace("'"," ")
            #print(capitano_)
            dataframe['Capitano'] = pd.Series(capitano_)


            # start the connection to the db
            cnx = psycopg2.connect(
                host="db_principale",
                port="5432",
                user="SQLuser",
                password="1234",
                database="PARTITE_database")

            # cursor is an object that allows you to run queries on the database and retrieve the results 
            cur = cnx.cursor() # curcose creation

            # divide the query syntax into two for convenience
            query_pt1 : str = "INSERT INTO PARTITE ( DATA_PARTITA, SQUADRA, ORA, COMPETIZIONE, GIRONE, GIORNO, STADIO, RISULTATO, RF, RS, AVVERSARIO, xG, xGA, POSSESSO, SPETTATORI, CAPITANO, FORMAZIONE, ARBITRO, REPORT_PARTITA)"
            query_pt2 : str = " VALUES ({})" # add {} so that I can then use the format string function to add the values 

            # join the parts
            query : str = query_pt1 + query_pt2

            # convert dataframe to array
            array = dataframe.to_numpy()

            # loop based on the length of the array
            for istance_pos in range(len(array)):

                istance = str(array[istance_pos].tolist()) # extract each instance based on location
                # removed items added by conversion to list 
                istance = istance.replace('[','')
                istance = istance.replace(']','')
                
                # add to the query string the values that are to be inputted into the dataframe
                q : str  = query.format(istance) 
                
                # method used to execute an SQL query on a database
                #print(q)
                cur.execute(q)
            
            # Salvataggio delle modifiche
            cnx.commit()

            # Chiusura della connessione
            cnx.close()
            
            # give a 3s stop so that we don't have problems during scraping 
            time.sleep(3)
    
