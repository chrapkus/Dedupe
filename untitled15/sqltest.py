import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "szymon",
    passwd = "Szympek98",
    database = "Allegro"
)
my_cursor = mydb.cursor()














#----------------------CREATOR OF DESIRE TABLE-----------------------------

# my_cursor.execute("""CREATE TABLE accounts3
#                 (
#                    account_id  INTEGER UNSIGNED PRIMARY KEY AUTO_INCREMENT,
#                    parent_id INTEGER UNSIGNED NULL DEFAULT NULL,
#                    first_name varchar(255) NULL DEFAULT  NULL,
#                    last_name varchar(255) NULL DEFAULT  NULL,
#                    NIP varchar(255) NULL DEFAULT  NULL,
#                    company_name varchar(255) NULL DEFAULT  NULL,
#                    email varchar(255) NULL DEFAULT NULL,
#                    email_status INTEGER NULL DEFAULT NULL,
#                    phone_1 INTEGER NULL DEFAULT NULL,
#                    phone_2 INTEGER NULL DEFAULT NULL,
#                    login varchar(255) NULL DEFAULT NULL,
#                    adress varchar(255) NULL DEFAULT NULL,
#                    UNIQUE KEY(login)
#                 )""" )

#---------------------ADD FOREIGN KEY TO BUILD HIERARCHICAL----------------
# --------------------STRUCTURE BY ADJACENTY LIST--------------------------

# my_cursor.execute("""ALTER TABLE accounts3 ADD FOREIGN KEY (parent_id)
#                      REFERENCES accounts3 (account_id)
#                   """)

#--------------------PUTING MAIN OBJECTS-------------------------------------
# my_cursor.execute(""" INSERT INTO accounts3 (login,parent_id) values
#                     ('main', NULL)
#                     """)
# mydb.commit()
my_cursor.execute(""" INSERT INTO accounts3 (login,parent_id) values
                    ('companies', 25) """)
mydb.commit()