import React, { useEffect, useState } from 'react';
import axios from 'axios';

function FAQList() {
  const [faqs, setFaqs] = useState([]);
  const [language, setLanguage] = useState('en');

  useEffect(() => {
    axios.get(`http://localhost:8000/api/faqs/?lang=${language}`)
      .then(res => {
        setFaqs(res.data);
      })
      .catch(err => {
        console.error(err);
      });
  }, [language]);

  return (
    <div>
      <h1>Frequently Asked Questions</h1>
      <select value={language} onChange={e => setLanguage(e.target.value)}>
        <option value="en">English</option>
        <option value="hi">Hindi</option>
        <option value="bn">Bengali</option>
      </select>
      <ul>
        {faqs.map(faq => (
          <li key={faq.id}>
            <h3>{faq.question}</h3>
            <p dangerouslySetInnerHTML={{ __html: faq.answer }} />
          </li>
        ))}
      </ul>
    </div>
  );
}

export default FAQList;
