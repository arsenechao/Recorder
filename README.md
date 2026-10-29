# ScoreSense｜學生註解框架：紙張擷取與透視校正

**這份是待完成的作業框架，不是可以直接執行的答案。**
所有 `.py` 檔案目前只有 `#` 註解；連函式簽章也以註解提供。
請自行輸入 `import`、`def` 與函式內容，不是將整份檔案取消註解。

每個函式都列有責任、輸入、回傳值、TODO、與完成後的檢查點。
`requirements.txt`、`.gitignore` 是可直接使用的環境／設定檔，不是影像處理答案。
老師會依序解鎖各功能；不要在函式未完成時直接執行整個流程。

## 範圍與拍照條件

只處理單張平整的白色樂譜紙：桌面較暗、背景簡單、四角完整，四周留出桌面。
紙張大致正立，不橫倒；上面兩角都應比下面兩角更靠上。

這是「在限定場景中找一個紙張四邊形」，不是判定真實物件是否為 A4，也沒有量測毫米或 DPI。
本版只使用灰階、Otsu、外輪廓、面積、周長、多邊形近似、四角排序與透視轉換。
沒有另外加入 Canny 雙路線、Hough、CLAHE、手動點角、深度學習或後續辨識功能。

## 固定架構

```text
ScoreSense/
├── main.py
├── requirements.txt
├── README.md
├── .gitignore
├── preprocessing/
│   ├── __init__.py
│   ├── paper_detector.py
│   ├── perspective.py
│   └── preprocess.py
├── samples/
│   ├── README.md
│   └── test6.jpg              ← 自行放入，壓縮包沒有照片
└── output/
    ├── .gitkeep
    └── run_執行時間/           ← 每次執行才產生
        ├── debug/
        ├── scanned.png        ← 只有成功才有
        └── gray.png           ← 只有成功才有
```

本階段沒有 `omr/`、`music/`、`web/` 或 `pipeline.py`。資料夾位置是正式位置，之後可以新增功能，不必搬動這些檔案。

## 八個功能與回傳約定

| 檔案 | 函式 | 回傳 |
| --- | --- | --- |
| paper_detector.py | create_paper_mask(image) | gray, binary |
| paper_detector.py | find_outer_contours(binary) | contours |
| paper_detector.py | approximate_paper_polygon(contour) | (4,2) float32 角點，或 None |
| paper_detector.py | detect_paper(image) | corners, debug |
| perspective.py | order_points(corners) | TL、TR、BR、BL 四點 |
| perspective.py | calculate_output_size(ordered_points) | width, height |
| perspective.py | correct_perspective(image, corners) | scanned 彩圖 |
| preprocess.py | preprocess_image(image) | 結果字典 |

`preprocess_image()` 的結果鍵固定為 `ok`、`message`、`corners`、`scanned`、`gray`、`debug`。
找不到紙張時 `ok=False`，`scanned` 與 `gray` 為 `None`，但 `debug` 仍有中間結果。
`corners` 保留偵測順序；只有 `order_points()` 的回傳保證指定順序。

`debug` 的名稱固定：`01_gray`、`02_binary`、`03_contours`、`04_paper_corners`。
成功校正後再加入 `05_scanned`、`06_gray`。請勿在其他檔案自行換鍵名。

## 環境

使用 Python 3.11 和桌面版 OpenCV。若課程環境已符合 requirements，直接沿用；不用重新學 Git 或重建 repository。

在新專案需要環境時，Windows 可在專案根目錄執行：

```powershell
py -3.11 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

macOS／Linux 已安裝 Python 3.11 時：

```bash
python3.11 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
```

套件版本沿用課程的教學組合，不代表最新版本。`opencv-python` 與 `opencv-python-headless` 不要混裝；後者沒有本課需要的桌面視窗功能。參見文末來源。
建議專案完整路徑使用英文字母，減少部分 Windows OpenCV 建置的中文路徑讀寫問題。

## 圖片與資料流

```text
main.py 讀圖
    ↓
preprocess_image()
    ├─ detect_paper()
    │    ├─ create_paper_mask()
    │    ├─ find_outer_contours()
    │    └─ approximate_paper_polygon()
    └─ correct_perspective()
         ├─ order_points()
         └─ calculate_output_size()
    ↓
返回圖片、狀態與 debug
    ↓
main.py 顯示／存檔
```

二值圖只用來尋找邊界；透視變換使用沒有畫框的原始彩圖。不要把黑白遮罩或紅框一起拉進成品。
四角排序採本課的簡單上下分組法，並非任意旋轉的通用排序。
輸出尺寸取投影邊長的較大值，是取樣尺度估計，不保證復原真實 A4 長寬比。

## 實作順序與檢查點

| 步驟 | 完成內容 | 在 main.py 檢查 |
| --- | --- | --- |
| 1 | create_paper_mask | 顯示原圖、灰階、二值圖；紙張應是白前景 |
| 2 | find_outer_contours | 印出數量並把所有輪廓畫在原圖副本 |
| 3 | approximate_paper_polygon | 對一個輪廓取得四點，或明確得到 None |
| 4 | detect_paper | 顯示選中的外框與四角；確認不是桌面框線 |
| 5 | order_points | 印出或標記 TL、TR、BR、BL |
| 6 | calculate_output_size | 印出正整數寬高；不要把寬高寫反 |
| 7 | correct_perspective | 先測手動四點，再接自動四點 |
| 8 | preprocess_image | 成功、無紙張兩種照片都能回報正確狀態 |
| 9 | main.py | 統一顯示及保存結果，移除前面的暫時串接 |

每完成一個函式，只更換 `main.py` 的課堂驗收區；已完成的功能留在正式檔案，不必搬移或重寫。

## 限制與驗收

先用正常光線、單張白紙與深色桌面。無法找出時先看二值圖、面積門檻與頂點數，不急著加入更多濾鏡。
15% 面積與周長 2% 的 epsilon 都是本版教學設定，不是所有照片的最佳值。
最大凸四邊形仍可能不是紙張；一定要看四角標記與成品是否保留五線、附點、符桿及頁邊資訊。
`ok=True` 表示程式完成幾何流程，不代表音符辨識正確或物件確實為 A4。

## 參考基礎與補充來源

- 原課程第 7 章：<https://felix-0901.github.io/ScoreSense/#lesson/07/>
- 原始 Markdown（輪廓、面積、透視範例）：<https://github.com/Felix-0901/ScoreSense/blob/main/course/content/07_%E5%82%BE%E6%96%9C%E5%81%B5%E6%B8%AC%E8%88%87%E6%97%8B%E8%BD%89%E6%A0%A1%E6%AD%A3.md>
- 本次新增：周長、多邊形近似、凸性、候選選擇與簡單四角排序。
- OpenCV 輪廓特徵：<https://docs.opencv.org/4.11.0/dd/d49/tutorial_py_contour_features.html>
- OpenCV 幾何轉換：<https://docs.opencv.org/4.x/da/d6e/tutorial_py_geometric_transformations.html>
- NumPy argsort：<https://numpy.org/doc/1.26/reference/generated/numpy.argsort.html>
- OpenCV 套件與桌面視窗：<https://pypi.org/project/opencv-python/4.8.1.78/>
