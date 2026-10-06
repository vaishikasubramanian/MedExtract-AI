import os
import zipfile

def package_project():
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    zip_filename = os.path.join(project_root, 'medextract.zip')

    ignore_dirs = {'.git', '.venv', '.pytest_cache', '__pycache__', 'output', '.idea', '.vscode'}
    ignore_extensions = {'.zip', '.pyc', '.pyo', '.pyd'}

    count = 0
    total_bytes = 0

    print(f"Packaging project from {project_root} into {zip_filename}...")

    with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(project_root):
            # Filter directories in place to avoid traversing ignored ones
            dirs[:] = [d for d in dirs if d not in ignore_dirs and not d.startswith('pytest-cache-files')]
            
            for file in files:
                ext = os.path.splitext(file)[1].lower()
                if ext in ignore_extensions:
                    continue
                if file == 'medextract.zip':
                    continue
                    
                abs_path = os.path.join(root, file)
                rel_path = os.path.relpath(abs_path, project_root)
                
                # Write file with relative path inside archive (with top-level folder 'medextract/')
                arcname = os.path.join('medextract', rel_path)
                zipf.write(abs_path, arcname)
                count += 1
                total_bytes += os.path.getsize(abs_path)

    zip_size = os.path.getsize(zip_filename)
    print(f"Successfully created {zip_filename}")
    print(f"Total files compressed: {count}")
    print(f"Uncompressed size: {total_bytes / (1024*1024):.2f} MB")
    print(f"Compressed ZIP size: {zip_size / (1024*1024):.2f} MB")

if __name__ == "__main__":
    package_project()
