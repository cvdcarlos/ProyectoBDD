from configuraciones import *
import psycopg2
conn = psycopg2.connect("dbname=%s user=%s password=%s"%(database,user,passwd))

cur = conn.cursor()

sql="""
insert into alumnos (rut, nombre, edad, correo, cod_curso, rut_apod) values ('18432989', 'Pedro', 15, 'Pedro@colegio.cl', '3', '4324342'),
																			('19423421', 'Pepo', 16, 'Pepo@colegio.cl', '3', '65645645'),
																			('17323211', 'car', 14, 'car@colegio.cl', '3', '67867866'),
																			('16434321', 'fgfg', 13, 'fgfg@colegio.cl', '3', '1244352');
"""
cur.execute(sql)

sql="""
insert into apoderados (rut, nombre, edad, telefono, correo) values ('12345678', 'Juan', 45, 2222123, 'Juan@mail.cl');
"""
cur.execute(sql)

sql="""
insert into cursos (grado, nivel, letra, rut_prof_jefe) values (1,'basico', 'A', '12234567'),
				 											   (1,'basico', 'B', '12234561'),
				 											   (1,'basico', 'C', '12234562'),
															   (2,'basico', 'A', '12234563'),
															   (2,'basico', 'B', '12234564'),
															   (2,'basico', 'C', '12234565'),
															   (3,'basico', 'A', '12234566'),
															   (3,'basico', 'B', '12234568'),
															   (3,'basico', 'C', '12234569'),
															   (4,'basico', 'A', '12234560'),
															   (4,'basico', 'B', '22234567'),
															   (4,'basico', 'C', '22234561'),
															   (5,'basico', 'A', '22234562'),
															   (5,'basico', 'B', '22234563'),
															   (5,'basico', 'C', '22234564'),
															   (6,'basico', 'A', '22234565'),
															   (6,'basico', 'B', '22234566'),
															   (6,'basico', 'C', '22234568'),
															   (7,'basico', 'A', '22234569'),
															   (7,'basico', 'B', '22234560'),
															   (7,'basico', 'C', '32234567'),
															   (8,'basico', 'A', '32234561'),
															   (8,'basico', 'B', '32234562'),
															   (8,'basico', 'C', '32234563'),
															   (1,'medio', 'A', '32234564'),
															   (1,'medio', 'B', '32234565'),
															   (1,'medio', 'C', '32234566'),
															   (2,'medio', 'A', '32234568'),
															   (2,'medio', 'B', '32234569'),
															   (2,'medio', 'C', '32234560'),
															   (3,'medio', 'A', '42234567'),
															   (3,'medio', 'B', '42234561'),
															   (3,'medio', 'C', '42234562'),
															   (4,'medio', 'A', '42234563'),
															   (4,'medio', 'B', '42234564'),
															   (4,'medio', 'C', '42234565'); 
"""
cur.execute(sql)

sql="""
insert into salas (cod_curso, num_sala) values (1, 102),
				 							   (2, 11),
				 							   (3, 123),
											   (4, 124),
											   (5, 203),
											   (6, 200),
											   (7, 201),
											   (8, 300),
											   (9, 911),
											   (10, 133),
											   (11, 131),
											   (12, 132),
											   (13, 500),
											   (14, 550),
											   (15, 23),
											   (16, 77),
											   (17, 78),
											   (18, 79),
											   (19, 80),
											   (20, 81),
											   (21, 82),
											   (22, 83),
											   (23, 84),
											   (24, 85),
											   (25, 86),
											   (26, 87),
											   (27, 88),
											   (28, 89),
											   (29, 90),
											   (30, 91),
											   (31, 92),
											   (32, 93),
											   (33, 94),
											   (34, 95),
											   (35, 96),
											   (36, 97);
"""
cur.execute(sql)

