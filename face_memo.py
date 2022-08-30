import os
import random
import cv2 as cv
from cv2 import imshow

def quiz_batch(faces):
  errs = []

  for face in faces:
    first,last = face.split("_")
    last = last[:-5]
    full_name = first + " " + last
    img = cv.imread(dir + face)
    imshow("Who is this?", img)
    print(">>> Who is this? ")
    guess = ""
    cv.waitKey(1)
    guess = input("")

    if guess.casefold() == full_name.casefold():
      print("Correct!")
    else:
      print("Incorrect: expected " + full_name)
      errs.append(full_name)
      if guess == "":
        print("Please type the correct name.")
        while guess.casefold() != full_name.casefold():
          guess = input("")

    input(">>> Press return to continue ")
  return errs

dir = os.path.dirname(os.path.realpath(__file__)) + "/faces/"
faces = os.listdir(dir)
faces = list(filter(lambda f: f[0] != ".", faces))
random.shuffle(faces)

batch_size = int(input(">>> How many faces do you want to learn at a time? "))
n_batches = (len(faces) + batch_size - 1) // batch_size

for i in range(n_batches):
  print(f"Round {i + 1}!")
  batch = faces[i * batch_size : (i+1) * batch_size]
  while True:
    errs = quiz_batch(batch)
    print(f"\nYou got {len(batch)-len(errs)}/{len(batch)} correct!")
    if len(errs) == 0:
      print("Congrats!\n")
      break
    print("You missed:")
    for err in errs:
      print(err)
    random.shuffle(batch)