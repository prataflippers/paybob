COLUMNS=$(tput cols)
title="THE CLEANSLATE PROGRAM"
line="-----------------------------------"
printf "%*s\n" $(((${#line}+$COLUMNS)/2)) "$line"
printf "%*s\n" $(((${#line}+$COLUMNS)/2)) "$line"
printf "%*s\n" $(((${#title}+$COLUMNS)/2)) "$title"
printf "%*s\n" $(((${#line}+$COLUMNS)/2)) "$line"
printf "%*s\n" $(((${#line}+$COLUMNS)/2)) "$line"
find . -name "*.pyc" -type f
find . -name "*.poc" -type f
find . -name ".DS_Store" -type f
find . -name "*.sqlite" -type f


echo "This operation will remove all compiled python files and erase the existing database"
read -r -p "Are you sure you want to delete all these files? [y/N] " response
case "$response" in
    [yY][eE][sS]|[yY])
        find . -name "*.pyc" -type f -delete
        find . -name "*.poc" -type f -delete
        find . -name ".DS_Store" -type f -delete
        find . -name "*.sqlite" -type f -delete
        echo "All files were successfully deleted."
        ;;
    *)
        echo "No files were deleted"
        ;;
esac
