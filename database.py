from app.secrets import get_database_credentials

creds = get_database_credentials()

DATABASE_URL = (
    f"postgresql://{creds['username']}:"
    f"{creds['password']}@"
    f"{creds['host']}:"
    f"{creds['port']}/"
    f"{creds['database']}"
)
