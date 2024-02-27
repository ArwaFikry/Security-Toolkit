import subprocess

def encode_message(infile,message,enckey):
    # print(infile,message)
    outfile = infile[:infile.find(".")] + "steg" + infile[infile.find("."):]
    passwd=1
    """Encode a message using the Snow tool."""
    snow_path = "SNOW.EXE"  # Replace with the actual path to the 'snow' executable
    command = f'{snow_path} -C -Q -p "{passwd}" -m "{message}" {infile} {outfile}'
    subprocess.run(command, shell=True, check=True)

def decode_message(outfile,key):
    passwd=1
    """Decode a message using the Snow tool."""
    snow_path = r'SNOW.EXE'  # Replace with the actual path to the 'snow' executable
    command = f'{snow_path} -C -p "{passwd}" {outfile}'
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, text=True, check=True)
    return result.stdout


