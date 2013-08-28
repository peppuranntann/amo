#!python3.3
# -*- coding: utf-8 -*-
import sqlite3 as sql3
import os

os.chdir(r"C:/Shares/Server1/data/amo_db") #change directory
os.getcwd() #confirm current directory



dbname = "game.sqlite3" #######set DB name#########



con = sql3.connect(dbname) # connect the DB
cur = con.cursor() # create cursor




cur.execute("""
CREATE TABLE AMO(   
    search_day text,
    search_day_UNIX integer,
    rank integer,
    app_title text,
    app_package text,
    developper text,
    title_KW integer,
    KW_in_description integer,
    KW_in_dev name integer,
    top_developper integer,
    ave_evaluation real,
    num_of_review integer,
    star1 integer,
    star2 integer,
    star3 integer,
    star4 integer,
    star5 integer,
    star1_percentage real,
    star2_percentage real,
    star3_percentage real,
    star4_percentage real,
    star5_percentage real,
    MIN_inst_num integer,
    MAX_inst_num integer,
    AVE_inst_num integer,
    Google_plus_1 integer,
    last_modified_day integer,
    current_version real,
    letters_in_description integer,
    size[KB] integer,
    rating integer,
    screen_shot_num integer,
    having_movie_or_not integer,
    price integer
);""")

