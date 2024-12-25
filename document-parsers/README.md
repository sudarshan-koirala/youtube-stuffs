# Different document parsers
### Setup steps
- Make sure you have `uv` installed. Refer to this [video](https://youtu.be/13eNodHGRjw?si=UJdgZQ_EcWHueMly) for getting started.
- Clone the repo
- Navigate inside the repo to `document-parsers` folder. From the root of the directory/folder , run `uv sync`
    - this will create the virtual env
    - Install all the necessary packages
    - If you use uv to run the file, no need to activate it, it will do it for you.
    - If you decided not to use uv to run file, you can activate the virtual env with `source .venv/bin/activate`
    - Example, `uv run docling data/page_24.pdf` vs `docling data/page_24.pdf`  
    ![alt text](images/image-1.png) vs ![alt text](images/image.png)
- If there is problem with tessaract, use other OCR types but if you want to use tessaract, this might help
```
uv remove tesserocr
uv pip install --no-binary :all: tesserocr
```