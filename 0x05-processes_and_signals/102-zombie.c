#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>

/**
 * main - entry point to the program.
 * Return: 0 on success
 */
int infinite_while(void);

int main(void)
{
	pid_t child;
	int status = 0, zombie_5 = 0;

	while (zombie_5 < 5)
	{
		child = fork();
		if (child == -1)
		{
			perror("error while creating a child");
			exit(1);
		}

		/* Child */
		if (child == 0)
		{
			fprintf(stdout, "Zombie process created, PID: %d\n",
			(int) getpid());
			exit(0);
		}

		child = wait(&status);
		zombie_5++;
	}
	infinite_while();

	return (0);
}

/**
 * infinite_while - infinite loop
 * Return: 0 on success
 */

int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}
