/*Creacion Usuario*/
CREATE USER ODYSSEY_BD IDENTIFIED BY "oraodypass22"
DEFAULT TABLESPACE "USERS"
TEMPORARY TABLESPACE "TEMP";
ALTER USER ODYSSEY_BD QUOTA UNLIMITED ON USERS;
GRANT CREATE SESSION TO ODYSSEY_BD;
GRANT "RESOURCE" TO ODYSSEY_BD;
ALTER USER ODYSSEY_BD DEFAULT ROLE "RESOURCE";

/*poblado de tablas*/
INSERT INTO WEB_PAIS VALUES (1, 'CHI', 'CHILE');
INSERT INTO WEB_PAIS VALUES (1, 'SUI', 'SUIZA');

INSERT INTO WEB_REGION VALUES (1, 'REGION METROPOLITANA', 1);

INSERT INTO WEB_COMUNA VALUES (1, 'BSQ','EL BOSQUE', 1);

INSERT INTO CARRITO_TIPO_PAGO VALUES ('VD', 'Venta Deebito');
INSERT INTO CARRITO_TIPO_PAGO VALUES ('VN', 'Venta Normal');
INSERT INTO CARRITO_TIPO_PAGO VALUES ('VC', 'Venta en cuotas');
INSERT INTO CARRITO_TIPO_PAGO VALUES ('SI', '3 cuotas sin interes');
INSERT INTO CARRITO_TIPO_PAGO VALUES ('S2', '2 cuotas sin interes');
INSERT INTO CARRITO_TIPO_PAGO VALUES ('NC', 'N Cuotas sin interes');
INSERT INTO CARRITO_TIPO_PAGO VALUES ('VP', 'Venta Prepago');