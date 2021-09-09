from ansible.module_utils.basic import AnsibleModule
import socket

def get_ip():
    return socket.gethostbyname(socket.gethostname()) 

def main():
    module = AnsibleModule(
        argument_spec=dict(
        )
    )

    result = dict(
        IPAddress=get_ip()
    )

    module.exit_json(**result)

if __name__ == '__main__':
    main()
