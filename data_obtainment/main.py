import pandas as pd 
import time
import psycopg2

from tools_do import tools_do

serieA : dict = {
    'ATALANTA' : 'https://fbref.com/it/squadre/922493f3/Statistiche-Atalanta#matchlogs_for', 
    'BOLOGNA': 'https://fbref.com/it/squadre/1d8099f8/Statistiche-Bologna#matchlogs_for',
    'CREMONESE': 'https://fbref.com/it/squadre/9aad3a77/Statistiche-Cremonese#matchlogs_for',
    'EMPOLI' : 'https://fbref.com/it/squadre/a3d88bd8/Statistiche-Empoli#matchlogs_for',
    'FIORENTINA': 'https://fbref.com/it/squadre/421387cf/Statistiche-Fiorentina#matchlogs_for',
    'HELLAS': 'https://fbref.com/it/squadre/0e72edf2/Statistiche-Hellas-Verona#stats_standard_11',
    'INTER': 'https://fbref.com/it/squadre/d609edc0/Statistiche-Internazionale#stats_standard_11',
    'JUVENTUS': 'https://fbref.com/it/squadre/e0652b02/Statistiche-Juventus#stats_standard_11',
    'LAZIO' : 'https://fbref.com/it/squadre/7213da33/Statistiche-Lazio#matchlogs_for',
    'LECCE' : 'https://fbref.com/it/squadre/ffcbe334/Statistiche-Lecce#stats_standard_11',
    'MILAN' : 'https://fbref.com/it/squadre/dc56fe14/Statistiche-Milan#matchlogs_for',
    'MONZA' : 'https://fbref.com/it/squadre/dc56fe14/Statistiche-Milan#matchlogs_for',
    'NAPOLI' : 'https://fbref.com/it/squadre/d48ad4ff/Statistiche-Napoli#stats_standard_11',
    'ROMA' : 'https://fbref.com/it/squadre/cf74a709/Statistiche-Roma#matchlogs_for',
    'SALERNITANA': 'https://fbref.com/it/squadre/c5577084/Statistiche-Salernitana#stats_standard_11',
    'SAMP' : 'https://fbref.com/it/squadre/8ff9e3b3/Statistiche-Sampdoria#matchlogs_for',
    'SASSUOLO' : 'https://fbref.com/it/squadre/e2befd26/Statistiche-Sassuolo#stats_standard_11',
    'SPEZIA' : 'https://fbref.com/it/squadre/68449f6d/Statistiche-Spezia#stats_standard_11',
    'TORINO' : 'https://fbref.com/it/squadre/105360fe/Statistiche-Torino#stats_standard_11',
    'UDINESE' : 'https://fbref.com/it/squadre/04eea015/Statistiche-Udinese#stats_standard_11'}

bundesliga : dict = {
    "AUGSBURG" : "https://fbref.com/it/squadre/0cdc4311/Statistiche-Augsburg#stats_standard_20",
    "BAYERN MONACO" : "https://fbref.com/it/squadre/054efa67/Statistiche-Bayern-Munich#stats_standard_20",
    "BOCHUM" : "https://fbref.com/it/squadre/b42c6323/Statistiche-Bochum#stats_standard_20",
    "DORTMUND" : "https://fbref.com/it/squadre/add600ae/Statistiche-Dortmund#stats_standard_20",
    "EINTRACHT FRANCOFORTE" : "https://fbref.com/it/squadre/f0ac8ee6/Statistiche-Eintracht-Frankfurt#stats_standard_20",
    "FRIBURGO" : "https://fbref.com/it/squadre/a486e511/Statistiche-Freiburg#stats_standard_20",
    "HERTHA BSC" : "https://fbref.com/it/squadre/2818f8bc/Statistiche-Hertha-BSC#stats_standard_20",
    "HOFFENHEIM" : "https://fbref.com/it/squadre/033ea6b8/Statistiche-Hoffenheim#stats_standard_20",
    "KOLN" : "https://fbref.com/it/squadre/bc357bf7/Statistiche-Koln#stats_standard_20",
    "LEVERKUSEN" : "https://fbref.com/it/squadre/c7a9f859/Statistiche-Bayer-Leverkusen#stats_standard_20",
    "M GLADBACH" : "https://fbref.com/it/squadre/32f3ee20/Statistiche-Monchengladbach#stats_standard_20",
    "MAINZ 05" : "https://fbref.com/it/squadre/a224b06a/Statistiche-Mainz-05#stats_standard_20",
    "RB LIPSIA" : "https://fbref.com/it/squadre/acbb6a5b/Statistiche-RB-Leipzig#stats_standard_20",
    "SCHALKE 04" : "https://fbref.com/it/squadre/c539e393/Statistiche-Schalke-04#stats_standard_20",
    "STUTTGART" : "https://fbref.com/it/squadre/598bc722/Statistiche-Stuttgart#stats_standard_20",
    "UNION BERLINO" : "https://fbref.com/it/squadre/7a41008f/Statistiche-Union-Berlin#stats_standard_20",
    "WERDER BREMA" : "https://fbref.com/it/squadre/62add3bf/Statistiche-Werder-Bremen#stats_standard_20",
    "WOLFSBURG" : "https://fbref.com/it/squadre/4eaa11d7/Statistiche-Wolfsburg#stats_standard_20",
}

