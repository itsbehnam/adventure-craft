from dotenv import dotenv_values

config = dotenv_values(".env")
provider = config.get('PROVIDER')

def main():
    if provider == 'OPENAI':
        pass
    elif provider == 'OLLAMA':
        pass

if __name__ == "__main__":
    main()
