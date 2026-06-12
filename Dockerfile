FROM python:3.12-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    wget \
    unzip \
    gnupg \
    curl \
    && rm -rf /var/lib/apt/lists/*

RUN CHROME_VERSION=$(google-chrome --product-version | cut -d '.' -f 1) && \
    DRIVER_VERSION=$(curl -s https://chromedriver.storage.googleapis.com/LATEST_RELEASE_$CHROME_VERSION) && \
    wget -O /tmp/chromedriver.zip \
    https://chromedriver.storage.googleapis.com/$DRIVER_VERSION/chromedriver_linux64.zip && \
    unzip /tmp/chromedriver.zip -d /usr/local/bin/ && \
    chmod +x /usr/local/bin/chromedriver

COPY . /app

RUN python -m venv /opt/venv

RUN source /opt/venv/bin/activate

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

RUN mkdir -p reports screenshots logs

CMD ["pytest",
     "-v",
     "--env=prod",
     "--alluredir=allure-results",
     "--self-contained-html"]