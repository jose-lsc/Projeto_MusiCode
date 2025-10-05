```mermaid

---
config:
  theme: mc
  look: handDrawn
---
flowchart TD
    A(["AFN"]) --> D["AFD (Decimal ou Inteiro)<br>Q0"] & C["AFD (Identificadores)<br>Q0"] & n10["AFD(palavra_chave_instrumento)<br>Q0"] & n31@{ label: "AFD(palavra_chave_nota)<br style=\"--tw-scale-x:\">Q0" } & n32@{ label: "AFD(palavra_chave_play)<br style=\"--tw-scale-x:\">Q0" } & n33@{ label: "AFD(palavra_chave_repetir)<br style=\"--tw-scale-x:\">Q0" } & n34@{ label: "AFD(palavra_chave_stop)<br style=\"--tw-scale-x:\">Q0" } & n35@{ label: "AFD(palavra_chave_ponto_virgula)<br style=\"--tw-scale-x:\">Q0" } & n67@{ label: "AFD(palavra_chave_Strings)<br style=\"--tw-scale-x:\">Q0" }
    D --> n6["AFD(Decimal ou Inteiro)<br>Q1"]
    n6 --> n7["AFD(Inteiro)<br>Q1 (loop)"] & n8["AFD(Decimal)<br>Q2"]
    n8 --> n9["AFD(Decimal)<br>Q3"]
    C --> n11@{ label: "AFD (Identificadores)<br style=\"--tw-scale-x:\">Q1" }
    n10 --> n12@{ label: "AFD(palavra_chave_instrumento)<br style=\"--tw-scale-x:\">Q1" }
    n12 --> n13@{ label: "AFD(palavra_chave_instrumento)<br style=\"--tw-scale-x:\">Q2" }
    n13 --> n14@{ label: "AFD(palavra_chave_instrumento)<br style=\"--tw-scale-x:\">Q3" }
    n14 --> n15@{ label: "AFD(palavra_chave_instrumento)<br style=\"--tw-scale-x:\">Q4" }
    n15 --> n16@{ label: "AFD(palavra_chave_instrumento)<br style=\"--tw-scale-x:\">Q5" }
    n16 --> n17@{ label: "AFD(palavra_chave_instrumento)<br style=\"--tw-scale-x:\">Q6" }
    n17 --> n18@{ label: "AFD(palavra_chave_instrumento)<br style=\"--tw-scale-x:\">Q7" }
    n18 --> n19@{ label: "AFD(palavra_chave_instrumento)<br style=\"--tw-scale-x:\">Q8" }
    n19 --> n20@{ label: "AFD(palavra_chave_instrumento)<br style=\"--tw-scale-x:\">Q9" }
    n20 --> n21@{ label: "AFD(palavra_chave_instrumento)<br style=\"--tw-scale-x:\">Q10" }
    n21 --> n22@{ label: "AFD(palavra_chave_instrumento)<br style=\"--tw-scale-x:\">Q11" }
    n22 --> n23@{ label: "AFD(palavra_chave_instrumento)<br style=\"--tw-scale-x:\">Q12" }
    n23 --> n24@{ label: "AFD(palavra_chave_instrumento)<br style=\"--tw-scale-x:\">Q13" }
    n24 --> n25@{ label: "AFD(palavra_chave_instrumento)<br style=\"--tw-scale-x:\">Q14" }
    n25 --> n26@{ label: "AFD(palavra_chave_instrumento)<br style=\"--tw-scale-x:\">Q15" }
    n26 --> n27@{ label: "AFD(palavra_chave_instrumento)<br style=\"--tw-scale-x:\">Q16" }
    n27 --> n28@{ label: "AFD(palavra_chave_instrumento)<br style=\"--tw-scale-x:\">Q17" }
    n28 --> n29@{ label: "AFD(palavra_chave_instrumento)<br style=\"--tw-scale-x:\">Q18" }
    n29 --> n30@{ label: "AFD(palavra_chave_instrumento)<br style=\"--tw-scale-x:\">Q19" }
    n31 --> n36@{ label: "AFD(palavra_chave_nota)<br style=\"--tw-scale-x:\">Q1" }
    n36 --> n37@{ label: "AFD(palavra_chave_nota)<br style=\"--tw-scale-x:\">Q2" }
    n37 --> n38@{ label: "AFD(palavra_chave_nota)<br style=\"--tw-scale-x:\">Q3" }
    n38 --> n39@{ label: "AFD(palavra_chave_nota)<br style=\"--tw-scale-x:\">Q4" }
    n39 --> n40@{ label: "AFD(palavra_chave_nota)<br style=\"--tw-scale-x:\">Q5" }
    n40 --> n41@{ label: "AFD(palavra_chave_nota)<br style=\"--tw-scale-x:\">Q6" }
    n41 --> n42@{ label: "AFD(palavra_chave_nota)<br style=\"--tw-scale-x:\">Q7" }
    n42 --> n43@{ label: "AFD(palavra_chave_nota)<br style=\"--tw-scale-x:\">Q8" }
    n43 --> n44@{ label: "AFD(palavra_chave_nota)<br style=\"--tw-scale-x:\">Q9" }
    n32 --> n45@{ label: "AFD(palavra_chave_play)<br style=\"--tw-scale-x:\">Q1" }
    n45 --> n46@{ label: "AFD(palavra_chave_play)<br style=\"--tw-scale-x:\">Q2" }
    n46 --> n47@{ label: "AFD(palavra_chave_play)<br style=\"--tw-scale-x:\">Q3" }
    n47 --> n48@{ label: "AFD(palavra_chave_play)<br style=\"--tw-scale-x:\">Q4" }
    n48 --> n49@{ label: "AFD(palavra_chave_play)<br style=\"--tw-scale-x:\">Q5" }
    n49 --> n50@{ label: "AFD(palavra_chave_play)<br style=\"--tw-scale-x:\">Q6" }
    n33 --> n51@{ label: "AFD(palavra_chave_repetir)<br style=\"--tw-scale-x:\">Q1" }
    n51 --> n52@{ label: "AFD(palavra_chave_repetir)<br style=\"--tw-scale-x:\">Q2" }
    n52 --> n53@{ label: "AFD(palavra_chave_repetir)<br style=\"--tw-scale-x:\">Q3" }
    n53 --> n54@{ label: "AFD(palavra_chave_repetir)<br style=\"--tw-scale-x:\">Q4" }
    n54 --> n55@{ label: "AFD(palavra_chave_repetir)<br style=\"--tw-scale-x:\">Q5" }
    n55 --> n56@{ label: "AFD(palavra_chave_repetir)<br style=\"--tw-scale-x:\">Q6" }
    n56 --> n57@{ label: "AFD(palavra_chave_repetir)<br style=\"--tw-scale-x:\">Q7" }
    n57 --> n58@{ label: "AFD(palavra_chave_repetir)<br style=\"--tw-scale-x:\">Q8" }
    n58 --> n59@{ label: "AFD(palavra_chave_repetir)<br style=\"--tw-scale-x:\">Q9" }
    n34 --> n60@{ label: "AFD(palavra_chave_stop)<br style=\"--tw-scale-x:\">Q1" }
    n60 --> n61@{ label: "AFD(palavra_chave_stop)<br style=\"--tw-scale-x:\">Q2" }
    n61 --> n62@{ label: "AFD(palavra_chave_stop)<br style=\"--tw-scale-x:\">Q3" }
    n62 --> n63@{ label: "AFD(palavra_chave_stop)<br style=\"--tw-scale-x:\">Q4" }
    n63 --> n64@{ label: "AFD(palavra_chave_stop)<br style=\"--tw-scale-x:\">Q5" }
    n64 --> n65@{ label: "AFD(palavra_chave_stop)<br style=\"--tw-scale-x:\">Q6" }
    n35 --> n66@{ label: "AFD(palavra_chave_ponto_virgula)<br style=\"--tw-scale-x:\">Q1" }
    n67 --> n68@{ label: "AFD(palavra_chave_Strings)<br style=\"--tw-scale-x:\">Q1" }
    n68 --> n69@{ label: "AFD(palavra_chave_Strings)<br style=\"--tw-scale-x:\">Q2" }
    n2["Anchor"]
    n5["Anchor"]
    n31@{ shape: rect}
    n32@{ shape: rect}
    n33@{ shape: rect}
    n34@{ shape: rect}
    n35@{ shape: rect}
    n67@{ shape: rect}
    n11@{ shape: rect}
    n12@{ shape: rect}
    n13@{ shape: rect}
    n14@{ shape: rect}
    n15@{ shape: rect}
    n16@{ shape: rect}
    n17@{ shape: rect}
    n18@{ shape: rect}
    n19@{ shape: rect}
    n20@{ shape: rect}
    n21@{ shape: rect}
    n22@{ shape: rect}
    n23@{ shape: rect}
    n24@{ shape: rect}
    n25@{ shape: rect}
    n26@{ shape: rect}
    n27@{ shape: rect}
    n28@{ shape: rect}
    n29@{ shape: rect}
    n30@{ shape: rect}
    n36@{ shape: rect}
    n37@{ shape: rect}
    n38@{ shape: rect}
    n39@{ shape: rect}
    n40@{ shape: rect}
    n41@{ shape: rect}
    n42@{ shape: rect}
    n43@{ shape: rect}
    n44@{ shape: rect}
    n45@{ shape: rect}
    n46@{ shape: rect}
    n47@{ shape: rect}
    n48@{ shape: rect}
    n49@{ shape: rect}
    n50@{ shape: rect}
    n51@{ shape: rect}
    n52@{ shape: rect}
    n53@{ shape: rect}
    n54@{ shape: rect}
    n55@{ shape: rect}
    n56@{ shape: rect}
    n57@{ shape: rect}
    n58@{ shape: rect}
    n59@{ shape: rect}
    n60@{ shape: rect}
    n61@{ shape: rect}
    n62@{ shape: rect}
    n63@{ shape: rect}
    n64@{ shape: rect}
    n65@{ shape: rect}
    n66@{ shape: rect}
    n68@{ shape: rect}
    n69@{ shape: rect}
    n2@{ shape: anchor}
    n5@{ shape: anchor}
