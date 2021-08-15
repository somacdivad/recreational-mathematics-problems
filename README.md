# recreational-mathematics-problems
Weekly recreational mathematics coding challenges with solutions

## Learn Math and Code Together
I've long been a proponent of using programming to aid in mathematical research. But recently, I've been enjoying pairing coding with recreational mathematics.

Exploring recreational mathematics with code offers a couple of benefits:

1. It has **broad appeal**: Recreational mathematics problems are often framed in language that has broader appeal than research mathematics. Folks who enjoy any kind of puzzle may also fin recreational mathematics attractive.
1. It **builds intuition**: Solving recreational mathematics problems builds mathematical intuition. Solving the problem with *code* adds another dimension — perhaps many. There is a _translation step_ that involves designing and implementing a model for the problem and an _algorithmic step_ that brings a solution to life. Knowing how to create a model and implement a solution carries over to practically all other disciplines.
1. It **enhances skill sets**: Modelling recreational mathematics problems introduces you to a wide range of data structures and algorithms, many, if not all, of which apply to domains outside of mathematics. Not only do you learn some computer science concepts, but you also get lots of practice with a programming language and increase your fluency. Your problem-solving skills get sharpened, too.

I thought other people would enjoy working on these kinds of problems, too, so I started a weekly recreational mathematics coding challenge. This repository houses the problem statements and solutions to the problems in this challenge.

Every Monday, I post a video going over my solution to the previous problem, some interesting solutions sent to me from the community, and then propose the problem for the current week.

You can watch the explainer video [here](https://www.youtube.com/watch?v=2aYDwfx-wvE).

The complete playlist of videos is available [here](https://www.youtube.com/playlist?list=PLLIPpKeh9v3Y3ZXXsz9lVUFqQBx34BK56).

## How To Submit Solutions

If you'd like to submit a solution to a weekly challenge problem, you can:

- Open a pull request
- Open an issue
- Or, send an email to recmath at davidamos dot dev

Please include how you would like to be referred to if your solution is submitted. For example, do you prefer your real name or something else?

> **Note:** By submitting a solution, you agree to release any code or text for the solution under the MIT license.

If you do *not* want your solution featured in a video, please indicate that in your submission.

Solutions to past challenges will still get reviewed and are eligible for getting featured in future videos.

## How This Repository is Structured

All of the problems are in the `problems/` folder.

Currently, each problem is contained in a folder with the following template: `YYYY-MM-DD <Challenge Name>`. In the future, I may organize these folders by year.

A problems folder has the following directory structure:

```
.
├── README.md
└── solutions/
    ├── community/
    └── solution.ipynb
```

Here's a breakdown of each file and folder:

- **`README.md`**: Contains the problem statement
- **`solutions/`**: Contains all of the solutions
- **`solutions/solution.ipynb`**: A Jupyter Notebook containing *my* solution
- **`solutions/community/`**: Contains all of the community submitted solutions
