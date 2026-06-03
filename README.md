# Race Condition with Python Threads

## الوصف
مشروع بسيط بيوضح مشكلة Race Condition وكيف الـ Lock بيحلها باستخدام Python Threads.

## الفكرة
1. **بدون Lock**: ثريدين بيزيدو نفس المتغير بنفس الوقت → النتيجة بتطلع غلط
2. **مع Lock**: الثريد التاني بستنى الأول يخلص → النتيجة صحيحة 100%

## طريقة التشغيل
```bash
python main.py
