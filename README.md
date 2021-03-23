# My blog
Sources for my blog

## Setup

If I write on a new computer.

```bash
git clone git@github.com:ClementC/pelican-blue.git   # Repo for the blog theme 
git clone https://github.com/ClementC/my_blog        # Actual repo for the blog sources
cd my_blog
git submodule init
git submodule update
conda create --name my_blog python=3.5 -y
conda activate my_blog
pip install -r requirements.txt
```

## Workflow

+ go into the `my_blog` directory
+ `conda activate my_blog`
+ `jupyter notebook`
+ create a new Jupyter notebook in the `content/articles` directory
+ write, write, write... (NB: the title will be directly inserted from the metadata file)
+ `pelican content` to build the static pages
+ `cd output/ && python -m http.server` to test the website locally
+ before publishing, add a file `new_post.ipynb-meta` (with the exact same filename as the notebook) for the metadata (title, publication date, URL slug, tags...)
+ commit and push changes, then go to the `output` directory, and commit & push there too (this is the git submodule for the actual blog)