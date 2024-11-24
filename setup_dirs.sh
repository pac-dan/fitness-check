# list of apps
apps=("goals" "notifications" "nutrition" "progress" "wearables" "workouts")

for app in "${apps[@]}"
do 
    echo "Setting up directories for $app app..."

    # Create templates directory and initial html file
    mkdir -p "$app/templates/$app"
    touch "$app/templates/$app/index.html"

    # Create static directory and initial css file
    mkdir -p "$app/static/$app/css"
    touch "$app/static/$app/css/style.css"

    echo "Directories for $app app have been created."
    echo "_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _"
done

echo "All directories have been created."
