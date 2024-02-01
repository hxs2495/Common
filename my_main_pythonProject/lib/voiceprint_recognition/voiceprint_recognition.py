# # import argparse
# # import functools
#
# from voiceprint_recognition.mvector.predict import MVectorPredictor
# from voiceprint_recognition.mvector.utils.record import RecordAudio
# # from voiceprint_recognition.mvector.utils.utils import add_arguments, print_arguments
#
# # 获取识别器
# predictor = MVectorPredictor(configs='voiceprint_recognition/configs/ecapa_tdnn.yml',
#                              threshold=0.45,
#                              audio_db_path='voiceprint_recognition/audio_db/',
#                              model_path='voiceprint_recognition/EcapaTdnn_Fbank/best_model/',
#                              use_gpu=False)
#
# record_audio = RecordAudio()
# record_seconds = 3
# register_seconds = 5
#
#
# def vr():
#     input(f"按下回车键开机录音，录音{record_seconds}秒中：")
#     audio_data = record_audio.record(record_seconds=record_seconds)
#     name = predictor.recognition(audio_data, sample_rate=record_audio.sample_rate)
#     if name:
#         print(f"识别说话的为：{name}")
#         return True
#     else:
#         print(f"没有识别到说话人，可能是没注册。")
#         return False
#
#
# def Register():
#     input(f"按下回车键开机录音，录音{register_seconds}秒中：")
#     audio_data = record_audio.record(record_seconds=register_seconds)
#     name = input("请输入该音频用户的名称：")
#     if name != '':
#         predictor.register(user_name=name, audio_data=audio_data, sample_rate=record_audio.sample_rate)
#
#
# def Delete():
#     name = input("请输入该音频用户的名称：")
#     if name != '':
#         predictor.remove_user(user_name=name)
