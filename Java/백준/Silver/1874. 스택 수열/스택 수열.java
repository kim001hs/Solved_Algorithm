import java.io.IOException;
import java.util.ArrayList;
import java.util.Scanner;
import java.util.Stack;

public class Main{
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        int n=sc.nextInt();
        Stack<Integer> stack = new Stack<>();
        ArrayList<String> result = new ArrayList<String>();
        int push_num=0;
        for(int i=0;i<n;i++){
            int temp = sc.nextInt();
            while(true){
                if(!stack.isEmpty()&&stack.peek()==temp){
                    stack.pop();
                    result.add("-");
                    break;
                }
                push_num++;
                stack.push(push_num);
                result.add("+");
                if(push_num>temp){
                    System.out.println("NO");
                    return;
                }
            }
        }
        for(String s : result){
            System.out.println(s);
        }
    }
}