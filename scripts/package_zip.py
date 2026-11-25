#!/usr/bin/env python3
"""
DRISHTI-NER Source Code Packager
Creates a standalone, clean, production-ready .zip archive of the entire codebase
for deployment, inspection, and local execution on any operating system.
"""

import os
import sys
import zipfile
from pathlib import Path

# Base workspace path
WORKSPACE_ROOT = Path(__file__).resolve().parent.parent
OUTPUT_ZIP = WORKSPACE_ROOT / "public" / "drishti-ner-source-code.zip"

# Exclude patterns
EXCLUDE_DIRS = {
    "node_modules",
    ".git",
    ".cache",
    "dist",
    ".tmp",
    "__pycache__",
    ".idea",
    ".vscode",
}

EXCLUDE_EXTENSIONS = {
    ".zip",
    ".tar",
    ".gz",
    ".log",
    ".tmp",
    ".swp",
}

EXCLUDE_FILENAMES = {
    ".DS_Store",
    "Thumbs.db",
    "drishti-ner-source-code.zip",
}

def should_include(rel_path: Path) -> bool:
    # Check directory parts
    for part in rel_path.parts[:-1]:
        if part in EXCLUDE_DIRS or part.startswith(".git"):
            return False
            
    # Check filename
    filename = rel_path.name
    if filename in EXCLUDE_FILENAMES:
        return False
        
    # Check extension
    if rel_path.suffix.lower() in EXCLUDE_EXTENSIONS:
        return False
        
    return True

def package_project():
    print(f"📦 Packaging DRISHTI-NER source code from: {WORKSPACE_ROOT}")
    
    # Ensure public folder exists
    OUTPUT_ZIP.parent.mkdir(parents=True, exist_ok=True)
    
    # Remove existing zip if present
    if OUTPUT_ZIP.exists():
        OUTPUT_ZIP.unlink()
        
    total_files = 0
    total_uncompressed_bytes = 0
    
    # Pre-filter files to include
    files_to_pack = []
    for root, dirs, files in os.walk(WORKSPACE_ROOT):
        # Filter directories in-place to avoid descending into excluded ones
        dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS and not d.startswith(".git")]
        
        for file in files:
            full_path = Path(root) / file
            rel_path = full_path.relative_to(WORKSPACE_ROOT)
            
            if should_include(rel_path):
                files_to_pack.append((full_path, rel_path))

    # Create ZIP archive
    with zipfile.ZipFile(OUTPUT_ZIP, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as zipf:
        for full_path, rel_path in sorted(files_to_pack, key=lambda x: str(x[1])):
            # Store files under top-level 'drishti-ner/' folder for clean extraction
            archive_path = Path("drishti-ner") / rel_path
            zipf.write(full_path, arcname=str(archive_path))
            total_files += 1
            total_uncompressed_bytes += full_path.stat().st_size
            
    # Verify archive
    with zipfile.ZipFile(OUTPUT_ZIP, "r") as zipf:
        test_result = zipf.testzip()
        if test_result is not None:
            print(f"❌ Zip verification failed on: {test_result}", file=sys.stderr)
            sys.exit(1)
            
    zip_size_bytes = OUTPUT_ZIP.stat().st_size
    zip_size_kb = zip_size_bytes / 1024
    uncompressed_mb = total_uncompressed_bytes / (1024 * 1024)
    
    print("✅ DRISHTI-NER source package successfully created!")
    print(f"📁 Destination: {OUTPUT_ZIP}")
    print(f"📄 Files packaged: {total_files}")
    print(f"📊 Uncompressed: {uncompressed_mb:.2f} MB")
    print(f"🗜️  ZIP archive size: {zip_size_kb:.2f} KB ({zip_size_bytes} bytes)")
    print("🚀 Ready for download and deployment on any operating system.")

if __name__ == "__main__":
    package_project()
