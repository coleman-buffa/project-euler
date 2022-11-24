//A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

//Find the largest palindrome made from the product of two 3-digit numbers.

void calcPalindrome()
{
    int maxPal = 0;
    int n1 = 0;
    int n2 = 0;
    for (int i = 999; i > 500; i--)
    {
        for (int j = 999; j > 500; j--)
        {
            int tempProduct = i * j;
            if (checkPalindrome(tempProduct))
            {
                if (maxPal < tempProduct)
                {
                    maxPal = tempProduct;
                    n1 = i;
                    n2 = j;
                }
            }
        }
    }

    Console.WriteLine("The largest palindromic product is {0} which is the product of {1} and {2}", maxPal, n1, n2);
}

bool checkPalindrome(int n)
{
    int temp = n;
    int reverseN = 0;
    while (n > 0)
    {
        int digit = n % 10;
        reverseN = reverseN * 10 + digit;
        n = n / 10;
    }

    return temp == reverseN ? true : false;
}

calcPalindrome();