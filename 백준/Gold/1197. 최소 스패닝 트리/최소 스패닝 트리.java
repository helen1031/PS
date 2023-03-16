import java.util.*;

public class Main {
	
	static int v, e; //정점, 간선
	static PriorityQueue<Node> q;
	static ArrayList<Integer> s;
	static int[] parent;
	
	static class Node implements Comparable<Node>{
		int c, a, b;
		
		Node(int c, int a, int b){
			this.c = c;
			this.a = a;
			this.b = b;
		}
		
		@Override
		public int compareTo(Node n) {
			return Integer.compare(this.c, n.c);
		}
	}
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		v= sc.nextInt();
		e= sc.nextInt();
		
		parent = new int[v+1];
		for(int i=1 ; i < v+1 ; i++) {
			parent[i] = i;
		}
		
		q = new PriorityQueue<>();
		for(int i=0 ; i < e ; i++) {
			int a = sc.nextInt();
			int b = sc.nextInt();
			int c = sc.nextInt();
			
			q.offer(new Node(c, a, b));
		}
		
		int cost = 0;
		s = new ArrayList<>();
		
		while(!q.isEmpty()) {
			Node least = q.poll();
			int a = least.a;
			int b = least.b;
			
			//cycle 아니면
			int ra = root(a);
			int rb = root(b);
			if(ra != rb) {
				cost += least.c;
				if(ra < rb) {
					parent[rb] = ra;
				}else {
					parent[ra] = rb;
				}
			}
			
		}
		
		System.out.println(cost);
	}
	
	static int root(int x) {
		if(parent[x]!= x) {
			parent[x] = root(parent[x]);
		}
		return parent[x];
	}
}