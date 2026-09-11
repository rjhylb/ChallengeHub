# Google Colab Setup

Use one persistent ChallengeHub folder in Google Drive for the duration of the course.

## One-time setup

Place the complete repository directly inside **My Drive**:

```text
My Drive/
└── ChallengeHub/
    ├── challengehub/
    ├── data/
    ├── tests/
    ├── notebooks/
    └── outputs/
        ├── M2LA2/
        ├── PO4/
        ├── M2CW/
        └── Final_Project/
```

Avoid creating an extra nested folder such as `My Drive/ChallengeHub/ChallengeHub/`.

## Each new Colab runtime

Open the course notebook and run its **Connect Course Project** cell.

The cell mounts Google Drive at `/content/drive`, uses `/content/drive/MyDrive/ChallengeHub` as the project root, changes the working directory to that folder, and adds the project root to Python's import path.

The repository is not re-created when the runtime restarts. Code, data, notebooks, and saved outputs remain in Google Drive.

If the setup cell cannot find the project, check that `ChallengeHub` is directly inside **My Drive**.
