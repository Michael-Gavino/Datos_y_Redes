def usar_api_key(api_key):
    return api_key == 'mi_clave'

# Simulación de autenticación IAM
def autorizar_con_iam(rol_usuario):
    return rol_usuario in ['admin', 'developer']

# Simulación de autenticación con Cognito (Token JWT)
def autorizar_con_cognito(token):
    return token == 'token_valido'

# Ejemplo de uso
if __name__ == '__main__':
    # Simulación de API Keys
    if usar_api_key('mi_clave'):
        print("Clave API valida. Acceso permitido.")
    
    # Simulación de IAM
    if autorizar_con_iam('admin'):
        print("Usuario autorizado por IAM. Acceso permitido.")
    
    # Simulación de Cognito
    if autorizar_con_cognito('token_valido'):
        print("Usuario autorizado por Cognito. Acceso permitido.")
