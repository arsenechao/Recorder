# ScoreSense｜影像前處理教學
# 檔案：preprocessing/preprocess.py
# 以下函式只處理資料；imshow、waitKey 與存檔由 main.py 負責。
# 來源與假設見 README.md。

# 本檔目前只有註解。需要自行輸入的匯入：
# import cv2
# from preprocessing.paper_detector import detect_paper
# from preprocessing.perspective import correct_perspective

# 函式簽章（請自行輸入）：
# def preprocess_image(image):
#
# 責任：串接紙張偵測與透視校正，統一回報結果，不重寫底層演算法。
# 輸入：原始 BGR uint8 圖片。
# 回傳字典（成功失敗的鍵都一致）：
#     ok：bool，只代表此程式完成擷取流程，不等於辨識正確率。
#     message：狀態說明。
#     corners：未排序的 (4,2) 角點；找不到時是 None。
#     scanned：拉正後彩圖；失敗時 None。
#     gray：拉正後灰階；失敗時 None。
#     debug：各階段圖片；失敗也保留前面已完成的階段。
# 目前只做到影像前處理，不呼叫任何外部辨識工具。
# 完成後檢查：用同一入口處理正常照片與無紙張照片；不能假造成功圖片。
#
# TODO 1：呼叫 detect_paper()，接收 corners、debug。
# TODO 2：先建立預設失敗的結果字典；scanned、gray 都設 None。
# TODO 3：若 corners 是 None，直接回傳此結果，不能繼續 warp。
# TODO 4：用原圖和角點呼叫 correct_perspective()。
#         角點無效產生 ValueError 時，保存原因並回傳失敗；不要無聲忽略。
# TODO 5：將拉正後的彩圖轉灰階；不要用找輪廓的二值遮罩當成最後成品。
# TODO 6：把 scanned、gray 加入 debug，分別使用 05_scanned、06_gray 這兩個鍵。
# TODO 7：填入成功狀態及圖片，回傳字典。仍不開視窗、不存檔。

# 【實作區】請依上方規格自行寫出函式，不要把 TODO 當成已完成。

