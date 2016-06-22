
## Intro

'salt'는 미디어 폴더(media)에 있는 mp4 파일 중 오래된 파일을 자동으로 압축(3M이하) 저장해주는 프로그램입니다.

만약, 짧은 동영상 (20초 미만)을 주로 고객들이 올리는 상황이고, 오래된 고객의 동영상을 잘라서 서비스해도 되는 상황에 최적화 된 프로그램입니다.


## Getting Started

### Prerequisites

- ffmpeg (apt-get, brew 등을 이용)
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

위의 설정대로 하는 경우 ./media_path/ 폴더에 있는 모든 mp4 파일을 재귀적으로(recursive) 검색하면서, 3M보다 크고, 5일이 지난 동영상인 경우, 압축하게 됩니다.

