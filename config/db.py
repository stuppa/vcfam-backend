from sqlalchemy import create_engine, MetaData

# Sustituye la contraseña oculta con tu contraseña real
DB_PASSWORD = "a09OtutxIaKVg2naCR-6_asIYS-HAGSQ"

# Construye la URL de conexión
DATABASE_URL = f"postgresql://wgowvvga:{DB_PASSWORD}@bubble.db.elephantsql.com/wgowvvga"

meta = MetaData()
engine = create_engine(DATABASE_URL)

conn = engine.connect()