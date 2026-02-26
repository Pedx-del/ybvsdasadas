import requests

def check_subdomains(file_path):
    working_domains = []
    with open(file_path, 'r') as file:
        subdomains = [line.strip() for line in file if line.strip()]

    for subdomain in subdomains:
        try:
            response = requests.get(f'http://{subdomain}', timeout=5)
            if response.status_code == 200:
                print(f'{subdomain} está funcionando.')
                working_domains.append(subdomain)
            else:
                print(f'{subdomain} não está funcionando.')
        except requests.exceptions.RequestException:
            print(f'{subdomain} não está funcionando.')

    print('\nDomínios funcionando:')
    for domain in working_domains:
        print(domain)

# Exemplo de uso: substitua 'subdominios.txt' pelo nome do seu arquivo
check_subdomains('sub.txt')