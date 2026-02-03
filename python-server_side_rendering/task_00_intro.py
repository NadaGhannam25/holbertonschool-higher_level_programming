#!/usr/bin/env python3 

def generate_invitations(template, attendees):
    # Check input types
    if not isinstance(template, str):
        print("Error: Template must be a string.")
        return

    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print("Error: Attendees must be a list of dictionaries.")
        return

    # Check empty template
    if template.strip() == "":
        print("Template is empty, no output files generated.")
        return

    # Check empty attendees list
    if len(attendees) == 0:
        print("No data provided, no output files generated.")
        return

    # Process each attendee
    for index, attendee in enumerate(attendees, start=1):
        output = template

        # Replace placeholders
        placeholders = ["name", "event_title", "event_date", "event_location"]
        for key in placeholders:
            value = attendee.get(key)
            if value is None:
                value = "N/A"
            output = output.replace("{" + key + "}", str(value))

        # Write to output file
        filename = f"output_{index}.txt"
        try:
            with open(filename, "w") as file:
                file.write(output)
        except Exception as e:
            print(f"Error writing file {filename}: {e}")

