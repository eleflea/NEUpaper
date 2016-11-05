NEUpaper
--------

### How

After the teachers release the exams, the ftp server (202.118.26.80) will generate hundreds of papers. For some unknow reason, every student ID will be linked with fixed paper, not random. Actually, your test paper will be doomed as soon as the exam releases. That's why we can foresee and even download the papers from the website (both http and ftp). Particularly, ftp server has a password. 

### Use

```Python
import NEUpaper as pa
res = pa.getExamIfo(studentID, dataSource)
```

student ID is eight digits, like 20124321.
dataSource is one of the follows:
- PRO
- COMPLEX
- MATHE

return a list with 2-tuple elements (exam name and src).

### Example

```Python
import NEUpaper as pa
res = pa.getExamIfo(20124321, pa.PRO)
```

if there are any exams during pending, res gives a feedback.

```Python
>> res
[('第3章 二维随机变量及其分布', 'http://202.118.26.80/PublishChoice/概率统计_GL/2012-11-11/04123/25sdc9624124c8t2sf68f2527025b4c1.zip')]
```