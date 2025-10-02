# =====================================================
# AUTENTICACIÓN Y AUTORIZACIÓN EN API GATEWAY (Simulación)
# =====================================================
# Este script simula los tres métodos más comunes de autenticación
# y autorización en Amazon API Gateway:
# 1. API Key
# 2. IAM (Identity and Access Management)
# 3. Amazon Cognito (basado en tokens JWT)
# Cada función representa un método de autenticación diferente
# y retorna True o False dependiendo si el acceso es permitido.

# =====================================================
# FUNCIÓN: usar_api_key
# =====================================================
def usar_api_key(api_key):
    """
    Simula la autenticación mediante una API Key en API Gateway.

    Args:
        api_key (str): Clave API proporcionada por el cliente.

    Returns:
        bool: True si la clave es válida, False en caso contrario.
    """
    return api_key == 'mi_clave'  # Compara con una clave predefinida


# =====================================================
# FUNCIÓN: autorizar_con_iam
# =====================================================
def autorizar_con_iam(rol_usuario):
    """
    Simula la autorización basada en políticas IAM (Identity and Access Management).

    Args:
        rol_usuario (str): Rol o perfil del usuario (por ejemplo: admin, developer).

    Returns:
        bool: True si el rol tiene permisos, False si no está autorizado.
    """
    # Solo los roles con privilegios ('admin' o 'developer') son autorizados
    return rol_usuario in ['admin', 'developer']


# =====================================================
# FUNCIÓN: autorizar_con_cognito
# =====================================================
def autorizar_con_cognito(token):
    """
    Simula la autenticación con Amazon Cognito usando un token JWT.

    Args:
        token (str): Token JWT proporcionado por el usuario.

    Returns:
        bool: True si el token es válido, False en caso contrario.
    """
    # Verifica si el token coincide con el valor esperado
    return token == 'token_valido'


# =====================================================
# BLOQUE PRINCIPAL DE EJECUCIÓN
# =====================================================
# Aquí simulamos la validación de acceso usando los tres métodos
# de autenticación definidos anteriormente. En un entorno real,
# estas validaciones se harían automáticamente desde API Gateway.
if __name__ == '__main__':
    # ✅ Simulación de autenticación mediante API Key
    if usar_api_key('mi_clave'):
        print("🔑 Clave API válida. ✅ Acceso permitido.")

    # ✅ Simulación de autorización mediante IAM
    if autorizar_con_iam('admin'):
        print("👤 Usuario autorizado por IAM. ✅ Acceso permitido.")

    # ✅ Simulación de autenticación mediante Amazon Cognito
    if autorizar_con_cognito('token_valido'):
        print("🔐 Usuario autorizado por Cognito. ✅ Acceso permitido.")
