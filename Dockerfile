FROM python:3.9-alpine
ARG DIRECTORY=/app
WORKDIR $DIRECTORY
COPY ./requirements.txt $DIRECTORY/requirements.txt
COPY requirements/ $DIRECTORY/requirements/
RUN pip install --no-cache-dir --upgrade -r $DIRECTORY/requirements.txt
COPY ./src $DIRECTORY
ENTRYPOINT ["sh", "bootup.sh"]