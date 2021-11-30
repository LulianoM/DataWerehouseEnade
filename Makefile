run-seed-enade: 
	python3 -m venv .venv
	bash -c "source .venv/bin/activate"
	pip3 install --upgrade pip
	pip3 install -r requirements.txt
	clear
	python3 1.ColetaDeDados/BaixarArquivosEnade.py

run-create-enade:
	python3 -m venv .venv
	bash -c "source .venv/bin/activate"
	pip3 install --upgrade pip
	pip3 install -r requirements.txt
	clear
	python3 3.BancodeDados/CriandoBancoDados.py

run-migrate-enade:
	python3 -m venv .venv
	bash -c "source .venv/bin/activate"
	pip3 install --upgrade pip
	pip3 install -r requirements.txt
	clear
	python3 3.BancodeDados/PopulandoBancoDados.py

run-create-seed-migrate-enade:
	make run-seed-enade
	make run-create-enade
	make run-migrate-enade

run-streamlit-covid:
	python3 -m venv .venv
	bash -c "source .venv/bin/activate"
	pip3 install --upgrade pip
	pip3 install -r requirements.txt
	pip3 install -r requirements_streamlit.txt
	clear
	streamlit run 4.VisualizacaoLearningDados/InterfaceStreamlit.py