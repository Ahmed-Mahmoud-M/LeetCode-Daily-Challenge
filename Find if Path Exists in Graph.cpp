
#include<vector>
#include<unordered_map>

#include<stack>
#include<unordered_set>
//procedure DFS_iterative(G, v) is
	//let S be a stack
	//S.push(v)
	//while S is not empty do
	//v = S.pop()
	// 
	//if v is not labeled as discovered then
	//label v as discovered
	//for all edges from v to w in G.adjacentEdges(v) do
	//if w is not labeled as discovered then
	//S.push(w)

static bool validPath(int n, std::vector<std::vector<int>>& edges, int source, int destination) {

	// convert edges to adjucent list

	std::unordered_map<int, std::vector<int>> adjucentlist;

	for (int i = 0; i < edges.size(); i++) {
		adjucentlist[edges[i][0]].emplace_back(edges[i][1]);
		adjucentlist[edges[i][1]].emplace_back(edges[i][0]);
	}


	std::unordered_set<int> vistited;
	std::stack<int> frontier;

	frontier.push(source);
	vistited.insert(source);

	while (!frontier.empty()) {
		int u = frontier.top();
		frontier.pop();
		if (u == destination) return true;
		// key is found

		for (auto u_edges : adjucentlist[u]) {
			if (vistited.find(u_edges) == vistited.end()) {
				//std::cout << "finded" << std::endl;
				frontier.push(u_edges);
				vistited.insert(u_edges);


			}

		}

	}





	/*for (auto element : vistited) {
		std::cout << element << std::endl;
	}*/



	return false;
}