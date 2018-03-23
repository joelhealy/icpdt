import os
from app import app
from flask import render_template, url_for, request, redirect, send_from_directory, flash, session
from werkzeug.utils import secure_filename

ALLOWED_EXTENSIONS = set(['txt', 'prn', 'pdf'])


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.')[1].lower() in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No import file selected', 'import-tab')
            return render_template('icpdt.html', tab_button='import-tab-button')
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No import file selected', 'import-tab')
            return render_template('icpdt.html', tab_button='import-tab-button')
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            flash('Import file: ' + file.filename + ' successfully uploaded.', 'edit-tab')
            sample_info = [
                { "batch_id": "4429",
                  "asr_number": 6684,
                  "sample_number": 21,
                  "qc_code": '__',
                  "initial_weight_volume": 1.008,
                  "diluted_volume": 1,
                  "solids_ratio": 1.02,
                  "spike_solution_id": "mock solution id"
                }, 
                { "batch_id": "4430",
                  "asr_number": 6684,
                  "sample_number": 21,
                  "qc_code": '__',
                  "initial_weight_volume": 1.011,
                  "diluted_volume": 1,
                  "solids_ratio": 1.02,
                  "spike_solution_id": "mock solution id"
                }, 
            ]
            import_lines = []
            line_count = 0
            with open(os.path.join(app.config['UPLOAD_FOLDER'], filename)) as f:
                for line in f:
                    mod_line = line
                    if line_count < 7:
                        # Strip leading Unicode magic number and Unicode null filler bytes if present
                        # excluded_chars = dict.fromkeys([0, 254, 255])
                        # mod_line = mod_line.translate(excluded_chars)
                        # if first character is " then remove the first two "s
                        if mod_line[0] == '"':
                            mod_line = mod_line[1:]
                            quote_pos = mod_line.find('"')
                            if quote_pos > -1:
                                mod_line = mod_line[:quote_pos] + mod_line[quote_pos+1:]
                        arr = mod_line.strip().split(",") 
                        # if len(arr[0]) > 0:
                        import_lines.append("%".join(arr))
                        sample_info_row = {}
                        sample_info_row["batch_id"] = filename
                        sample_info_row["asr_number"] = arr[0]
                        sample_info_row["sample_number"] = arr[1]
                        sample_info_row["qc_code"] = arr[2]
                        sample_info_row["initial_weight_volume"] = arr[3]
                        sample_info_row["diluted_volume"] = arr[4]
                        sample_info_row["solids_ratio"] = arr[5]
                        sample_info_row["spike_solution_id"] = 'spike_solution_id'
                        sample_info.append(sample_info_row)
                        line_count = line_count + 1
                    
            return render_template('icpdt.html',
                tab_button='edit-tab-button',
                sample_info=sample_info,
                import_lines=import_lines)

    return render_template('icpdt.html', tab_button='import-tab-button')


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


