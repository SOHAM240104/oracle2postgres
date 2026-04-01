import oracledb
import sys
import os

def extract_procedure(proc_name):
    print(f"[*] Extracting '{proc_name}' from Oracle...")
    try:
        user = os.environ.get("ORACLE_USER")
        password = os.environ.get("ORACLE_PASSWORD")
        dsn = os.environ.get("ORACLE_DSN")

        if not user or not password or not dsn:
            print("[-] Missing Oracle connection settings.")
            print("    Set ORACLE_USER, ORACLE_PASSWORD, and ORACLE_DSN in your environment.")
            sys.exit(1)

        # Connect to Oracle
        connection = oracledb.connect(
            user=user,
            password=password,
            dsn=dsn
        )
        cursor = connection.cursor()
        
        # Query Oracle's metadata table for the procedure's source code
        cursor.execute("""
            SELECT text FROM all_source 
            WHERE name = :name AND type = 'PROCEDURE' 
            ORDER BY line
        """, name=proc_name.upper())
        
        lines = cursor.fetchall()
        if not lines:
            print("[-] Procedure not found.")
            sys.exit(1)
            
        # Rebuild the PL/SQL block
        plsql_code = "".join([line[0] for line in lines])
        print("[+] Extraction successful!\n")
        return plsql_code

    except Exception as e:
        print(f"[-] Oracle Connection Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    # Test the extraction
    procedure_name = "PROCESS_ANNUAL_RAISES"
    oracle_source = extract_procedure(procedure_name)
    
    print("--- ORIGINAL ORACLE CODE ---")
    print(oracle_source)
