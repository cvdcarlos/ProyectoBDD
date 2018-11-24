from configuraciones import *
import psycopg2
conn = psycopg2.connect("dbname=%s user=%s password=%s"%(database,user,passwd))

cur = conn.cursor()
sql ="""select 'drop table "' || tablename || '" cascade;' from pg_tables;"""

cur.execute(sql)
sql="""

CREATE TABLE alumnos
				(rut varchar(9) PRIMARY KEY,nombre varchar,edad integer,correo varchar, cod_curso serial, rut_apod varchar);
"""

cur.execute(sql)
sql="""

CREATE TABLE apoderados
				(rut varchar(9) PRIMARY KEY,nombre varchar,edad integer,telefono integer,correo varchar);
"""

cur.execute(sql)
sql="""
CREATE TABLE cursos
				(cod_curso serial PRIMARY KEY, grado integer, nivel varchar, letra varchar, rut_prof_jefe varchar);
"""

cur.execute(sql)

sql="""
CREATE TABLE salas
				(cod_curso serial PRIMARY KEY, num_sala integer);
"""

cur.execute(sql)
sql="""
CREATE TABLE empleados
				(rut varchar(9) PRIMARY KEY, nombre varchar, rol integer, edad integer, correo varchar, cargo varchar, sueldo integer);
"""

cur.execute(sql)
sql="""
CREATE TABLE ramos
				(cod_ramo serial PRIMARY KEY,cod_curso serial, rut_prof varchar);
"""
cur.execute(sql)
sql="""
CREATE TABLE ramo_info
				(cod_ramo serial PRIMARY KEY, nombre varchar, depto varchar);
"""

cur.execute(sql)
sql="""
CREATE TABLE inasistencias
				(id_inasistencia serial PRIMARY KEY, rut_alum varchar);
"""

cur.execute(sql)
sql="""
CREATE TABLE notas
				(id_notas serial PRIMARY KEY, rut_alum varchar, cod_ramo serial, nota decimal);

"""

cur.execute(sql)


sql="""
CREATE TABLE horario
				(id serial PRIMARY KEY, rut_empleado varchar,dia varchar, modulo varchar);

"""
cur.execute(sql)

conn.commit()
cur.close()
conn.close()
