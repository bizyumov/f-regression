# f-regression

Primary-source archive and legacy code snapshot for Boris Izyumov's f-regression / fuzzy regression work.

The repository currently preserves:

- reference papers as PDFs;
- Markdown text extracted from those papers, stored next to the PDFs;
- minimal public bibliographic metadata for the EUSFLAT 2003 paper;
- a legacy `pyFuReA` source snapshot with a short technical analysis.

## Repository layout

```text
.
├── docs/
│   └── pyfurea-analysis.md
├── references/
│   ├── eusflat-2003-application-f-regression/
│   ├── oilfield-2013-processing-well-testing-f-regression/
│   ├── oilfield-2016-fuzzy-information-modeling/
│   ├── zittau-2000-fuzzy-regression-crisp-model/
│   └── zittau-2001-software-tools/
└── src/
    └── legacy/
```

## References

Each reference folder contains the source PDF and, where available, a Markdown text companion extracted from the PDF.

### Zittau 2000: Fuzzy regression analysis and application to a crisp model

Folder:

- `references/zittau-2000-fuzzy-regression-crisp-model/`

Files:

- `(2000) Kalinina, Wagenknecht- Fuzzy regression analysis and application to a crisp model.pdf`
- `(2000) Kalinina, Wagenknecht- Fuzzy regression analysis and application to a crisp model.md`

Bibliographic note:

- Eleonora Kalinina, Michael Wagenknecht.
- Proceedings of the 8th Zittau Fuzzy Colloquium, 2000.

### Zittau 2001: Software tools for regression analysis of fuzzy data

Folder:

- `references/zittau-2001-software-tools/`

Files:

- `(2001) Izyumov- Software tools for regression analysis of fuzzy data.pdf`
- `(2001) Izyumov- Software tools for regression analysis of fuzzy data.md`

Bibliographic note:

- Boris Izyumov, Eleonora Kalinina, Michael Wagenknecht.
- Proceedings of the 9th Zittau Fuzzy Colloquium, 2001.
- Pages 221–229.

### EUSFLAT 2003: Application of f-regression method to fuzzy classification problem

Folder:

- `references/eusflat-2003-application-f-regression/`

Files:

- `(2003) Izyumov- Application of f-regression method to fuzzy classification problem.pdf`
- `(2003) Izyumov- Application of f-regression method to fuzzy classification problem.md`
- `dblp-record.bib`
- `dblp-record.xml`

Bibliographic note:

- Boris Izyumov.
- EUSFLAT 2003, Zittau.
- Pages 761–766.
- DBLP record: <https://dblp.org/rec/conf/eusflat/Izyumov03>

### Zittau 2013: Processing of well testing data by fuzzy f-regression

Folder:

- `references/oilfield-2013-processing-well-testing-f-regression/`

Files:

- `(2013) Izyumov- Processing of the oil-producing well testing data by means of fuzzy f-regression model.pdf`
- `(2013) Izyumov- Processing of the oil-producing well testing data by means of fuzzy f-regression model.md`

Bibliographic note:

- Boris Izyumov.
- English paper on processing oil-producing well testing data by means of a fuzzy f-regression model.

### 2016: Principles of modeling fuzzy information for parametric identification in oil and gas production

Folder:

- `references/oilfield-2016-fuzzy-information-modeling/`

Files:

- `(2016) Изюмов- Принципы моделирования нечеткой информации для решения задач параметрической идентификации в нефтегазодобыче.pdf`
- `(2016) Изюмов- Принципы моделирования нечеткой информации для решения задач параметрической идентификации в нефтегазодобыче.md`
- `(2016) Izyumov- Principles of modeling fuzzy information for parametric identification in oil and gas production.en.md`

Bibliographic note:

- Изюмов Б. Д.
- «Автоматизация, телемеханизация и связь в нефтяной промышленности».
- 2016, №6, pages 21–32.
- eLibrary ID: 26168272.
- EDN: WAQQPZ.

## Legacy code

The historical Python source snapshot is stored in:

- `src/legacy/`

Main files:

- `pyFuReA.py` — core f-regression implementation.
- `pw-data.py` — well-test / piecewise-analysis visualization script using `pyFuReA`.
- `test2.py` — unrelated historical experiment kept as part of the snapshot.
- CSV/TSV/XLS/XLSX files — sample datasets used by the legacy scripts.
- `welltest_loglog_*.png` — illustrative well-test plots.

See `docs/pyfurea-analysis.md` for a technical inventory, known compatibility issues, and cleanup recommendations.

## Notes

- Word sources are intentionally not stored in this repository.
- The 2000 article is preserved as a PDF generated from the historical Word source.
- The 2016 folder contains both the Russian article text (`.md`) and an English Markdown translation (`.en.md`).
- The repository is an archive plus legacy snapshot, not yet a packaged modern Python implementation.
