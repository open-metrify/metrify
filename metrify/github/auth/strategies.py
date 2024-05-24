from metrify.github.utils import generate_jwt


def authenticate(client_id, private_key_path):
    print(client_id)
    print(private_key_path)
    print("JWT:", generate_jwt(client_id, private_key_path, 10))
    # make API call to retrieve access token
    # set acces token in application context
