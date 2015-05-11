using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApplication1
{
    class Program
    {
        static void Main(string[] args)
        {

            string[] lines = System.IO.File.ReadAllLines("input.txt");

            string code;
            int last;
            last = lines.Length - 1;
            code = "";
            for (int i = 0; i < lines[last].Length; i++)
            {

                if (char.IsUpper(lines[last],i)==true)
                {
                    for (int j = 0; j < lines.Length - 1; j++)
                    {
                        if (lines[last][i] == lines[j][0])
                            code = code + lines[j].Remove(0, 2) ;
                    }

                }
                else
                code += lines[last][i];
            }
            for (int i = 0; i < code.Length-1; i++)
            {
                if (code[i] == '.')
                {
                    code=code.Remove(i - 1, 2);
                }
            }


            System.Console.WriteLine(code);
            System.Console.WriteLine("result:");
            string t="";
            for (int i = 0; i < code.Length - 1; i++)
            {
                if (char.IsSymbol(code[i]) == true)
                {
                    for (int j = i; j < code.Length - 1; j++)
                    {
                        t += code[i];
                    }
                }
                else 
                    t = t+code[i];

            }
            code =t;
            System.Console.WriteLine(code);
            System.Console.ReadLine();
        }
    }
}
