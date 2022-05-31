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

/* REGIONES */
INSERT INTO WEB_REGION (nombre, id_pais_id) VALUES ('ARICA Y PARINACOTA' 1);
INSERT INTO WEB_REGION (nombre, id_pais_id) VALUES ('TARAPACÁ', 1);
INSERT INTO WEB_REGION (nombre, id_pais_id) VALUES ('ANTOFAGASTA', 1);
INSERT INTO WEB_REGION (nombre, id_pais_id) VALUES ('ATACAMA', 1);
INSERT INTO WEB_REGION (nombre, id_pais_id) VALUES ('COQUIMBO', 1);
INSERT INTO WEB_REGION (nombre, id_pais_id) VALUES ('VALPARAÍSO', 1);
INSERT INTO WEB_REGION (nombre, id_pais_id) VALUES ('LIBERTADOR GRAL. BERNARDO OHIGGINS', 1);
INSERT INTO WEB_REGION (nombre, id_pais_id) VALUES ('EL MAULE', 1);
INSERT INTO WEB_REGION (nombre, id_pais_id) VALUES ('ÑUBLE', 1);
INSERT INTO WEB_REGION (nombre, id_pais_id) VALUES ('BIOBÍO', 1);
INSERT INTO WEB_REGION (nombre, id_pais_id) VALUES ('LA ARAUCANÍA', 1);
INSERT INTO WEB_REGION (nombre, id_pais_id) VALUES ('LOS RÍOS', 1);
INSERT INTO WEB_REGION (nombre, id_pais_id) VALUES ('LOS LAGOS', 1);
INSERT INTO WEB_REGION (nombre, id_pais_id) VALUES ('AYSÉN DEL GRAL. CARLOS IBAÑEZ DEL CAMPO', 1);
INSERT INTO WEB_REGION (nombre, id_pais_id) VALUES ('MAGALLANES Y LA ANTÁRTICA CHILENA', 1);
INSERT INTO WEB_REGION (nombre, id_pais_id) VALUES ('METROPOLITANA DE SANTIAGO', 1);

/* COMUNAS */
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('ARI','ARICA', 1);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('CMR','CAMARONES', 1);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('PTR','PUTRE', 1);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('LAG','GENERAL LAGOS', 1);

INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('IQQ','IQUIQUE', 2);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('HSP','ALTO HOSPICIO', 2);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('PZA','POZO ALMONTE', 2);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('CAM','CAMIÑA', 2);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('COL','COLCHANE', 2);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('HUA','HUARA', 2);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('PCA','PICA', 2);

INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('AFG','ANTOFAGASTA', 3);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('MEJ','MEJILLONES', 3);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('SIE','SIERRA GORDA', 3);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('TAL','TALTAL', 3);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('CAL','CALAMA', 3);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('OLL','OLLAGÜE', 3);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('ATA','SAN PEDRO DE ATACAMA', 3);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('TPL','TOCOPILLA', 3);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('MAR','MARÍA ELENA', 3);

INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('CPO','COPIAPÓ', 4);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('CAL','CALDERA', 4);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('TAM','TIERRA AMARILLA', 4);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('CHA','CHAÑARAL', 4);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('DGA','DIEGO DE ALMAGRO', 4);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('VALL','VALLENAR', 4);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('CMN','ALTO DEL CARMEN', 4);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('FRE','FREIRINA', 4);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('HUA','HUASCO', 4);

INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('SER','LA SERENA', 5);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('COQ','COQUIMBO', 5);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('AND','ANDACOLLO', 5);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('HIG','LA HIGUERA', 5);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('PAI','PAIGUANO', 5);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('VIC','VICUÑA', 5);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('ILL','ILLAPEL', 5);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('CAN','CANELA', 5);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('VIL','LOS VILOS', 5);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('SAL','SALAMANCA', 5);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('OVA','OVALLE', 5);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('COM','COMBARBALÁ', 5);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('MNT','MONTE PATRIA', 5);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('PUN','PUNITAQUI', 5);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('HUR','RÍO HURTADO', 5);

INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('VAL','VALPARAÍSO', 6);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('CAS','CASABLANCA', 6);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('CON','CONCÓN', 6);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('JFN','JUAN FERNÁNDEZ', 6);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('PCV','PUCHUNCAVÍ', 6);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('QNT','QUINTERO', 6);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('VIÑ','VIÑA DEL MAR', 6);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('IPC','ISLA DE PASCUA', 6);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('AND','LOS ANDES', 6);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('LAR','CALLE LARGA', 6);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('RIN','RINCONADA', 6);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('EST','SAN ESTEBAN', 6);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('LIG','LA LIGUA', 6);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('CAB','CABILDO', 6);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('PAP','PAPUDO', 6);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('PET','PETORCA', 6);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('ZAP','ZAPALLAR', 6);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('QUI','QUILLOTA', 6);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('CAL','CALERA', 6);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('HIJ','HIJUELAS', 6);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('CRZ','LA CRUZ', 6);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('NOG','NOGALES', 6);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('SAN','SAN ANTONIO', 6);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('ALG','ALGARROBO', 6);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('CAR','CARTAGENA', 6);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('QSC','EL QUISCO', 6);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('TAB','EL TABO', 6);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('DOM','SANTO DOMINGO', 6);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('FEL','SAN FELIPE', 6);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('CAT','CATEMU', 6);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('LLY','LLAILLAY', 6);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('PQH','PANQUEHUE', 6);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('PUT','PUTAENDO', 6);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('SMA','SANTA MARÍA', 6);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('QUI','QUILPUÉ', 6);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('LIM','LIMACHE', 6);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('OLM','OLMUÉ', 6);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('ALE','VILLA ALEMANA', 6);

INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('RAN','RANCAGUA', 7);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('COD','CODEGUA', 7);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('COI','COINCO', 7);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('COL','COLTAUCO', 7);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('DOÑ','DOÑIGUE', 7);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('GRA','GRANEROS', 7);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('CAB','LAS CABRAS', 7);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('MAC','MACHALÍ', 7);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('MAL','MALLOA', 7);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('MOS','MOSTAZAL', 7);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('OLI','OLIVAR', 7);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('PEU','PEUMO', 7);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('PIC','PICHIDEGUA', 7);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('TIL','QUINTA DE TILCOCO', 7);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('REN','RENGO', 7);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('REQ','REQUÍNOA', 7);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('VIC','SAN VICENTE', 7);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('PIC','PICHILEMU', 7);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('EST','LA ESTRELLA', 7);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('LIT','LITUECHE', 7);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('MAR','MARCHIHUE', 7);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('NAV','NAVIDAD', 7);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('PAR','PAREDONES', 7);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('FER','SAN FERNANDO', 7);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('CHE','CHÉPICA', 7);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('CHI','CHIMBARONGO', 7);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('LOL','LOLOL', 7);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('NAN','NANCAGUA', 7);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('PAL','PALMILLA', 7);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('PER','PERALILLO', 7);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('PLA','PLACILLA', 7);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('PUM','PUMANQUE', 7);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('SCR','SANTA CRUZ', 7);

INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('TAL','TALCA', 8);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('CON','CONSTITUCION', 8);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('CUR','CUREPTO', 8);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('EMP','EMPEDRADO', 8);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('MAU','MAULE', 8);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('PEL','PELARCO', 8);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('PEN','PENCAHUE', 8);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('RCL','RÍO CLARO', 8);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('CLE','SAN CLEMENTE', 8);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('RAF','SAN RAFAEL', 8);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('CAU','CAUQUENES', 8);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('CHA','CHANCO', 8);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('PEL','PELLUHUE', 8);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('CCO','CURICÓ', 8);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('HLÑ','HUALAÑE', 8);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('LIC','LICANTÉN', 8);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('MOL','MOLINA', 8);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('RAU','RAUCO', 8);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('ROM','ROMERAL', 8);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('SFM','SAGRADA FAMILIA', 8);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('TEN','TENO', 8);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('VIC','VICHUQUÉN', 8);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('LIN','LINARES', 8);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('CBN','COLBÚN', 8);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('LON','LINGAVÍ', 8);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('PAR','PARRAL', 8);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('RET','RETIRO', 8);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('SJV','SAN JAVIER', 8);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('ALE','VILLA ALEGRE', 8);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('YBN','YERBAS BUENAS', 8);

INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('COB','COBQUECURA', 9);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('COE','COELEMU', 9);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('NIN','NINHUE', 9);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('POR','PORTEZUELO', 9);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('QUI','QUIRIHUE', 9);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('RQL','RÁNQUIL', 9);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('TRE','TREGUACO', 9);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('BUL','BULNES', 9);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('CHV','CHILLÁN VIEJO', 9);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('CHI','CHILLÁN', 9);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('CAR','EL CARMEN', 9);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('PEM','PEMUCO', 9);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('PIN','PINTO', 9);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('QUI','QUILLÓN', 9);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('IGN','SAN IGNACIO', 9);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('YGY','YUNGAY', 9);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('COI','COIHUECO', 9);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('ÑQN','ÑIQUÉN', 9);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('CAR','SAN CARLOS', 9);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('FAB','SAN FABIÁN', 9);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('NIC','SAN NICOLÁS', 9);

INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('CON','CONCEPCIÓN', 10);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('COR','CORONEL', 10);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('CHI','CHIGUAYANTE', 10);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('FLO','FLORIDA', 10);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('HUA','HUALQUI', 10);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('LOT','LOTA', 10);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('PEN','PENCO', 10);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('LPZ','SAN PEDRO DE LA PAZ', 10);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('JNA','SANTA JUANA', 10);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('TAL','TALCAHUANO', 10);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('TOM','TOMÉ', 10);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('HUA','HUALPÉN', 10);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('LEB','LEBU', 10);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('ARA','ARAUCO', 10);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('CAÑ','CAÑETE', 10);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('CON','CONTULMO', 10);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('CAR','CARANILAHUE', 10);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('ALA','LOS ÁLAMOS', 10);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('TIR','TIRÚA', 10);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('ANG','LOS ÁNGELES', 10);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('ANT','ANTUCO', 10);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('CAB','CABRERO', 10);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('LAJ','LAJA', 10);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('MUL','MULCHÉN', 10);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('NAC','NACIMIENTO', 10);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('NEG','NEGRETE', 10);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('QCO','QUILACO', 10);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('QLL','QUILLECO', 10);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('ROS','SAN ROSENDO', 10);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('BAR','SANTA BÁRBARA', 10);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('TUC','TUCAPEL', 10);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('YUM','YUMBEL', 10);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('ALT','ALTO BIOBÍO', 10);

INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('TEM','TEMUCO', 11);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('CAR','CARAHUE', 11);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('CUN','CUNCO', 11);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('CUR','CURARREHUE', 11);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('FRE','FREIRE', 11);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('GAL','GALVARINO', 11);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('GOR','GORBEA', 11);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('LAU','LAUTARO', 11);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('LON','LONCOCHE', 11);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('MEL','MELIPEUCO', 11);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('NIM','NUEVA IMPERIAL', 11);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('CAS','PADRE DE LAS CASAS', 11);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('PER','PERQUENCO', 11);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('PIT','PITRUFQUÉN', 11);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('PUC','PUCÓN', 11);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('SAA','SAAVEDRA', 11);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('SCH','TEODORO DE SCHMIDT', 11);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('TOL','TOLTÉN', 11);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('VIL','VILCÚN', 11);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('RCA','VILLARICA', 11);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('CHO','CHOLCHOL', 11);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('ANG','ANGOL', 11);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('COL','COLLIPULLI', 11);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('CUR','CURACAUTÍN', 11);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('ERC','ERCILLA', 11);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('LON','LONQUIMAY', 11);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('SAU','LOS SAUCES', 11);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('LUM','LUMACO', 11);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('PUR','PURÉN', 11);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('REN','RENAICO', 11);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('TRA','TRAIGUÉN', 11);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('VIC','VICTORIA', 11);

INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('VAL','VALDIVIA', 12);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('COR','CORRAL', 12);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('LAN','LANCO', 12);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('LAG','LOS LAGOS', 12);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('MAF','MAFIL', 12);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('MAR','MARIQUINA', 12);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('PAI','PAILLACO', 12);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('PAN','PANGUIPULLI', 12);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('LUN','LA UNIÓN', 12);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('FUT','FUTRONO', 12);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('RAN','LAGO RANCO', 12);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('BUE','RÍO BUENO', 12);

INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('MNT','PUERTO MONTT', 13);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('CAL','CALBUCO', 13);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('COC','COCHAMÓ', 13);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('FRE','FRESIA', 13);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('FRU','FRUTILLAR', 13);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('MUE','LOS MUERMOS', 13);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('LLA','LLANQUIHUE', 13);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('MAU','MAULLÍN', 13);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('VAR','PUERTO VARAS', 13);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('CAS','CASTRO', 13);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('ANC','ANCUD', 13);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('CHO','CHONCHI', 13);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('VEL','CURACO DE VÉLEZ', 13);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('DAL','DALCAHUE', 13);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('PUQ','PUQUELDÓN', 13);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('QLN','QUEILÉN', 13);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('QLL','QUELLÓN', 13);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('QMC','QUEMCHI', 13);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('QUI','QUINCHAO', 13);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('OSO','OSORNO', 13);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('POC','PUERTO OCTAY', 13);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('PRQ','PURRANQUE', 13);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('PUY','PUYEHUE', 13);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('RNG','RÍO NEGRO', 13);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('SJC','SAN JUAN DE LA COSTA', 13);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('SPB','SAN PABLO', 13);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('CTN','CHAITÉN', 13);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('FLF','FUTALEUFÚ', 13);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('HLH','HUALAIHUÉ', 13);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('PLN','PALENA', 13);

INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('CIQ','COYHAIQUE', 14);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('LVD','LAGO VERDE', 14);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('ASN','AISÉN', 14);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('CSN','CISNES', 14);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('GUA','GUAITECAS', 14);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('COC','COCHRANE', 14);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('OHI','OHIGGINS', 14);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('TTL','TORTEL', 14);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('CHC','CHILE CHICO', 14);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('RIB','RÍO IBAÑEZ', 14);

INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('PTA','PUNTA ARENAS', 15);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('LBN','LAGUNA BLANCA', 15);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('RVD','RÍO VERDE', 15);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('SGR','SAN GREGORIO', 15);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('HOR','CABO DE HORNOS (EX NAVARINO)', 15);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('ANT','ANTÁRTICA', 15);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('POR','PORVENIR', 15);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('PRI','PRIMAVERA', 15);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('TKL','TIMAKUEL', 15);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('NLS','NATALES', 15);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('TPA','TORRES DEL PAINE', 15);

INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('CER','CERRILLOS', 16);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('CNV','CERRO NAVIA', 16);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('CNL','CONCHALI', 16);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('BSQ','EL BOSQUE', 16);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('EST','ESTACIÓN CENTRAL', 16);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('HUE','HUECHURABA', 16);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('IND','INDEPENDENCIA', 16);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('LCS','LA CISTERNA', 16);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('FLO','LA FLORIDA', 16);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('GRJ','LA GRANJA', 16);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('PTN','LA PINTANA', 16);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('RNA','LA REINA', 16);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('LCD','LAS CONDES', 16);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('BRN','LO BARNECHEA', 16);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('ESP','LO ESPEJO', 16);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('PRA','LO PRADO', 16);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('MCL','MACUL', 16);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('MPU','MAIPÚ', 16);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('ÑÑA','ÑUÑOA', 16);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('PAC','PEDRO AGUIRRE CERDA', 16);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('PÑL','PEÑALOLÉN', 16);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('PVD','PROVIDENCIA', 16);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('PHL','PUDAHUEL', 16);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('QLC','QUILICURA', 16);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('QNM','QUINTA NORMAL', 16);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('REC','RECOLETA', 16);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('REN','RENCA', 16);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('SGO','SANTIAGO', 16);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('SJQ','SAN JOAQUIN', 16);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('SMG','SAN MIGUEL', 16);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('SRM','SAN RAMÓN', 16);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('VIT','VITACURA', 16);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('PTE','PUENTE ALTO', 16);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('PIR','PIRQUE', 16);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('SJM','SAN JOSE DE MAIPO', 16);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('COL','COLINA', 16);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('LAM','LAMPA', 16);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('TIL','TILTIL', 16);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('SBN','SAN BERNARDO', 16);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('BUI','BUIN', 16);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('TAN','CALERA DE TANGO', 16);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('PNE','PAINE', 16);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('MEL','MELIPILLA', 16);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('ALH','ALHUE', 16);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('CCV','CURACAVÍ', 16);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('MPT','MARÍA PINTO', 16);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('PED','SAN PEDRO', 16);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('TGN','TALAGANTE', 16);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('MTE','EL MONTE', 16);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('IMP','ISLA DE MAIPO', 16);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('HTD','PADRE HURTADO', 16);
INSERT INTO WEB_COMUNA (sigla, nombre, id_region_id) VALUES ('PÑF','PEÑAFLOR', 16);

INSERT INTO CARRITO_TIPO_PAGO VALUES ('VD', 'Venta Deebito');
INSERT INTO CARRITO_TIPO_PAGO VALUES ('VN', 'Venta Normal');
INSERT INTO CARRITO_TIPO_PAGO VALUES ('VC', 'Venta en cuotas');
INSERT INTO CARRITO_TIPO_PAGO VALUES ('SI', '3 cuotas sin interes');
INSERT INTO CARRITO_TIPO_PAGO VALUES ('S2', '2 cuotas sin interes');
INSERT INTO CARRITO_TIPO_PAGO VALUES ('NC', 'N Cuotas sin interes');
INSERT INTO CARRITO_TIPO_PAGO VALUES ('VP', 'Venta Prepago');