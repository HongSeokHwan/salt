
## Intro

'salt'는 미디어 폴더(media)에 있는 mp4 파일 중 오래된 파일을 자동으로 압축(3M이하) 저장해주는 프로그램입니다.

짧은 동영상(20초 미만)이 대부분이고, 오래된 동영상을 잘라도 되는 상황에 알맞은 프로그램입니다.

- 동영상 중요장면이 대부분 후반부에 있다는 가정하에 뒤 20초만 남깁니다.
- 압축한 파일은 2M정도가 됩니다. 
- 미디어 폴더, 압축할 시간, 영상 사이즈를 설정으로 변경할 수 있습니다. 

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

위의 설정대로 하는 경우 ./media_path/ 폴더에 있는 모든 mp4 파일을 재귀적으로(recursive) 검색하면서, 3M보다 크고, 5일이 지난 동영상인 경우, 압축하여 갱신합니다.

