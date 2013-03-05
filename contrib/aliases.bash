# Este contem facilidades para o shell e é importado pelo postactivate

PROJECT_ROOT="$VIRTUAL_ENV/project"

alias manage="python $PROJECT_ROOT/manage.py"
alias cdproject=" cd $PROJECT_ROOT"
alias cdsrc="cd $PROJECT_ROOT/src"
alias rmpyc="find . -iname '*.pyc' -exec rm {} \;"
alias cddjango="cd `virtualenvwrapper_get_site_packages_dir`/django"
