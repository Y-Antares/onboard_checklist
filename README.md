# onboard_checklist

The instructions here are for new members to get familar with group coding style and some mandatory knowledge.

1. General guideline:
  - You should always work on your own forked repo, and create a new branch there (always git pull when you start creating a new branch so as to keep it updated with the remote). Once your work is finished, create a PR to merge `your forked repo's branch in process` into `group main repo that you fork from`.
  
2. Learn to use Github:
  - Turn on your github account's email notification. Click your personal account on the top right corner -> Settings -> Notifications -> Turn on your emails for `Watching` and `Participating, @mentions and custom`.
  - Set up the private and public ssh keys for your github account. See [instructions](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent).
  - Fork this `onboard_checklist` repo by clicking on the top right corner on the github web of this repo.
  - SSH `git clone` your forked repo to your local computer.
  - Create a new branch of your repo `git checkout -b [your_name]`, usually the branch name refers to the issues or problems to be solved. Here as a tutorial, use your name as the branch name.
  - Add the group main repo into your repo setting by `git remote add upstream git@github.com:yanglonggroup/onboard_checklist.git`.
  - Run `git remote -v` to check if you set up correctly. It should show `origin` as your own forked repo; and show `upstream` as the group's main repo.
  - Create a new `[your_name].py file` at the people folder. You can write some simple codes in this file, such as some dummy codes like `import numpy` etc. Don't let it be empty, otherwise empty files cannot be uploaded to github. This is just for you to get familar with github workflow.
  - Use git add, git commit, git push to update your local work to remote. For the git commit messages, please refer to the (numpy commit message style)[https://numpy.org/devdocs/dev/development_workflow.html#writing-the-commit-message]. For example, we use `DOC, ENH, MNT` to represent the work for writing documentation, new codes, and updating old codes, respectively.
  - Go to the github web of your forked repo, create a PR (pull request), to merge the branch with your work to the main branch of the group.
  - Check the codes that you updated is correct, then write some words and at Prof. Yang to explain your PR, such as `@dragonyanglong, this PR is for me to learn github. please review and merge`.
  - Continue with comments or suggestions you received, until your PR is merged. Good job!

3. Repo structure:
  - A new project refers to a new repo, see the [group repo template](https://github.com/yanglonggroup/repo_template). The structure of the repo is explained as follows. It can be wrapped as a python package, so that others can install and import it.
  - `pkgname` folder: This is the major place for you to write codes. By the way, we usually rename `pkgname` to match the repo's name, always use lowercase.
  - `requirements` folder: This is for listing all the required external python modules and libraries, such as numpy, matploblib
  - `tests` folder: This is for writing tests to check if your codes fail.
  - `.gitignore`: This defines what files WILL BE ignored for github, so we can save spaces on the github server storage.
  - `AUTHORS.txt`: Write your name and email there.
  - `LICENSE`: This defines how others can use the open-sourced package. In most case, we don't need to change anything here.
  - `README.md`: This is the documentation for a repo, and it can appear at the main page of the website. We can write instructions for how to isntall a package and how to use it.
  - `__init__.py`: This is a default template file required for a python package, no changes needed.
  - `setup.py`: This is an IMPORTANT file to wrap the repo into a python package, modify it line by line.
  - other files that you don't need to care about at this moment yet: `docs`, `news`, `rever.xsh`.
  
4. Code style:
  - Please read [PEP 8](https://pep8.org/), and stick with this coding sytle for ALL of your work.
  - You may use some popular IDE to help correct your codes, such as PyCharm. See tutorial [here](https://zhuanlan.zhihu.com/p/33705005).
  - Keep the import packages on the top.
  - Please write codes in functions and classes in `pkgname` folder, except main.py where we import the functions you wrote elsewhere and just simply run it.
  - Always write comments (we use [Google docstring style](https://www.cnblogs.com/ryuasuka/p/11085387.html)) to explain your codes and functions, no matter how trivial the function is. This is important for people to reuse and maintain your codes. For example:
  ```
  def add(x, y):
    """
    This function sums up two numbers.

    Args:
        x (float): The first number to be added.
        y (float): The second number to be added.
        
    Returns:
        sum (float): The sum of x and y.
    """
    sum = x + y

    return sum
  ```
  
5. Commonly used packages:
  - numpy: for loading numerical data.
  - pandas: for loading csv style data.
  - matplotlib: we use it for plotting figures and results.
  - scipy: scientific computation.
  - sklearn: some machine learning related models and statistical methods.
