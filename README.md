# Git2sC

`git2sc` is a program to sync a git documentation repository to Confluence.

# Install

```bash
git clone https://git.paradigmadigital.com/seguridad/git2sc
cd git2sc
virtualenv -p python3 git2sc
source git2sc/bin/activate
pip3 install -r requirements.txt
python3 setup.py install
```

If you don't have pandoc and asciidoctor installed, do so:

```bash
sudo apt-get install pandoc asciidoctor
```

Set up the credentials of a user that can read and write the pages in the
environment variables:

* `GIT2SC_API_URL`: `https://company.atlassian.net/wiki/rest/api`
* `GIT2SC_AUTH`: `username:password`

# Usage

All commands require that you specify the `space` id of your project. To obtain
this value you have to go to your confluence page which may look like this

`https://company.atlassian.net/wiki/spaces/SPACE/overview`

Where `SPACE` is the space id.

## Update an article

This command will update the confluence article with id `{{ article_id }}` with
the content of the file in the path `{{ content }}`.

```bash
git2sc {{ space }} article update {{ article_id }} {{ content }}
```

## Create an article

This command will create an confluence article under the `{{ space }}` space,
with title `{{ title }}` and with the content of the file in the path `{{
content }}`.

```bash
git2sc {{ space }} article create {{ title }} {{ content }}
```

If you want to make the article a children of another article use the `-p {{
parent_id }}` flag

```bash
git2sc {{ space }} article create -p {{ parent_id }} {{ title }} {{ content }}
```

## Delete an article

This command will delete the confluence article with id `{{ article_id }}`.

```bash
git2sc {{ space }} article delete {{ article_id }}
```

## Upload a directory

This command will upload all the contents of a directory to the main page of
confluence creating a hierarchy of articles equally to the directory tree.

For each directory it will try to load the `README.adoc` or `README.md` to the
directory confluence page.

Even if confluence uses page_ids there can't be two articles with the same
title, so if you have two files with the same name it will create it with
name_1, name_2, and so on. Check
[this](https://git.paradigmadigital.com/seguridad/git2sc/issues/4) issue to view
the improvements. Try to avoid having files with the same name on your repo for
flawless results.

```bash
git2sc {{ space }} upload {{ directory_path }}
```

Optionally you can exclude some files and directories (by default `.git`,
`.gitignore`, and `.gitmodules`)

```bash
git2sc {{ space }} upload {{ directory_path }} --exclude file1 directory1 file2
```

If you don't want to upload the directory to the main page but starting from an
article you can specify it with the `-p` flag. Beware in this case, the
confluence page name is the basename of the `directory_path` therefore avoid
using `.` as `directory_path`.

```bash
git2sc {{ space }} upload {{ directory_path }} -p {{ parent_id }}
```

## Sync a directory

This command will sync all the contents of a directory to the main page of
confluence creating a hierarchy of articles equally to the directory tree.

For each directory it will try to load the `README.adoc` or `README.md` to the
directory confluence page.

Even if confluence uses page_ids there can't be two articles with the same
title, so if you have two files with the same name, the upload directory command
will create it with name_1, name_2, and so on. Check
[this](https://git.paradigmadigital.com/seguridad/git2sc/issues/4) issue to view
the improvements. But **the sync command won't update the files with `*_1`,
`*_2`, ... So try to avoid having files with the same names on your directory**.

```bash
git2sc {{ space }} sync {{ directory_path }}
```

Optionally you can exclude some files and directories (by default `.git`,
`.gitignore`, and `.gitmodules`)

```bash
git2sc {{ space }} sync {{ directory_path }} --exclude file1 directory1 file2
```

# Test

To run the tests first install `tox`

```bash
pip3 install tox
```

And then run the tests

```bash
tox
```

# Authors

jamatute@paradigmadigital.com
