import sys
from pylint import lint

# Set the threshold score below which the linter fails
THRESHOLD = 9  

# Specify the Python file you want to lint (e.g., app.py)
file_to_lint = "app.py"  # Change this to the name of your Flask app file

# Run pylint on the specified file
run = lint.Run([file_to_lint], do_exit=False)

# Retrieve the linter's global note (score)
score = run.linter.stats["global_note"]

# Check if the score is below the threshold and print appropriate messages
if score < THRESHOLD:
    print("Linter failed: Score < threshold value")
    sys.exit(1)  # Exit with a failure code

# If everything is fine, exit with a success code
print(f"Linter passed: Score = {score}")
sys.exit(0)
