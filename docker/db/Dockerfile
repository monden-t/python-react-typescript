# TODO FIXME ただのコピペ
FROM mysql:5.7

ADD ./my.cnf /etc/mysql/my.cnf
ADD ./initdb.d /docker-entrypoint-initdb.d

RUN chmod 644 /etc/mysql/my.cnf
RUN chmod -R 777 /docker-entrypoint-initdb.d

RUN touch /var/log/mysql/general.log
RUN touch /var/log/mysql/slow_query.log

RUN chmod 666 /var/log/mysql/general.log
RUN chmod 666 /var/log/mysql/slow_query.log
