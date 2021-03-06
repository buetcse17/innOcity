-- CUSTOMER TABLE --
CREATE TABLE CUSTOMER (
	CUSTOMERID NUMBER NOT NULL,
  NAME VARCHAR2(50),
  EMAIL VARCHAR2(50),
  USERNAME VARCHAR2(50),
  PASSWORD VARCHAR2(50),
  GENDER VARCHAR2(50),
  STREET VARCHAR2(50),
  ZIPCODE VARCHAR2(50),
  CITY VARCHAR2(50),
  COUNTRY VARCHAR2(50),
  PHONE_NUM VARCHAR2(50),
  ISVERIFIED VARCHAR2(10) DEFAULT 'NO',
	PRIMARY KEY (CUSTOMERID)
                          
);


--HOTEL TABLE --
CREATE TABLE HOTEL (
	HOTELID NUMBER NOT NULL,
  NAME VARCHAR2(66 ),
  STREET VARCHAR2(50 ),
  ZIPCODE VARCHAR2(50 ),
  CITY VARCHAR2(50 ),
  COUNTRY VARCHAR2(50 ),
  RATING NUMBER(3,2),
  RATINGCOUNT NUMBER,
  PASSWORD VARCHAR2(50 ),
	PRIMARY KEY (HOTELID)
);

-- HOTEL_FACILITY TABLE --
CREATE TABLE HOTEL_FACILITY (
	HOTELID NUMBER,
  FACILITIES VARCHAR2(30)
);

-- ROOM_TYPE TABLE --
CREATE TABLE ROOM_TYPE (
  ROOMTYPEID NUMBER NOT NULL,
  ROOMTYPE_NAME VARCHAR2(20),
  BED_TYPE VARCHAR2(20),
  COST_PER_DAY NUMBER,
  DISCOUNT NUMBER,
  HOTELID NUMBER NOT NULL,
	PRIMARY KEY (ROOMTYPEID),
	FOREIGN KEY (HOTELID) REFERENCES HOTEL (HOTELID)
)


-- ROOM TABLE --
CREATE TABLE ROOM (
	ROOMID NUMBER NOT NULL,
  FLOOR_NUMBER NUMBER,
  HOTELID NUMBER NOT NULL,
  ROOMTYPEID NUMBER NOT NULL,
	PRIMARY KEY(ROOMID),
	FOREIGN KEY(HOTELID) REFERENCES HOTEL(HOTELID),
	FOREIGN KEY(ROOMTYPEID) REFERENCES ROOM_TYPE(ROOMTYPEID)
	
);

-- ROOM_FACILITY TABLE --
CREATE TABLE ROOM_FACILITY (
  ROOMID NUMBER,
  FACILITIES VARCHAR2(50)
)

-- SERVICE TABLE --
CREATE TABLE SERVICE (
  SERVICEID NUMBER NOT NULL,
  SERVICE_TYPE VARCHAR2(20),
  SERVICE_SUBTYPE VARCHAR2(20),
  COST NUMBER,
  HOTELID NUMBER NOT NULL,
	PRIMARY KEY (SERVICEID),
	FOREIGN KEY (HOTELID) REFERENCES HOTEL (HOTELID)
)

-- PAYMENT TABLE --
CREATE TABLE PAYMENT (
  PAYMENTID NUMBER NOT NULL,
  PAYMENT_DATE DATE,
	PRIMARY KEY (PAYMENTID)

);

-- CREDIT CARD TABLE --
CREATE TABLE CREDIT_CARD (
  CARD_NUMBER NUMBER NOT NULL,
  CARD_USERNAME VARCHAR2(50),
  CARD_TYPE VARCHAR2(50),
  CVC NUMBER,
  EXPIRATION DATE,
  CUSTOMERID NUMBER NOT NULL,
	PRIMARY KEY (CARD_NUMBER),
	FOREIGN KEY (CUSTOMERID) REFERENCES CUSTOMER (CUSTOMERID)
);

-- MOBILE_BANKING TABLE --
CREATE TABLE MOBILE_BANKING (
  PHONE_NUMBER NUMBER NOT NULL,
  SERVICE_PROVIDER VARCHAR2(50),
  CUSTOMERID NUMBER NOT NULL,
	PRIMARY KEY (PHONE_NUMBER),
	FOREIGN KEY (CUSTOMERID) REFERENCES CUSTOMER (CUSTOMERID)
);

-- RESERVATION TABLE --
CREATE TABLE RESERVATION (
  RESERVATIONID NUMBER NOT NULL,
  DATE_OF_ARRIVAL DATE,
  DATE_OF_DEPARTURE DATE,
  CUSTOMERID NUMBER NOT NULL,
  PAYMENTID NUMBER NOT NULL,
  HOTELID NUMBER NOT NULL,
  RESERVATION_CHARGE NUMBER,
  RATING NUMBER,
	PRIMARY KEY (RESERVATIONID),
	FOREIGN KEY (CUSTOMERID) REFERENCES CUSTOMER (CUSTOMERID),
	FOREIGN KEY (HOTELID) REFERENCES HOTEL (HOTELID),
	FOREIGN KEY (PAYMENTID) REFERENCES PAYMENT (PAYMENTID)
);

-- RESERVATION_ROOM TABLE --
CREATE TABLE RESERVATION_ROOM (
  RESERVATIONID NUMBER NOT NULL,
  ROOMID NUMBER NOT NULL,
	PRIMARY KEY (RESERVATIONID, ROOMID),
	FOREIGN KEY (RESERVATIONID) REFERENCES RESERVATION (RESERVATIONID),
	FOREIGN KEY (ROOMID) REFERENCES ROOM (ROOMID)
);
-- RESERVATION_SERVICE TABLE --
CREATE TABLE RESERVATION_SERVICE (
  RESERVATIONID NUMBER NOT NULL,
  SERVICEID NUMBER NOT NULL,
  QUANTITY NUMBER NOT NULL,
	PRIMARY KEY (RESERVATIONID, SERVICEID),
	FOREIGN KEY (RESERVATIONID) REFERENCES RESERVATION (RESERVATIONID),
	FOREIGN KEY (SERVICEID) REFERENCES SERVICE (SERVICEID)
	
);