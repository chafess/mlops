import duckdb

db_path = "ventes.duckdb"
# These are the columns we expect to find
required_columns = {"date", "produit", "categorie", "quantite", "prix_unitaire", "ville"}

con = duckdb.connect(db_path)

# Check if the table exists and get columns
columns = con.execute("DESCRIBE ventes_raw").fetchall()
existing_columns = {col[0] for col in columns}

# Check for missing columns
missing = required_columns - existing_columns
if missing:
    con.close()
    raise ValueError(f"Colonnes manquantes : {missing}")

# Check for NULL values in critical columns
null_count = con.execute("""
    SELECT COUNT(*) FROM ventes_raw 
    WHERE produit IS NULL OR quantite IS NULL OR prix_unitaire IS NULL
""").fetchone()[0]

con.close()

if null_count > 0:
    raise ValueError(f"Données invalides : {null_count} lignes incomplètes")
else:
    print("Validation réussie : schéma et qualité minimale OK")