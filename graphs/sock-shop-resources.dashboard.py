import itertools
import operator
import os

from grafanalib.core import *

datasource = "prometheus"

dashboard = Dashboard(
    title="Socks Shop Resources",
    time=Time("now-30m", "now"),
    timezone="browser",
    refresh="5s",
    panels=[
        SingleStat(
            title="Memory",
            valueName="current",
            dataSource=datasource,
            format="percent",
            thresholds=[65, 90],
            span=6,
            colorValue=True,
            targets=[
                Target(
                    expr='sum(container_memory_working_set_bytes{namespace="sock-shop"}) / sum(machine_memory_bytes{}) * 100',
                    refId="A",
                ),
            ],
            gauge=Gauge(
                minValue=0,
                maxValue=100,
                thresholdMarkers=True,
                show=True,
            ),
        ),
        SingleStat(
            title="CPU Usage",
            valueName="current",
            dataSource=datasource,
            format="percent",
            thresholds=[65, 90],
            decimals=2,
            span=6,
            colorValue=True,
            targets=[
                Target(
                    expr='sum(rate(container_cpu_usage_seconds_total{namespace="sock-shop"}[1m])) / sum (machine_cpu_cores) * 100',
                    step="10s",
                    refId="A",
                ),
            ],
            gauge=Gauge(
                minValue=0,
                maxValue=100,
                thresholdMarkers=True,
                show=True,
            ),
        ),
        SingleStat(
            title="Used",
            valueName="current",
            valueFontSize="50%",
            height=Pixels(1),
            format="bytes",
            decimals=2,
            dataSource=datasource,
            span=3,
            targets=[
                Target(
                    expr='sum(container_memory_working_set_bytes{namespace="sock-shop"})',
                    refId="A",
                ),
            ],
        ),
        SingleStat(
            title="Total",
            valueName="current",
            valueFontSize="50%",
            height=Pixels(1),
            format="bytes",
            decimals=2,
            dataSource=datasource,
            span=3,
            targets=[
                Target(
                    expr='sum(machine_memory_bytes)',
                    refId="A",
                ),
            ],
        ),
        SingleStat(
            title="Used",
            valueName="current",
            valueFontSize="50%",
            height=Pixels(1),
            format="no format",
            decimals=2,
            dataSource=datasource,
            span=3,
            postfix=" cores",
            targets=[
                Target(
                    expr='sum(rate(container_cpu_usage_seconds_total{namespace="sock-shop"}[1m]))',
                    refId="A",
                ),
            ],
        ),
        SingleStat(
            title="Total",
            valueName="current",
            valueFontSize="50%",
            height=Pixels(1),
            format="no format",
            decimals=2,
            dataSource=datasource,
            span=3,
            postfix=" cores",
            targets=[
                Target(
                    expr='sum(machine_cpu_cores)',
                    refId="A",
                ),
            ],
        ),
        Graph(
            title="Memory Working Set",
            dataSource=datasource,
            span=12,
            lineWidth=1,
            legend=Legend(
                sideWidth=Pixels(200),
                show=True,
                alignAsTable=True,
                rightSide=True,
                avg=True,
                current=True,
            ),
            targets=[
                Target(
                    expr='sum(container_memory_working_set_bytes{namespace="sock-shop"}) by (pod_name)',
                    legendFormat="{{ pod_name }}",
                    refId='A',
                ),
            ],
            xAxis=XAxis(mode="time"),
            yAxes=[
                YAxis(format="bytes", show=True, label="used", min=None),
                YAxis(format="bytes", show=True, label="used", min=None),
            ],
        ),
        Graph(
            title="CPU Usage",
            dataSource=datasource,
            span=12,
            lineWidth=1,
            legend=Legend(
                sideWidth=Pixels(200),
                show=True,
                alignAsTable=True,
                rightSide=True,
                avg=True,
                current=True,
            ),
            targets=[
                Target(
                    expr='sum(rate(container_cpu_usage_seconds_total{namespace="sock-shop"}[1m])) by (pod_name)',
                    legendFormat="{{ pod_name }}",
                    refId='A',
                ),
            ],
            xAxis=XAxis(mode="time"),
            yAxes=[
                YAxis(format="no format", show=True, label="cores", min=None),
                YAxis(format="no format", show=True, label="cores", min=None),
            ],
        ),
    ],
).auto_panel_ids()
