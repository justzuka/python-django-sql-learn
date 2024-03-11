from .models import Exercise

def populate_exercises():
    # Real exercise data with descriptions, instructions, and target muscle groups
    exercise_data = [
        {"name": "Push-ups", "description": "Classic bodyweight exercise focusing on chest and triceps.",
         "instructions": "1. Start in a plank position\n2. Lower your body towards the ground\n3. Push back up to the starting position",
         "target_muscle_groups": "Chest, Triceps"},
         
        {"name": "Squats", "description": "Fundamental lower body exercise targeting quads, hamstrings, and glutes.",
         "instructions": "1. Stand with feet shoulder-width apart\n2. Bend knees and lower your hips\n3. Stand back up to the starting position",
         "target_muscle_groups": "Quads, Hamstrings, Glutes"},
         
        {"name": "Lunges", "description": "Great exercise for leg strength and stability.",
         "instructions": "1. Stand with feet together\n2. Take a step forward with one foot\n3. Lower your body until both knees are bent\n4. Return to the starting position and repeat on the other leg",
         "target_muscle_groups": "Quads, Hamstrings, Glutes"},
         
        {"name": "Plank", "description": "Core-strengthening exercise that also engages shoulders and back.",
         "instructions": "1. Start in a forearm plank position\n2. Keep your body in a straight line\n3. Hold the position for the desired duration",
         "target_muscle_groups": "Core, Shoulders, Back"},
         
        {"name": "Deadlifts", "description": "Compound exercise targeting multiple muscle groups, including back and hamstrings.",
         "instructions": "1. Stand with feet hip-width apart\n2. Bend at the hips and knees to lower the weights\n3. Keep your back straight and chest up\n4. Stand back up to the starting position",
         "target_muscle_groups": "Back, Hamstrings, Glutes"},
         
        {"name": "Bench Press", "description": "Classic chest exercise using a barbell or dumbbells.",
         "instructions": "1. Lie on a flat bench with a barbell or dumbbells\n2. Lower the weights to your chest\n3. Push the weights back up to the starting position",
         "target_muscle_groups": "Chest, Triceps, Shoulders"},
         
        {"name": "Pull-ups", "description": "Upper body exercise focusing on the back and biceps.",
         "instructions": "1. Hang from a bar with palms facing away\n2. Pull your body up until your chin is above the bar\n3. Lower your body back down",
         "target_muscle_groups": "Back, Biceps"},
         
        {"name": "Russian Twists", "description": "Effective exercise for oblique muscles and core rotation.",
         "instructions": "1. Sit on the floor with knees bent and feet elevated\n2. Twist your torso to one side, touching the floor with your hands\n3. Return to the center and repeat on the other side",
         "target_muscle_groups": "Obliques, Core"},
         
        {"name": "Calf Raises", "description": "Isolation exercise for strengthening the calf muscles.",
         "instructions": "1. Stand on a flat surface with feet hip-width apart\n2. Lift your heels off the ground by pushing through the balls of your feet\n3. Lower your heels back down",
         "target_muscle_groups": "Calves"},
         
        {"name": "Overhead Press", "description": "Shoulder-strengthening exercise using a barbell or dumbbells.",
         "instructions": "1. Stand with feet shoulder-width apart\n2. Lift the weights overhead, fully extending your arms\n3. Lower the weights back down to shoulder height",
         "target_muscle_groups": "Shoulders, Triceps"},
    ]

    for exercise in exercise_data:
        Exercise.objects.create(**exercise)  # Create exercise objects using dictionary unpacking

# Run the function to populate data (optional)
if __name__ == "__main__":
    populate_exercises()
