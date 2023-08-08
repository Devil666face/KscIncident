init:
	.dev/init.sh
remove:
	rm -rf python
	rm -rf venv
run:
	./venv/bin/python main.py
pip-install:
	./venv/bin/pip install -r requirements.txt