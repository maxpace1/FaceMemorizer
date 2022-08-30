# Face Memorizer
A program to help you remember people's faces!
Simply put all the face images you'd like to learn in a subfolder of the projcet directory titled `/faces` and run the script.
All images must follow the naming format "FirstName_LastName.jpeg".

### Using the program
Once your images are saved and properly formatted, run the `face_memo.py` script. You will be prompted with a question of how many faces you'd like to learn at a time. The program divides the list of people into "batches" so that you can focus on learning a few people at a time. I recommend choosing a number from 5-10 as a nice balance of seeing enough faces to not simply remember a person immediately and forget quickly while still being able to focus on only a handful of people at a time.

The program will display each picture in a CV2 window, but you will be prompted to identify the person in the terminal window you ran the script from. If you do not know the person, simply hit return/enter, and you will be told the correct answer and required to type the name correctly. If you make any mistakes or don't enter a name, you will stay on the same batch until you get all people correct. The program will terminate when you have successfully finished all batches.

### Inspiration
After applying to several competitive clubs and teams, I learned the impact remembering people's names can have. Of course, remembering 40+ names can be tricky. After attempting to use Quizlet to solve this problem, I was disappointed to learn that using images in Quizlet is not a free feature. Instead of giving into the premium features, I decided to write a program to solve the problem myself. I found the program to be rather effective, and I will continue using it in my future!
