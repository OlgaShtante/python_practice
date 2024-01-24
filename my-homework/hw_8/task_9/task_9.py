FILE_PATH = 'server_logs.txt'

def process_server_logs(file_path):
    request_counts = {"GET": {"success": 0, "failure": 0},
                      "POST": {"success": 0, "failure": 0},
                      "PUT": {"success": 0, "failure": 0}}

    resource_types = {"/index.html", "/login.php", "/upload.php"}

    with open(file_path, 'r') as file:
        for line in file:
            _, _, _, method, resource, response_code, _ = line.split()

            if resource in resource_types:
                if response_code.startswith(('2', '3')):
                    request_counts[method]["success"] += 1
                elif response_code.startswith(('4', '5')):
                    request_counts[method]["failure"] += 1

    print("Total Requests:\n")
    for method, counts in request_counts.items():
        print(f"Request type - {method}:")
        print(f"Successful: {counts['success']}")
        print(f"Unsuccessful: {counts['failure']}\n")

process_server_logs(FILE_PATH)