import os
import subprocess
from pathlib import Path

def ai_to_svg(input_folder, output_folder):
    """Convert all .ai files in folder to SVG using Inkscape"""

    input_folder = str(Path(input_folder))
    output_folder = str(Path(output_folder))

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    inkscape_paths = [
        r"C:\Program Files\Inkscape\bin\inkscape.exe"
    ]

    inkscape = None
    for path in inkscape_paths:
        if os.path.exists(path):
            inkscape = path
            break

    if not inkscape:
        raise FileNotFoundError("Inkscape not found. Please install Inkscape first")

    for filename in os.listdir(input_folder):
        if filename.lower().endswith('.ai'):
            input_path = os.path.join(input_folder, filename)
            output_name = f"{os.path.splitext(filename)[0]}.svg"
            output_path = os.path.join(output_folder, output_name)

            try:
                subprocess.run([
                    inkscape,
                    '--export-filename=' + output_path,
                    input_path
                ], check=True)
                print(f"✅ Converted: {filename}")
            except subprocess.CalledProcessError as e:
                print(f"❌ Failed to convert {filename}: {e}")

# Usage - Notice the raw strings (r prefix) for Windows paths
ai_to_svg(
    r'path\to\ai\folder',
    r'path\to\output\folder'
)