# Simulación de control de acceso en API Gateway

# Simulación de generación y uso de API Keys
def use_api_key(api_key):
    if api_key == 'my_api_key':
        return True
    else:
        return False

# Simulación de autenticación IAM
def authorize_with_iam(user_role):
    authorized_roles = ['admin', 'developer']
    if user_role in authorized_roles:
        return True
    else:
        return False

# Simulación de autenticación con Cognito (JWT Token)
def authorize_with_cognito(token):
    # Simulamos decodificar el token JWT
    if token == 'valid_jwt_token':
        return True
    else:
        return False

# Ejemplo de uso
if __name__ == '__main__':
    # Simulación de API Keys
    api_key = 'my_api_key'
    if use_api_key(api_key):
        print("API Key válida. Acceso permitido.")

    # Simulación de IAM
    user_role = 'admin'
    if authorize_with_iam(user_role):
        print("Usuario autorizado por IAM. Acceso permitido.")

    # Simulación de Cognito
    jwt_token = 'valid_jwt_token'
    if authorize_with_cognito(jwt_token):
        print("Usuario autorizado por Cognito. Acceso permitido.")
