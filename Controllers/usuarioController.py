from Models.Usuario import Usuario

def init(email,senha):

    global usuario
    usuario = None

    try:
        usuario = Usuario(email,senha)
    except Exception as error:
        print(error)
    
    if(usuario == None):
        del usuario
        return None

    return usuario
