import streamlit as st

st.markdown("# 新サーバーへの移行のお知らせ")

st.image("/workspaces/harunica-stock-anl_transfer-streamlit-to-render/株データ分析_アイコン.png")

st.markdown("""
「株リウム（配当管理アプリ）」をご利用いただきありがとうございます。

ご利用者様の増加に伴い、サーバーの負荷が高まったため、新しいサーバーへ移行いたしました。
今後もさらなる機能の向上を目指してまいりますので、引き続きご利用をお楽しみください。

今後は、以下のURLよりアクセスをお願いいたします。
""")

st.link_button("株リウム（配当管理アプリ）", "https://kaburium.onrender.com")
