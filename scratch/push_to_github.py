import subprocess
import urllib.request
import json
import sys

def run_cmd(cmd, cwd=None):
    print(f"Running: {cmd}")
    result = subprocess.run(cmd, cwd=cwd, shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error executing {cmd}")
        print(f"Stdout: {result.stdout}")
        print(f"Stderr: {result.stderr}")
    return result

def main():
    token = "REDACTED"
    username = "Junkyu-Lee"
    repo_name = "PMC_POC"
    workspace = r"d:\workspaces\PMC_POC"

    # 1. Create Github Repository
    print("Creating GitHub repository...")
    url = "https://api.github.com/user/repos"
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    data = {
        "name": repo_name,
        "private": True,
        "description": "LG SW Project Management Competition Project"
    }
    
    req = urllib.request.Request(url, data=json.dumps(data).encode("utf-8"), headers=headers, method="POST")
    try:
        with urllib.request.urlopen(req) as response:
            res_data = json.loads(response.read().decode())
            print(f"Repository created: {res_data['html_url']}")
    except urllib.error.HTTPError as e:
        err_msg = e.read().decode()
        if "name already exists on this account" in err_msg:
            print(f"Repository {repo_name} already exists. Proceeding to push.")
        else:
            print(f"Failed to create repository: {e.code} {e.reason}\n{err_msg}")
            sys.exit(1)

    # 2. Git Init and Commit
    run_cmd("git init", cwd=workspace)
    
    # Configure git username and email if not set
    run_cmd("git config user.name 'Junkyu-Lee'", cwd=workspace)
    run_cmd("git config user.email 'junkyu.lee@example.com'", cwd=workspace)
    
    # Set default branch to main
    run_cmd("git branch -m main", cwd=workspace)

    # 3. Add and Commit
    run_cmd("git add .", cwd=workspace)
    res = run_cmd("git commit -m \"Initial commit of PMC_POC\"", cwd=workspace)
    if "nothing to commit" in res.stdout:
        print("Nothing to commit, working tree clean.")
    
    # 4. Set remote and Push
    remote_url = f"https://{token}@github.com/{username}/{repo_name}.git"
    
    # Check if origin exists
    res = run_cmd("git remote -v", cwd=workspace)
    if "origin" in res.stdout:
        run_cmd(f"git remote set-url origin {remote_url}", cwd=workspace)
    else:
        run_cmd(f"git remote add origin {remote_url}", cwd=workspace)
        
    print("Pushing to GitHub...")
    push_res = run_cmd("git push -u origin main", cwd=workspace)
    if push_res.returncode == 0:
        print("Successfully pushed to GitHub!")
    else:
        # Try pushing to master if main fails
        print("Trying to push to master...")
        push_res = run_cmd("git push -u origin master", cwd=workspace)
        if push_res.returncode == 0:
            print("Successfully pushed to GitHub on branch master!")
        else:
            print("Failed to push.")

if __name__ == "__main__":
    main()
