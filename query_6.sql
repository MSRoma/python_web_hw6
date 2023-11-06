SELECT groups_name , fullname
FROM groups as gr
LEFT JOIN students as st ON gr.id = st.groups_id
