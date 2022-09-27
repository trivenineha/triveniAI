public class SimpleSolver {
  static int eval(String q) {
    int val = 0;
    java.util.StringTokenizer st = new java.util.StringTokenizer(q, "*/+-", true);
    while (st.hasMoreTokens()) {
      String next = st.nextToken().trim();
      if (next.equals("+")) {
        val += Integer.parseInt(st.nextToken().trim());
      } else if (next.equals("-")) {
        val -= Integer.parseInt(st.nextToken().trim());
      } else if (next.equals("*")) {
        val *= Integer.parseInt(st.nextToken().trim());
      } else if (next.equals("/")) {
        val /= Integer.parseInt(st.nextToken().trim());
      } else {
        val = Integer.parseInt(next);
      }
    }
    return val;
  }
  static String solve(String q) {
    char c = 0;
    for (int i = 0; i < q.length(); ++i) {
      if (Character.isAlphabetic(q.charAt(i))) {
        c = q.charAt(i);
        break;
      }
    }
    if (c == 0) {
      String[] ops = q.split("==");
      int o1 = eval(ops[0]), o2 = eval(ops[1]);
      if (o1 == o2) return q;
      else return "";
    } else {
      char[] dset = new char[10];
      for (int i = 0; i < q.length(); ++i)
        if (Character.isDigit(q.charAt(i)))
          dset[q.charAt(i)-'0'] = 1;
      for (int i = 0; i < 10; ++i) {
        if (dset[i] == 0) {
          String r = solve(q.replaceAll(String.valueOf(c),
              String.valueOf(i)));
          if (!r.isEmpty()) return r;
        }
      }
    }
    return "";
  }
  public static void main(String[] args) {
    String query = "ABCDE * A == EEEEEE";
    System.out.println(solve(query));
  }
}
