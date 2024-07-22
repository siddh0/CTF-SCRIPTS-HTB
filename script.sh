#!/bin/bash

# Define the host and port
HOST="83.136.254.16"
PORT="39521"

# Initialize an empty variable to store the concatenated flag characters
concatenated_flags=""

# Loop from 1 to 120
for ((i = 0; i <= 120; i++)); do
    # Send the current number to the specified host and port using netcat and capture the output
  
    output=$(echo "$i" | timeout 0.8 nc "$HOST" "$PORT" | cut -d ":" -f 3| tr -d ' ')
	
    # Concatenate the flag character with the existing concatenated flags
    concatenated_flags+="$output"
    
done

# Print the concatenated flag characters
echo "Concatenated Flag Characters: $concatenated_flags"
