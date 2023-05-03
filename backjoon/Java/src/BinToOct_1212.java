import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;

public class BinToOct_1212 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str = "";
        str = br.readLine();

        int strlen = str.length();

        if (strlen%3==1) {
            System.out.print(str.charAt(0));
        }
        else if(strlen%3==2) {
            System.out.print((str.charAt(0)-'0')*2+str.charAt(1)-'0');
        }

        for(int i=strlen%3;i<strlen;i+=3) {
            System.out.print((str.charAt(i)-'0')*4+(str.charAt(i+1)-'0')*2+(str.charAt(i+2)-'0'));
        }

    }

}

