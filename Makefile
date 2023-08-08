init:
	.dev/init.sh
init-local:
	python3 -m venv venv
	./venv/bin/pip install -r requirements.txt
	./venv/bin/pip install --no-index .dev/KlAkOAPI-1.0.0.0.tar.gz
remove:
	rm -rf python
	rm -rf venv
run:
	./venv/bin/python main.py
pip-install:
	./venv/bin/pip install -r requirements.txt
pycln:
	./venv/bin/pip install pycln
	./venv/bin/pycln --all .