sql="""
insert into empleados (rut, nombre, rol, edad, correo, cargo, sueldo) values ('12234567', 'Diego', 2, 33, 'Diego@prof.colegio.cl', 'profesor_jefe', 300000),
 																			('12234561', 'Jano', 2, 35, 'Jano@prof.colegio.cl', 'profesor_jefe', 3000000),
 																			('12234562', 'Juan', 2, 43, 'Juan@prof.colegio.cl', 'profesor_jefe', 30223000),
 																			('12234563', 'Dago', 2, 23, 'Dago@prof.colegio.cl', 'profesor_jefe', 100000),
 																			('12234564', 'Javier', 2, 30, 'Javier@prof.colegio.cl', 'profesor_jefe', 200000),
 																			('12234565', 'Perez', 2, 40, 'Perez@prof.colegio.cl', 'profesor_jefe', 500000),
 																			('12234566', 'Camila', 2, 33, 'Camila@prof.colegio.cl', 'profesor_jefe', 350000),
 																			('12234568', 'Camilo', 2, 35, 'Camilo@prof.colegio.cl', 'profesor_jefe', 370000),
 																			('12234569', 'Daniela', 2, 33, 'Daniela@prof.colegio.cl', 'profesor_jefe', 150000),
 																			('12234560', 'Diego', 2, 33, 'Diego@prof.colegio.cl', 'profesor_jefe', 300000),
 																			('22234567', 'Julio', 2, 34, 'Julio@prof.colegio.cl', 'profesor_jefe', 300000),
 																			('22234561', 'Julian', 2, 35, 'Julian@prof.colegio.cl', 'profesor_jefe', 3000000),
 																			('22234562', 'Julito', 2, 43, 'Julito@prof.colegio.cl', 'profesor_jefe', 30223000),
 																			('22234563', 'Mateo', 2, 23, 'Mateo@prof.colegio.cl', 'profesor_jefe', 100000),
 																			('22234564', 'Fernanda', 2, 30, 'Fernanda@prof.colegio.cl', 'profesor_jefe', 200000),
 																			('22234565', 'Fernando', 2, 40, 'Fernando@prof.colegio.cl', 'profesor_jefe', 500000),
 																			('22234566', 'Tamara', 2, 33, 'Tamara@prof.colegio.cl', 'profesor_jefe', 350000),
 																			('22234568', 'Juancho', 2, 35, 'Juancho@prof.colegio.cl', 'profesor_jefe', 370000),
 																			('22234569', 'Julieta', 2, 33, 'Julieta@prof.colegio.cl', 'profesor_jefe', 150000),
 																			('22234560', 'Romeo', 2, 33, 'Romeo@prof.colegio.cl', 'profesor_jefe', 300000),
 																			('32234567', 'Paulo', 2, 33, 'Paulo@prof.colegio.cl', 'profesor_jefe', 300000),
 																			('32234561', 'Paul', 2, 35, 'Paul@prof.colegio.cl', 'profesor_jefe', 3000000),
 																			('32234562', 'Paula', 2, 43, 'Paula@prof.colegio.cl', 'profesor_jefe', 30223000),
 																			('32234563', 'Paulina', 2, 23, 'Paulina@prof.colegio.cl', 'profesor_jefe', 100000),
 																			('32234564', 'Pauler', 2, 30, 'Pauler@prof.colegio.cl', 'profesor_jefe', 200000),
 																			('32234565', 'Paulz', 2, 40, 'Paulz@prof.colegio.cl', 'profesor_jefe', 500000),
 																			('32234566', 'Paulla', 2, 33, 'Paulla@prof.colegio.cl', 'profesor_jefe', 0),
 																			('32234568', 'Paullo', 2, 35, 'Paullo@prof.colegio.cl', 'profesor_jefe', 0),
 																			('32234569', 'Paulela', 2, 33, 'Paulela@prof.colegio.cl', 'profesor_jefe', 150000),
 																			('32234560', 'Pablo', 2, 33, 'Pablo@prof.colegio.cl', 'profesor_jefe', 300000),
 																			('42234567', 'Carloso', 2, 33, 'Carloso@prof.colegio.cl', 'profesor_jefe', 300000),
 																			('42234561', 'Carlosa', 2, 35, 'Carlosa@prof.colegio.cl', 'profesor_jefe', 3000000),
 																			('42234562', 'Carlota', 2, 43, 'Carlota@prof.colegio.cl', 'profesor_jefe', 30223000),
 																			('42234563', 'Carlali', 2, 23, 'Carlali@prof.colegio.cl', 'profesor_jefe', 100000),
 																			('42234564', 'Carloser', 2, 30, 'Carloser@prof.colegio.cl', 'profesor_jefe', 200000),
 																			('42234565', 'Carlosz', 2, 40, 'Carlosz@prof.colegio.cl', 'profesor_jefe', 500000);													
"""
cur.execute(sql)

sql="""
insert into ramos (cod_curso, rut_prof) values (1, '12234567'); 
"""
cur.execute(sql)

sql="""
insert into ramo_info (cod_ramo, nombre, depto) values (1, 'Matematicas', 'Ciencias'),
													   (2, 'Lenguaje', 'Humanista'),
													   (3, 'Historia', 'Humanista'),
													   (4, 'Fisica', 'Ciencias'),
													   (5, 'Quimica', 'Ciencias'),
													   (6, 'Biologia', 'Ciencias'),
													   (7, 'Ed.Fisica', 'Deporte'),
													   (8, 'Arte', 'arte'),
													   (9, 'Filosofia', 'Humanista'),
													   (10, 'Musica', 'arte'); 
"""
cur.execute(sql)

sql="""
insert into inasistencias (rut_alum) values ('18432989');
"""
cur.execute(sql)

sql="""
insert into notas (rut_alum, cod_ramo, nota) values ('18432989', 3, 5.0);
"""
cur.execute(sql)

sql="""
insert into horario (rut_empleado, dia, modulo) values ('12234567', 'Lunes', 'A'),
													   ('12234567', 'Miercoles', 'C'),
													   ('12234565', 'Jueves', 'A'),
													   ('22234567', 'Lunes', 'B'); 
"""
cur.execute(sql)

conn.commit()
cur.close()
conn.close()