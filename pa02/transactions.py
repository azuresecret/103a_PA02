import sqlite3

class Transaction:                
 
    def __init__(self, filename): 
        con=sqlite3.connect(filename)
        cur = con.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS transactions
                    ('item #'  text, amount integer, category text, date integer, description text)''')
        con.commit()
        con.close()
        self.filename = filename

    def select_all(self):
        ''' return all of the transactions as a list of dicts.'''
        con= sqlite3.connect(self.filename)
        cur = con.cursor()
        cur.execute("SELECT * from transactions")
        tuples = cur.fetchall()
        con.commit()
        con.close()
        return tuples

    def add(self,item):
        con= sqlite3.connect(self.filename)
        cur = con.cursor()
        cur.execute("INSERT INTO transactions VALUES(?, ?, ?, ?, ?)",(item['item #'],item['amount'],item['category'],item['date'], item['description']))
        con.commit()
        cur.execute("SELECT last_insert_rowid()")
        last_rowid = cur.fetchone()
        con.commit()
        con.close()
        return last_rowid[0]  

    def delete(self,trans_num):
        con= sqlite3.connect(self.filename)
        cur = con.cursor()
        cur.execute('''DELETE FROM transactions
                       WHERE "item #" = ?;
        ''', (trans_num,))
        con.commit()
        con.close()

    def summarize(self, col):
        con = sqlite3.connect(self.filename)
        cur=con.cursor()
        if col in ('date_', 'month', 'year'):
            if col == 'year':
                sub_str = 'substr(date,1,4)'
            elif col == 'month':
                sub_str = 'substr(date,5,2)'
            else:
                sub_str = 'substr(date,7,2)'
            cur.execute('''CREATE TEMPORARY TABLE tmp AS SELECT *, {0} as {1} FROM transactions;'''.format(sub_str, col))
            cur.execute('''
            SELECT {0}, COUNT(*), AVG(amount)
            FROM tmp
            GROUP BY {0};
            '''.format(col))
            tuples = cur.fetchall()
            cur.execute('''DROP TABLE tmp;''')
        else:
            cur.execute('''SELECT {0}, COUNT(*), AVG(amount)
                        FROM transactions
                        GROUP BY {0};'''.format(col))
            tuples = cur.fetchall()
        con.commit()
        con.close()
        print(tuples)
        return(tuples)
    