premier_legue : dict = {
    "ARSENAL" : "https://fbref.com/it/squadre/18bb7c10/Statistiche-Arsenal#stats_standard_9",
    "ASTON VILLA" : "https://fbref.com/it/squadre/8602292d/Statistiche-Aston-Villa#stats_standard_9",
    "BORNEMOUTH" : "https://fbref.com/it/squadre/4ba7cbea/Statistiche-Bournemouth#stats_standard_",
    "BRENTFORD" : "https://fbref.com/it/squadre/cd051869/Statistiche-Brentford#stats_standard_9",
    "BRIGHTON" : "https://fbref.com/it/squadre/d07537b9/Statistiche-Brighton-and-Hove-Albion#stats_standard_9",
    "CHELSEA" : "https://fbref.com/it/squadre/cff3d9bb/Statistiche-Chelsea#stats_standard_9",
    "CRYSTAL PALACE" : "https://fbref.com/it/squadre/47c64c55/Statistiche-Crystal-Palace#stats_standard_9",
    "EVERTON" : "https://fbref.com/it/squadre/d3fd31cc/Statistiche-Everton#stats_standard_9",
    "FULHAM" : "https://fbref.com/it/squadre/fd962109/Statistiche-Fulham#stats_standard_9",
    "LEEDS UNITED" : "https://fbref.com/it/squadre/5bfb9659/Statistiche-Leeds-United#stats_standard_9",
    "LEICESTER" : "https://fbref.com/it/squadre/a2d435b3/Statistiche-Leicester-City#stats_standard_9",
    "LIVERPOOL" : "https://fbref.com/it/squadre/822bd0ba/Statistiche-Liverpool#stats_standard_9",
    "MAN CITY" : "https://fbref.com/it/squadre/b8fd03ef/Statistiche-Manchester-City#stats_standard_9",
    "MAN UNITED" : "https://fbref.com/it/squadre/19538871/Statistiche-Manchester-United#stats_standard_9",
    "NEWCASTLE" : "https://fbref.com/it/squadre/b2b47a98/Statistiche-Newcastle-United#stats_standard_9",
    "NOTTINGHAM FOREST" : "https://fbref.com/it/squadre/e4a775cb/Statistiche-Nottingham-Forest#stats_standard_9",
    "SOUTHAMPTON" : "https://fbref.com/it/squadre/33c895d4/Statistiche-Southampton#stats_standard_9",
    "TOTTENHAM" : "https://fbref.com/it/squadre/361ca564/Statistiche-Tottenham-Hotspur#stats_standard_9",
    "WEST HAM" : "https://fbref.com/it/squadre/7c21e445/Statistiche-West-Ham-United#stats_standard_9",
    "WOLVES" : "https://fbref.com/it/squadre/8cec06e1/Statistiche-Wolverhampton-Wanderers#stats_standard_9"
}

