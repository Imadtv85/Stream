import subprocess
import requests
import time

# بيانات cookies من فيسبوك
cookies = {
    'datr': 'dSdBZ8ZGxPbQR8tNY23cgN_J',
    'sb': 'dSdBZ3uKi5P7y8smUuJjarYd',
    'ps_l': '1',
    'ps_n': '1',
    'wd': '431x809',
    'c_user': '61557829686505',
    'fr': '0nWlCq3pL1pOqh3ei.AWWdKhbVMMcrfFrP_TBldgmms6E.BnQSd1..AAA.0.0.BnQSed.AWW97AQd4nU',
    'xs': '37%3Ats7aR5f3BgV-kA%3A2%3A1732323231%3A-1%3A6995',
    'locale': 'fr_FR',
    'wl_cbv': 'v2%3Bclient_version%3A2679%3Btimestamp%3A1732323238',
    'fbl_st': '100727379%3BT%3A28872054',
    'vpd': 'v1%3B809x431x2.5062501430511475'
}

# القنوات والبث
channels = [
    {
        'm3u8_url': 'https://live4.beinconnect.us/YallaGoalApp/beINSports1.m3u8',
        'stream_key': 'FB-122166221492260989-0-AbyDiyB_Nr94DEcp'
    },
    {
        'm3u8_url': 'https://live4.beinconnect.us/YallaGoalApp/beINSports6.m3u8',
        'stream_key': 'FB-122166222230260989-0-AbzzM6v3SqBiOlmm'
    }
]

# دالة لتشغيل البث باستخدام FFmpeg
def start_stream(m3u8_url, stream_key):
    ffmpeg_command = [
        'ffmpeg',
        '-i', m3u8_url,  # رابط m3u8
        '-c:v', 'libx264',  # ترميز الفيديو
        '-preset', 'fast',
        '-max_muxing_queue_size', '1024',
        '-f', 'flv',  # تنسيق البث
        f'rtmps://live-api-s.facebook.com:443/rtmp/{stream_key}'  # رابط البث مع الـ Stream Key
    ]

    print(f"Starting stream with stream key: {stream_key}")
    subprocess.run(ffmpeg_command)

# دالة للحصول على رابط الـ Stream Key عبر Cookies (إن كنت بحاجة لها)
def get_stream_key(cookies):
    # في حال كانت هناك طريقة لجلب الـ stream key عبر الـ cookies، يمكنك تعديل هذه الدالة.
    # في هذه الحالة نحن نفترض أن الـ stream key متاح في القاموس
    return 'FB-122166221492260989-0-AbyDiyB_Nr94DEcp'  # استبدال ذلك بالمنطق الفعلي إذا كان ممكنًا

# دالة لإدارة بدء جميع البثوث
def start_all_streams():
    for channel in channels:
        print(f"Starting stream for Channel with stream key {channel['stream_key']}")
        start_stream(channel['m3u8_url'], channel['stream_key'])
        time.sleep(5)  # الانتظار بين البثوث (إذا كان هناك حاجة لذلك)

# بدء البث
if __name__ == "__main__":
    start_all_streams()
