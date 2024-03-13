import subprocess


def execute_command(command):
    try:
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {e}")


def redirect_input_output(command, input_file=None, output_file=None):
    stdin = None
    stdout = None

    if input_file:
        try:
            stdin = open(input_file, 'r')
        except IOError as e:
            print(f"Error opening input file: {e}")
            return None

    if output_file:
        try:
            stdout = open(output_file, 'w')
        except IOError as e:
            print(f"Error opening output file: {e}")
            return None

    try:
        subprocess.run(command, shell=True, check=True, stdin=stdin, stdout=stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {e}")
    finally:
        if stdin:
            stdin.close()
        if stdout:
            stdout.close()


def main():
    while True:
        command = input("Enter command (or 'exit' to quit): ")
        if command.strip() == 'exit':
            print("Exiting...")
            break

        parts = command.split(">")
        input_file = None

        if len(parts) == 2:
            input_command = parts[0].strip()
            output_command = parts[1].strip()
            parts = output_command.split("<")
            if len(parts) == 2:
                output_command = parts[0].strip()
                input_file = parts[1].strip()

            redirect_input_output(input_command, input_file)
            execute_command(output_command)
        else:
            execute_command(command)


if __name__ == "__main__":
    main()
