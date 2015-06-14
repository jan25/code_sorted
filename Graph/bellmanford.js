var V;
var adj = [[]]; // (v, w)

var dist = [];

var INF = 1e9; // infinite distance

function bellmanford(src) {
	for (var i = 0; i < V; ++i)
		dist[i] = INF;
	dist[src] = 0;

	for (var i = 0; i < V; ++i) {
		var outdegree = adj[i].length;
		for (var j = 0; j < outdegree; ++j) {
			var v = adj[i][j][0];
			var w = adj[i][j][1];
			if (dist[i] != INF && dist[i] + w < dist[v])
				dist[v] = dist[i] + w;
		}
	}

	for (var i = 0; i < V; ++i) {
		var outdegree = adj[i].length;
		for (var j = 0; j < outdegree; ++j) {
			var v = adj[i][j][0];
			var w = adj[i][j][1];
			if (dist[i] != INF && dist[i] + w < dist[v])
				console.log("Cycle Detected.");
		}
	}

	for (var i = 0; i < V; ++i)
		console.log(dist[i] + " ");
}

V = 5;
var edges = [[0, 1, -1], [0, 2, 4], [1, 2, 3], [1, 3, 2],
				[1, 4, 2], [3, 2, 5], [3, 1, 1], [4, 3, -3]];

for (var i = 0; i < V; ++i) adj.push([]);

for (var i = 0; i < edges.length; ++i) {
	var u = edges[i][0];
	var v = edges[i][1];
	var w = edges[i][2];
	adj[u].push([v, w]);
}

bellmanford(0);
