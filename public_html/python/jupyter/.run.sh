#To run always
cd jupyter
source bin/activate
~/.local/bin/jupyter-notebook --ip=0.0.0.0 --port=4567 --no-browser  &>/dev/null &
sleep 3 ; ~/.local/bin/jupyter-notebook list
