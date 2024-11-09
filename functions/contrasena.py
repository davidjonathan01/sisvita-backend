import bcrypt

# Hashing la contraseña
def hash_password(password):
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode(), salt)
    return hashed.decode()

# Verificando la contraseña
def check_password(stored_hash, password):
    return bcrypt.checkpw(password.encode(), stored_hash)

'''# Ejemplo de uso
password = "mi_contraseña_segura"
hashed_password = hash_password(password)
print(f"Hashed: {hashed_password}")

# Verificación
is_valid = check_password(hashed_password, password)
print(f"Contraseña válida: {is_valid}")'''
