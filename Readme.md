Monitoring
----------

Monitoring dashboards require the incoming data to be presented in a particular format. This allows us to easily visualize the data.

Ideally, the source of the data points, that is the server generating the data points should generate visualization friendly timeseries data points.

Till we facilitate the same, this repository should host backend pipelines for processing and pruning the required stats to be able to meet the current monitoring requirements.


Architecture
------------

Kafka Topics



+   +   +   +
|   |   |   |   +-------------------+       +---------------------+            +-------------------+
|   |   |   |   |                   |       |                     +------------>                   |
|   |   +------>+      Logstash     +------->   ElasticSearch     |            |    Kibana :5601   |
|   |   |   |   |                   |       |      Cluster        |            |                   |
|   |   |   |   |                   |       |                     +------+     |    Logs           |
|   |   |   |   +-------------------+       +---------------------+      |     |                   |
|   |   |   |                                                            |     |                   |
|   |   |   |                                                            |     |                   |
|   |   |   |                                                            |     +-------------------+
|   |   |   |                                                            |
|   |   |   |                               +----------------------+     |
|   |   |   |                               |                      |     |
|   |   |   |                               |                      |     |     +-------------------+
|   |   |   |   Topic: portkey-mon-ts       |                      |     |     |                   |
|   |   |   |                               |    Monitoring Util   |     |     |                   |
|   |   +<----------------------------------+    Python program    |     |     |   Grafana :3000   |
|   |   |   |                               |                      |     +----->   Real time mon   |
|   |   |   |                               |    - Poll for new    |           |     Dashboard     |
|   |   |   |                               |      logs            |           |                   |
|   |   |   |                               |    - Process logs    |           |                   |
|   |   |   |    Topic: Portkey             |      in mon. format  |           |                   |
|   |   |   |                               |    - Push to Kafka   |           +-------------------+
|   |   |   +------------------------------>+                      |
+   +   +   +                               +----------------------+

In very simple words, our monitoring utility program will take input data from the `Portkey` topic in the cluster,
process the incoming data & forward the processed data to `Portkey-mon-ts` topic in Kafka which will further be
pushed to Elasticsearch instance via. Logstash.

Data processing and pruning:
  - Transform text, string data into numerical format where ever applicable.
  - Create time series friendly data format so the data is ready to be visualized in grafana.
  - Add related fields for various functions like Mean/Avg etc. for Pi, Bar and Graph visualizations.
