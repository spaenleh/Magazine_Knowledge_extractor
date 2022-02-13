# Magazine Knowledge extractor

A simple project to extract the TOC of pdfs.

## Requirements

All requirements are listed in the file `requirements.txt`.
Use `conda` or `pip` to install the packages. 

_Note: this project may require you to install the `mupdf` C library.
To do so use: `brew mupdf` (on macOS)_

## Usage

```
python main.py
```

This produces 2 files called `Base_de_connaissance.xlsx` and `Base_de_connaissance.csv`.
The `.csv` file is there for debugging purposes. The 'real' output is the `.xlsx` file.


@spaeneh 2022
