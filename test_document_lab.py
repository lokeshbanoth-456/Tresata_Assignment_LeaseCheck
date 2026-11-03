"""Tests on a small, manually labelled synthetic set; not a real-world benchmark."""
import json, re, unittest
from pathlib import Path

DATA = json.loads((Path(__file__).parent / 'data' / 'labelled_examples.json').read_text())
FIELDS = ('term_months', 'monthly_rent', 'annual_escalation_percent')

def baseline(text):
    """Intentionally transparent regex baseline; not the LLM proposal path."""
    out = {k: None for k in FIELDS}
    t = text.lower()
    m = re.search(r'(\d+)\s*years?\s+and\s+(\d+)\s+months?', t)
    if m: out['term_months'] = int(m.group(1))*12+int(m.group(2))
    else:
        m = re.search(r'(\d+)\s*(?:months?|mos?\b)', t)
        if m: out['term_months'] = int(m.group(1))
        else:
            m = re.search(r'(?:runs? for|period is|term is|period of|term of|period shall be|term shall be|initial lease period is|initial term shall be)\s+(\d+)\s+years?', t)
            if m: out['term_months'] = int(m.group(1))*12
            else:
                m = re.search(r'(five|six|seven|eight|nine|ten)\s*\((\d+)\)\s*years?', t)
                if m: out['term_months'] = int(m.group(2))*12
    # Monthly fixed rent; annual rent conversion only when explicit annual language exists.
    m = re.search(r'(?:base rent|monthly rent|rent payable each month|monthly consideration|rent)\s*[:is]*\s*(?:inr|rs\.?|₹)?\s*([\d,]+)\s*(?:per month|monthly|each month)', t)
    if not m:
        m = re.search(r'(?:annual base rent|annual rent)\s*(?:is|:)?\s*(?:inr|rs\.?|₹)?\s*([\d,]+)', t)
        if m: out['monthly_rent'] = int(m.group(1).replace(',',''))//12
    if m and out['monthly_rent'] is None: out['monthly_rent'] = int(m.group(1).replace(',',''))
    m = re.search(r'(?:increases? by|increase of|escalation of|escalation:|annual escalation:|fixed annual increase:|fixed annual step-up of)\s*(\d+(?:\.\d+)?)\s*%', t)
    if not m: m = re.search(r'(\d+(?:\.\d+)?)\s*%\s*(?:annually|annual(?:ly)?|yearly|per annum)?\s*(?:fixed\s+)?(?:annual\s+)?(?:increase|escalation|step-up|increase)', t)
    if not m: m = re.search(r'(?:annual escalation|fixed annual increase|fixed annual step-up)\s*[:is]*\s*(\d+(?:\.\d+)?)\s*%', t)
    if m: out['annual_escalation_percent'] = float(m.group(1))
    return out

def quote_verify(value, quote, text, field):
    if value is None: return False
    if not quote or quote not in text: return False
    nums = [float(x.replace(',','')) for x in re.findall(r'\d[\d,]*(?:\.\d+)?', quote)]
    if any(abs(n-value) <= 1e-6*max(1,abs(value)) for n in nums): return True
    if field == 'term_months' and re.search(r'year', quote, re.I) and any(abs(n*12-value)<1e-6*max(1,abs(value)) for n in nums): return True
    if field == 'monthly_rent' and re.search(r'annual|annum|per year|yearly', quote, re.I) and any(abs(n/12-value)<1e-6*max(1,abs(value)) for n in nums): return True
    return False

class DocumentLabTests(unittest.TestCase):
    def test_dataset_has_prelabelled_synthetic_gold_and_expected_size(self):
        self.assertEqual(len(DATA), 12)
        self.assertEqual(len({x['id'] for x in DATA}), 12)
        self.assertTrue(all(set(x['gold']) == set(FIELDS) for x in DATA))

    def test_baseline_outputs_are_well_typed(self):
        for case in DATA:
            with self.subTest(case=case['id']):
                result = baseline(case['text'])
                self.assertEqual(set(result), set(FIELDS))
                for value in result.values(): self.assertTrue(value is None or isinstance(value, (int,float)))

    def test_verifier_rejects_missing_or_mismatched_quotes(self):
        text = 'Term: 60 months. Rent: INR 50,000 per month.'
        self.assertFalse(quote_verify(60, 'Term: 60 months', 'different source', 'term_months'))
        self.assertFalse(quote_verify(5000, 'Rent: INR 50,000 per month.', text, 'monthly_rent'))
        self.assertTrue(quote_verify(60, 'Term: 60 months.', text, 'term_months'))

    def test_report_baseline_metrics(self):
        total = len(DATA)*len(FIELDS); correct=0; per_field={k: {'correct':0,'total':len(DATA)} for k in FIELDS}
        for case in DATA:
            pred=baseline(case['text'])
            for f in FIELDS:
                if pred[f] == case['gold'][f]: correct += 1; per_field[f]['correct'] += 1
        print(f'\nSynthetic labelled set: {len(DATA)} documents, {total} field decisions; regex baseline exact matches {correct}/{total} ({correct/total:.1%})')
        for f in FIELDS: print(f'  {f}: {per_field[f]["correct"]}/{per_field[f]["total"]}')
        # The metric is reported, not asserted to be high; this test checks only the evaluator is stable.
        self.assertEqual(correct, 29)
        self.assertEqual(per_field['term_months']['correct'], 11)
        self.assertEqual(per_field['monthly_rent']['correct'], 6)
        self.assertEqual(per_field['annual_escalation_percent']['correct'], 12)

if __name__ == '__main__': unittest.main(verbosity=2)
