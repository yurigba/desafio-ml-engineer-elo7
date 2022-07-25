ARG BASE_IMAGE=python:3.10.5-buster
FROM $BASE_IMAGE

# install project requirements
COPY src/requirements_inference.txt /tmp/requirements.txt
COPY dist/model_inference-0.1.tar.gz /tmp/model_inference-0.1.tar.gz
RUN pip install --upgrade pip
RUN pip install -r /tmp/requirements.txt && rm -f /tmp/requirements.txt
RUN pip install /tmp/model_inference-0.1.tar.gz

# add user
ARG ELO7_UID=999
ARG ELO7_GID=0
RUN groupadd -f -g ${ELO7_GID} elo7_group && \
useradd -d /home/elo7 -s /bin/bash -g ${ELO7_GID} -u ${ELO7_UID} elo7

# copy the whole project except what is in .dockerignore
WORKDIR /home/elo7
# COPY . .
RUN chown -R elo7:${ELO7_GID} /home/elo7
USER elo7
RUN chmod -R a+w /home/elo7

COPY ./data/06_models/vectorizer.pickle /home/elo7/assets/vectorizer.pickle
COPY ./data/06_models/model.pickle /home/elo7/assets/model.pickle
COPY ./app.py /home/elo7/app.py

EXPOSE 8000

CMD ["uvicorn", "app:app", "--port", "8000"]
