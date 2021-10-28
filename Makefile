run-locally: 
	python3 -m venv .venv
	bash -c "source .venv/bin/activate"
	

run-seed:
	mkdir data_download
	echo "---Criando Pasta e fazendo download dos Microdados do Enade---"
	cd data_download/ && curl -O https://download.inep.gov.br/microdados/Enade_Microdados/microdados_enade_2019.zip && \
	curl -O https://download.inep.gov.br/microdados/Enade_Microdados/microdados_enade_2018.zip && \
	curl -O https://download.inep.gov.br/microdados/Enade_Microdados/microdados_Enade_2017_portal_2018.10.09.zip && \

