#!/bin/bash

# Array to store installed modules
installed_modules=()

while true; do
    python3 -m app.main 2>&1 | tee /tmp/error.log
    
    if grep -q "ModuleNotFoundError: No module named" /tmp/error.log; then
        module=$(grep "ModuleNotFoundError" /tmp/error.log | sed "s/.*No module named '\(.*\)'.*/\1/")
        echo "Installing missing module: $module"
        pip install $module
        
        # Add to installed modules array if not already there
        if [[ ! " ${installed_modules[@]} " =~ " ${module} " ]]; then
            installed_modules+=("$module")
        fi
    else
        break
    fi
done

# Save installed modules to requirements.txt
if [ ${#installed_modules[@]} -gt 0 ]; then
    echo "Saving installed modules to requirements.txt..."
    for module in "${installed_modules[@]}"; do
        # Get the installed version
        version=$(pip show "$module" 2>/dev/null | grep "Version:" | awk '{print $2}')
        if [ -n "$version" ]; then
            echo "$module==$version" >> requirements.txt
        else
            echo "$module" >> requirements.txt
        fi
    done
    echo "Successfully saved ${#installed_modules[@]} module(s) to requirements.txt"
else
    echo "No new modules were installed."
fi