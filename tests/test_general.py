import os
import re
import sqlite3
import sys
PATH = '../MirahezeBots'
MODULEPATH = '../MirahezeBots/modules'
sys.path.append(PATH)
from sqlalchemy import create_engine
import models

def test_db_schema_is_same():
    original, new = set(), set()
    with sqlite3.connect(os.path.join(PATH, 'hasan.db')) as conn:
        conn.text_factory = str
        res = conn.execute("SELECT name FROM sqlite_master WHERE type='table';")
        [original.add(tbl[0]) for tbl in res if not tbl[0] == 'nick_ids' and not tbl[0] == 'sqlite_sequence']
        
    try:
        os.unlink(os.path.join(PATH, "hasan2.db"))
    except FileNotFoundError:
        pass

    engine = create_engine('sqlite:///{0}'.format(os.path.join(PATH, "..", "hasan2.db")))
    models.Base.metadata.create_all(bind=engine)
    assert original == set(engine.table_names()) 

def test_line_length():
    MAX_LENGTH = 220+1
    for top, dirs, files in os.walk(MODULEPATH):
        for filen in files:
            if not filen.endswith('.py'):
                continue
            with open(os.path.join(MODULEPATH, filen)) as python_source:
                src = python_source.readlines()
                for line_number, line in enumerate(src):
                    assert len(line.strip()) < MAX_LENGTH, 'length of line #{0} exceeds limit'.format(line_number)

def future_test_db_cleanup():
    engine = create_engine('sqlite:///{0}'.format(os.path.join(PATH, "..", "hasan2.db")))
    models.Base.metadata.create_all(bind=engine)

def test_no_get_on_lists():
    reg = r'get\([0-9]'
    for top, dirs, files in os.walk(MODULEPATH):
        for filen in files:
            if not filen.endswith('.py'):
                continue
            with open(os.path.join(MODULEPATH, filen)) as python_source:
                src = python_source.read()
                assert not re.search(reg, src) 
