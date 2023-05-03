import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class OctToBin_1373 {

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str = "";
        str = br.readLine();

        System.out.print(Integer.toBinaryString(str.charAt(0)-'0'));

        for(int i=1;i<str.length();i++) {
            String bin = Integer.toBinaryString(str.charAt(i)-'0');
            if (bin.length()==1)
                System.out.print("00"+bin);
            else if (bin.length()==2)
                System.out.print("0"+bin);
            else
                System.out.print(bin);
        }
    }

}
