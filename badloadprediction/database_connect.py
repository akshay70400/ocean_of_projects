import sqlite3


def insert_record(loan_amnt,term,int_rate,emp_length,home_ownership,annual_inc,purpose,addr_state,dti,delinq_2yrs,revol_util,total_acc,longest_credit_length,verification_status,output):
    
    try:
        con =sqlite3.connect('loan_data.db')
        cur =con.cursor()

        cur.execute(""" CREATE TABLE IF NOT EXISTS customer(
                                        loan_amnt integer Not Null,
                                        term integer Not Null,
                                        int_rate real Not Null,
                                        emp_length real Not Null,
                                        home_ownership integer Not Null,
                                        annual_inc real Not Null,
                                        purpose integer Not Null,
                                        addr_state integer Not Null,
                                        dti float Not Null,
                                        delinq_2yrs float Not Null,
                                        revol_util float Not Null,
                                        total_acc float Not Null,
                                        longest_credit_length float Not Null,
                                        verification_status integer Not Null,
                                        bad_loan integer Not Null
                                    ); """)
        #rec=[feat for x in record for feat in x]
        cur.execute("""INSERT INTO customer(loan_amnt,term,int_rate,emp_length,home_ownership,annual_inc,purpose,addr_state,dti,delinq_2yrs,revol_util,total_acc,longest_credit_length,verification_status,bad_loan)
                        VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""", 
                        (loan_amnt,term,int_rate,emp_length,home_ownership,annual_inc,purpose,addr_state,dti,delinq_2yrs,revol_util,total_acc,longest_credit_length,verification_status,output))
        print("Record Inserted")
    except Exception as e:
        print("Unable to insert",e)   
    con.commit()
    con.close()