# SIMPLE Project Workout API

## Requirements

- Python
- Django
- Django REST Framework

## Installation

first clone the repo

```
git clone ...
```

After you cloned the repository, you want to create a virtual environment, so you have a clean python installation.
You can do this by running the command

```
python -m venv venv
```

After this, it is necessary to activate the virtual environment.

```
venv\Scripts\activate.ps1
```

Navigate to the project directory and install requirements:

```
cd project_workouts
pip install -r requirements.txt
```

Perform database migrations:

```
python manage.py migrate
```

Populate the exercises database with 10 default exercises:

```
python manage.py populate_exercises
```

Run the development server:

```
python manage.py runserver
```

Access the Swagger documentation at /swagger to interact with the endpoints.

Now we need to signup or login to use other APIs.

## Create users and Tokens

Open signup in swagger and click try it out, after execute it should return something like this.

```
{
  "token": "69801041f80ff02466cff7708ca7d7543a0766db",
  "user": {
    "id": 8,
    "username": "zukaK",
    "password": "zuka123",
    "email": "zukaK@gmail.com"
  }
}
```

Now we take the token, and use it for authorization. on the up right corner, there is an authorization button.

Paste your token like this.

```
Token 69801041f80ff02466cff7708ca7d7543a0766db
```

Now user should be authorized.

## Get and Create exercises and workout plans.

Find /workouts/default-exercises and click try it out and execute.
If you have done populate_exercises than u should see something like this.

```
[
  {
    "id": 6,
    "name": "Bench Press",
    "description": "Classic chest exercise using a barbell or dumbbells.",
    "instructions": "1. Lie on a flat bench with a barbell or dumbbells\n2. Lower the weights to your chest\n3. Push the weights back up to the starting position",
    "target_muscle_groups": "Chest, Triceps, Shoulders"
  },
  {
    "id": 9,
    "name": "Calf Raises",
    "description": "Isolation exercise for strengthening the calf muscles.",
    "instructions": "1. Stand on a flat surface with feet hip-width apart\n2. Lift your heels off the ground by pushing through the balls of your feet\n3. Lower your heels back down",
    "target_muscle_groups": "Calves"
  },
  ...
]
```

These are the default exercises that are there already.

Now lets create a workout plan for the user.

Find workouts/create-workout-plan and input something like this.

```
{
  "name": "Noobie workout plan",
  "frequency": 3,
  "goal": "Get stronger",
  "duration": 90
}
```

Which should return something like this.

```
{
  "id": 5,
  "name": "Noobie workout plan",
  "frequency": 3,
  "goal": "Get stronger",
  "duration": 90,
  "user": 8
}
```

Here the frequency is defined already, there are specific choices for frequency, to see the choices find /workouts/get-frequency-choises
and run it.

```
{
  "1": "Daily",
  "2": "Every Other Day",
  "3": "Once in a week"
}
```

These are values that we have there for now, so 3 means Once in a week.

Now we need to create and add workoutplanexercises to the workoutplan.

To do that find workouts/create-workout-plan-exercise and input something like this.

```
{
  "workout_plan": 5,
  "exercise": 1,
  "repetitions": 4,
  "sets": 4,
  "duration": 100,
  "distance": 0
}
```

Here workout_plan is an id of the workout plan we created, so take it from there, and exercise is the id of the predefined exercises
that we saw before, 1 means pushups here.

Now we should see that workoutplanexercise was created, and it is connected to the workout plan we created.

```
{
  "id": 8,
  "repetitions": 4,
  "sets": 4,
  "duration": 100,
  "distance": 0,
  "workout_plan": 5,
  "exercise": 1
}
```

Now create couple more like this and than find workouts/get-wokout-plan-exercises/{workout_plan_id} that will give all corresponding workoutplanexercises.

```
[
  {
    "id": 8,
    "repetitions": 4,
    "sets": 4,
    "duration": 100,
    "distance": 0,
    "workout_plan": 5,
    "exercise": 1
  },
  {
    "id": 9,
    "repetitions": 5,
    "sets": 7,
    "duration": 30,
    "distance": 0,
    "workout_plan": 5,
    "exercise": 3
  }
]
```

## Get, Update and Create goals.

To create a goal find workouts/create-goal, and input something like this.

```
{
  "type": "weight",
  "weight_target": 60,
  "exercise": 3,
  "target_value": 5
}
```

And this should return

```
{
  "id": 10,
  "type": "weight",
  "weight_target": 60,
  "target_value": 5,
  "user": 8,
  "exercise": 3
}
```

Tere type is another predefined choices paramter, to get it, find goal type choices.

```
{
  "weight": "Weight Loss/Gain",
  "exercise": "Exercise Specific"
}
```

To update the goal just find update_goal.

There are couple more endpoints as well.
