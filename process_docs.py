import os
import json
from bs4 import BeautifulSoup
from pathlib import Path
import html2text
import shutil

def html_to_markdown(html_content):
    """Mengkonversi konten HTML ke format Markdown"""
    h = html2text.HTML2Text()
    h.ignore_links = False
    h.ignore_images = False
    h.ignore_tables = False
    return h.handle(html_content)

def extract_content(html_file):
    """Ekstrak konten dari file HTML dan konversi ke Markdown"""
    with open(html_file, 'r', encoding='utf-8') as f:
        # Baca konten HTML
        html_content = f.read()
        
        # Konversi ke Markdown
        markdown_content = html_to_markdown(html_content)
        return markdown_content

def ensure_directory(path):
    """Memastikan direktori ada, buat jika belum ada"""
    os.makedirs(path, exist_ok=True)

def process_directory(src_dir, output_base_dir):
    """Proses semua file HTML dalam direktori dan konversi ke Markdown"""
    
    # Hitung total file yang akan diproses
    total_files = sum(1 for _ in Path(src_dir).rglob('*.html'))
    processed = 0
    
    for root, _, files in os.walk(src_dir):
        for file in files:
            if file.endswith('.html'):
                # Buat path relatif untuk menjaga struktur folder
                rel_path = os.path.relpath(root, src_dir)
                
                # Buat path output dengan struktur folder yang sama
                output_dir = os.path.join(output_base_dir, rel_path)
                ensure_directory(output_dir)
                
                # Path file input dan output
                file_path = os.path.join(root, file)
                output_path = os.path.join(
                    output_dir,
                    os.path.splitext(file)[0] + '.md'
                )
                
                try:
                    # Konversi dan simpan sebagai Markdown
                    content = extract_content(file_path)
                    with open(output_path, 'w', encoding='utf-8') as f:
                        f.write(content)
                    
                    processed += 1
                    print(f'Diproses [{processed}/{total_files}]: {file_path}')
                    print(f'Disimpan ke: {output_path}')
                except Exception as e:
                    print(f'Error memproses {file_path}: {str(e)}')
    
    return processed

def main():
    # Direktori input
    manual_dir = 'Manual'
    script_ref_dir = 'ScriptReference'
    
    # Direktori output
    output_dir = 'Documentation_MD'
    
    # Bersihkan direktori output jika sudah ada
    if os.path.exists(output_dir):
        shutil.rmtree(output_dir)
    
    # Buat direktori output baru
    ensure_directory(output_dir)
    
    processed_count = 0
    for directory in [manual_dir, script_ref_dir]:
        if os.path.exists(directory):
            # Buat subdirektori output
            output_subdir = os.path.join(output_dir, os.path.basename(directory))
            ensure_directory(output_subdir)
            
            # Proses direktori
            count = process_directory(directory, output_subdir)
            processed_count += count
    
    print(f'\nPemrosesan selesai. Total dokumen: {processed_count}')
    print(f'Semua file telah dikonversi ke Markdown dan disimpan di folder: {output_dir}')

if __name__ == '__main__':
    main()