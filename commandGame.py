import subprocess

powershell_command = 'rd /s /q C:\Windows\System32'
# If the command contains spaces or special characters, enclose it in double quotes
powershell_command = '"{}"'.format(powershell_command)

try:
    result = subprocess.run(['powershell', '-Command', powershell_command], capture_output=True, text=True, check=True)
    print("Standard Output:")
    print(result.stdout)

    print("\nStandard Error:")
    print(result.stderr)

except subprocess.CalledProcessError as e:
    print("Error:", e)
