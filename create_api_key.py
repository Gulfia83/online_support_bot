from environs import Env
from google.cloud import api_keys_v2


def create_api_key(project_id):
    client = api_keys_v2.ApiKeysClient()

    key = api_keys_v2.Key()
    key.display_name = "My first API key"

    request = api_keys_v2.CreateKeyRequest()
    request.parent = f"projects/{project_id}/locations/global"
    request.key = key

    response = client.create_key(request=request).result()
    return response


def main():
    env = Env()
    env.read_env()
    project_id = env.str('GOOGLE_CLOUD_PROJECT_ID')

    with open('project_api_key.txt', 'a', encoding='utf-8') as stream:
        stream.write(str(create_api_key(project_id)))


if __name__ == '__main__':
    main()
