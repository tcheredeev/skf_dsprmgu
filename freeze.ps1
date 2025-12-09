# pipreqs wsgy  --force --all --savepath .\requirements.txt
pip freeze --exclude pywin32 > ./requirements.txt
pip freeze > ./requirements_win.txt