def process_file(file_name):
    """
    Processes the input file and extracts the Grand Prix name and lap times.

    :param file_name: Path to the input file
    :return: Tuple containing the Grand Prix name and lap times dictionary
    :raises: FileNotFoundError if file doesn't exist
    :raises: ValueError if file format is invalid
    """
    if not file_name:
        raise ValueError("File name cannot be empty")
        
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()

        if not lines:
            raise ValueError("File is empty")

        # First line is the Grand Prix location
        grand_prix = lines[0].strip()
        if not grand_prix:
            raise ValueError("Grand Prix name missing")

        # Process lap times
        lap_times = []
        for line_num, line in enumerate(lines[1:], 2):
            try:
                driver_code = line[:3].strip()
                lap_time = float(line[3:])
                if not driver_code or lap_time <= 0:
                    raise ValueError(f"Invalid data format at line {line_num}")
                lap_times.append((driver_code, lap_time))
            except (ValueError, IndexError) as e:
                raise ValueError(f"Error parsing line {line_num}: {str(e)}")

        return grand_prix, lap_times
        
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {file_name}")
