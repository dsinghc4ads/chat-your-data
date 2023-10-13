import os
import glob

# Set the folder path where the HTML files are stored
folder_path = "data"

# Find all HTML files in the folder using glob
html_files = glob.glob(os.path.join(folder_path, "*.html"))

# Open a new file to write the concatenated HTML to
with open("dhaka_stock_exchange.html", "w") as outfile:
    # Loop over each HTML file and concatenate it to the output file
    for html_file in html_files[0:5]:
        with open(html_file, "r") as infile:
            outfile.write(infile.read().strip() + "\n")
