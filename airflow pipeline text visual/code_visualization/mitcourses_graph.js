function graph() {

  // clean up
  document.getElementById('target').innerHTML = '';

  // ---------------- TIP ----------------
  var tip = d3.tip()
    .attr('class', 'd3-tip')
    .html(function (d) { return '<span>' + d.word + ' (' + d.score + ')</span>'; })
    .offset([-12, 0]);

  // ---------------- DATA PREP ----------------
  // remove super-common words so bubbles aren't dominated by "and/of/in/the"
  var stop = {
    "and": 1, "of": 1, "in": 1, "to": 1, "the": 1, "a": 1, "an": 1, "for": 1, "on": 1, "with": 1,
    "I": 1, "II": 1, "III": 1, "IV": 1
  };

  // scores is defined in words.js (ex: scores = {...})
  var data = Object.keys(scores)
    .filter(function (k) { return !stop[k]; })
    .map(function (k) { return { word: k, score: +scores[k] }; })
    .sort(function (a, b) { return b.score - a.score; })
    .slice(0, 80); // change to 50/100/150 if you want more/less

  var minScore = d3.min(data, function (d) { return d.score; });
  var maxScore = d3.max(data, function (d) { return d.score; });

  // ---------------- SCALES ----------------
  var padding = 6;

  var radius = d3.scale.log()
    .domain([Math.max(1, minScore), maxScore])
    .range([10, 70])
    .clamp(true);

  var color = d3.scale.category10();

  // ---------------- SVG ----------------
  var svgW = 1920, svgH = 960;

  var svg = d3.select("div[id=target]").append("svg")
    .attr("width", svgW)
    .attr("height", svgH)
    .attr("class", "vis")
    .append("g");

  svg.call(tip);

  // ---------------- NODES ----------------
  var nodes = data.map(function (d) {
    return {
      radius: radius(d.score),
      color: color(d.word.length),
      word: d.word,
      score: d.score
    };
  });

  // ---------------- FORCE ----------------
  var force = d3.layout.force()
    .nodes(nodes)
    .size([svgW, svgH])
    .gravity(0.06)
    .charge(function (d) { return -Math.pow(d.radius, 2) / 2; })
    .on("tick", tick)
    .start();

  var circle = svg.selectAll("circle")
    .data(nodes)
    .enter().append("circle")
    .attr("r", function (d) { return d.radius; })
    .style("fill", function (d) { return d.color; })
    .on('mouseover', tip.show)
    .on('mouseout', tip.hide)
    .call(force.drag);

  function tick(e) {
    circle
      .each(collide(0.5))
      .attr("cx", function (d) { return d.x; })
      .attr("cy", function (d) { return d.y; });
  }

  // ---------------- COLLISION ----------------
  function collide(alpha) {
    var quadtree = d3.geom.quadtree(nodes);
    return function (d) {
      var r = d.radius + 70 + padding,
        nx1 = d.x - r,
        nx2 = d.x + r,
        ny1 = d.y - r,
        ny2 = d.y + r;

      quadtree.visit(function (quad, x1, y1, x2, y2) {
        if (quad.point && quad.point !== d) {
          var x = d.x - quad.point.x,
            y = d.y - quad.point.y,
            l = Math.sqrt(x * x + y * y),
            r = d.radius + quad.point.radius + padding;

          if (l < r) {
            l = (l - r) / l * alpha;
            d.x -= x *= l; d.y -= y *= l;
            quad.point.x += x; quad.point.y += y;
          }
        }
        return x1 > nx2 || x2 < nx1 || y1 > ny2 || y2 < ny1;
      });
    };
  }
}
