import os


class Config(object):
    API_HASH = os.environ.get("API_HASH", "f8d3a289bf28a13a7159ad0b2ed114e7")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6277675242:AAHLzhcXbiFM3MHh0kdJu36iJN7ih1plAfM")
    TELEGRAM_API = 26872474
    OWNER = os.environ.get("OWNER", "5211097531")
    OWNER_USERNAME = os.environ.get("OWNER_USERNAME", "RBEagle2k)
    PASSWORD = os.environ.get("PASSWORD", "2000")
    DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://Kannan:kannan@cluster0.jjtayw9.mongodb.net/?retryWrites=true&w=majority")
    LOGCHANNEL = os.environ.get("LOGCHANNEL", "-1001985824630")  # Add channel id as -100 + Actual ID
    GDRIVE_FOLDER_ID = os.environ.get("GDRIVE_FOLDER_ID","root")
    USER_SESSION_STRING = os.environ.get("USER_SESSION_STRING", "AQAaiBkAEUNJQS3sxBH8CZHER2wO43NijOq9RZ2RByOsk45i_4_lYKntILiSb0G0wmYIcu2xLrxtIGTF7lqb_g22hhPpXVTBmY0PGV7gepVCN5KH_mbOeexNclEt-IQ0bS3L8mLFHEClAL-Di4cag4r4mT5l93GC3IuF9ngWtgG4J51u0rSKR_fnZu7xG4MsBnUhINNdy3_3DQEl6fhjWHxKZhB-hZr-339Cc9jN-9jeAtLd6aK_pHI64xOBGedRCJvqSCjzJGLQeowb_QzShjPdYtrOuFI2t0pG-FtuBbljaHyouMzEKaHYDCENUU-kkF75RqMSPKIKwwkamNzIRY8yynw6CwAAAABRsDH9AA")
    IS_PREMIUM = True
    MODES = ["video-video", "video-audio", "video-subtitle","extract-streams"]
