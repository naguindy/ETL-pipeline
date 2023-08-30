import psycopg2
import pandas as pd


def connect_to_redshift(dbname, host, port, user, password):
    """Method that connects to redshift. This gives a warning so will look for another solution"""

    connect = psycopg2.connect(
        dbname=dbname, host=host, port=port, user=user, password=password
    )

    print("connection to redshift made")

    return connect


def extract_transaction_data(dbname, host, port, user, password):
    connect = connect_to_redshift(dbname, host, port, user, password)

    query = """select  ot.customer_id,
                        ot.invoice ,
                        ot.stock_code, 
                        ot.quantity, 
                        cast(ot.invoice_date as datetime) as invoice_date , 
                        ot.price, 
                        ot.country, 
                        case when sd.description is null then 'Unknown'
                             else  sd.description 
                        end as description, 
                        case 
                             when extract(month from cast(ot.invoice_date as datetime)) = 1  then 'Jan'
                             when extract(month from cast(ot.invoice_date as datetime)) = 2  then 'Feb'
                             when extract(month from cast(ot.invoice_date as datetime)) = 3  then 'March'
                             when extract(month from cast(ot.invoice_date as datetime)) = 4  then 'April'
                             when extract(month from cast(ot.invoice_date as datetime)) = 5  then 'Mai'
                             when extract(month from cast(ot.invoice_date as datetime)) = 6  then 'Jun'
                             when extract(month from cast(ot.invoice_date as datetime)) = 7  then 'Jul'
                             when extract(month from cast(ot.invoice_date as datetime)) = 8  then 'Aug'
                             when extract(month from cast(ot.invoice_date as datetime)) = 9  then 'Sep'
                             when extract(month from cast(ot.invoice_date as datetime)) = 10 then 'Oct'
                             when extract(month from cast(ot.invoice_date as datetime)) = 11 then 'Nov'
                             else 'Dec'
                        end as invoice_month, 
                        extract('DOW' from cast(ot.invoice_date as datetime)) as DOW, 
                        case
                            when extract('DOW' from cast(ot.invoice_date as datetime)) = 0 then 'MON'
                            when extract('DOW' from cast(ot.invoice_date as datetime)) = 1 then 'TUES'
                            when extract('DOW' from cast(ot.invoice_date as datetime)) = 2 then 'WED'
                            when extract('DOW' from cast(ot.invoice_date as datetime)) = 3 then 'THUR'
                            when extract('DOW' from cast(ot.invoice_date as datetime)) = 4 then 'FRI'
                            when extract('DOW' from cast(ot.invoice_date as datetime)) = 5 then 'SAT'
                            else 'SUN'
                        end as invoice_dow_name
    from   bootcamp.online_transactions ot 
    left join (select *
               from bootcamp.stock_description 
               where description <> '?') sd
    on ot.stock_code = sd.stock_code       
    where customer_id <> ''
    and ot.stock_code not in ('BANK CHARGES','POST','D','M','CRUK')

    """
    online_transactions_cleaned = pd.read_sql(query, connect)

    connect.close()

    return online_transactions_cleaned



