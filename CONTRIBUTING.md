First of all, thank you for your interest in contributing to this repository! :rocket:

However, before you create your pull request (or commit), there are a few things you need to know!

## Contributing
We all know how frightening it is contributing for the first time to a repository. Don't worry, though!
If you follow all steps in this page, your pull request will be welcome with open arms!

1. Make sure you have Git installed on your computer
2. Fork this repository
3. Clone your fork to your computer using `git clone <URL of your fork>`
4. Checkout the `develop` branch using `git checkout develop`
5. Create a new branch for your changes using `git checkout -b <branch name>`
   
   It's name *should* be something concise and as descriptive as possible and may start with a type. 
   Some good examples are `feature/fix-wrong-output-encoding`, `feature/add-support-for-toml-files`, `release/1.0.0`, or `hotfix/fix-vulnerability-in-parser`. 
   
   This is also know as the [Git Flow](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow) workflow
   and helps ensure that the repository remains organized.
   
6. Make your changes
7. Stage the files you've changed for commit using `git add <files>`
8. Commit your changes using `git commit`

   In this repository, we follow the [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) specification.
   *Your contribution **will not** be accepted if your commits do not follow said specification.*
   
   That said, you can use [gitmoji](https://gitmoji.dev/) in your commit message to spice it up a bit.
   An acceptable commit message with gitmoji in it would look something like `docs(readme): :memo: add instalation instructions`.
   
9. Push your changes to your fork using `git push`
10. Go to your fork's Github page, select the branch you've created and start a pull request

    The base for your pull should be the `develop` branch.

If you've completed these steps, you should now have an open pull request in this repository.
Now, you can sit back, relax, and wait for someone in the [@MIEIC-FEUP/quiz-trainer-core](https://github.com/orgs/MIEIC-FEUP/teams/quiz-trainer-core) team to review your pull request.

If you are asked to make some changes and you don't know how to do them, don't be afraid to ask! We are here to help you!

## TL;DR for experienced users
In this repository, we enforce the use of the [Git Flow](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow) workflow and the [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) specification.
If your changes do not cumply with any of those, your contribution will be rejected.

That said, the use of [gitmoji](https://gitmoji.dev/) is allowed, but not required.

An acceptable commit message with gitmoji in it would look something like `docs(readme): :memo: add instalation instructions`.
