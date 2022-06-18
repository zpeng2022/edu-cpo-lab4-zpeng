# pip install pycodestyle pyflakes pytest coverage
pycodestyle --ignore=E111 .
# pyflakes .
# sudo gem install mdl
mdl README.md
# mypy .
coverage run -m pytest --verbose
