# ---------------------------------
# Mini SOC Log Analyzer - Version 2
# ---------------------------------

failed_attempts = {}
successful_logins =  {}

# Leer los logs
with open("sample_logs.txt", "r") as file:
    logs = file.readlines()


# Procesar los logs
for line in logs:

    line = line.strip()

    # Detectar login fallido
    if "Failed login" in line:
        ip = line.split()[-1]

        if ip in failed_attempts:
            failed_attempts[ip] += 1
        else:
            failed_attempts[ip] = 1
    

    # Detectar login exitoso
    elif "login success" in line.lower():
        ip = line.split()[-1]

        if ip in successful_logins:
            successful_logins[ip] += 1
        else:
            successful_logins[ip] = 1

print("\n===== SOC ANALYSIS REPORT =====\n")


# Detectar brute force
for ip, attempts in failed_attempts.items():

    print(f"[INFO] {ip} -> Failed attempts: {attempts}")

    if attempts >= 3:
        print(f"ALERT: Possible brute force attack from {ip} ")


# Detectar login sospechoso
for ip in successful_logins:

    if ip in failed_attempts and failed_attempts[ip] >= 3:
        print(f"ALERT: Successful login AFTER multiple failures -> {ip}" )


# Detectar actividad sospechosa
for ip, attempts in failed_attempts.items():

    if attempts >= 5:
        print(f"ALERT: High suspicious activity from {ip}" )

print("\n======== END OF REPORT ========")