# Używamy obrazu bazowego z systemd i Pythonem
FROM python:3.8-slim

# Instalujemy systemd i click
RUN apt-get update && apt-get install -y systemd && pip install click

# Ustawiamy katalog roboczy i kopiujemy aplikację do kontenera
WORKDIR /app
COPY random_writer.py /app/random_writer.py

# Tworzymy katalog i plik output/output.txt
RUN mkdir -p /app/output && touch /app/output/output.txt

# Tworzymy plik usługi dla aplikacji
RUN echo "[Unit]\n\
Description=Random Writer Service\n\
After=network.target\n\
[Service]\n\
ExecStart=/usr/local/bin/python /app/random_writer.py /app/output/output.txt 10\n\
Restart=always\n\
[Install]\n\
WantedBy=multi-user.target" > /etc/systemd/system/random_writer.service

# Włączamy usługę systemową
RUN systemctl enable random_writer.service

# Uruchamiamy systemd jako proces główny
CMD ["/bin/systemd"]
