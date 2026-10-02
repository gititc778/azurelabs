import os
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient

vault_url = os.environ["KEY_VAULT_URL"]

credential = DefaultAzureCredential()
client = SecretClient(vault_url=vault_url, credential=credential)

for secret_properties in client.list_properties_of_secrets():
    secret_name = secret_properties.name
    secret = client.get_secret(secret_name)

    env_name = secret_name.replace("-", "_").upper()
    os.environ[env_name] = secret.value

    print(f"Loaded: {env_name}")

print("All Key Vault secrets loaded.")