from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ninja

class Dojo:
    def __init__(self,data):

        self.id= data['id']
        self.primer_nombre = data['primer_nombre']

        self.ninja=[]

    @classmethod
    def create_dojo(cls, data):
        query = "INSERT INTO dojos (primer_nombre, creado_en, actualizado_en) VALUES (%(primer_nombre)s, NOW(), NOW());"
        return connectToMySQL('esquema_dojos_y_ninjas').query_db(query, data)

    @classmethod
    def all_dojos(cls):
        query = "SELECT * FROM dojos;"
        dojos_db =  connectToMySQL('esquema_dojos_y_ninjas').query_db(query)
        dojos =[]
        for dojo in dojos_db:
            dojos.append(cls(dojo))
        return dojos

    @classmethod
    def ninjas_con_dojos( cls , data ):
        print("COMO LLEGA EL DATO?", data)
        query = """SELECT  dojos.id, dojos.primer_nombre, ninjas.nombre, ninjas.apellido, ninjas.edad  FROM dojos LEFT JOIN 
        ninjas ON ninjas.dojo_id = dojos.id WHERE dojos.id = %(id)s;"""
        results = connectToMySQL('esquema_dojos_y_ninjas').query_db( query, data )
        print(results, "RESULTADO QUERY")
        dojo = cls( results[0] )
        for row_db in results:
            ninja_data = {
                "id" : row_db["id"],
                "nombre" : row_db["nombre"],
                "apellido" : row_db["apellido"],
                "edad" : row_db["edad"],
            }
            dojo.ninja.append(ninja.Ninja( ninja_data ) )
        return dojo 