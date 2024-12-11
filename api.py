from flask import Flask, request, jsonify

app = Flask(__name__)

# Data saran kesehatan
saran_kesehatan = {
    "Nyeri dada": "Segera periksa ke dokter jantung karena bisa menjadi tanda penyakit jantung koroner.",
    "Bahu kiri terasa tidak enak": "Cobalah beristirahat dan hindari aktivitas berat. Jika gejala berlanjut, konsultasikan dengan dokter.",
    "Keringat dingin": "Ini bisa menjadi tanda serangan jantung. Segera cari bantuan medis.",
    "Sesak nafas": "Lakukan pemeriksaan fungsi paru dan jantung. Hindari aktivitas berat sampai penyebabnya diketahui.",
    "Gangguan pencernaan": "Perhatikan pola makan dan hindari makanan berlemak. Jika gejala berlanjut, periksakan diri ke dokter.",
    "Mual": "Hindari makanan berlemak dan minum obat antimual. Periksakan ke dokter jika gejala berlanjut.",
    "Detak jantung tidak teratur": "Segera periksa ke dokter untuk EKG.",
    "Pusing": "Istirahat sejenak dan cek tekanan darah. Jika pusing berlanjut, konsultasikan dengan dokter.",
    "Kaki bengkak": "Angkat kaki saat duduk atau tidur untuk mengurangi pembengkakan. Konsultasikan dengan dokter.",
    "Jantung berdebar-debar": "Kurangi konsumsi kafein dan rokok. Jika gejala berlanjut, periksakan ke dokter.",
    "Mudah lelah": "Pastikan Anda cukup istirahat dan nutrisi yang baik. Konsultasikan dengan dokter jika kelelahan berlanjut.",
    "Nyeri di daerah dada tengah": "Segera cari bantuan medis karena bisa menjadi tanda serangan jantung.",
    "Mudah berkeringat": "Periksakan diri ke dokter untuk mengetahui penyebabnya.",
    "Dada mengencang": "Hindari aktivitas berat dan segera periksa ke dokter.",
    "Pembengkakan pada jantung": "Ini bisa menjadi tanda gagal jantung. Segera konsultasikan dengan dokter.",
    "Kelainan fungsi hati": "Lakukan pemeriksaan fungsi hati di laboratorium.",
    "Pendarahan dari hidung": "Hindari mengupil dan jaga kelembapan hidung. Jika berlanjut, periksakan ke dokter.",
    "Wajah kemerahan": "Bisa menjadi tanda tekanan darah tinggi. Periksakan tekanan darah Anda.",
    "Batuk": "Minum obat batuk dan istirahat. Jika batuk berlanjut, periksakan diri ke dokter.",
    "Sakit perut": "Hindari makanan pedas dan asam. Jika sakit berlanjut, konsultasikan dengan dokter.",
    "Detak jantung cepat": "Hindari kafein dan stres. Jika berlanjut, periksakan ke dokter.",
    "Nyeri di daerah lengan kiri": "Ini bisa menjadi tanda serangan jantung. Segera cari bantuan medis.",
    "Punggung terasa tidak enak": "Cobalah istirahat dan peregangan. Jika nyeri berlanjut, konsultasikan dengan dokter.",
    "Sakit kepala": "Minum air putih yang cukup dan istirahat. Jika sakit kepala berlanjut, periksakan ke dokter."
}

@app.route('/saran', methods=['POST'])
def get_saran():
    gejala = request.json.get('gejala', [])
    saran = [saran_kesehatan.get(g, "Konsultasikan dengan dokter.") for g in gejala]
    return jsonify({"saran": saran})

if __name__ == '__main__':
    app.run(debug=True)
