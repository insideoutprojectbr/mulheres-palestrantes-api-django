FROM python:3.7.2
RUN apk add -U -q --no-cache gcc make musl-dev linux-headers tzdata
RUN cp /usr/share/zoneinfo/America/Sao_Paulo /etc/localtime && echo "America/Sao_Paulo" >/etc/timezone
WORKDIR ${HOME}/app
ADD . .
CMD ["make", "run"]
