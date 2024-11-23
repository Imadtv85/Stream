import subprocess

# بيانات القنوات وStream Keys
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

# وظيفة لبدء البث باستخدام FFmpeg
def start_stream(m3u8_url, stream_key):
    ffmpeg_command = [
        'ffmpeg', 
        '-i', m3u8_url,  # رابط M3U8
        '-c:v', 'copy',  # نسخ الفيديو بدون تغيير الترميز
        '-c:a', 'copy',  # نسخ الصوت بدون تغيير الترميز
        '-f', 'flv',  # تحديد صيغة الإخراج
        '-reconnect', '1',  # إعادة المحاولة تلقائيًا عند فشل الاتصال
        '-reconnect_streamed', '1',  # إعادة المحاولة للبث
        '-reconnect_delay_max', '2',  # الحد الأقصى للتأخير بين المحاولات
        f'rtmp://live-api-s.facebook.com/rtmp/{stream_key}'  # رابط فيسبوك مع الـ Stream Key
    ]
    
    try:
        print(f"Starting stream for stream key: {stream_key}")
        subprocess.run(ffmpeg_command, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while streaming: {e}")
    except FileNotFoundError:
        print("FFmpeg not found. Please install FFmpeg.")

# بدء البث لجميع القنوات
def start_all_streams():
    for channel in channels:
        start_stream(channel['m3u8_url'], channel['stream_key'])

if __name__ == "__main__":
    start_all_streams()
