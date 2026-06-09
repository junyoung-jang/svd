## 목표: 
ARRAY나 MATRIX 등을 제외한 NUMPY 함수를 사용하지 않고 SVD 및 POD를 구현해서 IMAGE RECONSTRUCTION, 더 나아가 FLOW FIELD의 RECONSTRUCTION 구현

## 기간 
2026.05.18 - Present

## 구현 방식

Power Method와 Hoteling Deflation을 사용하여 $${A^TA}$$의 Eigenvalues와 Eigenvectors를 임의의 N차 모드 까지 계산

 - Power Method:  
   $${n \times n}$$ matrix의 가장 큰 eigenvalues를 구하는 수치해석 기법
   임의의 벡터 $${e_0}$$가 행렬 $${A}$$의 고유벡터로 이루어졌다 가정하면  
   $$e_0 = c_1 v_1 + c_2 v_2 + \dots + c_n v_n$$

   이 때 eigenvector 성질을 이용하여 행렬을 계속 곱할경우 가장 큰 eigenvalue만 남음

- Hoteling Deflation:
  1) Symmetric Matrix의 가장 큰 eigenvalue와 eigenvector의 영향을 제외하여 새로운 벡터를 만드는 기법
  이를 통해 n개의 eigenvalue를 만들고자 함

  2) 임의의 행렬 $${A}$$ $${(m \times n )}$$ 이 있다 할때 행렬 $${B}$$ = $${A^TA}$$을 가정하자
  4) 행렬의 matrix transpose 성질에 의해 $$B^T = ({A^TA})^T = A^TA  $$ 이므로 SVD 구현시 Hoteling Deflation 방식은 사용가능한 방식이기 때문에 해당 방법을 통해 진행 예정
  
   
## 진행 상황
- 1단계 : 행렬곱 구현 (**CLEAR**)
- 2단계 : POWER METHOD 구현 (**CLEAR**)
- 3단계 : HOTELING DEFLATION 구현 (NOT YET)
- 4단계 : 임의의 이미지로 시험 (NOT YET)
- 5단계 : 임의의 유동장으로 시험 (NOT YET)
