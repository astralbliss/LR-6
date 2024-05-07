def load_config(config_file):
    with open(config_file, 'r') as f:
        config_data = f.readlines()
        for line in config_data:
            if line.startswith('home_directory'):
                home_directory = line.split('=')[1].strip()
                home_directory = home_directory.strip('"')
                return home_directory