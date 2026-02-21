# Hesiod Flashcards
Uses [Project Hesiod](https://github.com/boconnor2017/hesiod), a Photon based approach to initiate, launch, and manage a test platform for flashcards. 

## Prerequisites
1. Deploy a [Hesiod Node](https://github.com/boconnor2017/hesiod?tab=readme-ov-file#deploy-hesiod-nodes). Run all remaining steps on this node.
# Quick Start
*Recommended: run these scripts as root.*
```
cd /usr/local/
```
```
git clone https://github.com/boconnor2017/hesiod-flashcards
```
```
cp -r hesiod/python/ hesiod-flashcards/hesiod
```
```
cd hesiod-flashcards/
```
Create a multiple choice questionnaire using the json structure in `/usr/local/hesiod-flashcards/json/lab_environment.json` and run:
```
python3 hesiod-flashcards.py
```
