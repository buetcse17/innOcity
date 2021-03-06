from django.db import connection
from random import randint, uniform


def customer_id_change():

    with connection.cursor() as cur:
        sql = "SELECT CUSTOMERID FROM CUSTOMER"
        cur.execute(sql)
        res = cur.fetchall()
        current_ids = [row[0] for row in res]
        size = len(current_ids)

        random_ids = set()
        while len(random_ids) < size:
            x = randint(10000000, 99999999)
            random_ids.add(x)

        # dropping the foreign key constraint from table RESERVATION
        sql = "SELECT CONSTRAINT_NAME FROM USER_CONS_COLUMNS WHERE TABLE_NAME='RESERVATION' " \
              "AND COLUMN_NAME='CUSTOMERID'"
        cur.execute(sql)
        constraint_name = cur.fetchone()[0]
        sql = "ALTER TABLE RESERVATION DROP CONSTRAINT " + constraint_name
        cur.execute(sql)

        # replacing old customer ids with new ones in both tables
        for current, rand in zip(current_ids, random_ids):
            sql = "UPDATE RESERVATION SET CUSTOMERID = %s WHERE CUSTOMERID = %s"
            cur.execute(sql, [rand, current])
            connection.commit()
            sql = "UPDATE CUSTOMER SET CUSTOMERID = %s WHERE CUSTOMERID = %s"
            cur.execute(sql, [rand, current])
            connection.commit()

        # adding the foreign key constraint to table RESERVATION again
        sql = "ALTER TABLE RESERVATION ADD FOREIGN KEY(CUSTOMERID) REFERENCES CUSTOMER(CUSTOMERID)"
        cur.execute(sql)


def hotel_id_change():

    with connection.cursor() as cur:

        sql = "SELECT HOTELID FROM HOTEL"
        cur.execute(sql)
        result = cur.fetchall()
        current_ids = [row[0] for row in result]
        size = len(current_ids)

        random_ids = set()
        while len(random_ids) < size:
            x = randint(10000000, 99999999)
            random_ids.add(x)

        # dropping foreign key constraints from tables reservation, room, service

        sql = "SELECT CONSTRAINT_NAME FROM USER_CONS_COLUMNS WHERE TABLE_NAME='RESERVATION' " \
              "AND COLUMN_NAME='HOTELID'"
        cur.execute(sql)
        constraint_name = cur.fetchone()[0]
        sql = "ALTER TABLE RESERVATION DROP CONSTRAINT " + constraint_name
        cur.execute(sql)

        sql = "SELECT CONSTRAINT_NAME FROM USER_CONS_COLUMNS WHERE TABLE_NAME='ROOM' " \
              "AND COLUMN_NAME='HOTELID'"
        cur.execute(sql)
        constraint_name = cur.fetchone()[0]
        sql = "ALTER TABLE ROOM DROP CONSTRAINT " + constraint_name
        cur.execute(sql)

        sql = "SELECT CONSTRAINT_NAME FROM USER_CONS_COLUMNS WHERE TABLE_NAME='SERVICE' " \
              "AND COLUMN_NAME='HOTELID'"
        cur.execute(sql)
        constraint_name = cur.fetchone()[0]
        sql = "ALTER TABLE SERVICE DROP CONSTRAINT " + constraint_name
        cur.execute(sql)

        # replacing old hotel ids with new ones in all tables

        for current, rand in zip(current_ids, random_ids):
            sql = "UPDATE RESERVATION SET HOTELID = %s WHERE HOTELID = %s"
            cur.execute(sql, [rand, current])
            connection.commit()

            sql = "UPDATE ROOM SET HOTELID = %s WHERE HOTELID = %s"
            cur.execute(sql, [rand, current])
            connection.commit()

            sql = "UPDATE SERVICE SET HOTELID = %s WHERE HOTELID = %s"
            cur.execute(sql, [rand, current])
            connection.commit()

            sql = "UPDATE HOTEL SET HOTELID = %s WHERE HOTELID = %s"
            cur.execute(sql, [rand, current])
            connection.commit()

            sql = "UPDATE HOTEL_FACILITY SET HOTELID = %s WHERE HOTELID = %s"
            cur.execute(sql, [rand, current])
            connection.commit()

        # adding the foreign key constraints again
        sql = "ALTER TABLE RESERVATION ADD FOREIGN KEY(HOTELID) REFERENCES HOTEL(HOTELID)"
        cur.execute(sql)

        sql = "ALTER TABLE ROOM ADD FOREIGN KEY(HOTELID) REFERENCES HOTEL(HOTELID)"
        cur.execute(sql)

        sql = "ALTER TABLE SERVICE ADD FOREIGN KEY(HOTELID) REFERENCES HOTEL(HOTELID)"
        cur.execute(sql)


