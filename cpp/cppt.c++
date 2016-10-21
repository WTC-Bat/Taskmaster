#include <iostream>
#include <string>
using namespace std;

void pargs(string args[])
{
	int cnt;

	cnt = 0;
	// cout << args->size();
	// return;
	while (cnt < args->size() - 1)
	{
		cout << "Arg (" << cnt << "): " << args[cnt];
		cnt++;
	}
}

int	main()
{
	// string teststr = "Cheese";
	//
	// cout << teststr;
	string args[5];

	args[0] = "Cheese";
	args[1] = "and";
	args[2] = "crackers";
	args[3] = "are";
	args[4] = "great";

	pargs(args);
}
