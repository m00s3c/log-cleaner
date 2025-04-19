import os

def process_file(input_path, output_path):
    # preheader lines
    preheader_lines = [
        "WigleWifi-1.4,appRelease=2.0,model=S33,release=XtremeFW,device=Flipper Zero,display=Monochrome LCD,board=ESP32,brand=Flipper Devices\n",
        "MAC,SSID,AuthMode,FirstSeen,Channel,RSSI,CurrentLatitude,CurrentLongitude,AltitudeMeters,AccuracyMeters,Type\n"
    ]

    processed_lines = []
    found_data = False

    # open/read input file
    with open(input_path, 'r') as file:
        for line in file:
            if not found_data:
                # check for the pipe symbol "|"
                if '| ' in line and line.split()[0].isdigit():
                    found_data = True
                    processed_lines.extend(preheader_lines)  # add preheader
                    processed_line = line.split('| ', 1)[1]  # remove number and pipe
                    processed_lines.append(processed_line)
            elif found_data:
                # process the rest
                if '| ' in line:
                    processed_line = line.split('| ', 1)[1]  # remove number and pipe
                    processed_lines.append(processed_line)
                else:
                    processed_lines.append(line)  # leave other lines unchanged

    # write to output file
    with open(output_path, 'w') as file:
        file.writelines(processed_lines)

    print(f"Output saved to: {output_path}, now go upload to WiGLE!")


if __name__ == "__main__":
    input_directory = "./logs"  # Directory containing input .log files
    output_directory = "./processed_logs"  # Directory for output .log files

    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # Process each .log file in the input directory
    for filename in os.listdir(input_directory):
        if filename.endswith(".log"):
            input_file = os.path.join(input_directory, filename)
            output_file = os.path.join(output_directory, f"processed_{filename}")
            process_file(input_file, output_file)
            
