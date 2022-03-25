'''
test_transaction runs unit and integration tests on the trasactions module
'''

import pytest
from transactions import Transaction

@pytest.fixture
def dbfile(tmpdir):
    ''' create a database file in a temporary file system '''
    return tmpdir.join('test_tracker.db')

@pytest.fixture
def empty_db(dbfile):
    ''' create an empty database '''
    db = Transaction(dbfile)
    yield db


@pytest.fixture
def small_db(empty_db):
    ''' create a small database, and tear it down later'''
    id1=empty_db.add({'item #': '1', 'amount': 120, 'category': 'food', 'date': '20220201', 'description': 'kfc'})
    id2=empty_db.add({'item #': '2', 'amount': 30, 'category': 'food', 'date': '20220101', 'description': 'popeyes'})
    id3=empty_db.add({'item #': '3', 'amount': 120000, 'category': 'car', 'date': '20210101', 'description': 'BMW'})
    yield empty_db
    empty_db.delete(id3)
    empty_db.delete(id2)
    empty_db.delete(id1)

def test_select_all(small_db):
    rows = small_db.select_all()
    assert(len(rows)==3)

def test_add(small_db):
    num_of_rows = len(small_db.select_all())
    small_db.add({'item #': '5', 'amount': 30, 'category': 'fun', 'date': '20210201', 'description': 'movie night'})
    rows = small_db.select_all()
    assert(len(rows)==num_of_rows+1)


def test_delete(small_db):
    num_of_rows = len(small_db.select_all())
    small_db.delete('1')
    rows = small_db.select_all()
    assert(len(rows)==num_of_rows-1)

def test_summarize(small_db):
    assert(small_db.summarize('date_')==[('01', 3, 40050.0)])
    assert(small_db.summarize('month')==[('01', 2, 60015.0), ('02', 1, 120.0)])
    assert(small_db.summarize('year') == [('2021', 1, 120000.0), ('2022', 2, 75.0)])
    assert(small_db.summarize('category')==[('car', 1, 120000.0), ('food', 2, 75.0)])