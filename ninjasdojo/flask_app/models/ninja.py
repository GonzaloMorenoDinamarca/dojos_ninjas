from flask_app.config.mysqlconnection import connectToMySQL

class Ninja:
    def __init__(self,data):

        self.id = data['id']
        self.nombre = data['nombre']
        self.apellido = data['apellido']
        self.edad = data['edad']
	
    @classmethod
    def create_ninja(cls, data):
        query = "INSERT INTO ninjas (nombre, apellido, edad, dojo_id, creado_en, actualizado_en) VALUES (%(nombre)s, %(apellido)s, %(edad)s, %(dojo_id)s, NOW(), NOW())"
        return connectToMySQL('esquema_dojos_y_ninjas').query_db(query, data)

    @classmethod
    def all_ninjas(cls):
        query = "SELECT * FROM ninjas;"
        ninjas_db =  connectToMySQL('esquema_dojos_y_ninjas').query_db(query)
        ninjas =[]
        for n in ninjas_db:
            ninjas.append(cls(n))
        return ninjas

"""    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM ninjas WHERE dojo.id = %(id)s;"
        ninjas_db = connectToMySQL('esquema_dojos_y_ninjas').query_db(query,data)
        return cls(ninjas_db[0])  """