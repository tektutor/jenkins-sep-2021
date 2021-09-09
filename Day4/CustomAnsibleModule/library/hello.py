from ansible.module_utils.basic import AnsibleModule

def sayHello(msg):
    return "Hello " + msg + " custom module !"

def main():
    module = AnsibleModule(
        argument_spec=dict(
            msg=dict(type='str')
        )
    )

    message = module.params['msg']

    result = dict(
        response=sayHello(message)
    )

    module.exit_json(**result,changed=True)
    #module.fail_json(msg="Fatal error occurred")

if __name__ == '__main__':
    main()

