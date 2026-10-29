# ScoreSense｜影像前處理教學
# 檔案：preprocessing/perspective.py
# 以下函式只處理資料；imshow、waitKey 與存檔由 main.py 負責。
# 來源與假設見 README.md。

# 本檔目前只有註解。需要自行輸入的匯入：
# import cv2
# import numpy as np

# 函式簽章（請自行輸入）：
# def order_points(corners):
#
# 責任：將四個角點排成 TL 左上、TR 右上、BR 右下、BL 左下。
# 輸入：shape (4, 2) 的四個不同角點；順序任意。
# 回傳：shape (4, 2)、dtype float32 的已排序角點，不修改輸入。
# 本版方法：先按 y 找較上面兩點與較下面兩點，再分別按 x 分左右。
# 重要假設：紙張大致正立，上面兩角真的都比下面兩角靠上。
# 這不是任意角度排序器；橫倒、菱形或嚴重透視先重拍，不加入進階方法。
# 完成後檢查：印出順序或在原圖標 TL/TR/BR/BL；不能只看函式有回傳。
#
# TODO 1：用 np.asarray() 轉 float32，檢查形狀恰好是 (4, 2)。
# TODO 2：確認四點是有限數值且彼此不同；無效時 raise ValueError。
# TODO 3：用 points[:, 1] 取得所有 y，再用 np.argsort() 得到排序索引。
# TODO 4：依索引排序整列座標；前兩列是上方，後兩列是下方。
# TODO 5：分別依 x 排序上下兩組，取得 tl、tr、bl、br。
# TODO 6：按 tl、tr、br、bl 建立新的 float32 陣列；注意下方順序反過來。
# TODO 7：確認排序後仍是有面積的凸四邊形，否則報錯；成功則回傳。

# 【實作區】請依上方規格自行寫出函式，不要把 TODO 當成已完成。


# ====================================================================

# 函式簽章（請自行輸入）：
# def calculate_output_size(ordered_points):
#
# 責任：用四條邊的像素距離，估計透視輸出畫布的寬高。
# 輸入：已經是 TL、TR、BR、BL 順序的 (4, 2) float32 角點。
# 回傳：width, height，兩個至少為 2 的 Python 整數。
# 規則：寬取上下邊較長者，高取左右邊較長者；向上取整再加 1。
# 注意：這是簡單的取樣尺寸估計，不是恢復紙張真實長寬比、毫米尺寸或 DPI。
# 不負責：排序點、改變圖片、產生視窗。
# 完成後檢查：矩形 (10,20) 到 (109,219) 應得到 100×200。
#
# TODO 1：依順序拆出 tl、tr、br、bl。
# TODO 2：使用 np.linalg.norm() 計算上邊與下邊的兩點距離。
# TODO 3：同樣計算左邊與右邊距離。
# TODO 4：寬、高各取兩條對邊較長的距離，用 np.ceil() 向上取整。
# TODO 5：距離代表端點座標差，加 1 作為此範例的包含兩端像素數約定。
# TODO 6：轉成 int，最小設定為 2，回傳寬在前、高在後。

# 【實作區】請依上方規格自行寫出函式，不要把 TODO 當成已完成。


# ====================================================================

# 函式簽章（請自行輸入）：
# def correct_perspective(image, corners):
#
# 責任：用原圖與四個紙張角點產生拉正後的彩色紙張。
# 輸入：非空的 BGR uint8 原圖；corners 為原圖座標中的四點。
# 回傳：scanned，(輸出高, 輸出寬, 3) 的 uint8 BGR 圖片。
# 不修改來源，不使用二值化或已畫框圖片當作最後輸入。
# 完成後檢查：紙張方向、四邊、完整內容與細小附點都要看，不只看有無圖片。
#
# TODO 1：確認原圖非空且為 BGR uint8；呼叫 order_points() 排序。
# TODO 2：確認每個角點都在原圖的寬高範圍內。
# TODO 3：呼叫 calculate_output_size() 取得 width, height。
# TODO 4：用 float32 建立目標矩形四角，順序也必須是 TL、TR、BR、BL。
#         右邊座標是 width-1，下面座標是 height-1。
# TODO 5：呼叫 getPerspectiveTransform()；它只算 3×3 矩陣，不改圖片。
# TODO 6：呼叫 warpPerspective() 作用在原始 image；尺寸順序是 (寬, 高)。
#         使用 INTER_LINEAR，空白位置使用 BGR 白色 (255,255,255)。
# TODO 7：回傳 scanned；顯示與儲存仍放 main.py。

# 【實作區】請依上方規格自行寫出函式，不要把 TODO 當成已完成。

