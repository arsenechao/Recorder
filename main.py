# ScoreSense｜目前的入口：只執行影像前處理
#
# 目前輸入：samples/test6.jpg，由你自己放入真正的桌面紙張照片。
# 目前輸出：output/run_時間/，內含 debug/、scanned.png、gray.png。
# 只有各功能完成後，才使用完整 preprocess_image() 入口。
# 開發期間直接呼叫當下完成的函式並 imshow；不要另外建立重複的功能檔。
#
# 匯入規劃：cv2、pathlib.Path、datetime.datetime，以及 preprocess_image。
# 讀圖／存檔先用講義已有的 imread、imwrite，建議將專案放在英文路徑。
#
# TODO 1：由 Path(__file__).resolve().parent 取得專案根目錄。
# TODO 2：輸入路徑固定為根目錄 / samples / test6.jpg；讀不到要明確報錯。
# TODO 3：呼叫 preprocess_image(image)，印出 ok、message、corners。
# TODO 4：建立本次獨立輸出目錄，避免舊成功圖片被誤認為新結果。
#         datetime.now().strftime() 可產生時間標籤，%f 是微秒。
# TODO 5：把 debug.items() 的圖片各自存檔，檢查 imwrite 的布林回傳值。
# TODO 6：只有 ok 為 True 才寫 scanned.png 和 gray.png；不要覆寫來源圖片。
# TODO 7：用一個可縮放視窗依序顯示原圖和各階段；每按一鍵才進下一張。
#         Esc 可以提早停止顯示。顯示結束一定要 destroyAllWindows。
# TODO 8：放一個 SHOW_STEPS 開關；False 時只處理／存檔，不開視窗。
#
# 課堂檢查點 A：只完成 create_paper_mask 時，暫時匯入它，顯示 gray、binary。
# 課堂檢查點 B：find_outer_contours 完成後，印 len，在 image.copy() 畫全部輪廓。
# 課堂檢查點 C：detect_paper 完成後，只呼叫它，逐張顯示 debug。
# 課堂檢查點 D：先用四組手動座標測 correct_perspective，再接自動 corners。
# 課堂檢查點 E：以上都正確後，移除暫時串接，改回完整 preprocess_image。
# 這些測試碼可在 main.py 暫時替換；功能函式仍留在原本正式檔案。

# 【實作區】逐項完成；在功能尚未完成時，先使用上方的課堂檢查點。
