"""
University Workshop Feedback Manager
Description: Processes messy student feedback text, demonstrates file I/O 
             operations (write, read, append), handles file exceptions safely, 
             and generates a feedback summary report.
"""

def main():
    # =========================================================================
    # QUESTION 1: STRING MANIPULATION & CLEANING
    # =========================================================================
    print("==================================================")
    print("  : STRING MANIPULATION & CLEANING      ")
    print("==================================================")
    
    # Raw feedback collected from the student survey
    raw_feedback = " THE SPEAKER WAS GREAT but THE ROOM WAS COLD "
    
    # 1. Strip leading/trailing spaces and convert to lowercase
    step1_clean = raw_feedback.strip().lower()
    
    # 2. Replace "speaker" with "presenter" and fix internal extra spaces
    step2_replaced = step1_clean.replace("speaker", "presenter")
    step2_clean_spaces = " ".join(step2_replaced.split())
    
    # 3. Convert cleaned text to title case
    final_cleaned_feedback = step2_clean_spaces.title()
    
    # Display results using f-string
    print(f"Raw Feedback     : '{raw_feedback}'")
    print(f"Cleaned Output   : '{final_cleaned_feedback}'\n")

    # =========================================================================
    # QUESTION 2: FILE I/O OPERATIONS (WRITE, READ, APPEND)
    # =========================================================================
    print("==================================================")
    print("  : FILE I/O OPERATIONS                 ")
    print("==================================================")
    
    feedback_file = "feedback.txt"
    
    # List containing three cleaned feedback messages
    feedback_list = [
        final_cleaned_feedback,
        "The Presentation Was Great And Very Informative",
        "Overall Great Experience But Started Late"
    ]
    
    # 1. Write the initial list to feedback.txt (each entry on a new line)
    with open(feedback_file, "w") as file:
        for entry in feedback_list:
            file.write(entry + "\n")
    print(f"--> Successfully wrote {len(feedback_list)} entries to '{feedback_file}'.\n")

    # 2. Read and print initial contents of feedback.txt
    print(f"--- Contents of '{feedback_file}' (Initial Read) ---")
    with open(feedback_file, "r") as file:
        for line in file:
            print(line.strip())
    print("--------------------------------------------------\n")

    # 3. Append a fourth feedback message to the file
    appended_message = "The Content Was Good But Could Be Shorter"
    with open(feedback_file, "a") as file:
        file.write(appended_message + "\n")
    print(f"--> Successfully appended 1 new entry to '{feedback_file}'.\n")

    # Read and print the full updated list
    print(f"--- Contents of '{feedback_file}' (Updated Read) ---")
    with open(feedback_file, "r") as file:
        for line in file:
            print(line.strip())
    print("--------------------------------------------------\n")

    # =========================================================================
    # QUESTION 3: STRUCTURED EXCEPTION HANDLING
    # =========================================================================
    print("==================================================")
    print("  : EXCEPTION HANDLING DEMONSTRATION    ")
    print("==================================================")
    
    # Safe reading block with specific error handling and finally block
    try:
        print(f"Attempting to open and read '{feedback_file}'...")
        with open(feedback_file, "r") as file:
            file_contents = file.read()
            print("\nFile read successfully!")
            
    except FileNotFoundError:
        print("File not found. Please create feedback.txt first.")
        
    except PermissionError:
        print("Permission denied. Close the file and try again.")
        
    finally:
        print("Operation completed.\n")

    # =========================================================================
    # : ANALYTICS & SUMMARY REPORT GENERATION
    # =========================================================================
    print("==================================================")
    print("  QUESTION 4: SUMMARY REPORT GENERATION           ")
    print("==================================================")
    
    total_feedback_count = 0
    great_mention_count = 0
    summary_file = "summary.txt"

    try:
        # 1. Read file and count occurrences of "great" (case-insensitive)
        with open(feedback_file, "r") as file:
            for line in file:
                cleaned_line = line.strip()
                if cleaned_line:  # Exclude empty lines
                    total_feedback_count += 1
                    if "great" in cleaned_line.lower():
                        great_mention_count += 1

        # 2. Prepare formatted summary text
        summary_content = (
            "=== Workshop Feedback Summary ===\n"
            f"Total Feedback: {total_feedback_count}\n"
            f"Mentions of 'Great': {great_mention_count}\n"
        )

        # Write summary report to summary.txt
        with open(summary_file, "w") as file:
            file.write(summary_content)
        print(f"--> Successfully generated '{summary_file}'.\n")

        # 3. Print formatted summary to console using f-strings
        print("--- Console Output Summary ---")
        print(f"=== Workshop Feedback Summary ===")
        print(f"Total Feedback: {total_feedback_count}")
        print(f"Mentions of 'Great': {great_mention_count}")
        print("------------------------------")

    except FileNotFoundError:
        print(f"Error: {feedback_file} does not exist.")


if __name__ == "__main__":
    main()
