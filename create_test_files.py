import os
from pathlib import Path

def create_test_files():
    test_dir = Path("test_files")
    test_dir.mkdir(exist_ok=True)

    files = [
        "image1.jpg", "image2.png",
        "video1.mp4", "video2.mkv",
        "doc1.pdf", "doc2.docx", "text.txt",
        "song.mp3",
        "archive.zip",
        "unknown.xyz"
    ]

    for filename in files:
        with open(test_dir / filename, "w") as f:
            f.write("dummy content")
    
    print(f"Created test files in {test_dir.absolute()}")

if __name__ == "__main__":
    create_test_files()