ligue1 : dict = {
    "AJACCIO": "https://fbref.com/it/squadre/7a54bb4f/Statistiche-Ajaccio#stats_standard_13",
    "ANGERS": "https://fbref.com/it/squadre/69236f98/Statistiche-Angers#stats_standard_13",
    "AUXERRE": "https://fbref.com/it/squadre/5ae09109/Statistiche-Auxerre#stats_standard_13",
    "BREST": "https://fbref.com/it/squadre/fb08dbb3/Statistiche-Brest#stats_standard_13",
    "CLERMONT": "https://fbref.com/it/squadre/d9676424/Statistiche-Clermont-Foot#stats_standard_13",
    "LENS": "https://fbref.com/it/squadre/fd4e0f7d/Statistiche-Lens#stats_standard_13",
    "LILLE": "https://fbref.com/it/squadre/cb188c0c/Statistiche-Lille#stats_standard_13",
    "LORIENT": "https://fbref.com/it/squadre/d2c87802/Statistiche-Lorient#stats_standard_13",
    "LYON": "https://fbref.com/it/squadre/d53c0b06/Statistiche-Lyon#stats_standard_13",
    "MARSEILLE": "https://fbref.com/it/squadre/5725cc7b/Statistiche-Marseille#stats_standard_13",
    "MONACO": "https://fbref.com/it/squadre/fd6114db/Statistiche-Monaco#stats_standard_13",
    "MONTPELLIER": "https://fbref.com/it/squadre/281b0e73/Statistiche-Montpellier#stats_standard_13",
    "NANTES": "https://fbref.com/it/squadre/d7a486cd/Statistiche-Nantes#stats_standard_13",
    "NICE": "https://fbref.com/it/squadre/132ebc33/Statistiche-Nice#stats_standard_13",
    "PSG": "https://fbref.com/it/squadre/e2d8892c/Statistiche-Paris-Saint-Germain#stats_standard_13",
    "REIMS": "https://fbref.com/it/squadre/7fdd64e0/Statistiche-Reims#stats_standard_13",
    "RENNES": "https://fbref.com/it/squadre/b3072e00/Statistiche-Rennes#stats_standard_13",
    "STRASBOURG": "https://fbref.com/it/squadre/c0d3eab4/Statistiche-Strasbourg#stats_standard_13",
    "TOULOUSE" : "https://fbref.com/it/squadre/3f8c4b5f/Statistiche-Toulouse#stats_standard_13",
    "TROYES" : "https://fbref.com/it/squadre/54195385/Statistiche-Troyes#stats_standard_13"}

laliga : dict = {
    "ALMERIA": "https://fbref.com/it/squadre/78ecf4bb/Statistiche-Almeria#stats_standard_12",
    "ATHLETIC CLUB": "https://fbref.com/it/squadre/2b390eca/Statistiche-Athletic-Club#stats_standard_12",
    "ATLETICO MADRID": "https://fbref.com/it/squadre/db3b9613/Statistiche-Atletico-Madrid#stats_standard_12",
    "BARCELLONA": "https://fbref.com/it/squadre/206d90db/Statistiche-Barcelona#stats_standard_12",
    "BETIS": "https://fbref.com/it/squadre/fc536746/Statistiche-Real-Betis#stats_standard_12",
    "CADIZ": "https://fbref.com/it/squadre/ee7c297c/Statistiche-Cadiz#stats_standard_12",
    "CELTA VIGO": "https://fbref.com/it/squadre/f25da7fb/Statistiche-Celta-Vigo#stats_standard_12",
    "ELCHE": "https://fbref.com/it/squadre/6c8b07df/Statistiche-Elche#stats_standard_12",
    "ESPANYOL": "https://fbref.com/it/squadre/a8661628/Statistiche-Espanyol#stats_standard_12",
    "GETAFE": "https://fbref.com/it/squadre/7848bd64/Statistiche-Getafe#stats_standard_12",
    "GIRONA": "https://fbref.com/it/squadre/9024a00a/Statistiche-Girona#stats_standard_12",
    "MALLORCA": "https://fbref.com/it/squadre/2aa12281/Statistiche-Mallorca#stats_standard_12",
    "OSASUNA": "https://fbref.com/it/squadre/03c57e2b/Statistiche-Osasuna#stats_standard_12",
    "RAYO VALLECANO": "https://fbref.com/it/squadre/98e8af82/Statistiche-Rayo-Vallecano#stats_standard_12",
    "REAL MADRID": "https://fbref.com/it/squadre/53a2f082/Statistiche-Real-Madrid#stats_standard_12",
    "REAL SOCIEDAD": "https://fbref.com/it/squadre/e31d1cd9/Statistiche-Real-Sociedad#stats_standard_12",
    "SIVIGLIA": "https://fbref.com/it/squadre/ad2be733/Statistiche-Sevilla#stats_standard_12",
    "VALENCIA": "https://fbref.com/it/squadre/dcc91a7b/Statistiche-Valencia#stats_standard_12",
    "VALLADOLID": "https://fbref.com/it/squadre/17859612/Statistiche-Valladolid#stats_standard_12",
    "VILLAREAL": "https://fbref.com/it/squadre/2a8183b3/Statistiche-Villarreal#stats_standard_12"}


if __name__ == "__main__":
    time.sleep(40)
    tools_do.sql_savior(serieA)
    #tools_do.sql_savior(bundesliga)
    #tools_do.sql_savior(premier_legue)
    #tools_do.sql_savior(ligue1)
    #tools_do.sql_savior(laliga)