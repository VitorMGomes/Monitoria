import java.util.*;


public class Q5
{

    public static boolean stop(String input)
    {
        boolean stop = false;
        int len = input.length(); 

        if(len == 3 && input.charAt(0) == 'F' && input.charAt(1) == 'I' && input.charAt(2) == 'M')
        {
            stop = true;
        }

        return stop;
    }

    public static boolean compare(String str1, String str2)
    {
        boolean resp = false;

        if(str1.length() == str2.length())
        {
            resp = true;
            int len = str1.length();

            for(int i = 0; i < len; i++)
            {
                for(int j = 0; j < i)
            }
        }

        return resp;
    }


    public static void main(String[] args) {
        
        Scanner scanf = new Scanner(System.in);

        String input = scanf.nextLine();

        while(!stop(input))
        {
            String splitted[] = input.split(" - ");
            boolean resp = compare(splitted[0],splitted[1]);

            System.out.println(resp ? "SIM" : "NÃO");

            input = scanf.nextLine();
        }

        scanf.close();
    }
}