def room_id_change():

    with connection.cursor() as cur:
        sql = "SELECT ROOMID FROM ROOM"
        cur.execute(sql)
        res = cur.fetchall()
        current_ids = [row[0] for row in res]
        size = len(current_ids)

        random_ids = set()
        while len(random_ids) < size:
            x = randint(10000000, 99999999)
            random_ids.add(x)

        # dropping the foreign key constraint from table RESERVATION
        sql = "SELECT CONSTRAINT_NAME FROM USER_CONS_COLUMNS WHERE TABLE_NAME='RESERVATION' " \
              "AND COLUMN_NAME='ROOMID'"
        cur.execute(sql)
        constraint_name = cur.fetchone()[0]
        sql = "ALTER TABLE RESERVATION DROP CONSTRAINT " + constraint_name
        cur.execute(sql)

        # replacing old room ids with new ones in all tables
        for current, rand in zip(current_ids, random_ids):
            sql = "UPDATE RESERVATION SET ROOMID = %s WHERE ROOMID = %s"
            cur.execute(sql, [rand, current])
            connection.commit()

            sql = "UPDATE ROOM SET ROOMID = %s WHERE ROOMID = %s"
            cur.execute(sql, [rand, current])
            connection.commit()

            sql = "UPDATE ROOM_FACILITY SET ROOMID = %s WHERE ROOMID = %s"
            cur.execute(sql, [rand, current])
            connection.commit()

        # adding the foreign key constraint to table RESERVATION again
        sql = "ALTER TABLE RESERVATION ADD FOREIGN KEY(ROOMID) REFERENCES ROOM(ROOMID)"
        cur.execute(sql)


def payment_id_change():

    with connection.cursor() as cur:
        sql = "SELECT PAYMENTID FROM PAYMENT"
        cur.execute(sql)
        res = cur.fetchall()
        current_ids = [row[0] for row in res]
        size = len(current_ids)

        random_ids = set()
        while len(random_ids) < size:
            x = randint(10000000, 99999999)
            random_ids.add(x)

        # dropping the foreign key constraint from table RESERVATION
        sql = "SELECT CONSTRAINT_NAME FROM USER_CONS_COLUMNS WHERE TABLE_NAME='RESERVATION' " \
              "AND COLUMN_NAME='PAYMENTID'"
        cur.execute(sql)
        constraint_name = cur.fetchone()[0]
        sql = "ALTER TABLE RESERVATION DROP CONSTRAINT " + constraint_name
        cur.execute(sql)

        # replacing old customer ids with new ones in both tables
        for current, rand in zip(current_ids, random_ids):
            sql = "UPDATE RESERVATION SET PAYMENTID = %s WHERE PAYMENTID = %s"
            cur.execute(sql, [rand, current])
            connection.commit()
            sql = "UPDATE PAYMENT SET PAYMENTID = %s WHERE PAYMENTID = %s"
            cur.execute(sql, [rand, current])
            connection.commit()

        # adding the foreign key constraint to table RESERVATION again
        sql = "ALTER TABLE RESERVATION ADD FOREIGN KEY(PAYMENTID) REFERENCES PAYMENT(PAYMENTID)"
        cur.execute(sql)


def service_id_change():

    with connection.cursor() as cur:
        sql = "SELECT SERVICEID FROM SERVICE"
        cur.execute(sql)
        res = cur.fetchall()
        current_ids = [row[0] for row in res]
        size = len(current_ids)

        random_ids = set()
        while len(random_ids) < size:
            x = randint(10000000, 99999999)
            random_ids.add(x)

        # dropping the foreign key constraint from table RESERVATION
        sql = "SELECT CONSTRAINT_NAME FROM USER_CONS_COLUMNS WHERE TABLE_NAME='RESERVATION_SERVICE' " \
              "AND COLUMN_NAME='SERVICEID'"
        cur.execute(sql)
        constraint_name = cur.fetchone()[0]
        sql = "ALTER TABLE RESERVATION_SERVICE DROP CONSTRAINT " + constraint_name
        cur.execute(sql)

        # replacing old customer ids with new ones in both tables
        for current, rand in zip(current_ids, random_ids):
            sql = "UPDATE RESERVATION_SERVICE SET SERVICEID = %s WHERE SERVICEID = %s"
            cur.execute(sql, [rand, current])
            connection.commit()
            sql = "UPDATE SERVICE SET SERVICEID = %s WHERE SERVICEID = %s"
            cur.execute(sql, [rand, current])
            connection.commit()

        # adding the foreign key constraint to table RESERVATION again
        sql = "ALTER TABLE RESERVATION_SERVICE ADD FOREIGN KEY(SERVICEID) REFERENCES SERVICE(SERVICEID)"
        cur.execute(sql)


