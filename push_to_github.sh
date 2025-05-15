#!/bin/bash
git init
git add .
git commit -m "Deploy full Venture North Admin platform"
git branch -M main
git remote add origin https://github.com/gecko1134/venture-north-admin.git
git push -u origin main