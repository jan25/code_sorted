var V;
var G = [[]]; // input edge weights

var dist = [[]]; // distance matrix

// for all pairs shortest paths
// O(V^3)
function floydwarshall() {
	for (var i = 0; i < V; ++i) {
		for (var j = 0; j < G[i].length; ++j) {
			dist[i].push(G[i][j]);
		}
	}

	// pick intermediate vertex
	for (var k = 0; k < V; ++k) {

		// pick src
		for (var i = 0; i < V; ++i) {
			// pick dest
			for (var j = 0; j < V; ++j) {
				if (dist[i][k] + dist[k][j] < dist[i][j])
					dist[i][j] = dist[i][k] + dist[k][j];
			}
		}
	}

}
