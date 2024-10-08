TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8"/>
    <title>JCCI Result</title>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/crypto-js/4.1.1/crypto-js.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/echarts/5.4.2/echarts.min.js"
            integrity="sha512-VdqgeoWrVJcsDXFlQEKqE5MyhaIgB9yXUVaiUa8DR2J4Lr1uWcFm+ZH/YnzV5WqgKf4GPyHQ64vVLgzqGIchyw=="
            crossorigin="anonymous" referrerpolicy="no-referrer"></script>
    <script src="./#{JS-FILE-PATH}#"></script>
</head>
<body>

<div id="main" style="width: 100%;height: 1000px;"></div>
<script type="text/javascript">
    var myChart = echarts.init(document.getElementById('main'));
    var graphCategories = [];
    var optionGraph = {
        tooltip: {},
        legend: {
            show: false
        },
        series: [
            {
                type: 'graph',
                layout: 'none',
                data: [],
                links: [],
                categories: [],
                edgeSymbol: ['circle', 'arrow'],
                edgeSymbolSize: [4, 10],
                edgeLabel: {
                    fontSize: 20
                },
                roam: true,
                labelLayout: {
                    hideOverlap: true
                },
                lineStyle: {
                    color: 'source',
                    curveness: 0.3
                },
                // 添加数据缩放组件
                dataZoom: [
                    {
                        type: 'inside'
                    },
                    {
                        type: 'slider'
                    }
                ],
                // 开启平移功能
                panZoom: {
                    enable: true
                }
            }]
    };
    let resultGraph = graphData;
    optionGraph.series[0].data = resultGraph.nodes;
    optionGraph.series[0].links = resultGraph.links;
    graphCategories = resultGraph.categories;
    optionGraph.series[0].categories = graphCategories;
    let graphLegend = graphCategories.map(function (a) {
        return a.name;
    });
    optionGraph.legend[0].data = graphLegend;
    myChart.setOption(optionGraph);
</script>
</body>
</html>
"""