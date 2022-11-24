//The prime factors of 13195 are 5, 7, 13 and 29.

//What is the largest prime factor of the number 600851475143 ?

maxPrimeFactor(600851475143);

void maxPrimeFactor (long n)
{
    long maxPrime = -1;

    while (n % 2 == 0)
    {
        maxPrime = 2;
        n /= 2;
    }

    for (int i = 3; i < Math.Sqrt(n) + 1; i += 2)
    {
        while (n % i == 0)
        {
            maxPrime = i;
            n = n / i;
        }
    }

    if (n > 2)
    {
        maxPrime = n;
    }       

    Console.WriteLine("The larget print factor of 600851475143 is {0}", maxPrime);       
}

