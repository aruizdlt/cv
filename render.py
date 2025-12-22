#!/usr/bin/env python3
import os
import subprocess
import sys

def render_cv(language):
    """Renders the CV in the specified language"""
    yaml_file = f"cv_{language}.yaml"
    output_dir = f"output/{language}"
    
    if not os.path.exists(yaml_file):
        print(f"❌ Error: File {yaml_file} not found")
        return False
    
    # Create output directory
    os.makedirs(output_dir, exist_ok=True)
    
    print(f"🔨 Generating CV in {language.upper()}...")
    try:
        subprocess.run(
            ["rendercv", "render", yaml_file, "--output-folder-name", output_dir],
            check=True
        )
        print(f"✅ CV successfully generated in {output_dir}/")
        print(f"   📄 PDF: {output_dir}/{yaml_file.replace('.yaml', '.pdf')}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error generating CV: {e}")
        return False

def main():
    print("=" * 60)
    print("RenderCV - Bilingual CV Generator")
    print("=" * 60)
    print()
    
    if len(sys.argv) > 1:
        lang = sys.argv[1].lower()
        if lang in ['es', 'en']:
            render_cv(lang)
        else:
            print("❌ Invalid language. Use 'es' or 'en'")
            print("\nUsage:")
            print("  python render.py es    # Spanish only")
            print("  python render.py en    # English only")
            print("  python render.py       # Both languages")
    else:
        # Generate both languages
        print("📚 Generating CVs in Spanish and English...\n")
        success_es = render_cv('es')
        print()
        success_en = render_cv('en')
        print()
        
        if success_es and success_en:
            print("🎉 All CVs generated successfully!")
        elif success_es or success_en:
            print("⚠️  Some CVs could not be generated")
        else:
            print("❌ Error generating CVs")

if __name__ == "__main__":
    main()