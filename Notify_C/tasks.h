#ifndef TASKS_H
#define TASKS_H

struct Task {
  char taskname[100];
  int category;
};

void create_task();
void list_tasks();
void edit_task();
void delete_task();
void display_tasks_for_date(int year, int month, int day);
void save_tasks();
void load_tasks();

#endif
