/*
Start at Dec 11th, 16:00.
gcc version 11.3.0 (Ubuntu 11.3.0-1ubuntu1~22.04
I test it by running following, line by line:

gcc -ansi dijkstra.c -o solution
./solution
5
50
30 5
100 20 50
10 x x 10


Finish at Dec 11th 18:34. This project takes me 2 hour 34 minues.
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define INF 0x3f3f3f3f
/*Assume all input weights are smaller that INF, which is a 10-digit string in decimal.
The longest input line is the last line of 100 cities case, which involves at most 1100 characters. */
#define CLI_LIMIT 2000

int read_number_of_cities()
{
    int n = 0;
    printf("Please entry the number of cities n, an integer from 1 to 100:\n");
    while (1)
    {
        if (scanf("%d", &n) == 0)
        {
            while (fgetc(stdin) != '\n')
                ;
            printf("The input should be a string of number.\n");
            continue;
        }
        if (n >= 1 && n <= 100)
            break;
        else
        {
            printf("n should be an integer between 1 and 100(inclusive).\n");
        }
    };
    fflush(stdin);
    return n;
}

void read_lower_triangle_of_adjacency_matrix(int n, int *Graph)
{
    int i = 0, j = 0, current_value = 0, buffer_pointer = 0;
    size_t bufsize = CLI_LIMIT;
    char *line_buffer = NULL;
    char *current_value_string;

    printf("Please enter lower triangular part of the adjacency matrix.\n");
    printf("Please enter 2nd-nth line in order:\n");

    getline(&line_buffer, &bufsize, stdin);
    i = 1;
    for (i; i < n; i++)
    {
        getline(&line_buffer, &bufsize, stdin);
        current_value_string = strtok(line_buffer, " ");
        j = 0;
        for (j; j < i; j++)
        {
            if (strcmp(current_value_string, "x") == 0)
            {
                current_value = INF;
            }
            else
            {
                current_value = atoi(current_value_string);
            }
            current_value_string = strtok(NULL, " ");
            Graph[i * n + j] = current_value;
            Graph[j * n + i] = current_value;
        }
    }
    return;
}

void print_matrix(int n, int *Graph)
{
    int i = 0, j = 0, val = 0;
    for (i; i < n; i++)
    {
        j = 0;
        for (j; j < n; j++)
        {
            val = Graph[i * n + j];
            if (j == n - 1)
            {
                printf("%d\n", val);
            }
            else
            {
                printf("%d ", val);
            }
        }
    }
    return;
}

int search_time_required_throughtout_empire(int n, int *graph_adjacency_matrix)
{
    int costs_to_travel_cities[n * n], visited[n];
    int i = 0, j, max_cost_thoughout_empire = 0, cities_left_count;
    int newly_visited_city, min_distance_from_capitol;
    int new_cost;

    for (i; i < n; i++)
    {
        visited[i] = 0;
        j = 0;
        for (j; j < n; j++)
        {
            costs_to_travel_cities[i * n + j] = graph_adjacency_matrix[i * n + j];
        }
    }

    /*Initialization for message spreading from capitol*/
    cities_left_count = n - 1;
    visited[0] = 1;

    while (cities_left_count >= 0)
    {
        min_distance_from_capitol = INF;
        i = 0;
        for (i; i < n; i++)
        {
            if (visited[i] == 0 && costs_to_travel_cities[i] < min_distance_from_capitol)
            {
                min_distance_from_capitol = costs_to_travel_cities[i];
                newly_visited_city = i;
            }
        }
        visited[newly_visited_city] = 1;
        i = 0;
        for (i; i < n; i++)
        {
            if (!visited[i])
            {
                new_cost = min_distance_from_capitol + costs_to_travel_cities[newly_visited_city * n + i];
                if (new_cost < costs_to_travel_cities[i])
                {
                    costs_to_travel_cities[i] = new_cost;
                    costs_to_travel_cities[i * n] = new_cost;
                }
            }
        }
        cities_left_count--;
    }
    i = 0;
    for (i; i < n; i++)
    {
        if (costs_to_travel_cities[i] > max_cost_thoughout_empire)
        {
            max_cost_thoughout_empire = costs_to_travel_cities[i];
        }
    }
    return max_cost_thoughout_empire;
}

int main()
{
    int n = read_number_of_cities();
    int *graph_adjacency_matrix;
    int time_required_to_reach_all_cities;
    graph_adjacency_matrix = malloc((n * n) * sizeof(int));
    read_lower_triangle_of_adjacency_matrix(n, graph_adjacency_matrix);

    /* Test input parsing
    printf("The adjacency Matrix is:\n");
    print_matrix(n, graph_adjacency_matrix);
    */

    time_required_to_reach_all_cities = search_time_required_throughtout_empire(n, graph_adjacency_matrix);
    printf("The minimum time required for the message to travel troughout the empire is:\n");
    printf("%d\n", time_required_to_reach_all_cities);

    return 0;
}