def reservation_id_change():

    with connection.cursor() as cur:
        sql = "SELECT RESERVATIONID FROM RESERVATION"
        cur.execute(sql)
        res = cur.fetchall()
        current_ids = [row[0] for row in res]
        size = len(current_ids)

        random_ids = set()
        while len(random_ids) < size:
            x = randint(10000000, 99999999)
            random_ids.add(x)

        # dropping the foreign key constraint from table RESERVATION
        sql = "SELECT CONSTRAINT_NAME FROM USER_CONS_COLUMNS WHERE TABLE_NAME='RESERVATION_SERVICE' " \
              "AND COLUMN_NAME='RESERVATIONID'"
        cur.execute(sql)
        constraint_name = cur.fetchone()[0]
        sql = "ALTER TABLE RESERVATION_SERVICE DROP CONSTRAINT " + constraint_name
        cur.execute(sql)

        # replacing old customer ids with new ones in both tables
        for current, rand in zip(current_ids, random_ids):
            sql = "UPDATE RESERVATION_SERVICE SET RESERVATIONID = %s WHERE RESERVATIONID = %s"
            cur.execute(sql, [rand, current])
            connection.commit()
            sql = "UPDATE RESERVATION SET RESERVATIONID = %s WHERE RESERVATIONID = %s"
            cur.execute(sql, [rand, current])
            connection.commit()

        # adding the foreign key constraint to table RESERVATION again
        sql = "ALTER TABLE RESERVATION_SERVICE ADD FOREIGN KEY(RESERVATIONID) REFERENCES RESERVATION(RESERVATIONID)"
        cur.execute(sql)


def room_to_reservation():

    with connection.cursor() as cur:

        sql = "SELECT RESERVATIONID, HOTELID FROM RESERVATION"
        cur.execute(sql)
        result = cur.fetchall()

        for row in result:
            reservation_id = row[0]
            hotel_id = row[1]

            sql = "SELECT ROOMID FROM ROOM WHERE HOTELID = %s"
            cur.execute(sql, [hotel_id])
            rooms = cur.fetchall()
            rand_id = randint(0, len(rooms)-1)
            room_id = rooms[rand_id][0]

            sql = "UPDATE RESERVATION SET ROOMID = %s WHERE RESERVATIONID = %s"
            cur.execute(sql, [room_id, reservation_id])
            connection.commit()


def set_hotel_pass():

    with connection.cursor() as cur:
        sql_alter = "ALTER TABLE HOTEL ADD PASSWORD VARCHAR(50)"
        cur.execute(sql_alter)
        connection.commit()

        sql = "SELECT HOTELID FROM HOTEL"
        cur.execute(sql)
        ids = cur.fetchall()

        for id in ids:
            password = str(randint(1, 10000000))
            password = hashlib.md5(password.encode()).hexdigest()
            sql_update = "UPDATE HOTEL SET PASSWORD = %s WHERE HOTELID = %s"
            cur.execute(sql_update, [password, id[0]])
            connection.commit()


def fix_hotel_rating():

    with connection.cursor() as cur:

        sql = "ALTER TABLE HOTEL MODIFY RATING NUMBER(3,2)"
        cur.execute(sql)

        sql = "SELECT HOTELID FROM HOTEL"
        cur.execute(sql)
        rows = cur.fetchall()

        for row in rows:
            hotelid = row[0]
            rating = round(uniform(2.0, 5.0), 2)
            print(rating)
            sql = "UPDATE HOTEL SET RATING = %s WHERE HOTELID = %s"
            cur.execute(sql, [rating, hotelid])
            connection.commit()


