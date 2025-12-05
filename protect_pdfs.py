#!/usr/bin/env python3
"""
Script to protect all PDF files with password using pypdf
Password is read from environment variable PDF_PASSWORD or config file
"""

import os
from pathlib import Path
from pypdf import PdfReader, PdfWriter

# Password to protect PDFs - read from environment variable or config file
PASSWORD = os.getenv('PDF_PASSWORD')
if not PASSWORD:
    # Try to read from local config file (not committed to git)
    config_file = Path(__file__).parent / 'pdf_password.txt'
    if config_file.exists():
        PASSWORD = config_file.read_text(encoding='utf-8').strip()
    else:
        print("ERROR: Password not found!")
        print("Please set PDF_PASSWORD environment variable or create pdf_password.txt file")
        print("Example: export PDF_PASSWORD='your_password'")
        exit(1)

# Directory containing PDFs
BASE_DIR = Path(__file__).parent

def protect_pdf(input_path, output_path, password):
    """Protect a PDF file with password using pypdf"""
    try:
        # Read the PDF
        reader = PdfReader(input_path)
        writer = PdfWriter()
        
        # Copy all pages
        for page in reader.pages:
            writer.add_page(page)
        
        # Add password (AES 256-bit encryption)
        writer.encrypt(user_password=password, owner_password=password, use_128bit=True)
        
        # Write protected PDF
        with open(output_path, 'wb') as output_file:
            writer.write(output_file)
        
        return True
    except Exception as e:
        print(f"Error protecting {input_path}: {str(e)}")
        return False

def find_all_pdfs(directory):
    """Find all PDF files in directory and subdirectories"""
    pdf_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.lower().endswith('.pdf'):
                pdf_files.append(os.path.join(root, file))
    return pdf_files

def main():
    print("=" * 60)
    print("PDF Password Protection Script")
    print("=" * 60)
    print(f"Password: {PASSWORD}")
    print(f"Directory: {BASE_DIR}")
    print()
    
    # Find all PDF files
    pdf_files = find_all_pdfs(BASE_DIR)
    
    if not pdf_files:
        print("No PDF files found!")
        return
    
    print(f"Found {len(pdf_files)} PDF file(s):")
    for pdf in pdf_files:
        print(f"  - {pdf}")
    print()
    
    # Ask for confirmation
    response = input(f"Do you want to protect all {len(pdf_files)} PDF file(s)? (yes/no): ")
    if response.lower() not in ['yes', 'y']:
        print("Operation cancelled.")
        return
    
    print()
    print("Protecting PDF files...")
    print("-" * 60)
    
    success_count = 0
    failed_count = 0
    
    for pdf_path in pdf_files:
        rel_path = os.path.relpath(pdf_path, BASE_DIR)
        print(f"Processing: {rel_path}...", end=" ")
        
        # Create backup
        backup_path = pdf_path + ".backup"
        try:
            import shutil
            shutil.copy2(pdf_path, backup_path)
        except Exception as e:
            print(f"Warning: Could not create backup - {str(e)}")
        
        # Protect PDF
        if protect_pdf(pdf_path, pdf_path, PASSWORD):
            print("✓ Protected")
            success_count += 1
            # Remove backup if successful
            try:
                if os.path.exists(backup_path):
                    os.remove(backup_path)
            except:
                pass
        else:
            print("✗ Failed")
            failed_count += 1
            # Restore backup if failed
            try:
                if os.path.exists(backup_path):
                    shutil.move(backup_path, pdf_path)
            except:
                pass
    
    print("-" * 60)
    print(f"\nSummary:")
    print(f"  Successfully protected: {success_count}")
    print(f"  Failed: {failed_count}")
    print()
    print("All PDF files are now password protected!")
    print(f"Password: {PASSWORD}")

if __name__ == "__main__":
    main()

