#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - inserts a node into a sorted singly linked list
 * @head: pointer to pointer to the head of the list
 * @number: integer to be inserted
 * Return: address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
    listint_t *new_node = malloc(sizeof(listint_t));
    if (!new_node)
        return NULL;

    new_node->n = number;
    new_node->next = NULL;

    listint_t *current = *head;
    listint_t *prev = NULL;
    while (current && current->n < number) {
        prev = current;
        current = current->next;
    }

    if (prev == NULL) {
        new_node->next = *head;
        *head = new_node;
    } else {
        prev->next = new_node;
        new_node->next = current;
    }

    return new_node;
}