def fix_room_price():

    with connection.cursor() as cur:

        sql = "UPDATE ROOM R SET R.COST_PER_DAY = " \
              "(SELECT CEIL(AVG(R2.COST_PER_DAY)) FROM ROOM R2 WHERE R2.HOTELID = R.HOTELID " \
              "AND R2.ROOM_TYPE = R.ROOM_TYPE AND R2.BED_TYPE = R.BED_TYPE), " \
              "R.DISCOUNT = " \
              "(SELECT CEIL(AVG(R3.DISCOUNT)) FROM ROOM R3 WHERE R3.HOTELID = R.HOTELID " \
              "AND R3.ROOM_TYPE = R.ROOM_TYPE AND R3.BED_TYPE = R.BED_TYPE)"

        cur.execute(sql)
        connection.commit()


def check(start_date, inter, rid, stay):

    with connection.cursor() as cur:
        sql = "SELECT COUNT(*) FROM RESERVATION R, RESERVATION_ROOM RR WHERE R.RESERVATIONID = RR.RESERVATIONID " \
              " AND RR.ROOMID = %s AND R.DATE_OF_DEPARTURE > (TO_DATE(%s, 'DD-MM-YYYY') + INTERVAL '" + str(inter) + "' DAY) " \
              " AND R.DATE_OF_ARRIVAL < (TO_DATE(%s, 'DD-MM-YYYY') + INTERVAL '" + str(inter + stay) + "' DAY)"
        print(sql)
        cur.execute(sql, [rid, start_date, start_date])
        if cur.fetchone()[0] == 0:
            return True
        else:
            return False


def insert_into_reservation():

    hotelid = 49833330
    with connection.cursor() as cur:
        cur.execute('SELECT CUSTOMERID FROM CUSTOMER')
        res = cur.fetchall()
        all_customers = [r[0] for r in res]
        cur.execute('SELECT ROOMID FROM ROOM WHERE HOTELID = %s', [hotelid])
        res = cur.fetchall()
        all_rooms = [r[0] for r in res]
        start_date = '20-12-2020'

        for i in range(10):
            total = random.choice([1, 2, 3, 4, 5, 6, 7, 8])
            random.shuffle(all_rooms)
            random.shuffle(all_customers)
            booked = 0
            print('day ', i, 'total', total)
            for j in range(total):
                cid = all_customers[j]
                rn = random.randint(1, 100)
                if rn % 5 == 0:
                    rooms = 2
                elif rn % 10 == 0:
                    rooms = 2
                else:
                    rooms = 1
                st = random.randint(1, 100) % 3 + 1
                print('stay: ', st, 'rooms:', rooms)

                reservation_id = cur.callfunc('GENERATE_ID', int, ['RESERVATION', 'RESERVATIONID'])
                payment_id = cur.callfunc('GENERATE_ID', int, ['PAYMENT', 'PAYMENTID'])
                room_list = []
                for r in range(rooms):
                    if booked == 12:
                        break
                    rid = all_rooms[booked]
                    booked += 1
                    if check(start_date, i, rid, st):
                        room_list.append(rid)
                    else:
                        r -= 1
                if len(room_list) > 0:
                    reservation_charge = 0
                    for room in room_list:
                        cur.execute("SELECT RT.COST_PER_DAY FROM ROOM_TYPE RT, ROOM R WHERE RT.ROOMTYPEID = "
                                    "R.ROOMTYPEID AND R.ROOMID = %s", [room])
                        reservation_charge += cur.fetchone()[0] * st
                    cur.execute("INSERT INTO PAYMENT VALUES(%s, SYSDATE)", [payment_id])
                    connection.commit()
                    sql = "INSERT INTO RESERVATION(RESERVATIONID, DATE_OF_ARRIVAL, DATE_OF_DEPARTURE, CUSTOMERID, PAYMENTID, " \
                          "HOTELID, RESERVATION_CHARGE) VALUES (%s, (TO_DATE(%s, 'DD-MM-YYYY') + INTERVAL '" + str(i) +"' DAY), " \
                            "(TO_DATE(%s, 'DD-MM-YYYY') + INTERVAL '"+ str(i+st) +"' DAY), %s, %s, %s, %s)"
                    cur.execute(sql, [reservation_id, start_date, start_date, cid, payment_id, hotelid, reservation_charge])
                    connection.commit()

                    for room in room_list:
                        cur.execute("INSERT INTO RESERVATION_ROOM VALUES(%s, %s)", [reservation_id, room])
                        connection.commit()



