from Models.Usuario.Usuario import Usuario

def init(cursor,email,senha):

    global usuario
    usuario = None

    try:
        usuario = Usuario(cursor,email,senha)
    except Exception as error:
        print(error)
    
    if(usuario == None):
        del usuario
        return None

    return usuario
