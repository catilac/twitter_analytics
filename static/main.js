$(document).ready(function() {
  var drawTopContent = scatterPlotFunc("/top-content.json", 
                  "retweet_count", "favorites_count", "#top-content .graph");
  var drawTopUsers = scatterPlotFunc("/top-users.json", 
                  "total_rts", "total_fav", "#top-users .graph");

  drawTopContent();
  drawTopUsers();
});

/**
 * Returns a function that draws a scatter plot
 *
 * @param {String} route, where to get datas
 * @param {String} xAxisName, name of the key for x-axis data
 * @param {String} yAxisName, name of the key for y-axis data
 * @param {String} graphElem, where to attach the graph in the DOM
 * @return {Function}
 */
function scatterPlotFunc(route, xAxisName, yAxisName, graphElem) {
  return function() {
    var margin = {top: 20, right: 20, bottom: 30, left: 40},
    width = 960 - margin.left - margin.right,
    height = 500 - margin.top - margin.bottom;

    var x = d3.scale.linear()
    .range([0, width]);

    var y = d3.scale.linear()
    .range([height, 0]);

    var color = d3.scale.category10();

    var xAxis = d3.svg.axis()
    .scale(x)
    .orient("bottom");

    var yAxis = d3.svg.axis()
    .scale(y)
    .orient("left");

    var svg = d3.select(graphElem).append("svg")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
    .append("g")
    .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

    d3.json(route, function(err, data) {
      var testX = x.domain(d3.extent(data, function(d) { return d[xAxisName]; })).nice();
      var testY = y.domain(d3.extent(data, function(d) { return d[yAxisName]; })).nice();

      var xMax = testX.domain()[1];
      var yMax = testY.domain()[1];
      var mul = xMax + yMax;

      var interpolate = d3.interpolateNumber(3, 20);

      svg.append("g")
      .attr("class", "x axis")
      .attr("transform", "translate(0," + height + ")")
      .call(xAxis)
      .append("text")
      .attr("class", "label")
      .attr("x", width)
      .attr("y", -6)
      .style("text-anchor", "end")
      .text(xAxisName);

      svg.append("g")
      .attr("class", "y axis")
      .call(yAxis)
      .append("text")
      .attr("class", "label")
      .attr("transform", "rotate(-90)")
      .attr("y", 6)
      .attr("dy", ".71em")
      .style("text-anchor", "end")
      .text(yAxisName);

      svg.selectAll(".dot")
      .data(data)
      .enter().append("circle")
      .attr("class", "dot")
      .attr("r", function(d) { return interpolate((d[xAxisName]+d[yAxisName])/(mul));})
      .attr("cx", function(d) { return x(d[xAxisName]); })
      .attr("cy", function(d) { return y(d[yAxisName]); })
      .append("svg:title")
      .text(function(d) { return d.user_id + ": " + d.text; });
    });
  }
}
