FROM fluent/fluentd-kubernetes-daemonset:v1.11.1-debian-elasticsearch7-1.3

USER root

# Kopiere das benutzerdefinierte Entrypoint-Skript
COPY entrypoint.sh /fluentd-entrypoint.sh
RUN chmod +x /fluentd-entrypoint.sh

ENTRYPOINT ["/fluentd-entrypoint.sh"]