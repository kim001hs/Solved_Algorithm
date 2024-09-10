import java.io.IOException;
import java.util.Scanner;
import java.util.TreeMap;

public class Main{
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();
        for(int i=0; i<T; i++){
            int k = sc.nextInt();
            TreeMap<Integer, Integer> map = new TreeMap<>();//TreeMap: key값을 기준으로 오름차순 정렬됨

            for(int j=0; j<k; j++){//k개의 연산 진행

                String s = sc.next();
                int temp=sc.nextInt();

                if(s.equals("I")){
                    map.put(temp, map.getOrDefault(temp, 0)+1);//map에 temp를 key로 가지는 값이 있으면 value값을 1증가시키고 없으면 1로 초기화
                    //getOrDefault: key값이 있으면 key값에 해당하는 value값을 반환하고 없으면 기본값을 반환
                }else if(s.equals("D")&&!map.isEmpty()){
                    int n=(temp==1)?map.lastKey():map.firstKey();
                    if(map.put(n, map.get(n) - 1) == 1){//n의 value값을 1감소시키고 0이되면 map에서 n을 제거
                        //put: key값이 있으면 value값을 수정 및 기존 value를 반환, 없으면 key와 value를 추가 및 NULL 반환
                        map.remove(n);
                    }
                }
            }
            if(map.isEmpty()){
                System.out.println("EMPTY");
            }else{
                System.out.println(map.lastKey()+" "+map.firstKey());
            }
        }
        sc.close();
    }
}