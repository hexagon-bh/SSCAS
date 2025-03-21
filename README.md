# 🚇 SSCAS

<div align="center">
  <img src="https://github.com/rkdgus0810/AI-PADS/assets/84117112/1f5b33d0-9bcc-4fe8-9bd6-dc321fe4c727" width="45%" alt="지하철 혼잡도 분석 시스템 이미지1">
  <img src="https://github.com/rkdgus0810/AI-PADS/assets/84117112/3f6d8c98-867d-4cfe-91b8-22a6a23741ec" width="45%" alt="지하철 혼잡도 분석 시스템 이미지2"> 
</div>

## 📹 작동 영상
[지하철 혼잡도 분석 시스템 작동 영상](https://youtu.be/0AYyNVzy4B8?si=hcutIGUzp9lQbuFH)

## 👥 팀 정보
- **팀명:** 업서요 ❌
- **팀원:**
  - 김강현 (AI & Web)
  - 조윤혁 (Engineering)
  - 박진우 (Leader)
  - 이승우 (Electronic)
  - 이동현 (Engineering)

## 🗓️ 프로젝트 기간
2023.10 ~ 2023.11

## 📄 보고서
[지하철 혼잡도 분석 시스템 제작 보고서](https://drive.google.com/file/d/1CG6QdgF31UuFq7VJwwACHVaHhqqa7FVJ/view?usp=drivesdk)

## 🏆 수상 내역
LG CNS AI Genius Academy 4등 (EGS 상)

---

## ✨ 프로젝트 요약 및 제작 계기

지하철 혼잡도를 분석하고 알림을 제공하는 웹 서비스입니다. **Roboflow**를 사용하여 사람을 학습시킨 이미지 분류 모델을 통해 지하철 내 사람들을 인식하고, 인식된 사람들의 위치와 차지하는 면적을 계산하여 혼잡도 수치를 산출합니다. 이러한 혼잡도 수치를 바탕으로 **Python의 Matplotlib** 라이브러리를 활용하여 히트맵을 제작, 사용자들에게 시각적인 혼잡도 정보를 제공합니다. 마지막으로, **Node.js의 Express** 라이브러리를 통해 웹 서비스 형태로 제공됩니다.

---

## 🛠️ 기술 스택 및 구현 내용

*   **AI 모델:** Roboflow를 활용한 이미지 분류 모델 (사람 인식)
*   **혼잡도 분석:** 이미지 분석을 통한 사람 위치 및 면적 계산 기반 혼잡도 수치화
*   **시각화:** Python Matplotlib 라이브러리를 이용한 히트맵 제작
*   **웹 서비스:** Node.js Express 라이브러리를 이용한 웹 서비스 구축

### 📊 데이터 수집 및 모델 학습

- **데이터 수집:** CCTV 영상 및 이미지 데이터 수집
- **데이터 전처리:** 이미지 크기 조정 및 노이즈 제거
- **모델 학습:** Roboflow를 활용한 이미지 분류 모델 학습

### 📈 웹 서비스 구현

- **프론트엔드:** 사용자 인터페이스 구현
- **백엔드:** Node.js Express를 활용한 API 구축
- **데이터베이스:** MongoDB를 활용한 데이터 저장 및 관리

---

## 🚀 기대 효과

*   **실시간 혼잡도 정보 제공:** 지하철 이용객들에게 실시간 혼잡도 정보를 제공하여 쾌적한 여행을 돕습니다.
*   **효율적인 지하철 운영:** 데이터 기반의 혼잡도 분석을 통해 효율적인 지하철 운영이 가능합니다.
*   **혼잡 시간대 피하기:** 혼잡 시간대를 피하여 지하철 이용이 더 편리해집니다.

---

## 📝 문제점 및 해결 방안

- **문제점:** 초기 모델의 정확도가 낮았던 문제
- **해결 방안:** 데이터셋의 다양성을 높이고, 모델의 하이퍼파라미터 조정을 통해 성능 개선

---

## 📚 참고 자료

- **Roboflow:** [https://roboflow.com/](https://roboflow.com/)
- **Python Matplotlib:** [https://matplotlib.org/](https://matplotlib.org/)
- **Node.js Express:** [https://expressjs.com/](https://expressjs.com/)

---

## 📝 느낀점 및 소감

- **프로젝트 진행 중:** 팀원들과의 협업을 통해 많은 것을 배웠습니다.
- **개선 방향:** 더 다양한 데이터를 수집하고, 모델의 성능을 높이는 방향으로 개선할 계획입니다.
