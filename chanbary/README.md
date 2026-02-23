<div align="center">
  
# 🏥 Brain Stroke CT Analysis
### Deep Neural Network for Medical Image Diagnostics

[![Python](https://img.shields.io/badge/Python-3.13+-red.svg?style=for-the-badge&logo=python)](https://www.python.org/)
[![Kaggle](https://img.shields.io/badge/Dataset-Brain_Stroke_CT-20BEFF.svg?style=for-the-badge&logo=kaggle)](https://www.kaggle.com/datasets/ozguraslank/brain-stroke-ct-dataset)
[![Status](https://img.shields.io/badge/Status-Clinical_Research-blue.svg?style=for-the-badge)]()
[![License](https://img.shields.io/badge/License-MIT-purple.svg?style=for-the-badge)]()

</div>

<section style="
    padding: 40px 20px;
    background: linear-gradient(135deg, #0a1928 0%, #1a2f3f 100%);
    border-radius: 30px;
    margin: 30px 0;
    border: 2px solid #ff6b6b;
    box-shadow: 0 20px 40px rgba(0,0,0,0.5), 0 0 30px rgba(255,107,107,0.2);
    position: relative;
    overflow: hidden;">

  <!-- عناصر پس‌زمینه سیتی اسکن -->
  <div style="
      position: absolute;
      top: 0;
      left: 0;
      right: 0;
      bottom: 0;
      background-image: radial-gradient(circle at 30% 50%, rgba(255,107,107,0.1) 0%, transparent 25%),
                        radial-gradient(circle at 70% 30%, rgba(78,205,196,0.1) 0%, transparent 30%),
                        repeating-linear-gradient(45deg, rgba(255,255,255,0.02) 0px, rgba(255,255,255,0.02) 2px, transparent 2px, transparent 8px);
      pointer-events: none;">
  </div>

  <div style="
      max-width: 900px;
      margin: 0 auto;
      position: relative;
      z-index: 2;">
    <!-- هدر با تصاویر سیتی اسکن -->
    <div style="
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 20px;
        margin-bottom: 30px;
        flex-wrap: wrap;">  
    <div style="
          width: 80px;
          height: 80px;
          background: #1e3b4a;
          border-radius: 50%;
          display: flex;
          align-items: center;
          justify-content: center;
          border: 3px solid #ff6b6b;
          box-shadow: 0 0 20px #ff6b6b;">
        <span style="font-size: 40px;">🧠</span>
      </div>   
      <div style="
          background: rgba(0,0,0,0.4);
          padding: 15px 30px;
          border-radius: 50px;
          backdrop-filter: blur(10px);
          border: 1px solid #ff6b6b;">
        <span style="color: #ff6b6b; font-weight: bold; font-size: 18px;">🩻 CLINICAL DATASET</span>
      </div>
      <div style="
          width: 80px;
          height: 80px;
          background: #1e3b4a;
          border-radius: 50%;
          display: flex;
          align-items: center;
          justify-content: center;
          border: 3px solid #4ecdc4;
          box-shadow: 0 0 20px #4ecdc4;">
        <span style="font-size: 40px;">🩻</span>
      </div>
    </div>
    <!-- عنوان اصلی با افکت پزشکی -->
    <h1 style="
        font-size: 48px;
        font-weight: 900;
        margin: 20px 0;
        background: linear-gradient(135deg, #ff6b6b, #4ecdc4, #ff6b6b);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-shadow: 0 0 30px rgba(255,107,107,0.3);
        letter-spacing: -1px;
        line-height: 1.2;">
      Deep Gradient Analysis<br>in CT Brain Scans
    </h1>
    <!-- بخش دیتاست با هایلایت ویژه -->
    <div style="
        background: rgba(30, 59, 74, 0.7);
        backdrop-filter: blur(10px);
        border-radius: 20px;
        padding: 25px;
        margin: 30px 0;
        border-left: 8px solid #ff6b6b;
        border-right: 8px solid #4ecdc4;
        box-shadow: 0 10px 30px rgba(0,0,0,0.5);">
      <div style="display: flex; align-items: center; gap: 15px; flex-wrap: wrap; justify-content: center;">
        <img src="https://img.icons8.com/fluency/96/medical-doctor.png" width="50" style="border-radius: 10px;"/>
        <div>
          <h3 style="color: #ff6b6b; margin: 0; font-size: 24px;">📊 Kaggle Dataset Integration</h3>
          <p style="color: #fff; font-size: 18px; margin: 10px 0 0;">
            <strong style="color: #4ecdc4;">Brain Stroke CT Dataset</strong> by ozguraslank
          </p>
          <p style="color: #aaa; font-size: 14px; margin: 5px 0 0;">
            🔬 1,500+ CT Scans | 🏥 3 Clinical Classes | 📈 Real-world Medical Data
          </p>
        </div>
      </div>
      <!-- لینک دیتاست با افکت -->
      <div style="margin-top: 20px;">
        <a href="https://www.kaggle.com/datasets/ozguraslank/brain-stroke-ct-dataset" 
           style="
              display: inline-block;
              background: linear-gradient(90deg, #ff6b6b, #4ecdc4);
              color: white;
              padding: 12px 30px;
              border-radius: 30px;
              text-decoration: none;
              font-weight: bold;
              font-size: 16px;
              box-shadow: 0 5px 20px rgba(255,107,107,0.4);
              transition: transform 0.3s;">
          🔗 ACCESS DATASET ON KAGGLE →
        </a>
      </div>
    </div>
    <!-- نمایش نمونه سیتی اسکن (شبیه‌سازی شده با CSS) -->
    <div style="
        display: flex;
        gap: 15px;
        justify-content: center;
        margin: 40px 0;
        flex-wrap: wrap;">
      <div style="
          width: 150px;
          height: 150px;
          background: linear-gradient(145deg, #2c4a5e, #1a2f3f);
          border-radius: 20px;
          border: 3px solid #ff6b6b;
          position: relative;
          overflow: hidden;">
        <div style="
            position: absolute;
            top: 20px;
            left: 20px;
            right: 20px;
            bottom: 20px;
            border: 2px solid #4ecdc4;
            border-radius: 10px;
            opacity: 0.5;"></div>
        <div style="
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            width: 60px;
            height: 60px;
            background: rgba(78,205,196,0.2);
            border-radius: 50%;
            border: 2px dashed #ff6b6b;"></div>
        <div style="position: absolute; bottom: 5px; right: 5px; color: #ff6b6b; font-size: 10px;">STROKE+</div>
      </div>
      <div style="
          width: 150px;
          height: 150px;
          background: linear-gradient(145deg, #2c4a5e, #1a2f3f);
          border-radius: 20px;
          border: 3px solid #4ecdc4;
          position: relative;
          overflow: hidden;">
        <div style="
            position: absolute;
            top: 20px;
            left: 20px;
            right: 20px;
            bottom: 20px;
            border: 2px solid #ff6b6b;
            border-radius: 10px;
            opacity: 0.5;"></div>
        <div style="
            position: absolute;
            top: 30%;
            left: 30%;
            width: 40px;
            height: 40px;
            background: rgba(255,107,107,0.2);
            border-radius: 5px;"></div>
        <div style="position: absolute; bottom: 5px; right: 5px; color: #4ecdc4; font-size: 10px;">NORMAL</div>
     </div>    
      <div style="
          width: 150px;
          height: 150px;
          background: linear-gradient(145deg, #2c4a5e, #1a2f3f);
          border-radius: 20px;
          border: 3px solid #ffd93d;
          position: relative;
          overflow: hidden;">
        <div style="
            position: absolute;
            top: 10px;
            left: 10px;
            right: 10px;
            bottom: 10px;
            background: radial-gradient(circle at 30% 40%, rgba(255,217,61,0.1) 0%, transparent 50%);"></div>
        <div style="position: absolute; bottom: 5px; right: 5px; color: #ffd93d; font-size: 10px;">HEMORRHAGE</div>
      </div>
    </div>
    <!-- آمار و ارقام پیشرفت -->
    <div style="
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
        gap: 20px;
        margin: 40px 0;">
      <div style="
          background: rgba(0,0,0,0.3);
          backdrop-filter: blur(5px);
          padding: 20px;
          border-radius: 15px;
          border: 1px solid #ff6b6b;">
        <div style="font-size: 30px;">🧮</div>
        <div style="font-size: 28px; font-weight: bold; color: #ff6b6b;">150,528</div>
        <div style="color: #aaa;">Input Features (224x224x3)</div>
      </div>
      <div style="
          background: rgba(0,0,0,0.3);
          backdrop-filter: blur(5px);
          padding: 20px;
          border-radius: 15px;
          border: 1px solid #4ecdc4;">
        <div style="font-size: 30px;">📊</div>
        <div style="font-size: 28px; font-weight: bold; color: #4ecdc4;">13-Layer</div>
        <div style="color: #aaa;">Deep MLP Architecture</div>
      </div>
      <div style="
          background: rgba(0,0,0,0.3);
          backdrop-filter: blur(5px);
          padding: 20px;
          border-radius: 15px;
          border: 1px solid #ffd93d;">
        <div style="font-size: 30px;">⚡</div>
        <div style="font-size: 28px; font-weight: bold; color: #ffd93d;">3-Class</div>
        <div style="color: #aaa;">Stroke Classification</div>
      </div>
    </div>
    <!-- وضعیت تحقیقات -->
    <div style="
        background: rgba(255,107,107,0.1);
        padding: 20px;
        border-radius: 15px;
        border: 2px dashed #ff6b6b;
        margin-top: 30px;">
      <p style="color: #fff; font-size: 18px; margin: 0;">
        🔬 <strong>Clinical Research Progress:</strong> Implementing gradient flow analysis on real CT scans 
        to detect vanishing/exploding gradients in deep medical imaging networks
      </p>
    </div>
    <!-- تکنولوژی‌های استفاده شده -->
    <div style="
        margin-top: 30px;
        display: flex;
        gap: 10px;
        justify-content: center;
        flex-wrap: wrap;">
      <span style="background: #ff6b6b; padding: 5px 15px; border-radius: 20px; font-size: 14px; color: white;">🧬 NumPy From Scratch</span>
      <span style="background: #4ecdc4; padding: 5px 15px; border-radius: 20px; font-size: 14px; color: #1a2f3f;">📈 Gradient Analysis</span>
      <span style="background: #ffd93d; padding: 5px 15px; border-radius: 20px; font-size: 14px; color: #1a2f3f;">🩻 CT Image Processing</span>
      <span style="background: #a06b9a; padding: 5px 15px; border-radius: 20px; font-size: 14px; color: white;">🔬 Medical AI Research</span>
    </div>

  </div>
</section>

---

## 🧪 Dataset Overview: Brain Stroke CT

<div align="center">
  
| Feature | Specification | Clinical Significance |
|:--------|:--------------|:----------------------|
| **Source** | [Kaggle Dataset](https://www.kaggle.com/datasets/ozguraslank/brain-stroke-ct-dataset) | Real patient CT scans |
| **Classes** | Normal, Ischemic Stroke, Hemorrhagic Stroke | 3 critical diagnostic categories |
| **Image Size** | 224x224x3 | Standardized for deep learning |
| **Total Samples** | 1,500+ annotated CT images | Clinically validated |
| **Format** | JPEG/PNG | Ready for preprocessing |

</div>

### 📊 Class Distribution

```python
# Dataset split for clinical validation
dataset_config = {
    'train': 0.70,      # 1050+ images for training
    'validation': 0.15,  # 225+ images for validation  
    'test': 0.15         # 225+ images for testing
}
