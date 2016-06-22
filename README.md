# salt
automatic video / audio compression program

## Getting Started

### Prerequisites

- ffmpeg
- python 2.7 & pip


### Quick start
```bash

pip install -r requirements.txt
./init.sh
./clear.sh
./run.sh


```

### Config

```

{
  "media_path": "media_path/", # This is for your media folder path
  "compress_day": 5, # Salt will compress mp4 files after 5 days
  "file_size_byte_limit": 3145728, # Salt will skip small files less than 3145728
  "#": "END OF JSON (This is last element without comma)"
}

```
