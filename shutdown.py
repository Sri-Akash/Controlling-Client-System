import paramiko

def remote_sleep(hostname, username, password):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        ssh.connect(hostname, username=username, password=password)
        stdin, stdout, stderr = ssh.exec_command('sudo systemctl suspend')
        response = stdout.read().decode()
        return f"Success: {response}" if "Connection to" not in response else f"Error: {response}"
    except Exception as e:
        print(f"Error: {e}")
    finally:
        ssh.close()


def remote_shutdown(hostname, username, password):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        ssh.connect(hostname, username=username, password=password)
        stdin, stdout, stderr = ssh.exec_command('sudo shutdown -h now')
        response = stdout.read().decode()
        return f"Success: {response}" if "Connection to" not in response else f"Error: {response}"
    except Exception as e:
        print(f"Error: {e}")
    finally:
        ssh.close()

def remote_logoff(hostname, username, password):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        ssh.connect(hostname, username=username, password=password)
        stdin, stdout, stderr = ssh.exec_command('shutdown /l')
        response = stdout.read().decode()
        return f"Success: {response}" if "Connection to" not in response else f"Error: {response}"
    except Exception as e:
        print(f"Error: {e}")
    finally:
        ssh.close()


def main():
    print("********** Welcome to the Administration **********")
    print('''Enter the option you want to perform on your client machine:\n
            1. Sleep\n
            2. Shutdown\n
            3. Restart\n
            4. Log off
    ''')

    option = int(input())
    no_of_devices = int(input("Enter the number of devices you want to perform the operation on: "))

    for i in range(no_of_devices):
        hostname = input("Enter the remote device IP address: ")
        username = input("Enter the username: ")
        password = input("Enter the password: ")

        if option == 1:
            result = remote_sleep(hostname, username, password)
        elif option == 2:
            result = remote_shutdown(hostname, username, password)
        elif option == 3:
            pass
        elif option == 4:
            result = remote_logoff(hostname, username, password)
        else:
            print("Invalid option. Please choose a valid option.")
            continue

    print(f"Operation result for {hostname}: {result}")

if __name__ == "__main__":
    main()