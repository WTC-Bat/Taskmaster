#include <iostream>
#include <string>
using namespace std;

class Program
{
  public:
    string progname;	//char *	//std::string
	string command;
	int procnum;
	bool autolaunch;
	int starttime;
	string restart;
	int retries;
	string stopsig;
	int stoptime;
	list<int> exitcodes;	//std::list<int>
	string stdout;
	string stderr;
	bool redout;
	bool rederr;
	map envvars;			//std::map
	string workingdir;
	string umask;			//string??
	Program(string args[]);
};

Program::Program(string args[])
{
	int cnt;

	cnt = 0;
	cout << "Constructing 'Program'" << endl
	while (cnt < args.size())
	{
		cout << "Arg (" << cnt << "): " << arg[cnt];
		cnt++;
	}
}
